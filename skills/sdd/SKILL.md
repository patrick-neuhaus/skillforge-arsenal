---
name: sdd
description: "Spec Driven Development — anti-vibecoding workflow. Four-phase pipeline: Research codebase, write detailed Spec, Implement with fresh context, Review with Trident. Prevents context window bloat and ensures deterministic implementation. NOT the same as Claude Code native plan mode — this is a full spec-driven pipeline with Trident review. Use when user asks to: implement a feature, 'quero adicionar funcionalidade', build something new, 'como implemento isso?', plan implementation, 'faz um plano antes', 'planeja antes de codar', 'antes de sair codando', 'planeja antes de implementar', 'não sai codando', anti-vibecoding, spec driven, '/research', '/spec', '/implement', plan before coding, structured implementation, spec first then code. Supports: full pipeline, individual phases."
---

# SDD — Spec Driven Development

IRON LAW: NEVER skip a phase. Research → Spec → Implement → Review. Each phase starts with `/clear` to reclaim context window. No spec, no code.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--phase <p>` | Run specific phase: research, spec, implement, review | auto (next phase) |
| `--target <t>` | Feature description or scope | - |
| `--resume` | Continue from last completed phase | - |

## Workflow

```
SDD Progress:

- [ ] Phase 1: Research ⚠️ REQUIRED
  - [ ] 1.1 Analyze codebase structure and patterns
  - [ ] 1.2 Identify relevant files and dependencies
  - [ ] 1.3 Check existing conventions
  - [ ] 1.4 Generate prd.md (compact handoff document)
  - [ ] ⛔ GATE: User reviews prd.md before proceeding
- [ ] Phase 2: Spec
  - [ ] 2.1 Read prd.md
  - [ ] 2.2 Define exact file paths and actions (create/modify/delete)
  - [ ] 2.3 Write pseudocode for each file change
  - [ ] 2.4 Generate spec.md
  - [ ] ⛔ GATE: User reviews spec.md before proceeding
- [ ] Phase 3: Implement
  - [ ] 3.1 Read spec.md (sole source of truth)
  - [ ] 3.2 Execute changes file by file
  - [ ] 3.3 Run tests after each file
- [ ] Phase 4: Review
  - [ ] 4.1 Invoke Trident on all changes
  - [ ] 4.2 Present findings
```

## Phase 1: Research

**Goal:** Understand the codebase well enough to write a precise spec. Output: `prd.md`.

Load `references/research-checklist.md` for the complete investigation checklist.

1. **Query context-tree first** — check if domain knowledge already exists before searching from scratch
2. **Search for reusables** — before creating anything new, scan codebase for existing components/functions that solve the same problem. Load `references/dedup-checklist.md`
3. **Read project structure** — `ls`, package.json, folder conventions
4. **Identify the area of change** — which modules, files, patterns are involved
5. **Check conventions** — naming, imports, state management, testing, file organization
6. **Map dependencies** — what touches the area of change
7. **Import external patterns (optional)** — use `.tmp` technique to clone reference repos and extract patterns. Load `references/tmp-technique.md`
8. **Over-engineering check** — is there a simpler solution already in the codebase?
9. **Document findings** in `prd.md` (see `references/prd-example.md` for format)

### prd.md Format

```markdown
# PRD: [Feature Name]

## Context
[What the feature does, why it's needed — from user input]

## Codebase Analysis
- **Stack:** [framework, language, key libs]
- **Relevant files:** [list with brief description of each]
- **Conventions:** [naming, patterns, testing approach observed]
- **Dependencies:** [what the changed area touches]

## Constraints
[Technical constraints, existing patterns to follow, gotchas found]

## Scope
[What's IN scope and what's explicitly OUT of scope]
```

⛔ **GATE:** User must review `prd.md` before proceeding. Ask: "PRD ready. Review and confirm to proceed to spec phase."

**After approval:** Tell user to `/clear` and start Phase 2 with `--phase spec`.

## Phase 2: Spec

**Goal:** Translate PRD into exact implementation instructions. Output: `spec.md`.

**Rule:** spec.md must be so specific that a fresh conversation can implement it without any other context. Every file path is exact. Every action is explicit.

Load `references/spec-writing-guide.md` for the complete path→action format and examples.
Load `references/spec-structures.md` for page/component/behavior decomposition and issue breakdown patterns.

1. Read `prd.md`
2. For large features: decompose into atomic issues by behavior (1 issue = 1 behavior or 1 page). Prototype issues first, then functional issues.
3. For each change, specify:
   - **File path** — exact path
   - **Action** — create / modify / delete
   - **What** — pseudocode or exact code for the change
   - **Why** — brief rationale

### spec.md Format

```markdown
# Spec: [Feature Name]

## Changes

### 1. [File path] — [create/modify/delete]
**What:** [Pseudocode or exact description]
**Why:** [Rationale]

### 2. [File path] — [create/modify/delete]
**What:** [Pseudocode or exact description]
**Why:** [Rationale]

## Testing
[What to test and how]

## Rollback
[How to undo if something goes wrong]
```

⛔ **GATE:** User must review `spec.md` before proceeding. Ask: "Spec ready. Review and confirm to proceed to implement phase."

**After approval:** Tell user to `/clear` and start Phase 3 with `--phase implement`.

## Phase 3: Implement

**Goal:** Execute spec.md changes with fresh context. No improvisation.

1. Read `spec.md` — this is the sole source of truth
2. Execute changes file by file, in order
3. After each file: run tests or type check if available
4. If spec is ambiguous, STOP and ask user — do NOT improvise

**Context window rule (40-50%):** Never use more than half the context window. If approaching the limit, `/clear` and resume with spec.md. Quality degrades silently past 50%.

## Phase 4: Review

**Goal:** Verify implementation quality using Trident.

1. Invoke Trident on all changes: `trident --mode all-local`
2. Present findings
3. Fix confirmed bugs (with user approval)

## Anti-Patterns

- **Skipping research** — "just implement it" leads to rework. Research takes 5min, rework takes hours.
- **Vague spec** — "add authentication" is not a spec. Every file path must be exact.
- **Improvising during implement** — spec says what to do. If spec is wrong, go back to spec phase.
- **Not clearing context** — bloated context = degraded quality. `/clear` between phases.
- **Spec too large** — >20 file changes? Split into 2+ specs. Implement in batches.
- **Skipping review** — untested code is unfinished code. Trident catches what you miss.

## Pre-Delivery Checklist

Per phase:
- **Research:** prd.md has codebase analysis, constraints, scope boundary
- **Spec:** Every change has exact path + action + pseudocode
- **Implement:** All spec items completed, tests passing
- **Review:** Trident run, findings addressed

## When NOT to use

- One-line fix or trivial change → just do it
- Exploratory/prototype work → vibecoding is fine for throwaway code
- Bug fix where the problem is already clear → skip research, go to spec
- Confused about which skill to use → invoke maestro

## Integration

- **Trident** — used in Phase 4 for code review
- **Architecture Guard** — use after implement to validate architectural rules (thin client/fat server)
- **Code Dedup Scanner** — use in Phase 1 to find reusable code before creating new
- **Pattern Importer** — use in Phase 1 for `.tmp` technique (import external patterns)
- **Context Guardian** — use between phases to monitor context window and generate handoffs
- **React Patterns** — use `--scaffold` during implement phase for React features
- **Component Architect** — use `--plan` during spec phase for component work
