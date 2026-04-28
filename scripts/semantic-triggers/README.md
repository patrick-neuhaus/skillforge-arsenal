# Semantic Triggers Parser (Onda α)

Parser post-hoc dos logs nativos do Claude Code. Extrai padrões semânticos de pensamento do modelo (erros, decisões, applied learnings, etc.) e agrega em arquivos markdown por categoria.

**Status:** Onda α — MVP post-hoc. Hooks real-time (Onda β) e features do context-tree (Onda γ) são bloqueadas até esta validar.

## Pra que serve

Transforma os `~/.claude/projects/*/sessions/*.jsonl` (JSONL natural do Claude Code com thinking blocks em texto plain) em base de conhecimento agregada. Em vez de cada sessão morrer com seus learnings, patterns de pensamento são capturados retroativamente pra alimentar a context-tree.

## Como rodar

### Pré-requisitos

```bash
pip install pyyaml
```

(Não precisa de API key nem LLM externo — regex puro.)

### Execuções comuns

```bash
# Rodar no histórico completo
python parser.py

# Só sessões desde uma data
python parser.py --since 2026-04-01

# Filtrar por projeto (substring em cwd)
python parser.py --project skillforge-arsenal

# Dry-run — calcula mas não escreve
python parser.py --dry-run

# Validar precisão (mostra 10 exemplos por categoria no stderr)
python parser.py --sample 10

# Só uma categoria (nome exato do patterns.yaml)
python parser.py --category "Erros do Claude"
```

### Output

Escreve 5 arquivos em `~/.claude/context-tree/patrick-pessoal/skills-ecosystem/`:

- `erros-do-claude.md`
- `iron-law-gaps.md`
- `decisoes-arquiteturais.md`
- `applied-learnings.md`
- `skill-invocations.md`

Cada arquivo tem:
- **Frontmatter YAML** compatível com context-tree (source, category, generated_at, maturity, importance, connects_to)
- **Breakdown por pattern** (tabela de contagens)
- **Tabela consolidada** (1 linha por match)
- **Trechos com contexto** (match + janela configurada)

## Como adicionar pattern novo

Abra `patterns.yaml` e adicione uma entrada em `patterns` da categoria relevante:

```yaml
- label: "meu-pattern"              # short tag pra dedup + output
  regex: '\b(foo|bar)\s+baz\b'       # regex raw (multi-token obrigatório)
  flags: ["I"]                       # I=case-insensitive, M=multiline, S=dotall
  context_window: {before: 3, after: 5}
```

**Convenções de qualidade:**
- Multi-token obrigatório (evita false-positive de palavra única)
- Case-insensitive por default ("I")
- Use negative lookahead pra reduzir ruído (ex: `(?!palavra)`)
- Teste em `--sample 10` antes de rodar full

## Como interpretar os matches

Cada match tem:
- **Timestamp** — quando aconteceu
- **Session + slug** — qual sessão do Claude Code (agrupa thinking/tool/text)
- **cwd** — projeto onde rolou
- **Pattern label** — qual regex casou
- **Match (literal)** — texto exato que o regex pegou
- **Trecho (contexto)** — janela configurada (antes/depois) pra dar contexto

**False-positive típico:** match isolado sem contexto relacionado. Ex: regex de "escolhi X porque Y" pegando uma explicação genérica, não uma decisão arquitetural real. Se >30% dos matches de uma categoria forem assim, ajustar regex (adicionar negative lookahead ou aumentar contexto).

## Validação (checkpoint α)

Critério de sucesso da Onda α:
- **≥70% dos matches de cada categoria são úteis** (julgamento do Patrick em amostra)
- **≥3 das 5 categorias passam** → onda α aprovada, desbloqueia β
- **<3 das 5 passam** → reavalia patterns (max 2 iterações) ou aborta

Rodar `python parser.py --sample 10` e Patrick classifica os 50 exemplos (10 × 5 categorias) como útil / ruído.

## Troubleshooting

**"logs_root não existe"** — ajuste `logs_root` em `patterns.yaml`. Default é `~/.claude/projects`.

**Match muito longo no output** — o `context_window` gera trechos grandes. Reduza `before`/`after` no pattern específico em `patterns.yaml`.

**Muitos matches numa categoria (>500)** — ajuste `max_matches_per_category` em settings do yaml. Default 500 pra evitar arquivo gigante.

**Regex match travando / muito lento** — evite `.*` ambíguo. Use `[^.]{0,N}?` (non-greedy bounded).

## Arquitetura

```
scripts/semantic-triggers/
├── parser.py          # lógica + CLI
├── patterns.yaml      # configuração (5 categorias × N patterns cada)
└── README.md          # este arquivo

~/.claude/context-tree/patrick-pessoal/skills-ecosystem/
├── handoff-wave-c-2026-04-18.md    # (existente)
├── erros-do-claude.md                # output α
├── iron-law-gaps.md                  # output α
├── decisoes-arquiteturais.md         # output α
├── applied-learnings.md              # output α
└── skill-invocations.md              # output α
```

## Próximas ondas (gate-locked)

### Onda β — Hook real-time
Depende de α validar. Hook `Stop` que aplica os mesmos patterns em tempo real + append incremental.

### Onda γ — Features do context-tree
Depende de β validar. `--ingest` automático em plan mode, `--lint` com contradições, `--archive-findings`.

Ver plan completo em `~/.claude/plans/snazzy-shimmying-prism.md` ou no seed `D:\DOWNLOADS\context-tree-evolution-prompt.md`.
