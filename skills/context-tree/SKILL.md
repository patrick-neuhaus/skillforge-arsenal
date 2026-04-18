---
name: context-tree
description: "Hierarchical knowledge management system with scoring and decay. Organizes domain knowledge across skills using importance scoring, maturity tiers, and automatic archival. Unified reader across user-level tree (~/.claude/context-tree/) and project-level byterover storage (.brv/context-tree/). Use when user asks to: organize knowledge, 'quero catalogar isso', score references, manage context tree, 'o que já sei sobre X?', prune stale knowledge, knowledge base status, cross-domain connections, 'conecta isso com o que já tenho', save this knowledge, what do I know about, knowledge base, organize what I learned. Supports: add entries, query knowledge, prune stale, view status, 'catalogar aprendizados sobre projeto', 'guardar o que aprendi', 'organizar num lugar'."
---

# Context Tree

IRON LAW: NEVER add knowledge without scoring it — unscored knowledge becomes noise. Every entry gets importance (0-100) + maturity tier.

## Storage Paths (unified read)

Context Tree lê de DUAS fontes, na ordem abaixo:

1. **User-level tree** — `~/.claude/context-tree/`
   - Root manifest: `~/.claude/context-tree/_manifest.md`
   - Domains: `~/.claude/context-tree/<domain>/_index.md` + `<topic>.md` files
   - Exemplo atual: `~/.claude/context-tree/meta/` com 9+ entries (autoparody-anti-pattern, ccinspect-vs-rubric-hybrid, community-vs-native-skills, etc.)
   - **Fonte primária** — onde entries manuais do Patrick vivem

2. **Project-level byterover storage** — `.brv/context-tree/` (relativo ao projeto atual)
   - Criado/populado pelo `brv-curate` (MCP) e `brv curate` (CLI)
   - Uma árvore por projeto (byterover tem namespace por diretório de trabalho)
   - Listar registered projects: `brv locations`
   - **Fonte secundária** — onde curates feitos durante a sessão acumulam

**Fallback order em --query:**
1. Primeiro tenta match no user-level tree (manifest + domain indexes)
2. Se não achar, tenta project-level byterover tree
3. Merge de resultados com dedup por topic name, rank por importance
4. Se zero match em ambos, retorna "no matches" + sugere `--add`

**Por que unified read resolve o gap do Teste 12:** antes da skill documentar explicitamente o path user-level, Claude precisava fazer `find` manual pra localizar `_manifest.md`. Agora o path é fonte de verdade inline aqui — zero ambiguidade.

**Por que não depende de LLM provider:** esta skill lê markdown direto e deixa o reasoning pro Claude (keyword match + rationale), sem precisar de embeddings. Funciona zero-key como fallback universal. **Observação (pós-Wave G descoberta):** byterover tem um free built-in provider (`brv providers connect byterover`) que habilita `brv query` com semantic search nativo, também zero-cost. Se o built-in tiver conectado, a unified read ainda vale como safety net — mas o primário pode ser `brv query` quando a pergunta é semântica ambígua.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--add` | Add new knowledge entry with scoring (to user-level tree) | - |
| `--query <q>` | Search unified (user-level + byterover) knowledge base by topic | - |
| `--prune` | Archive stale entries (draft + low importance + >21d, user-level only) | - |
| `--status` | Show tree overview with health metrics (both sources) | default |
| `--connect` | Find cross-domain connections for an entry | - |
| `--architecture` | Generate architecture.md from project analysis | - |
| `--skills` | Map available skills for progressive disclosure block | - |

## Workflow

```
Context Tree Progress:

- [ ] Phase 1: Detect Operation
  - [ ] 1.1 Parse user intent (add/query/prune/status/connect)
  - [ ] 1.2 Identify target domain
- [ ] Phase 2: Execute
  - [ ] Load references/scoring-guide.md
  - [ ] 2.0 Resolve storage paths:
    - User-level: ~/.claude/context-tree/_manifest.md
    - Project-level: ./.brv/context-tree/ (if initialized via `brv locations`)
  - [ ] 2.1 [add] Score entry + find connections + save to user-level
  - [ ] 2.2 [query] Unified search:
    - Read user-level manifest → match domains → read entries
    - Read project-level tree (if exists) → match → read entries
    - Merge + dedup + rank by importance
  - [ ] 2.3 [prune] Find candidates in user-level + archive
  - [ ] 2.4 [status] Scan both sources + report health
  - [ ] 2.5 [connect] Find cross-domain links
  - [ ] 2.6 [architecture] Analyze project → generate architecture.md (load references/architecture-template.md)
  - [ ] 2.7 [skills] Scan skills/ → generate progressive disclosure block for system prompt
- [ ] Phase 3: Update Indexes
  - [ ] 3.1 Update domain _index.md (user-level)
  - [ ] 3.2 Update root _manifest.md (user-level)
```

## Tree Structure

```
# User-level (~/.claude/context-tree/)
context-tree/
├── _manifest.md              # Root index — all domains + health metrics
├── [domain]/                 # One dir per knowledge domain
│   ├── _index.md             # Domain index — all entries + scores
│   ├── [topic].md            # Individual knowledge entries
│   └── _archive/             # Stale entries (searchable stubs)

# Project-level (./.brv/context-tree/ per project)
.brv/
└── context-tree/
    └── <byterover-managed structure>
```

Domains correspond to skill areas: `frontend/`, `infra/`, `product/`, `leadership/`, `security/`, `meta/` etc.

## Scoring System

Load `references/scoring-guide.md` for detailed criteria.

### Importance (0-100)

| Range | Label | Criteria |
|-------|-------|----------|
| 80-100 | **Core** | Seminal knowledge. Foundation of the domain. |
| 50-79 | **Useful** | Practical, complementary. Applied framework or technique. |
| 30-49 | **Supplemental** | Secondary resource. Context, not action. |
| 0-29 | **Marginal** | Mentioned for completeness. Not essential. |

Adjustments: +3 when searched by need, +5 when curated manually by user.

### Maturity

| Tier | Meaning | Decay? |
|------|---------|--------|
| **draft** | Newly added, not yet applied | Yes — prune candidate after 21d if importance <35 |
| **validated** | Applied in real context, confirmed useful | No |
| **core** | Referenced repeatedly, foundation of domain | Never |

### Decay Rule

Entries that meet ALL three criteria are archive candidates:
1. maturity = `draft`
2. importance < 35
3. Last accessed > 21 days ago

Archived entries become one-line stubs in `_archive/` (searchable, recoverable via git history).

## Operations

### --add

1. Ask: What's the knowledge? Which domain?
2. Score: importance (0-100) + maturity (draft/validated/core)
3. Connect: Find at least 1 connection with existing entries (search both user-level + byterover)
4. Save: Create `~/.claude/context-tree/[domain]/[topic].md` with frontmatter
5. Update: `[domain]/_index.md` + `_manifest.md`

Entry format:
```markdown
---
topic: [name]
domain: [domain]
importance: [0-100]
maturity: [draft|validated|core]
added: [YYYY-MM-DD]
last_accessed: [YYYY-MM-DD]
connections:
  - [domain/topic] — [relationship]
---

[Knowledge content — concise, actionable]
```

### --query (unified read)

1. Load `~/.claude/context-tree/_manifest.md` — parse domain list
2. For each candidate domain, read `<domain>/_index.md` for entries matching query keywords
3. Check `.brv/context-tree/` exists in cwd — if yes, scan byterover-managed entries as secondary source
4. Merge results with dedup by topic name (user-level wins on conflict)
5. Rank by importance DESC, then last_accessed DESC
6. Return top N with connections + source tag (`[user-level]` or `[byterover]`)

Example output:
```
Query: "n8n applied learnings"

[user-level] meta/autoparody-anti-pattern.md (importance=75, validated)
  → Connected: meta/constitutional-ai-drift-lesson.md
  → Excerpt: "...autoparody risk when skill references own absence..."

[byterover] curated/wave-g-correcoes.md (importance=60, draft)
  → Excerpt: "...Wave G corrigiu applied learning n8n..."
```

### --prune

1. Scan user-level tree for decay candidates (byterover has its own prune via `brv` CLI)
2. Present candidates with scores and last access date
3. ⛔ **GATE:** User confirms before archiving
4. Move to `_archive/` as one-line stubs

### --status

Report:
```markdown
## Context Tree Health

### User-level (~/.claude/context-tree/)
| Domain | Entries | Core | Validated | Draft | Archive Candidates |
|--------|---------|------|-----------|-------|--------------------|

### Project-level (.brv/context-tree/, if present)
| Project | Entries | Notes |
|---------|---------|-------|

**Total entries (unified):** X
**Cross-domain connections:** Y
**Prune candidates:** Z (user-level only)
```

### --connect

1. Take an entry and scan all domains (both sources) for related knowledge
2. Suggest connections based on keyword overlap and domain relationships
3. Update both entries with bidirectional links (user-level only — byterover entries are append-only via curate)

## Anti-Patterns

- **Dump without scoring** — every entry needs importance + maturity. No exceptions.
- **Never pruning** — tree grows into noise. Run `--prune` monthly.
- **Isolated entries** — knowledge without connections is a dead note. Find at least 1 link.
- **Duplicate entries** — search before adding (both sources). Update existing entries instead.
- **Over-archiving** — validated/core entries never decay. Only draft + low importance.
- **Storing code patterns** — code belongs in the codebase, not the tree. Store decisions and rationale.
- **MCP over CLI** — if a tool is available via CLI, prefer CLI over MCP to reduce context bloat. Load `references/cli-vs-mcp-guide.md` when detecting heavy MCP usage.
- **No brand asset mapping** — when project has a design system, map where assets live (logos, palettes, fonts) in the tree for skills like ui-design-system to find.
- **Ignoring unified read** — always check BOTH user-level and project-level sources in `--query`. Missing the byterover source means stale answers.

## Pre-Delivery Checklist

Before adding knowledge:
- [ ] Scored with importance (0-100) and maturity tier
- [ ] At least 1 connection with existing entry (searched both user-level + byterover)
- [ ] Domain correctly identified
- [ ] Not a duplicate of existing entry in either source
- [ ] Content is actionable, not just informational
- [ ] Index files updated (user-level)

## When NOT to use

- Storing code snippets → keep in codebase or skill references
- Git history / changelog → use `git log`
- Temporary task tracking → use tasks/todos
- Documentation → belongs in project docs, not knowledge tree
- Confused about which skill to use → invoke maestro
- Semantic similarity search across massive corpus → that's byterover-query with LLM provider (we use keyword + reasoning instead, zero key)

## Integration

- **Reference Finder** — findings can be scored and added to tree. When reference-finder finishes, suggest `context-tree --add` to preserve findings with scoring.
- **Skill Builder** — skill domain knowledge feeds into tree. When a new domain is explored during skill creation, add key insights to tree.
- **SDD** (Phase 1 Research) — query tree FIRST before searching from scratch. Existing knowledge in the tree avoids redundant web searches and provides instant context.
- **Maestro** — maestro can suggest context-tree as part of knowledge chains (e.g., reference-finder → context-tree).
- **Architecture Guard** — `--architecture` generates the architecture.md that architecture-guard validates against.
- **Context Guardian** — context-tree maps what consumes context; context-guardian monitors it at runtime.
- **ByteRover (brv-curate)** — curates feitos via `brv-curate` MCP vão pra `.brv/context-tree/` (project-level). Esta skill lê essa fonte no `--query` como unified read, sem precisar de LLM provider.
