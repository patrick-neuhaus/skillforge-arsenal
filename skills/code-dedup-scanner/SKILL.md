---
name: code-dedup-scanner
description: "Scan codebase to find reusable components, functions, and patterns before creating new code. Prevents duplication and wasted tokens. Use when user asks: 'já tem isso no projeto?', find duplicates, 'antes de criar verifica se existe', scan for reusables, check existing code, 'tem componente parecido?', 'posso reutilizar algo?', find similar code, duplicate scan, code reuse, 'não quero duplicar', 'existe algo parecido?', dedup check, 'antes de implementar busca se já tem'. Sub-step of SDD Phase 1 Research. Also useful standalone before any implementation. Complementa component-architect: este escaneia o que existe, component-architect planeja o que criar. Ao iniciar, faça scan proativo (glob *.tsx *.ts *.jsx) ANTES de perguntar 'qual componente?' — mostre o que já existe primeiro."
---

# Code Dedup Scanner — Encontrar Reutilizáveis

IRON LAW: NEVER report a duplicate without showing the exact location AND usage context of the original. False positives waste more time than they save — every match must include file path, line number, and how the original is currently used.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--scan` | Full codebase scan for reusables | default |
| `--check <desc>` | Check if something similar exists before creating | - |
| `--report` | Generate full dedup report | - |

## Workflow

```
Code Dedup Scanner Progress:

- [ ] Step 1: Understand Intent ⚠️ REQUIRED
  - [ ] 1.1 What is the user about to create? (component, function, query, hook)
  - [ ] 1.2 What domain? (UI, data, auth, utils)
  - [ ] 1.3 What keywords describe it? (Button, Modal, formatDate, useAuth)
- [ ] Step 2: Scan
  - [ ] 2.1 Search by name (exact and fuzzy)
  - [ ] 2.2 Search by pattern (similar functionality)
  - [ ] 2.3 Search installed dependencies
  - [ ] 2.4 Search shadcn/ui or design system
- [ ] Step 3: Report ⛔ BLOCKING
  - [ ] 3.1 Present matches with Reuse/Extend/Create recommendation
  - [ ] 3.2 Show exact location + usage context for each match
  - [ ] ⛔ GATE: User decides action per match
```

If `--check`: Quick mode — Steps 1+2 focused on the specific description → report.
If `--report`: Full scan — all potential duplicates across codebase → comprehensive report.

## Step 1: Understand Intent

Ask (if not clear from context):
- "O que você vai criar?" — component, function, hook, query, page, util
- "Qual o domínio?" — invoices, auth, users, products, settings
- "Descreve a funcionalidade em 1 frase"

Extract search keywords from the answers.

## Step 2: Scan

### 2.1 Search by Name

```bash
# Exact name search
grep -r "ComponentName\|functionName" src/ --include="*.ts" --include="*.tsx" -l

# Fuzzy: search related terms
grep -r "Button\|Btn\|button" src/components/ --include="*.tsx" -l

# Exports available
grep -r "export.*function\|export.*const\|export default" src/lib/ src/utils/ -l
```

### 2.2 Search by Pattern

Load `references/scanning-strategies.md` for pattern-based search techniques.

| What to create | Search pattern |
|---------------|---------------|
| UI Component | `src/components/` by name + shadcn/ui registry |
| Hook | `src/hooks/` + `use[Keyword]` pattern |
| Utility function | `src/lib/` + `src/utils/` by operation name |
| API/Query | `src/lib/supabase/` or `src/app/api/` by resource name |
| Server Action | `src/actions/` or `"use server"` grep |
| Validation Schema | `src/lib/validations/` or Zod schemas by name |

### 2.3 Search Dependencies

```bash
# Check if installed package already solves this
grep -r "dependency-name" node_modules/.package-lock.json 2>/dev/null
# Or check package.json directly
cat package.json | grep -A 50 '"dependencies"'
```

Common cases:
- Date formatting? → check for `date-fns`, `dayjs`, `luxon`
- Form validation? → check for `zod`, `yup`, `valibot`
- Animation? → check for `framer-motion`, `motion`
- HTTP client? → check for `axios`, `ky`, native fetch wrappers

### 2.4 Search Design System

If project uses shadcn/ui:
- Check `components/ui/` for existing primitives
- Check shadcn registry for components not yet installed: `npx shadcn@latest add --list`

## Step 3: Report

### Match Format

```markdown
## Dedup Scan Results

**Scanning for:** [description of what user wants to create]

### Matches Found

#### Match 1: [name] — REUSE ✅
**Location:** src/components/ui/Button.tsx:1
**What it does:** [brief description]
**Current usage:** Used in 12 files (InvoiceForm, UserProfile, SettingsPage...)
**Recommendation:** Import directly. Exact match for your need.

#### Match 2: [name] — EXTEND 🔄
**Location:** src/components/features/DataTable.tsx:1
**What it does:** [brief description]
**Gap:** Missing sort functionality, has filter + pagination
**Recommendation:** Add sort prop instead of creating new table component.

### No Match — CREATE 🆕
**What:** [description]
**Suggested path:** src/components/features/[domain]/[Name].tsx
**Rationale:** Nothing similar found in codebase or dependencies.
```

### Decision Table

| Scenario | Action | Why |
|----------|--------|-----|
| Identical component/function exists | **REUSE** | Import it |
| Similar exists but missing feature | **EXTEND** | Add prop/variant — don't fork |
| Similar exists in installed package | **USE PACKAGE** | Don't reinvent |
| Similar exists but different domain | **EXTRACT** | Generalize into shared util |
| Nothing similar exists | **CREATE** | Document in spec as new code |

⛔ **GATE:** Present all matches. User decides per match: reuse, extend, or create new.

## Anti-Patterns

- **Reporting without context:** "Button.tsx exists" is useless. Show WHERE it's used and HOW
- **Missing package search:** The user might not know `date-fns` is installed and handles their case
- **Over-matching:** A `UserCard` and `ProductCard` share "Card" but aren't duplicates. Match by functionality, not name
- **Skipping shadcn:** Half the "missing" components already exist in shadcn's registry
- **Full codebase scan for simple check:** `--check` is fast. `--report` is thorough. Default to `--check`

## Pre-Delivery Checklist

- [ ] Every match includes exact file path + line number
- [ ] Every match shows current usage context (who imports it)
- [ ] Recommendation is one of: REUSE / EXTEND / USE PACKAGE / EXTRACT / CREATE
- [ ] No false positives (name match ≠ functionality match)
- [ ] Dependencies checked (package.json)
- [ ] Design system checked (shadcn/ui if applicable)

## When NOT to use

- Reviewing code quality → use **trident**
- Planning component architecture → use **component-architect**
- Finding bugs → use **trident**
- Greenfield project (nothing to scan) → skip

## Integration

- **SDD** — Phase 1, Step 2: run before spec to find reusables
- **Component Architect** — this scans what EXISTS; component-architect plans what to CREATE
- **Trident** — complementary: dedup prevents waste, trident prevents bugs
