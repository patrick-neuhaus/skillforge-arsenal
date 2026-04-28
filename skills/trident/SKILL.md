---
name: trident
description: "Three-pronged code review pipeline: Scan, Verify, Judge. Deep codebase audit for bugs, security vulnerabilities, logic errors, SOLID violations, and dead code with independent 3-agent verification. Use when user asks to: review code, audit code, find bugs, security review, 'revisa esse código', 'tem bug nisso?', 'faz um audit', review PR, review changes, code quality check, check for vulnerabilities, 'analisa esse código', inspect codebase, is this code safe, check my PR, what's wrong with this code. Supports: unstaged, staged, PR, commit range, directory scan. Use --dedup mode for pre-implementation duplicate scan ('verifica antes de criar', 'já tem isso no projeto?', 'tem componente parecido?', find duplicates, code reuse). Don't use for: style-only reviews, trivial one-line changes, test coverage, UX review. Se o arquivo não for encontrado no worktree, pedir paste do código inline — não bloquear análise."
---

# Trident

IRON LAW: NEVER implement changes without explicit user confirmation. This is review-first — scan, verify, judge, then ASK.

Three-pronged pipeline: **Scan → Verify → Judge**. Multi-lens scanning (SOLID, security, quality, dead code) with independent 3-agent verification for high-confidence findings.

## Boundaries (skills similares)

- **`--design` é code-level** (CSS, layout, performance, a11y dentro do código). Para auditoria de **experiência do usuário** (fluxos, heurísticas Nielsen, dark patterns, jornada), use **`ux-audit`** — não trident --design.
- **`--skill` é review holístico** de uma skill como produto (estrutura + GEO + distribuição). Para **otimização cirúrgica de description** apenas, use **`geo-optimizer`** — não trident --skill.
- **Para code review use trident, sempre.** A skill built-in `simplify` (Anthropic) parece similar mas tem cobertura inferior (sem 3-agent verification, sem multi-lens scan, sem severity P0-P3).
- **`--dedup` substitui `code-dedup-scanner`** (absorvida em Wave 1, 2026-04-29). Pre-implementation scan pra evitar duplicação. Use ANTES de criar componente/função/hook novo.

**Exemplo de disambiguation:**
> "revisa o checkout" → ambíguo. Pergunta:
> - "O código do checkout tem bugs?" → `trident --mode dir --target src/checkout`
> - "O fluxo de checkout tá confuso pro usuário?" → `ux-audit` apontando pra URL/screenshots
> - "O CSS/perf da página de checkout tá OK?" → `trident --design`

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | Review mode: unstaged, staged, all-local, pr, range, dir | auto-detect |
| `--target <t>` | PR number, commit range, or directory path | current changes |
| `--design` | Design review: visual consistency + accessibility + performance (3 layers) | false |
| `--skill` | Review a skill as product: GEO, structure, distribution readiness | false |
| `--dedup` | Pre-implementation scan: find existing components/functions before creating | false |

## Workflow

```
Trident Progress:

- [ ] Phase 1: Scope & Preflight ⚠️ REQUIRED
  - [ ] 1.1 Detect review mode (auto or --mode)
  - [ ] 1.2 Gather diff and context
  - [ ] 1.3 Handle edge cases (empty diff, large diff)
- [ ] Phase 2: Scanner (Agent 1)
  - [ ] Dispatch with prompts/scanner-prompt.md
  - [ ] Collect output (max 15 findings)
- [ ] Phase 3: Verifier (Agent 2) ⚠️ REQUIRED
  - [ ] Dispatch with prompts/verifier-prompt.md
  - [ ] Independent re-read of cited code
- [ ] Phase 4: Arbiter (Agent 3)
  - [ ] Dispatch with prompts/arbiter-prompt.md
  - [ ] Final verdicts on disputed findings
- [ ] Phase 5: Present ⛔ BLOCKING
  - [ ] Format findings with severity and evidence
  - [ ] ⛔ GATE: Present to user — NO changes without confirmation
```

## Phase 1: Scope & Preflight

Load `references/review-modes.md` for detailed commands per mode.

### Review Modes

| Mode | Trigger | Diff |
|------|---------|------|
| `unstaged` | Default | `git diff` |
| `staged` | "staged" or unstaged empty | `git diff --cached` |
| `all-local` | "all" / "everything" | `git diff HEAD` |
| `pr` | PR URL, #number, "review PR" | `gh pr diff {N}` |
| `range` | Commit range, branch, "since X" | `git diff {A}..{B}` |
| `dir` | Directory path, "review src/" | Read all files |

### Edge Cases
- **Empty diff:** auto-try staged → ask user for pr/range
- **Large diff (>500 lines):** batch by module/feature area
- **PR not found:** suggest checking number or providing diff manually

Set `{TARGET}` (files/diff) and `{CONTEXT}` (mode, metadata, intent) for Scanner.

## Phase 2: Scanner (Agent 1)

Dispatch subagent with `./prompts/scanner-prompt.md`, filling `{TARGET}`, `{CONTEXT}`, `{REVIEW_MODE}`.

The Scanner performs multi-lens scanning across 5 dimensions:
1. **SOLID + Architecture** — SRP violations, coupling, code smells
2. **Security** — injection, auth gaps, secrets, race conditions
3. **Code Quality** — error handling, performance, boundary conditions
4. **Data Integrity** — transactions, validation, idempotency
5. **Dead Code** — unused, redundant, feature-flagged off

Output: max 15 findings (max 4 SUSPICIOUS), each with evidence + forced counterargument.

## Phase 3: Verifier (Agent 2)

Dispatch subagent with `./prompts/verifier-prompt.md`, filling `{SCANNER_OUTPUT}`.

The Verifier MUST re-read cited code independently — no trusting Scanner's text. For each finding: CONFIRMED, REJECTED, or INSUFFICIENT_EVIDENCE.

## Phase 4: Arbiter (Agent 3)

Dispatch subagent with `./prompts/arbiter-prompt.md`, filling `{SCANNER_OUTPUT}` and `{VERIFIER_OUTPUT}`.

Final verdicts: REAL_BUG, NOT_A_BUG, or NEEDS_HUMAN_CHECK. May re-inspect disputed or high-severity findings.

## Phase 5: Present ⛔ BLOCKING

### Severity Levels

| Level | Action |
|-------|--------|
| **P0** Critical | Must block merge — security vuln, data loss, correctness bug |
| **P1** High | Fix before merge — logic error, perf regression, major SOLID |
| **P2** Medium | Fix or follow-up — code smell, maintainability |
| **P3** Low | Optional — style, naming, minor suggestion |

### Output Format

```markdown
## Trident Review

**Files reviewed**: X files, Y lines changed
**Assessment**: [APPROVE / REQUEST_CHANGES / COMMENT]

### Confirmed Bugs (REAL_BUG)
| Bug ID | Severity | Confidence | Category | Title | Location |
|--------|----------|------------|----------|-------|----------|

### Dismissed (NOT_A_BUG)
| Bug ID | Original Severity | Reason |

### Needs Human Review
| Bug ID | Severity | What Would Settle It |

### Removal Plan (if applicable)
### Additional Suggestions (optional, not blocking)

## Next Steps
1. **Fix all** — implement all fixes
2. **Fix P0/P1 only** — critical and high priority
3. **Fix specific items** — tell me which
4. **No changes** — review complete
```

⛔ **Confirmation Gate:** NEVER proceed to fix without explicit user choice.

### Clean Review (no bugs found)
State: what was checked, areas not covered, residual risks, recommended follow-ups.

## Dedup Mode (--dedup)

**Quando usar:** ANTES de criar componente, função, hook, query. Sub-step do SDD Phase 1 Research. Evita duplicação invisível em codebase grande.

**Workflow compacto (3 steps):**

1. **Intent** — entender o que vai criar:
   - "O que vai criar?" (component, function, hook, query, page, util)
   - "Qual domínio?" (UI, data, auth, utils, invoices)
   - "Descreve a funcionalidade em 1 frase"
   - Extrai keywords pra search.

2. **Scan** — busca multi-vector:
   - Por nome exato + fuzzy: `grep -r "ComponentName\|functionName" src/ --include="*.ts*"`
   - Por padrão funcional: keywords related (Button, Btn, button)
   - Em `node_modules` (deps instaladas) e `src/components/ui/` (shadcn/design system)
   - Pra cada match: file path, line number, usage context atual.

3. **Report ⛔ GATE** — apresentar com recomendação por match:
   - **🟢 REUSE** (>80% match) → use o que existe, não cria
   - **🟡 EXTEND** (40-80%) → forka/configura o existente
   - **🔴 CREATE** (nada cobre) → cria novo, justifica por quê

IRON LAW (--dedup): NEVER report a duplicate without showing exact location + usage context. False positives custam mais tempo que economizam.

**Output format:**

```markdown
## Dedup Scan: <intent>

### Matches found (N)
| Match | Path | Lines | Action | Why |
|-------|------|-------|--------|-----|
| Button | src/components/ui/button.tsx | 1-45 | 🟢 REUSE | Same variants needed |

### Decision per match
[user decides REUSE/EXTEND/CREATE]
```

Diferente de `--mode dir` (review de bugs em código existente): `--dedup` busca REUSO antes de implementação, não bugs em código já escrito.

## Shared Output Contract

All agents use `bug_id` keyed schema. Each stage appends:

| Field | Scanner | Verifier | Arbiter |
|-------|---------|----------|---------|
| `bug_id`, `title`, `location` | Creates | Preserves | Preserves |
| `severity` (P0-P3) | Initial | May revise | Final |
| `category` | Creates | Preserves | Preserves |
| `tier` | CONFIRMED/SUSPICIOUS | — | — |
| `status` | — | CONFIRMED/REJECTED/INSUFFICIENT_EVIDENCE | — |
| `verdict` | — | — | REAL_BUG/NOT_A_BUG/NEEDS_HUMAN_CHECK |

## Design Principles

1. **Independent re-inspection.** Each agent reads actual code. No trusting prior text alone.
2. **Bounded recall.** Scanner: max 15 findings, max 4 suspicious. Quality over quantity.
3. **Evidence-based.** Every claim: specific location + concrete trigger + failure story.
4. **Forced counterargument.** Scanner states strongest reason each finding might be wrong.
5. **Permission to abstain.** INSUFFICIENT_EVIDENCE and NEEDS_HUMAN_CHECK exist for a reason.
6. **Review-first.** Never implement without user confirmation.

## Anti-Patterns

- Skip the Verifier — false positive rate jumps to 30-60%
- Judge without codebase access — produces rhetoric, not truth
- Remove Scanner caps — unlimited findings collapse into triage noise
- Force binary verdicts — some findings genuinely need human judgment
- Same model instance for all 3 agents — consensus collapse risk
- Implement before user confirms — violates Iron Law

## Integration

- **SDD** (Phase 4 Review) — SDD invokes trident as its review phase. Input: `git diff` from implement phase.
- **React Patterns** — run react-patterns `--audit` for React-specific issues BEFORE trident for domain-level bugs.
- **Security Audit** — if trident finds security-related findings, suggest security-audit for deep OWASP analysis.
- **Maestro** — maestro routes code review requests to trident. Part of multiple composition chains.
- **Architecture Guard** — trident finds bugs, architecture-guard finds structural violations. Run both for complete review.
- **GEO Optimizer** — `--skill` mode uses GEO scoring to evaluate description quality. Load `references/skill-product-review.md`.
- **UI Design System** — `--design` mode validates frontend output in 3 layers. Load `references/design-review-checklist.md`.

## Prompt Templates & References

| File | Purpose |
|------|---------|
| `prompts/scanner-prompt.md` | Agent 1: multi-lens scan with counterarguments |
| `prompts/verifier-prompt.md` | Agent 2: independent verification |
| `prompts/arbiter-prompt.md` | Agent 3: evidence-based judgment |
| `references/solid-checklist.md` | SOLID smell prompts and heuristics |
| `references/security-checklist.md` | Web/app security checklist |
| `references/code-quality-checklist.md` | Error handling, performance, boundaries |
| `references/removal-plan.md` | Deletion candidate template |
