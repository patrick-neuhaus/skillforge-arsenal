---
name: component-architect
description: "Plan and build component architecture using atomic design, composition patterns, and shadcn/ui. Generates component trees, defines interfaces, scaffolds components with proper structure. Use when user asks to: plan components, create component tree, 'como organizo meus componentes', decompose monolithic component, refactor component, component hierarchy, 'componente tá muito grande', atomic design, composition over props, slot pattern, 'quantos props é demais'. Supports: planning, creation, refactoring, audit."
---

# Component Architect

IRON LAW: NEVER create a new component without first checking if an existing one can be composed or extended. Search the codebase BEFORE writing.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--plan` | Generate component tree for a feature | default |
| `--create` | Scaffold component with proper structure | - |
| `--refactor` | Decompose monolithic component | - |
| `--audit` | Check component health (prop count, depth, reuse) | - |

## Workflow

```
Component Architect Progress:

- [ ] Phase 1: Codebase Audit ⚠️ REQUIRED
  - [ ] 1.1 Scan existing components (names, locations, patterns)
  - [ ] 1.2 Identify shared components, UI library (shadcn, Radix, MUI)
  - [ ] 1.3 Check for component conventions (naming, folder structure, exports)
- [ ] Phase 2: Plan
  - [ ] 2.1 Define component tree (atoms → molecules → organisms)
  - [ ] 2.2 Map data flow (props down, events up)
  - [ ] 2.3 Identify reuse opportunities from Phase 1
- [ ] Phase 3: Interface Design
  - [ ] Load references/composition-patterns.md
  - [ ] 3.1 Define props (max 7 per component)
  - [ ] 3.2 Define variants (via props, not separate components)
  - [ ] 3.3 Define slots for flexible composition
- [ ] Phase 4: Review ⛔ BLOCKING
  - [ ] Present component plan with interfaces
  - [ ] ⛔ GATE: Get approval before creating/modifying files
- [ ] Phase 5: Build
  - [ ] Create/refactor components following approved plan
```

## Phase 1: Codebase Audit

Before planning anything:
1. **Scan `src/components/`** (or equivalent) — list all existing components
2. **Check UI library** — is the project using shadcn/ui, Radix, MUI, Chakra, Ant Design?
3. **Identify conventions** — file naming (PascalCase?), co-location (styles, tests, stories), export patterns (barrel files? named exports?)
4. **Map reuse** — which components are used in 3+ places? Which are one-offs?

For `--audit` mode: report component health metrics (see references/composition-patterns.md for thresholds).

## Phase 2: Plan — Atomic Design

Load `references/composition-patterns.md` when reaching this phase.

Classify components into 5 levels:

| Level | What | Examples | Rule |
|-------|------|----------|------|
| **Atoms** | Smallest UI unit, no dependencies | Button, Input, Badge, Avatar | No business logic. Pure visual. |
| **Molecules** | 2-3 atoms combined | SearchBar, FormField, UserChip | Minimal state. Thin wrapper. |
| **Organisms** | Complex UI sections | Header, DataTable, CommentThread | Can fetch data. Has local state. |
| **Templates** | Page layouts with slots | DashboardLayout, AuthLayout | No data. Only structure + slots. |
| **Pages** | Templates + real data | /dashboard, /settings | Connect to data sources. |

For each new component, ask: "Is this an atom, molecule, or organism?" If you can't decide, it's probably too big — decompose.

## Phase 3: Interface Design

### Props — The 7-Prop Rule

> If a component has >7 props, it's doing too much. Decompose or use composition.

Design props by category:
- **Data** — what the component displays (max 2-3)
- **Variants** — visual variations via discriminated union, not booleans
- **Handlers** — callbacks for user actions (max 2)
- **Slots** — children, header, footer for composition

```tsx
// ❌ 11 props — too many
<Card title={} subtitle={} image={} badge={} onClick={} size={} variant={} loading={} error={} footer={} className={} />

// ✅ Composed — each piece is simple
<Card variant="elevated" onClick={}>
  <CardHeader badge={<Badge>New</Badge>}>
    <CardTitle>{title}</CardTitle>
    <CardSubtitle>{subtitle}</CardSubtitle>
  </CardHeader>
  <CardImage src={image} />
  <CardFooter>{footer}</CardFooter>
</Card>
```

### Variant Pattern

Use discriminated unions, not boolean soup:

```tsx
// ❌ Boolean soup — 2^3 = 8 possible states, most invalid
<Button primary={} outlined={} destructive={} />

// ✅ Discriminated — exactly 4 valid states
<Button variant="primary" | "secondary" | "ghost" | "destructive" />
```

## Phase 4: Review

Present:
1. **Component tree** — visual hierarchy (indented list or ASCII tree)
2. **Interface table** — component name, props, variants, slots
3. **Reuse map** — which existing components are reused vs. new

⛔ **GATE:** Do NOT create files without explicit user approval.

## Anti-Patterns

- **God Component** — >200 lines, >7 props, mixes concerns → decompose
- **Prop Drilling** — passing props through 3+ levels → use context, composition, or state management
- **Boolean Soup** — `<Btn primary outlined small />` → use variant discriminated union
- **Premature Abstraction** — creating shared component used only once → wait for 3 uses
- **Copy-Paste Components** — near-identical components with slight variations → extract shared base
- **Wrapper Hell** — `<Box><Flex><Container><Card>` 4+ nesting levels → flatten, use slots

## Pre-Delivery Checklist

Before creating components:
- [ ] Searched codebase for existing components that overlap
- [ ] Every component classified (atom/molecule/organism)
- [ ] No component exceeds 7 props
- [ ] Variants use discriminated unions, not booleans
- [ ] Data flow is unidirectional (props down, events up)
- [ ] Composition via slots where flexible layout needed

## When NOT to use

- One-off UI tweak — just edit the component directly
- Styling changes only → use `ui-design-system` instead
- State management decisions → that's architecture, not component design
- Backend/API work → not applicable

## Integration

- **UI Design System** — apply design tokens to component specs
- **React Patterns** — follow server/client component boundaries
