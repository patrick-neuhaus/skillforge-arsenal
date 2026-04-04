---
name: geo-optimizer
description: "Optimize skill descriptions, READMEs, and package metadata for Generative Engine Optimization (GEO) — making them discoverable by AI agents, not just humans. Use when user wants to: optimize description, improve triggering, GEO, keyword bombing, 'minha skill não aciona', 'ninguém acha minha skill', 'a description tá fraca', improve discoverability, 'otimizar pra agentes', 'melhorar a description', agent discovery, optimize for Find Skills, skills.sh optimization, skill SEO, 'como faço minha skill ser encontrada', package metadata, 'a skill não aparece nas buscas'. Also: analyze Find Skills algorithm, generate keywords, benchmark description quality."
---

# GEO Optimizer — Generative Engine Optimization

IRON LAW: NEVER optimize a description without generating keywords from the agent's perspective first. The agent is the customer, not the human — ask Claude what IT would search for before writing a single word.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--analyze` | Analyze existing description and score quality | default |
| `--optimize` | Full optimization: analyze → keywords → rewrite → validate | - |
| `--benchmark` | Compare description against top skills in same domain | - |
| `--keywords` | Generate keyword list only (no rewrite) | - |

## Workflow

```
GEO Optimizer Progress:

- [ ] Step 1: Analyze Current State ⚠️ REQUIRED
  - [ ] 1.1 Read the current description (or accept text input)
  - [ ] 1.2 Score against GEO checklist
  - [ ] 1.3 Identify gaps (missing verbs, nouns, phrases, differentiation)
- [ ] Step 2: Generate Keywords ⚠️ REQUIRED
  - [ ] 2.1 Agent-perspective keyword generation
  - [ ] 2.2 Domain mapping (verbs, nouns, natural phrases PT-BR + EN)
  - [ ] 2.3 Competitor analysis (optional — for skills.sh publishing)
- [ ] Step 3: Rewrite ⛔ BLOCKING
  - [ ] 3.1 Draft optimized description
  - [ ] 3.2 Validate against checklist
  - [ ] 3.3 Check character limit (1024 max)
  - [ ] ⛔ GATE: Present before/after comparison to user
```

If `--analyze`: Execute Steps 1 only → report score and gaps.
If `--keywords`: Execute Steps 1-2 only → return keyword list.
If `--benchmark`: Execute Step 1 + compare against top skills in same domain.

## Step 1: Analyze Current State

Read the description and score each dimension:

| Dimension | Score | Criteria |
|-----------|:-----:|----------|
| Core capability | 0-2 | First sentence clearly states what it does (2) / vague (1) / missing (0) |
| Action verbs | 0-3 | 5+ (3) / 3-4 (2) / 1-2 (1) / 0 (0) |
| Domain nouns | 0-3 | 5+ (3) / 3-4 (2) / 1-2 (1) / 0 (0) |
| Natural phrases PT-BR | 0-2 | 3+ (2) / 1-2 (1) / 0 (0) |
| Natural phrases EN | 0-2 | 3+ (2) / 1-2 (1) / 0 (0) |
| Differentiation | 0-2 | Clear "don't use for X" (2) / partial (1) / none (0) |
| Length | 0-1 | Under 1024 chars (1) / over (0) |

**Total: /15.** Rating: 12-15 = Excellent, 8-11 = Good, 4-7 = Needs Work, 0-3 = Critical.

Load `references/find-skills-analysis.md` for how ranking algorithms weight these dimensions.

## Step 2: Generate Keywords

### 2.1 Agent-Perspective Generation

Ask Claude (literally — use this prompt):

```
"Se voce fosse um agente de IA buscando uma ferramenta que [o que a skill faz],
quais termos voce usaria? Liste:
- 10+ verbos de acao (PT-BR e EN)
- 10+ substantivos de dominio
- 5+ frases naturais em PT-BR que um dev digitaria
- 5+ frases naturais em EN
- 3+ formas alternativas de descrever o mesmo problema"
```

### 2.2 Domain Mapping

Load `references/keyword-generation.md` for domain-specific keyword templates.

Organize keywords into:
- **Must-have:** keywords that MUST appear (core functionality)
- **Should-have:** keywords that improve coverage
- **Nice-to-have:** edge case triggers

### 2.3 Competitor Analysis (optional)

If publishing to skills.sh:
- Search similar skills: `npx skills find <query>`
- Analyze top 5 descriptions
- Identify gaps — keywords they miss that you should cover
- Identify overlaps — differentiate explicitly

## Step 3: Rewrite

Load `references/examples.md` for before/after examples.

### Structure

```
[Core capability — 1 sentence, what it does]
[Key techniques/features — comma-separated list]
Use when/SEMPRE que: [natural phrases PT-BR], [natural phrases EN]
[Differentiation: NÃO use pra X — use Y]
```

### Validation Checklist

- [ ] First sentence = core capability (no adjectives, no marketing)
- [ ] 5+ action verbs present
- [ ] 5+ domain nouns present
- [ ] 3+ natural phrases PT-BR
- [ ] 3+ natural phrases EN
- [ ] Clear differentiation with similar skills
- [ ] Under 1024 characters
- [ ] Zero marketing adjectives ("powerful", "advanced", "cutting-edge")
- [ ] No redundant phrases (same idea said twice)

⛔ **GATE:** Present before/after comparison with score delta. User must approve.

## Anti-Patterns

- **Marketing speak:** "A powerful AI-powered tool for..." — agents don't care about adjectives
- **Only EN or only PT-BR:** Missing half the trigger surface. Always include both
- **No differentiation:** Similar skills steal triggers. "NÃO use pra X" is required
- **Keyword stuffing:** Cramming irrelevant terms degrades precision. Every keyword must be honest
- **Copy-paste from similar skill:** Each skill has unique keywords. Generate fresh, don't borrow
- **Description > 1024 chars:** Hard limit on skills.sh. Prioritize high-impact keywords

## Pre-Delivery Checklist

- [ ] Score improved from before (show delta)
- [ ] All must-have keywords present
- [ ] Under 1024 characters
- [ ] Before/after comparison presented to user
- [ ] User approved the new description

## When NOT to use

- Writing the full SKILL.md → use **skill-builder**
- Optimizing prompts (not descriptions) → use **prompt-engineer --geo**
- Creating a skill from scratch → use **skill-builder --full** (includes GEO step)

## Integration

- **skill-builder** — Step 4 of skill-builder calls geo-optimizer for description quality
- **prompt-engineer** — `--geo` mode handles prompt-level GEO; this skill handles description-level
- **maestro** — use when optimizing descriptions across multiple skills in batch
