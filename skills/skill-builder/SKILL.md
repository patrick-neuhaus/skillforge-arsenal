---
name: skill-builder
description: "Create, improve, and optimize Claude Code skills with battle-tested techniques. Expert guidance on skill architecture, progressive loading, workflow design, description optimization (GEO), and packaging. Use when user wants to: create skill, build skill, new skill, improve skill, refactor skill, debug skill, package skill, evolve skill, write SKILL.md, 'transforma isso numa skill', 'quero automatizar esse processo', 'a skill tá ruim', 'a skill não tá funcionando', update skill, edit skill, test skill, optimize description, 'capturar esse workflow', 'salvar esse processo', scaffold skill, init skill, validate skill. Na dúvida entre skill e prompt: 'Instruções persistentes pro Claude (skill) ou prompt avulso?'"
---

# Skill Builder

> **Templates source (Wave 2):** `~/.claude/library/templates/{templates,cli-first-template,design-skill-template}.md` (canonical). Local `references/` kept 7d backup. v3

IRON LAW: NEVER generate a skill without reading 2+ existing skills as reference first. Copying patterns from real skills that work beats inventing from scratch every time.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--quick` | Scaffold only (structure + frontmatter + TODOs) | false |
| `--full` | Full guided process with all steps (includes Step 0) | true |
| `--evolve` | Improve existing skill (read → diagnose → improve) | false |
| `--evolve --light` | Small edits: boundary notes, examples, anti-patterns (skips Step 0) | false |
| `--evolve --heavy` | Restructure: workflow, IRON LAW, references (runs full validation) | false |
| `--validate` | Run validation only on existing skill (structure + content + handoff to prompt-engineer for text) | false |
| `--skill-prompt` | Optimize prompts/text WITHIN a SKILL.md (migrated from prompt-engineer in v3) | false |

## Workflow

Copy this checklist and track progress:

```
Skill Builder Progress:

- [ ] Step 0: Pre-build Research ⚠️ REQUIRED ⛔ BLOCKING (v3 NEW)
  - [ ] 0.1 Run the 8 questions (see Step 0 section below)
  - [ ] 0.2 If 3+ fail → REFUSE creation, recommend 2h spike instead
  - [ ] 0.3 If passes, document answers in skill-rationale.md (lives next to SKILL.md)
- [ ] Step 1: Understand ⚠️ REQUIRED
  - [ ] 1.1 Read 2+ reference skills (IRON LAW)
  - [ ] 1.2 Clarify purpose, problem, use cases
  - [ ] 1.3 Collect 3+ concrete examples ("I say X, Claude does Y")
- [ ] Step 2: Research Domain (conditional — skip for operational skills)
  - [ ] 2.1 Search frameworks and methodologies
  - [ ] 2.2 Transform references into instructions
- [ ] Step 3: Plan Architecture
  - [ ] 3.1 Choose agentic pattern (default: Linear)
  - [ ] 3.2 Identify scripts, references, assets
  - [ ] 3.3 Design progressive loading (<250 lines in SKILL.md)
- [ ] Step 4: Write Description ⚠️ REQUIRED
  - [ ] 4.1 Apply keyword bombing (GEO)
  - [ ] 4.2 Verify under 1024 characters
  - [ ] ⛔ GATE: Present description to user for approval
- [ ] Step 5: Write SKILL.md ⚠️ REQUIRED
  - [ ] 5.1 Set Iron Law
  - [ ] 5.2 Design workflow checklist with ⚠️/⛔ markers
  - [ ] 5.3 Write instructions (question-style)
  - [ ] 5.4 Add confirmation gates before destructive/generative ops
  - [ ] 5.5 Add anti-patterns list
  - [ ] 5.6 Add pre-delivery checklist
  - [ ] 5.7 Verify SKILL.md under 250 lines
- [ ] Step 6: Build Resources (conditional)
  - [ ] 6.1 Scripts for deterministic operations
  - [ ] 6.2 Reference files for domain knowledge
- [ ] Step 7: Validate ⛔ BLOCKING
  - [ ] Run pre-delivery checklist
  - [ ] ⛔ GATE: Present complete skill to user for approval
```

If `--quick`: Execute Step 1.1 → scaffold with `scripts/init_skill.py` → done.
If `--evolve`: Read existing skill → diagnose with checklist → improve → validate.
If `--validate`: Skip to Step 7 only.

## Step 0: Pre-build Research ⚠️ REQUIRED ⛔ BLOCKING (v3)

Load `references/step-0-pre-build-research.md` for the 8 blocking questions + gate logic.

**Purpose:** before creating a new skill, verify it makes sense vs using existing tools. User already has 40+ skills — innovation tokens are limited (Choose Boring Technology). Building "skill 41 to solve the problem of having too many skills" is self-parody.

**Gate:** if 3+ questions fail → REFUSE creation, recommend a 2h spike using `reference-finder --solution-scout <topic>` first. Return to skill-builder only after the spike produced evidence that no existing solution serves.

**Skip only if:** `--evolve --light` (surgical textual edit on existing skill that already passed Step 0).

## Step 1: Understand ⚠️ REQUIRED

### 1.1 Read Reference Skills (IRON LAW)

Before anything else, read 2+ existing skills similar in domain or pattern:
- Skills in the current project (`skills/`)
- Community skills (`community/`)
- Ask: "What existing skill is closest to what you want?"

Extract: structure, description style, workflow pattern, edge case handling.

### 1.2–1.3 Discovery

Load `references/discovery-guide.md` for the complete question framework.

Key questions (start here, dig deeper with the guide):
- What does this skill do that Claude can't already do well on its own?
- What would you literally type to trigger it? Give me 3+ examples.
- What should this skill NOT do?

If the user said "transforma isso numa skill" mid-conversation, extract the workflow from history first — present what you captured and ask for confirmation.

## Step 2: Research Domain (conditional)

**Skip** for operational/technical skills (CSV converter, file formatter, API wrapper).

**Do** for domain skills (UX, sales, security, management): search frameworks and methodologies. The goal is to transform domain knowledge into executable instructions — not citations.

Load `references/writing-guide.md` for research patterns and the principle hierarchy.

## Step 3: Plan Architecture

Load `references/agentic-patterns.md` to choose the right pattern.

Ask: Is this process linear? Does it need adversarial verification? Independent parallel analyses? Self-evaluation? Default to Linear — only add complexity when Linear fails.

Load `references/cli-first-template.md` if the skill wraps a CLI tool or API.
Load `references/design-skill-template.md` if the skill involves visual output or branding.

Key constraints:
- SKILL.md must stay under 250 lines — move everything else to `references/`
- References organized by domain, one level deep, each with "when to load" pointer
- Scripts for deterministic, repeatable operations only

## Step 4: Write Description ⚠️ REQUIRED

Load `references/description-guide.md` for the keyword bombing technique (GEO).
Load `references/geo-module.md` for the full GEO process (keyword generation via Claude, Find Skills analysis).

Four dimensions of a great description:
1. **Core capability** — first sentence, what it does
2. **Action verbs** — 5+ things users ask to do
3. **Object nouns** — 5+ things users mention
4. **Natural phrases** — what users would literally type

All "when to use" info goes HERE in the description — the SKILL.md body loads after triggering, which is too late.

⛔ **Confirmation Gate:** Present the description to the user before proceeding.

## Step 5: Write SKILL.md ⚠️ REQUIRED

Load `references/writing-guide.md` for principles, techniques, and examples.
Load `references/templates.md` for templates by skill type (process, technical, audit).

### Required structure

```
skill-name/
├── SKILL.md           # <250 lines — workflow + instructions
├── scripts/           # Deterministic ops (no context cost)
├── references/        # Loaded on demand via pointers
└── assets/            # Used in output, never loaded into context
```

### Seven elements every skill needs

1. **Iron Law** — top of file, after frontmatter. Ask: "What ONE mistake will the model make?"
2. **Workflow checklist** — trackable with ⚠️ REQUIRED / ⛔ BLOCKING markers
3. **Question-style instructions** — "Ask: what happens if X is null?" beats "Handle edge cases"
4. **Confirmation gates** — before destructive/generative operations
5. **Anti-patterns** — "What would Claude's lazy default look like?" Then forbid it explicitly
6. **Pre-delivery checklist** — specific, verifiable checks (not "ensure quality")
7. **Progressive loading** — "Load references/X.md" at the step where needed, not upfront
8. **Roteiro de perguntas** — structured questions the skill asks the user when context is missing. Mandatory for non-trivial skills. Questions > instructions for gathering context

### Writing rules (summary — details in writing-guide.md)

- Imperative: "Analyze X" not "You should analyze X"
- Explain the why: each important rule has a reason
- Examples > instructions: one input/output example beats 10 lines of explanation
- Don't repeat Claude's base behavior (be polite, think step by step)
- Calibrate for Claude 4.x: clear instructions > caps lock screaming
- Portuguese brasileiro for all content, except universal technical terms

## Step 6: Build Resources

### Scripts
- Encapsulate deterministic ops (validation, conversion, search)
- In SKILL.md, document only: command + arguments + what it returns
- Test every script before packaging

### References
- Organized by domain, not by type
- One level of nesting only
- Each file has a "when to load" pointer in SKILL.md
- Files >100 lines get a table of contents

## Step 7: Validate ⛔ BLOCKING

Run `scripts/validate.py <skill-path>` for automated checks, then the manual checklist below.

### Pre-Delivery Checklist

**Structure:**
- [ ] SKILL.md under 250 lines
- [ ] Frontmatter has `name` + `description` (and optionally `allowed-tools`, `argument-hint`)
- [ ] Description uses keyword bombing — 5+ verbs, 5+ nouns, natural phrases
- [ ] No README.md or unnecessary documentation files

**Quality:**
- [ ] Has Iron Law at the top
- [ ] Has trackable workflow checklist with ⚠️/⛔ markers
- [ ] Has confirmation gates before critical operations
- [ ] Uses question-style instructions, not vague directives
- [ ] Lists anti-patterns explicitly
- [ ] References loaded progressively (not all upfront)
- [ ] Has at least 1 input/output example
- [ ] Each important rule explains why it exists

**Anti-Patterns (fix ANY of these before delivery):**
- SKILL.md over 250 lines → move content to references/
- No workflow → model freestyles without structure
- Vague description like "A tool for X" → apply keyword bombing
- No Iron Law → model takes shortcuts
- No confirmation gates → model runs unchecked
- "When to Use" in body instead of description → too late to trigger
- Placeholders left (TODO, FIXME) → fill or remove
- Excessive MUST/NEVER without explanation → explain why instead
- Copy-pasted docs → extract principles, transform into instructions

⛔ **Confirmation Gate:** Present the complete skill to the user. Get explicit approval before considering it done.

## Integration & Boundaries

### Skills invoked during workflow

| Step | Skill | When |
|------|-------|------|
| 0 | **reference-finder --solution-scout** | Step 0 Q3: search existing solutions before building |
| 2 | **reference-finder** | Research domain frameworks and methodologies |
| 5+7 | **prompt-engineer --validate --type system-prompt** | After writing SKILL.md text — validates rubric + detects anti-patterns (caps, all-negatives, encyclopedia). skill-builder owns structure; prompt-engineer owns textual quality. |

### Boundary with prompt-engineer (v3)

| Task | Skill |
|------|-------|
| Structure of SKILL.md (line count, frontmatter, references org) | **skill-builder --validate** |
| Internal text of SKILL.md (Iron Law, instructions, examples) | **prompt-engineer --validate --type system-prompt** |
| Create new SKILL.md from scratch | **skill-builder --full** |
| Small textual edit in SKILL.md (boundary note, example) | **skill-builder --evolve --light** |
| Major refactor of SKILL.md (workflow, Iron Law core) | **skill-builder --evolve --heavy** + prompt-engineer --validate |
| Create prompt OUTSIDE SKILL.md (chatbot, agent, JSON) | **prompt-engineer --create** |
| Validate prompt OUTSIDE SKILL.md (CLAUDE.md, plans, IRON LAWS) | **prompt-engineer --validate --type <type>** |

## When NOT to use

- One-off prompt → use **Prompt Engineer**
- Lovable knowledge → use **Lovable Knowledge**
- Run an existing skill → just run it directly
- Quick question about how skills work → answer directly
