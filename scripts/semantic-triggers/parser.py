#!/usr/bin/env python
"""
Semantic Triggers Parser (Onda α)
---------------------------------

Lê os logs nativos do Claude Code (~/.claude/projects/*/sessions/*.jsonl),
aplica regex calibrado de 5 categorias (definidas em patterns.yaml), e
gera 5 arquivos markdown agregados em ~/.claude/context-tree/patrick-pessoal/skills-ecosystem/.

Uso:
    python parser.py                    # roda no histórico completo
    python parser.py --since 2026-04-10 # só sessões desde essa data
    python parser.py --project skillforge-arsenal  # filtra por cwd
    python parser.py --dry-run          # calcula matches sem escrever arquivos
    python parser.py --sample 10        # mostra 10 exemplos por categoria (validação)
    python parser.py --category "Erros do Claude"  # só uma categoria

Output por arquivo .md:
    - Resumo: contagem, sessões cobertas, date range
    - Tabela consolidada: timestamp | session | pattern | trecho curto
    - Trechos expandidos (context window) pra cada match

Precisão:
    - Regex multi-token (evita false-positive de palavra única)
    - Context window por pattern (3 linhas antes, 5 depois por default)
    - Dedup por (sessionId, uuid, pattern_label)
    - Min match length configurável em settings
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

import yaml


# ------------------------------------------------------------------
# Data classes
# ------------------------------------------------------------------


@dataclass
class Match:
    category: str
    pattern_label: str
    matched_text: str
    trecho: str  # context window
    timestamp: str
    session_id: str
    uuid_: str
    cwd: str
    git_branch: str
    slug: str
    prompt_id: str
    content_type: str  # "thinking" | "text"


@dataclass
class PatternConfig:
    regex: str
    label: str
    context_before: int
    context_after: int
    flags: int
    compiled: re.Pattern = field(init=False)

    def __post_init__(self):
        self.compiled = re.compile(self.regex, self.flags)


@dataclass
class CategoryConfig:
    name: str
    output_file: str
    description: str
    patterns: list[PatternConfig]


@dataclass
class Settings:
    logs_root: Path
    output_dir: Path
    dedup: bool
    max_matches_per_category: int
    min_match_length: int
    max_age_days: int
    text_extraction_priority: list[str]


# ------------------------------------------------------------------
# Config loading
# ------------------------------------------------------------------


def _parse_flags(flags_list: list[str]) -> int:
    flag_value = 0
    mapping = {"I": re.IGNORECASE, "M": re.MULTILINE, "S": re.DOTALL}
    for f in flags_list or []:
        if f.upper() not in mapping:
            raise ValueError(f"Flag desconhecida: {f}")
        flag_value |= mapping[f.upper()]
    return flag_value


def load_config(yaml_path: Path) -> tuple[list[CategoryConfig], Settings]:
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    categories: list[CategoryConfig] = []
    for cat in data["categories"]:
        patterns = []
        for p in cat["patterns"]:
            cw = p.get("context_window", {"before": 3, "after": 5})
            patterns.append(
                PatternConfig(
                    regex=p["regex"],
                    label=p["label"],
                    context_before=cw.get("before", 3),
                    context_after=cw.get("after", 5),
                    flags=_parse_flags(p.get("flags", ["I"])),
                )
            )
        categories.append(
            CategoryConfig(
                name=cat["name"],
                output_file=cat["output_file"],
                description=cat.get("description", ""),
                patterns=patterns,
            )
        )

    s = data["settings"]
    settings = Settings(
        logs_root=Path(s["logs_root"]).expanduser(),
        output_dir=Path(s["output_dir"]).expanduser(),
        dedup=s.get("dedup", True),
        max_matches_per_category=s.get("max_matches_per_category", 500),
        min_match_length=s.get("min_match_length", 8),
        max_age_days=s.get("max_age_days", 0),
        text_extraction_priority=s.get("text_extraction_priority", ["thinking", "text"]),
    )

    return categories, settings


# ------------------------------------------------------------------
# Log iteration
# ------------------------------------------------------------------


def iter_jsonl_files(logs_root: Path, project_filter: str | None = None) -> Iterator[Path]:
    """Enumera todos os .jsonl das sessões. Filtra por cwd se project_filter dado."""
    if not logs_root.exists():
        raise FileNotFoundError(f"logs_root não existe: {logs_root}")
    for project_dir in sorted(logs_root.iterdir()):
        if not project_dir.is_dir():
            continue
        if project_filter and project_filter.lower() not in project_dir.name.lower():
            continue
        for jsonl in sorted(project_dir.glob("*.jsonl")):
            yield jsonl


def iter_log_entries(jsonl_path: Path) -> Iterator[dict]:
    """Stream JSONL line-by-line. Skip lines inválidas silenciosamente."""
    with open(jsonl_path, "r", encoding="utf-8", errors="replace") as f:
        for line_num, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError:
                continue


def extract_text_from_entry(entry: dict, priority: list[str]) -> list[tuple[str, str]]:
    """
    Extrai texto relevante de uma entry.
    Retorna lista de (content_type, text).
    Prioriza thinking > text (mas retorna ambos se existirem).
    """
    out = []
    msg = entry.get("message") or {}
    content = msg.get("content")

    # content pode ser string (1ª user message) ou array (demais)
    if isinstance(content, str):
        out.append(("text", content))
        return out

    if not isinstance(content, list):
        return out

    for item in content:
        if not isinstance(item, dict):
            continue
        ctype = item.get("type")
        if ctype == "thinking" and "thinking" in priority:
            text = item.get("thinking") or ""
            if text:
                out.append(("thinking", text))
        elif ctype == "text" and "text" in priority:
            text = item.get("text") or ""
            if text:
                out.append(("text", text))

    return out


# ------------------------------------------------------------------
# Matching
# ------------------------------------------------------------------


def find_matches_in_text(
    text: str,
    entry_meta: dict,
    content_type: str,
    categories: list[CategoryConfig],
    min_match_length: int,
) -> list[Match]:
    """Aplica todos os patterns de todas as categorias no texto. Retorna matches."""
    lines = text.splitlines()
    matches: list[Match] = []

    for cat in categories:
        for pat in cat.patterns:
            for m in pat.compiled.finditer(text):
                matched = m.group(0).strip()
                if len(matched) < min_match_length:
                    continue

                # Calcular linha do match pra extrair context window
                start = m.start()
                # Que linha começou o match?
                line_idx = text.count("\n", 0, start)
                lo = max(0, line_idx - pat.context_before)
                hi = min(len(lines), line_idx + pat.context_after + 1)
                trecho = "\n".join(lines[lo:hi]).strip()

                matches.append(
                    Match(
                        category=cat.name,
                        pattern_label=pat.label,
                        matched_text=matched,
                        trecho=trecho,
                        timestamp=entry_meta.get("timestamp", ""),
                        session_id=entry_meta.get("sessionId", ""),
                        uuid_=entry_meta.get("uuid", ""),
                        cwd=entry_meta.get("cwd", ""),
                        git_branch=entry_meta.get("gitBranch", ""),
                        slug=entry_meta.get("slug", ""),
                        prompt_id=entry_meta.get("promptId", ""),
                        content_type=content_type,
                    )
                )
    return matches


# ------------------------------------------------------------------
# Main processing
# ------------------------------------------------------------------


def process_all(
    categories: list[CategoryConfig],
    settings: Settings,
    project_filter: str | None = None,
    since: datetime | None = None,
    only_category: str | None = None,
) -> dict[str, list[Match]]:
    """
    Processa todos os .jsonl e retorna dict[category_name, list[Match]].
    """
    by_category: dict[str, list[Match]] = defaultdict(list)
    seen_dedup: set[tuple[str, str, str]] = set()

    if only_category:
        categories = [c for c in categories if c.name.lower() == only_category.lower()]
        if not categories:
            print(f"⚠ Categoria '{only_category}' não encontrada.", file=sys.stderr)
            return by_category

    total_files = 0
    total_entries = 0
    total_matches = 0

    for jsonl_path in iter_jsonl_files(settings.logs_root, project_filter):
        total_files += 1
        for entry in iter_log_entries(jsonl_path):
            total_entries += 1

            # Filtro temporal
            if since:
                ts = entry.get("timestamp", "")
                if ts:
                    try:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        if dt < since:
                            continue
                    except ValueError:
                        pass

            # Só processamos entries com message
            if entry.get("type") not in ("assistant", "user"):
                continue

            texts = extract_text_from_entry(entry, settings.text_extraction_priority)
            if not texts:
                continue

            entry_meta = {
                "timestamp": entry.get("timestamp", ""),
                "sessionId": entry.get("sessionId", ""),
                "uuid": entry.get("uuid", ""),
                "cwd": entry.get("cwd", ""),
                "gitBranch": entry.get("gitBranch", ""),
                "slug": entry.get("slug", ""),
                "promptId": entry.get("promptId", ""),
            }

            for content_type, text in texts:
                found = find_matches_in_text(
                    text, entry_meta, content_type, categories, settings.min_match_length
                )
                for m in found:
                    if settings.dedup:
                        key = (m.session_id, m.uuid_, m.pattern_label)
                        if key in seen_dedup:
                            continue
                        seen_dedup.add(key)
                    by_category[m.category].append(m)
                    total_matches += 1

    print(f"✓ Processados: {total_files} arquivos, {total_entries:,} entries, {total_matches} matches.", file=sys.stderr)
    return by_category


# ------------------------------------------------------------------
# Output rendering
# ------------------------------------------------------------------


def render_markdown(category: CategoryConfig, matches: list[Match], settings: Settings) -> str:
    """Gera markdown estruturado pra 1 categoria."""
    lines: list[str] = []

    # Frontmatter YAML (compatível com context-tree entry)
    lines.append("---")
    lines.append(f"source: semantic-triggers-parser")
    lines.append(f"category: {category.name}")
    lines.append(f"generated_at: {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"matches_total: {len(matches)}")
    lines.append(f"maturity: draft")
    lines.append(f"importance: 60")
    lines.append(f"connects_to:")
    lines.append(f"  - patrick-pessoal/skills-ecosystem/handoff-wave-c-2026-04-18")
    lines.append("---")
    lines.append("")

    # Header
    lines.append(f"# {category.name}")
    lines.append("")
    lines.append(f"> **Descrição:** {category.description}")
    lines.append(f"> **Gerado por:** `scripts/semantic-triggers/parser.py` (Onda α)")
    lines.append(f"> **Total de matches:** {len(matches)}")
    lines.append("")

    if not matches:
        lines.append("_Nenhum match encontrado nesta execução._")
        lines.append("")
        return "\n".join(lines)

    # Cap pelo max_matches_per_category
    cap = settings.max_matches_per_category
    if len(matches) > cap:
        matches = sorted(matches, key=lambda m: m.timestamp or "", reverse=True)[:cap]
        lines.append(f"_⚠ Exibindo top {cap} mais recentes (de {len(matches)}). Ajuste `max_matches_per_category` em patterns.yaml pra expandir._")
        lines.append("")

    # Breakdown por pattern
    by_pattern: dict[str, int] = defaultdict(int)
    for m in matches:
        by_pattern[m.pattern_label] += 1

    lines.append("## Breakdown por pattern")
    lines.append("")
    lines.append("| Pattern | Matches |")
    lines.append("|---|---:|")
    for label in sorted(by_pattern, key=lambda x: by_pattern[x], reverse=True):
        lines.append(f"| `{label}` | {by_pattern[label]} |")
    lines.append("")

    # Tabela consolidada
    lines.append("## Tabela consolidada")
    lines.append("")
    lines.append("| # | Timestamp | Session (slug) | cwd | Pattern | Match |")
    lines.append("|--:|---|---|---|---|---|")
    for i, m in enumerate(sorted(matches, key=lambda m: m.timestamp or "", reverse=True), 1):
        ts_short = (m.timestamp or "")[:19].replace("T", " ")
        slug = m.slug or m.session_id[:8]
        cwd_short = _short_cwd(m.cwd)
        match_short = _truncate(m.matched_text, 60)
        lines.append(f"| {i} | {ts_short} | {slug} | {cwd_short} | `{m.pattern_label}` | {match_short} |")
    lines.append("")

    # Trechos expandidos
    lines.append("## Trechos com contexto")
    lines.append("")
    for i, m in enumerate(sorted(matches, key=lambda m: m.timestamp or "", reverse=True), 1):
        lines.append(f"### Match #{i} — `{m.pattern_label}`")
        lines.append("")
        lines.append(f"- **Timestamp:** {m.timestamp}")
        lines.append(f"- **Session:** {m.session_id[:8]} ({m.slug or 'no slug'})")
        lines.append(f"- **cwd:** {m.cwd}")
        lines.append(f"- **Branch:** {m.git_branch or 'N/A'}")
        lines.append(f"- **Content type:** {m.content_type}")
        lines.append("")
        lines.append("```")
        lines.append(m.trecho)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def _truncate(s: str, max_len: int) -> str:
    s = s.replace("\n", " ").replace("|", "\\|").strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _short_cwd(cwd: str) -> str:
    if not cwd:
        return "-"
    parts = cwd.replace("\\", "/").rstrip("/").split("/")
    if len(parts) <= 2:
        return cwd
    return ".../" + "/".join(parts[-2:])


def write_outputs(
    categories: list[CategoryConfig],
    by_category: dict[str, list[Match]],
    settings: Settings,
    dry_run: bool = False,
) -> None:
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    for cat in categories:
        matches = by_category.get(cat.name, [])
        md = render_markdown(cat, matches, settings)
        path = settings.output_dir / cat.output_file
        if dry_run:
            print(f"[dry-run] Would write {len(md):,} bytes → {path}", file=sys.stderr)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"✓ {path} ({len(matches)} matches, {len(md):,} bytes)", file=sys.stderr)


# ------------------------------------------------------------------
# Sample mode (validation helper)
# ------------------------------------------------------------------


def print_samples(by_category: dict[str, list[Match]], n: int = 10) -> None:
    """Mostra N exemplos por categoria no stderr — pra Patrick validar precisão."""
    print("\n" + "=" * 60, file=sys.stderr)
    print(f"SAMPLE MODE — {n} exemplos por categoria pra validação manual", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)

    for cat_name, matches in by_category.items():
        print(f"\n### {cat_name} (total: {len(matches)})\n", file=sys.stderr)
        sample = matches[:n] if len(matches) <= n else matches[::max(1, len(matches) // n)][:n]
        for i, m in enumerate(sample, 1):
            print(f"  [{i}] {m.pattern_label} | {m.timestamp[:19]} | {m.slug or m.session_id[:8]}", file=sys.stderr)
            print(f"      \"{_truncate(m.matched_text, 100)}\"", file=sys.stderr)
            print(f"      (trecho: {_truncate(m.trecho, 150)})", file=sys.stderr)
            print("", file=sys.stderr)


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Semantic Triggers Parser — Onda α (post-hoc)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--config",
        default=str(Path(__file__).parent / "patterns.yaml"),
        help="Caminho do patterns.yaml",
    )
    parser.add_argument(
        "--project",
        help="Filtrar logs por nome do projeto (substring case-insensitive em cwd)",
    )
    parser.add_argument(
        "--since",
        help="ISO date (YYYY-MM-DD) — só sessões desde essa data",
    )
    parser.add_argument(
        "--category",
        help="Rodar só 1 categoria (usa o 'name' exato)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Calcula matches e reporta contagens, mas não escreve arquivos",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=0,
        help="Imprime N exemplos por categoria pra validação manual (pós-processamento)",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"✗ Config não existe: {config_path}", file=sys.stderr)
        sys.exit(1)

    categories, settings = load_config(config_path)
    print(f"✓ Config carregado: {len(categories)} categorias", file=sys.stderr)
    print(f"  logs_root: {settings.logs_root}", file=sys.stderr)
    print(f"  output_dir: {settings.output_dir}", file=sys.stderr)

    since_dt = None
    if args.since:
        try:
            since_dt = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)
            print(f"  since: {since_dt.isoformat()}", file=sys.stderr)
        except ValueError:
            print(f"✗ --since inválido: {args.since} (use YYYY-MM-DD)", file=sys.stderr)
            sys.exit(1)

    if args.project:
        print(f"  project filter: {args.project}", file=sys.stderr)

    print("", file=sys.stderr)

    by_category = process_all(
        categories=categories,
        settings=settings,
        project_filter=args.project,
        since=since_dt,
        only_category=args.category,
    )

    print("\nContagem por categoria:", file=sys.stderr)
    for cat in categories:
        if args.category and cat.name.lower() != args.category.lower():
            continue
        print(f"  {cat.name}: {len(by_category.get(cat.name, []))} matches", file=sys.stderr)
    print("", file=sys.stderr)

    if args.sample:
        print_samples(by_category, args.sample)

    write_outputs(categories, by_category, settings, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
