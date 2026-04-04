---
name: react-patterns
description: "Audit and implement modern React/Next.js patterns. Server Components, App Router, Server Actions, Suspense, error boundaries, data fetching, caching. Use when user asks to: audit React code, fix React anti-patterns, 'tá certo esse padrão?', migrate to App Router, server vs client component, 'onde coloco essa lógica?', scaffold Next.js feature, 'posso usar use client aqui?', optimize React performance, fix hydration errors, server component vs client, fix useEffect, hydration error, App Router patterns. Supports: pattern audit, scaffolding, migration, performance review."
---

# React Patterns

IRON LAW: NEVER put business logic in client components — Thin Client, Fat Server. Zero `fetch()`, zero data transformation, zero validation in `'use client'` files. If it doesn't need `useState`, `useEffect`, or browser APIs, it's a Server Component.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--audit` | Check for anti-patterns in current code | default |
| `--scaffold` | Scaffold feature with correct patterns | - |
| `--migrate` | Fix anti-patterns (client logic → server) | - |

## Workflow

```
React Patterns Progress:

- [ ] Phase 1: Stack Detection ⚠️ REQUIRED
  - [ ] 1.1 Detect framework (Next.js version, Remix, Vite, CRA)
  - [ ] 1.2 Identify state management (Zustand, Jotai, Redux, Context)
  - [ ] 1.3 Check styling approach (Tailwind, CSS Modules, styled-components)
  - [ ] 1.4 Check data fetching (React Query, SWR, server actions, tRPC)
- [ ] Phase 2: Pattern Audit
  - [ ] Load references/pattern-guide.md
  - [ ] 2.1 Server vs Client component boundaries
  - [ ] 2.2 Data fetching patterns
  - [ ] 2.3 State management patterns
  - [ ] 2.4 Error/loading handling
- [ ] Phase 3: Recommendations ⛔ BLOCKING
  - [ ] Present findings with before/after examples
  - [ ] ⛔ GATE: Get approval before modifying code
- [ ] Phase 4: Implement
  - [ ] Apply approved patterns
```

## Phase 1: Stack Detection

Check these files to detect the stack:
- `package.json` — framework, dependencies, scripts
- `next.config.*` / `vite.config.*` — bundler config
- `tsconfig.json` — TypeScript settings
- `app/` vs `pages/` — App Router vs Pages Router (Next.js)
- `tailwind.config.*` — styling

Report: "[Framework] [Version] with [State Mgmt] + [Data Fetching] + [Styling]"

## Phase 2: Pattern Audit

Load `references/pattern-guide.md` for complete patterns reference.

### Server vs Client Decision Tree

```
Does the component need...
├── useState/useReducer?          → 'use client'
├── useEffect?                    → 'use client' (but ask: can this be server?)
├── Browser APIs (window, etc.)?  → 'use client'
├── Event handlers (onClick)?     → 'use client'
├── None of the above?            → Server Component (default)
```

### Key Patterns to Check

**Data Fetching:**
- Server Components fetch data directly (async/await, no useEffect)
- Server Actions for mutations (form submissions, writes)
- Route Handlers (`app/api/`) for external API consumers only
- React Query/SWR for client-side real-time data only

**Loading & Error:**
- `loading.tsx` for route-level Suspense
- `error.tsx` for route-level error boundaries
- `<Suspense fallback={}>` for component-level loading
- `notFound()` for 404 handling

**Performance:**
- `React.memo()` only when profiler shows re-render problem (not preventively)
- `useMemo`/`useCallback` only for expensive computations or stable references
- Dynamic `import()` for heavy client-only components
- Image optimization via `next/image`

## Phase 3: Recommendations

Present findings as a table:

```markdown
| File | Issue | Pattern | Fix |
|------|-------|---------|-----|
| `app/dashboard/page.tsx` | Client-side fetch in useEffect | Data on server | Move to server component async |
| `components/Chart.tsx` | 'use client' on wrapper | Push client boundary down | Extract interactive part only |
```

⛔ **GATE:** Do NOT modify code without explicit user approval.

## Anti-Patterns

- **`useEffect` for data fetching** — in App Router, fetch in Server Components directly
- **`'use client'` at page level** — push the boundary down to the smallest interactive piece
- **Business logic in client** — validation, transforms, calculations → move to server
- **Prop drilling through 3+ levels** — use server components to avoid, or Context/Zustand
- **`useEffect` for derived state** — compute during render, not in effect
- **Fetching in parent, passing to children** — let each Server Component fetch its own data
- **`React.memo` everywhere** — premature optimization. Profile first, memo second.

## Pre-Delivery Checklist

Before recommending/implementing patterns:
- [ ] Confirmed framework and version (patterns differ between Next 13/14/15)
- [ ] Server Components are default — `'use client'` only where needed
- [ ] No `fetch()` or data transforms in client components
- [ ] Loading states handled (Suspense or loading.tsx)
- [ ] Error boundaries in place (error.tsx)
- [ ] No `useEffect` for data fetching (use server components or React Query)
- [ ] Images use `next/image` (if Next.js)

## When NOT to use

- Non-React project (Vue, Svelte, etc.) → not applicable
- React Native → different patterns entirely
- Pure CRA/Vite SPA without SSR → only client patterns apply
- Styling-only changes → use `ui-design-system` instead
- Confused about which skill to use → invoke maestro

## Integration

- **Component Architect** — defines structure, this skill defines patterns within that structure
- **UI Design System** — provides tokens, this skill ensures they're applied correctly (server vs client)
- **Trident** — run `--audit` before Trident review to catch React-specific issues
- **SDD** — use `--scaffold` during the implement phase

### Remotion Patterns
Load `references/remotion-react-patterns.md` for React patterns specific to Remotion (video composition, timeline, animation sequences).

### Motion Animations
When building interactive UI with Framer Motion / Motion library, combine this skill's server/client boundaries with Motion's animation APIs — animations are client-only concerns.
