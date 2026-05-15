---
name: architecture-guard
description: "Validate code implementations against architectural rules and conventions. Enforces thin client/fat server, behavior-based organization, layer separation, and project-specific rules defined in architecture.md. Use when user asks: 'tá seguindo a arquitetura?', validate architecture, check architecture rules, 'tem lógica no frontend?', 'tá respeitando thin client?', architecture lint, 'valida se tá certo a estrutura', 'o código tá no lugar certo?', guard architecture, enforce conventions, 'verificar camadas', layer violation, 'tá organizado por comportamento?', check code placement, 'antes de mergear valida a arquitetura'. Complementa o Trident: Trident busca bugs, architecture-guard busca violações estruturais."
---

# Architecture Guard — Lint de Arquitetura

IRON LAW: NEVER approve business logic in client components. If you find `use client` with fetch, mutation, validation, or state machine logic — it's a violation. No exceptions, no "it's just a small helper."

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--scan` | Scan codebase against rules | default |
| `--init` | Generate architecture.md template for the project | - |
| `--check <path>` | Check specific file/directory | - |
| `--rules` | List all active rules and their status | - |

## Workflow

```
Architecture Guard Progress:

- [ ] Phase 1: Load Rules ⚠️ REQUIRED
  - [ ] 1.1 Find and read architecture.md (or generate with --init)
  - [ ] 1.2 Load built-in rules from references/
  - [ ] 1.3 Merge: project rules override built-in defaults
- [ ] Phase 2: Scan
  - [ ] 2.1 Identify files in scope
  - [ ] 2.2 Apply each rule category
  - [ ] 2.3 Collect violations with evidence
- [ ] Phase 3: Report ⛔ BLOCKING
  - [ ] 3.1 Present violations grouped by severity
  - [ ] 3.2 Show exact file:line for each violation
  - [ ] ⛔ GATE: User decides which violations to fix
```

If `--init`: Generate `architecture.md` from `references/rule-templates.md` → ask user to customize → done.
If `--rules`: List all active rules with pass/fail status → done.

## Phase 1: Load Rules

### Finding architecture.md

Search in order:
1. `architecture.md` in project root
2. `docs/architecture.md`
3. `ARCHITECTURE.md`
4. `.claude/architecture.md`

If not found: suggest `--init` to create one. Load `references/rule-templates.md` for the template.

### Built-in Rules

Load `references/thin-client-rules.md` for the core rule set. These apply to ALL projects unless overridden.

### Rule Categories

| Category | What it checks | Severity |
|----------|---------------|:--------:|
| **Thin Client** | Business logic in client components | P0 |
| **Layer Separation** | Cross-layer imports, logic in wrong layer | P1 |
| **Behavior Organization** | Files organized by behavior vs by type | P2 |
| **Convention Compliance** | Naming, imports, patterns match project conventions | P2 |
| **Security Placement** | Auth, validation, secrets in correct layer | P0 |

## Phase 2: Scan

### Thin Client Check (P0)

Scan all files with `'use client'` or client-side indicators for:

| Violation | Pattern | Example |
|-----------|---------|---------|
| **Fetch in client** | `fetch(`, `axios.`, `supabase.from` in 'use client' file | Business logic leak |
| **Mutation logic** | Complex state machines, business rules in client | Should be server action |
| **Direct DB access** | Supabase client queries with business logic | Use server-side query |
| **Validation logic** | Zod schemas with business rules in client | Move to server, keep UI validation only |
| **Secret access** | `process.env` (non-NEXT_PUBLIC) in client | Security violation |

Load `references/thin-client-rules.md` for the complete scan patterns.

### Layer Separation Check (P1)

| Rule | Violation Example |
|------|------------------|
| UI imports data layer directly | `import { db } from '@/lib/db'` in component |
| Server action has UI logic | Returns JSX or manipulates DOM |
| Shared util has side effects | Util function that writes to DB |
| Circular dependencies | A imports B imports A |

### Behavior Organization Check (P2)

Ask: are files organized by behavior/feature or by type?

```
# BAD: organized by type (efeito cobertor de pobre)
src/
  components/     # ALL components mixed together
  hooks/          # ALL hooks mixed together
  utils/          # ALL utils mixed together

# GOOD: organized by behavior/feature
src/
  features/
    invoices/     # Everything about invoices together
      components/
      hooks/
      utils/
    auth/         # Everything about auth together
      components/
      hooks/
```

## Phase 3: Report

### Violation Format

```markdown
## Violations Found

### P0 — Must Fix (blocks merge)

#### [V001] Business logic in client component
**File:** src/components/InvoiceForm.tsx:42
**Rule:** thin-client/no-business-logic
**Evidence:** `const total = items.reduce((sum, i) => sum + i.price * i.qty, 0)`
**Fix:** Move calculation to server action or utility
**Why:** Client code is accessible "with two clicks in the browser" (Video 2)

### P1 — Should Fix

#### [V002] Cross-layer import
**File:** src/components/Dashboard.tsx:5
**Rule:** layer-separation/no-direct-db
**Evidence:** `import { supabase } from '@/lib/supabase'`
**Fix:** Use server action or query function
```

⛔ **GATE:** Present all violations. User decides which to fix. Never auto-fix architectural violations.

## Anti-Patterns

- **Over-enforcement:** Not every project needs all rules. Respect architecture.md overrides
- **False positives on simple state:** `useState` for UI state (toggle, modal open) is NOT a violation — only business state machines are
- **Ignoring project conventions:** The project's architecture.md trumps built-in rules
- **Fixing without asking:** Architecture violations often have context. Always ask before fixing
- **Checking generated code:** Skip `node_modules/`, `.next/`, `dist/`, generated files

## Pre-Delivery Checklist

- [ ] architecture.md loaded (or generated with --init)
- [ ] All P0 violations flagged with exact file:line
- [ ] Evidence shown for each violation (not just "violation found")
- [ ] Fix suggestions are actionable (not "refactor this")
- [ ] No false positives on legitimate UI state

## When NOT to use

- Finding bugs → use **trident**
- Security vulnerabilities → use **security-audit**
- UX issues → use **ux-audit**
- Setting up project from scratch → just create architecture.md manually
- Trivial changes (rename, comment, typo) → skip

## Integration

- **SDD** — run after Phase 3 (Implement) as complemento do Trident
- **Trident** — Trident finds bugs, architecture-guard finds structural violations. Run both.
- **React Patterns** — shares Thin Client Iron Law. architecture-guard enforces, react-patterns teaches
- **Context Tree** — can generate architecture.md via `--architecture` mode
