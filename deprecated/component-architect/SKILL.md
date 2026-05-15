---
name: component-architect
description: "Plan and build component architecture using atomic design, composition patterns, shadcn/ui, state contracts and component behavior. Generates component trees, interfaces, variants, slots, loading/disabled/focus/pressed state contracts, a11y behavior, and scaffolds components. Use when user asks: plan components, create component tree, como organizo meus componentes, decompose monolithic component, refactor component, component hierarchy, componente muito grande, quebrar componente, atomic design, composition over props, slot pattern, quantos props e demais, component state contract, loading state, disabled state, focus-visible, pressed state. Supports: planning, creation, refactoring, audit. NAO use para visual tokens/easing (ui-design-system) ou motion polish criativo (motion-design)."
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
  - [ ] Load references/states-inventory.md for interactive components
  - [ ] 3.1 Define props (max 7 per component)
  - [ ] 3.2 Define variants (via props, not separate components)
  - [ ] 3.3 Define slots for flexible composition
  - [ ] 3.4 Define state/microinteraction contract (loading, disabled, focus-visible, pressed)
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

### State Contract

For interactive components, load `references/states-inventory.md` and declare behavior for default, hover, focus-visible, active/pressed, disabled and loading. This skill owns anatomy, ARIA, focus, events and layout stability. `ui-design-system` owns visual tokens/easing; `motion-design` owns refined motion spec when the interaction needs polish.

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
- [ ] Interactive components declare state/microinteraction contract
- [ ] Data flow is unidirectional (props down, events up)
- [ ] Composition via slots where flexible layout needed

## When NOT to use

- One-off UI tweak — just edit the component directly
- Styling changes only → use `ui-design-system` instead
- State management decisions → that's architecture, not component design
- Backend/API work → not applicable
- Confused about which skill to use → invoke maestro

## Integration

- **UI Design System** — apply design tokens to component specs. **Boundary:** `ui-design-system` owns visual state tokens (colors/contrast/motion via `component-state-rubric.md`); this skill owns anatomy + a11y behavior (canonical state inventory in `states-inventory.md`)
- **React Patterns** — follow server/client component boundaries
- **Code Dedup Scanner** — run BEFORE creating components to find existing reusables. This skill plans what to CREATE; dedup-scanner finds what already EXISTS
- **Trident** — `--design` mode validates component output (visual, a11y, performance)

### Remotion Components
Load `references/remotion-patterns.md` when building video/animation components with Remotion.
