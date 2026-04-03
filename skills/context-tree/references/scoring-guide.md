# Scoring Guide — Detailed Criteria

Consulte este arquivo no **Phase 2** quando for adicionar ou auditar entries.

---

## Importance Score (0-100)

### Detailed Criteria by Range

#### 80-100: Core Knowledge
- Seminal works (books, frameworks, methodologies that define a field)
- Architectural decisions with long-term impact
- Lessons learned from critical incidents (postmortems, production failures)
- Foundational patterns used across multiple projects

**Examples:**
- "Clean Architecture by Robert C. Martin" → importance: 90
- "Postmortem: cascade failure from missing circuit breaker in payment service" → importance: 95
- "React Server Components mental model" → importance: 82

#### 50-79: Useful Knowledge
- Practical frameworks applied in current work
- Techniques validated in real projects
- Cross-domain insights connecting two areas
- Best practices for specific tools/technologies

**Examples:**
- "RICE prioritization framework for backlog" → importance: 65
- "shadcn/ui compound component patterns" → importance: 58
- "Supabase RLS patterns for multi-tenant" → importance: 72

#### 30-49: Supplemental Knowledge
- Interesting articles with one useful takeaway
- Alternative approaches not yet validated
- Historical context (how we got here)
- Conference talks with practical tips

**Examples:**
- "Article on micro-frontends at Netflix" → importance: 40
- "Alternative to Zustand: Jotai atomic state model" → importance: 35

#### 0-29: Marginal Knowledge
- Passing mentions for completeness
- Outdated approaches still occasionally referenced
- Tools evaluated but not adopted
- General industry news without actionable insight

**Examples:**
- "CoffeeScript existed before TypeScript" → importance: 10
- "Tool X evaluated, decided against for reason Y" → importance: 25

### Score Adjustments

| Event | Adjustment | Rationale |
|-------|-----------|-----------|
| User searched for this knowledge | +3 | Demand-driven relevance |
| User manually curated/edited | +5 | Human validation |
| Used as reference in a decision | +5 | Proven utility |
| Connected to 3+ other entries | +3 | High connectivity = high value |
| Not accessed in 30 days | -2 | Fading relevance (draft only) |

---

## Maturity Tiers

### draft

**What it means:** Newly added, not yet applied in a real context.

**Criteria:**
- Just discovered or cataloged
- Seems relevant but unproven
- May have been added from research, not experience

**Transitions to validated:** When the user applies it in a real project and confirms it worked.

**Decay risk:** YES — if importance <35 AND not accessed for 21 days, becomes archive candidate.

### validated

**What it means:** Applied in a real context, confirmed useful.

**Criteria:**
- User explicitly confirmed value ("yes, this worked")
- Referenced during actual implementation or decision
- Connected to concrete outcomes

**Transitions to core:** When referenced 3+ times across different contexts.

**Decay risk:** NO — validated knowledge is preserved indefinitely.

### core

**What it means:** Foundational knowledge referenced repeatedly. Part of the user's mental model.

**Criteria:**
- Referenced in 3+ different conversations or projects
- Shapes decisions consistently
- Would be a significant loss if forgotten

**Decay risk:** NEVER — core knowledge is permanent.

---

## Archive Process

### Criteria (ALL must be true)

1. `maturity = draft`
2. `importance < 35`
3. `last_accessed` > 21 days ago

### Archive Format

Original entry moved to `[domain]/_archive/[topic].md` as a one-line stub:

```markdown
---
topic: [name]
archived: [YYYY-MM-DD]
original_importance: [score]
reason: decay (draft + low importance + stale)
---

[One-line summary]. Full content recoverable via git history.
```

### Recovery

If an archived entry becomes relevant again:
1. Restore from `_archive/` to parent domain directory
2. Re-score importance
3. Set maturity to `draft` (needs re-validation)
4. Update indexes

---

## Entry Format (Full)

```markdown
---
topic: [descriptive name]
domain: [domain directory name]
importance: [0-100]
maturity: [draft|validated|core]
added: [YYYY-MM-DD]
last_accessed: [YYYY-MM-DD]
connections:
  - [domain/topic] — [relationship type: complements|contradicts|extends|replaces]
tags: [optional, for cross-cutting concerns]
---

## Summary
[2-3 sentences: what is this knowledge and why does it matter]

## Key Insights
- [Bullet points of actionable takeaways]

## Source
[Where this came from: book, article, experience, conversation]

## Application Notes
[How/when this was applied, if validated]
```

---

## Index Formats

### Domain _index.md

```markdown
# [Domain] — Knowledge Index

Last updated: [YYYY-MM-DD]
Entries: [count] | Core: [count] | Validated: [count] | Draft: [count]

## Entries (by importance)

| Topic | Importance | Maturity | Last Accessed | Connections |
|-------|-----------|----------|---------------|-------------|
| [topic] | [score] | [tier] | [date] | [count] |

## Archive Candidates
[List entries meeting decay criteria]
```

### Root _manifest.md

```markdown
# Context Tree Manifest

Last updated: [YYYY-MM-DD]
Total entries: [count] | Domains: [count] | Connections: [count]

## Domains

| Domain | Entries | Core | Validated | Draft | Health |
|--------|---------|------|-----------|-------|--------|

## Cross-Domain Connections
[Top connections between domains]

## Maintenance
- Last prune: [date]
- Archive candidates: [count]
- Orphan entries (0 connections): [count]
```
