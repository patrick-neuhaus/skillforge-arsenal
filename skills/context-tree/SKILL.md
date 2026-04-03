---
name: context-tree
description: "Hierarchical knowledge management system with scoring and decay. Organizes domain knowledge across skills using importance scoring, maturity tiers, and automatic archival. Use when user asks to: organize knowledge, 'quero catalogar isso', score references, manage context tree, 'o que já sei sobre X?', prune stale knowledge, knowledge base status, cross-domain connections, 'conecta isso com o que já tenho'. Supports: add entries, query knowledge, prune stale, view status."
---

# Context Tree

IRON LAW: NEVER add knowledge without scoring it — unscored knowledge becomes noise. Every entry gets importance (0-100) + maturity tier.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--add` | Add new knowledge entry with scoring | - |
| `--query <q>` | Search knowledge base by topic | - |
| `--prune` | Archive stale entries (draft + low importance + >21d) | - |
| `--status` | Show tree overview with health metrics | default |
| `--connect` | Find cross-domain connections for an entry | - |

## Workflow

```
Context Tree Progress:

- [ ] Phase 1: Detect Operation
  - [ ] 1.1 Parse user intent (add/query/prune/status/connect)
  - [ ] 1.2 Identify target domain
- [ ] Phase 2: Execute
  - [ ] Load references/scoring-guide.md
  - [ ] 2.1 [add] Score entry + find connections + save
  - [ ] 2.2 [query] Search indexes + return ranked results
  - [ ] 2.3 [prune] Find candidates + archive
  - [ ] 2.4 [status] Scan tree + report health
  - [ ] 2.5 [connect] Find cross-domain links
- [ ] Phase 3: Update Indexes
  - [ ] 3.1 Update domain _index.md
  - [ ] 3.2 Update root _manifest.md
```

## Tree Structure

```
context-tree/
├── _manifest.md              # Root index — all domains + health metrics
├── [domain]/                 # One dir per knowledge domain
│   ├── _index.md             # Domain index — all entries + scores
│   ├── [topic].md            # Individual knowledge entries
│   └── _archive/             # Stale entries (searchable stubs)
```

Domains correspond to skill areas: `frontend/`, `infra/`, `product/`, `leadership/`, `security/`, etc.

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
3. Connect: Find at least 1 connection with existing entries
4. Save: Create `[domain]/[topic].md` with frontmatter
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

### --query

1. Search `_manifest.md` for domain match
2. Search domain `_index.md` for topic match
3. Return ranked by importance, show connections
4. If cross-domain, check connected domains too

### --prune

1. Scan all domains for decay candidates
2. Present candidates with scores and last access date
3. ⛔ **GATE:** User confirms before archiving
4. Move to `_archive/` as one-line stubs

### --status

Report:
```markdown
## Context Tree Health

| Domain | Entries | Core | Validated | Draft | Archive Candidates |
|--------|---------|------|-----------|-------|--------------------|

**Total entries:** X
**Cross-domain connections:** Y
**Prune candidates:** Z (draft + low importance + >21d stale)
```

### --connect

1. Take an entry and scan all domains for related knowledge
2. Suggest connections based on keyword overlap and domain relationships
3. Update both entries with bidirectional links

## Anti-Patterns

- **Dump without scoring** — every entry needs importance + maturity. No exceptions.
- **Never pruning** — tree grows into noise. Run `--prune` monthly.
- **Isolated entries** — knowledge without connections is a dead note. Find at least 1 link.
- **Duplicate entries** — search before adding. Update existing entries instead.
- **Over-archiving** — validated/core entries never decay. Only draft + low importance.
- **Storing code patterns** — code belongs in the codebase, not the tree. Store decisions and rationale.

## Pre-Delivery Checklist

Before adding knowledge:
- [ ] Scored with importance (0-100) and maturity tier
- [ ] At least 1 connection with existing entry
- [ ] Domain correctly identified
- [ ] Not a duplicate of existing entry
- [ ] Content is actionable, not just informational
- [ ] Index files updated

## When NOT to use

- Storing code snippets → keep in codebase or skill references
- Git history / changelog → use `git log`
- Temporary task tracking → use tasks/todos
- Documentation → belongs in project docs, not knowledge tree

## Integration

- **Reference Finder** — findings can be scored and added to tree
- **Skill Builder** — skill domain knowledge feeds into tree
- **SDD** — research phase can query tree for existing domain knowledge
