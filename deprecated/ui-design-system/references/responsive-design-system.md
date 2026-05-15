# 05 — `references/responsive-design-system.md` (proposed)

> Proposed new reference file. Distills DR-02 into rubric: macro × micro architecture, breakpoints in rem, fluid tokens, 9 named primitives, per-component responsive behavior, visual QA matrix. Loaded in Phase 3.

---

# Responsive Design System

This reference defines **how** UI scales across viewports and containers. SKILL.md loads it in Phase 3 (token generation). The schema (`design-json-schema.md`) defines the JSON shape; this file defines the **architecture**.

## 1. Macro × micro: the root rule

Two kinds of "responsive" exist and must not be conflated.

| Kind | What it sees | When to use | CSS mechanism |
|---|---|---|---|
| **Macro layout** | Viewport size / device class | Application shell: header, sidebar regimes, main column, footer. Anything that depends on "is this a phone or a desktop?" | `@media (min-width: ...)`, viewport units (`dvh`, `svh`, `lvh`), `min-width` in rem |
| **Micro layout** | The component's own container size | Cards, forms, KPI grids, tables, any component reused at multiple widths in the same app | `@container (min-width: ...)`, `cqi/cqw/cqb` units |

**Rule:** Viewport queries live in **shell primitives** (`page-shell`, `sidebar-layout`). Container queries live in **components** (`form-grid`, `responsive-grid`, `media-shell`). A card that promotes from 1 column to 2 must not depend on viewport — it must depend on **its container**. Otherwise, the same card renders 1-col inside a wide sidebar and 2-col inside a narrow main column, which is exactly backwards.

## 2. Breakpoints — in rem

```
sm:   20rem   ( 320px @ 16px root)   — minimum supported phone
md:   30rem   ( 480px)                — comfortable phone
lg:   48rem   ( 768px)                — tablet portrait, narrow laptop
xl:   64rem   (1024px)                — laptop, tablet landscape
2xl:  80rem   (1280px)                — desktop
3xl: 120rem   (1920px)                — large desktop, ultrawide
```

**Why rem, not px:** users who set browser font-size to 20px (a real accessibility need) get a proportionally rescaled layout. Pixel breakpoints betray them — the layout still flips at 768px viewport, but text is 25% larger, breaking the implicit assumption of "tablet portrait fits this content".

**Migration from px:** divide by 16 (or by user's root font-size if non-default). Round to a sensible rem value.

## 3. Fluid tokens

Token | Formula | Use
--- | --- | ---
`--page-pad-inline` | `clamp(1rem, 4vw, 4rem)` | Outer horizontal page padding
`--section-space` | `clamp(2rem, 6vw, 6rem)` | Vertical rhythm between major sections
`--card-pad` | `clamp(1rem, 2cqi, 2rem)` | Inner card padding (note: `cqi` — relative to card's container)
`--grid-gap` | `clamp(0.75rem, 1.5vw, 1.5rem)` | Gap between grid items
`--header-height` | `clamp(3rem, 8vh, 4.5rem)` | Sticky header
`--sidebar-expanded` | `clamp(14rem, 22vw, 20rem)` | Sidebar wide regime width
`--sidebar-rail` | `4rem` | Sidebar rail regime fixed
`--container-reading` | `min(70ch, 100% - 2rem)` | Max width for prose
`--container-page` | `min(90rem, 100%)` | Max width for app shell content
`--container-page-wide` | `min(120rem, 100%)` | Max width for marketing/showcase

## 4. Modern unit playbook

| Unit | Use | Avoid |
|---|---|---|
| `dvh` | Full-viewport surfaces that should resize with mobile chrome (drawers, modals) | Heroes that should NOT jump when address bar collapses (use `svh` instead) |
| `svh` | Above-the-fold heroes that should remain stable as Safari/Chrome chrome shifts | Anything that must always fill the actual viewport (use `dvh`) |
| `lvh` | Rare; force "tallest possible viewport" baseline | Default vh use (use `dvh`) |
| `cqi` | Inline size of containing query container (width-ish in horizontal writing) | Outside `container-type` ancestor |
| `cqw` | Width of containing query container (explicit) | When you really mean inline |
| `cqb` | Block size of containing query container | Same caveats |
| `ch` | Reading line-length targets (`max-width: 70ch`) | Fixed-width UI; varies per font |
| `rem` | All breakpoints, gaps, paddings | Sub-pixel use for borders (use `px`) |
| `px` | Hairline borders, 1-2px elements | Type, spacing, breakpoints |
| `%` | Inside known-width containers | At root layout (use rem/clamp) |

## 5. The 9 named primitives

Every shell and reusable layout pattern uses one of these. Naming them prevents `<div className="grid grid-cols-..." >` ad-hoc spreading.

### 5.1 `page-shell`
- **Role:** root of every page; provides `--page-pad-inline`, max width, vertical baseline.
- **Mechanism:** viewport query. Switches column count.
- **API:** `<PageShell>{children}</PageShell>` or class.

### 5.2 `responsive-grid`
- **Role:** auto-fitting card grid (collections, dashboards).
- **Mechanism:** **container query**. `grid-template-columns: repeat(auto-fit, minmax(min(20rem, 100%), 1fr))`.
- **API:** `<ResponsiveGrid minItem="20rem">`.

### 5.3 `cluster`
- **Role:** wrap row of inline things (chips, tag list, action bar). Wraps when needed.
- **Mechanism:** `display: flex; flex-wrap: wrap; gap: var(--cluster-gap)`.
- **API:** `<Cluster>`.

### 5.4 `stack`
- **Role:** vertical rhythm; consistent gap between block siblings.
- **Mechanism:** `display: flex; flex-direction: column; gap: var(--stack-gap)`.
- **API:** `<Stack space="md">`.

### 5.5 `sidebar-layout`
- **Role:** app shell with sidebar + main. Three regimes: drawer (mobile), rail (tablet), persistent (desktop).
- **Mechanism:** **viewport query**. `sm`: drawer; `lg`: rail (toggle to expanded); `xl+`: persistent expanded.
- **API:** `<SidebarLayout regime="auto">`.

### 5.6 `form-grid`
- **Role:** form fields that promote 1→2 columns when their container supports it.
- **Mechanism:** **container query**. `grid-template-columns: 1fr` baseline; `@container (min-width: 30rem) { grid-template-columns: 1fr 1fr }`.
- **API:** `<FormGrid>`.

### 5.7 `table-wrap`
- **Role:** make a wide table scroll horizontally **inside its container**, not on the page.
- **Mechanism:** `overflow-x: auto; min-width: 0` parent; sticky first column optional.
- **API:** `<TableWrap>{table}</TableWrap>`.

### 5.8 `preview-frame`
- **Role:** showcase/preview area for technical content (code preview, embedded design canvas, screenshots) that must not push the page.
- **Mechanism:** `aspect-ratio: 16/9` (or set), `contain: layout`, `overflow: hidden`.
- **API:** `<PreviewFrame ratio="16/9">`.

### 5.9 `media-shell`
- **Role:** image / video / iframe holder that maintains aspect ratio and constrains size.
- **Mechanism:** `aspect-ratio` + `object-fit: cover|contain`.
- **API:** `<MediaShell ratio="4/3" fit="cover">`.

## 6. Per-component responsive behavior

| Component | Container threshold | Behavior |
|---|---|---|
| Button | < 20rem container | Optionally full-width if part of a Stack of CTAs; otherwise inline |
| Input / TextField | always | Stretches to container; `max-inline-size: 30rem` for non-form inputs |
| Form | < 30rem container | 1-column FormGrid |
| Form | ≥ 30rem container | 2-column FormGrid, but sticky labels stay above inputs (not aligned right) |
| Card | < 18rem container | Stack image above title |
| Card | ≥ 18rem container | Inline image left of content |
| Modal / Dialog | mobile | Full-screen sheet via `dvh` |
| Modal / Dialog | desktop | Centered, max-width `min(40rem, 100% - 2rem)` |
| Drawer | always | Width `min(28rem, 100%)`; full height via `dvh` |
| Sidebar | sm viewport | Drawer regime |
| Sidebar | lg viewport | Rail regime, expandable on click |
| Sidebar | xl+ viewport | Persistent, expanded by default; user can collapse |
| Table | always | Wrapped in `table-wrap` |
| Table | < 40rem container | Consider list/card view variant; not in scope of this rubric (component decision) |
| KPI grid | container query | `auto-fit, minmax(min(14rem, 100%), 1fr)` |
| Auth split | < 64rem viewport | Single column, brand panel collapses to logo |
| Auth split | ≥ 64rem viewport | 2-column 50/50 |

This list is **layout behavior only**. Component anatomy (slots, variants, props, a11y contracts) lives in `component-architect`.

## 7. Visual QA matrix

Phase 5 of the SKILL pipeline runs this matrix. Required viewports (CSS px equivalent):

```
320, 360, 390, 430, 768, 1024, 1280, 1366, 1440, 1920, 2560 (ultrawide spot check)
```

For each viewport, test these states:
- Default
- Long text (paste 200ch into a single input/title)
- Empty (no content)
- Loading
- Error
- No-results (search returned nothing)

For each combination, also test:
- Browser zoom 200% (text reflow, no horizontal scroll on shell)
- Browser zoom 400% (reflow target per WCAG 1.4.10)
- `prefers-reduced-motion: reduce` ON
- Dark mode (if supported)

Record screenshots per row. Block on any horizontal page scroll at 320 CSS px.

## 8. Common failure patterns to block

- ❌ Component layout depending on `@media (min-width: ...)` when reused at multiple widths in the same app.
- ❌ `100vh` on hero (jumps when mobile chrome collapses) — use `100svh` or fixed `clamp()`.
- ❌ Sidebar at fixed `220px` on mobile (eats half the screen).
- ❌ Table without `table-wrap` (pushes the page wider than the viewport).
- ❌ Modal at `max-width: 600px` with no `inline-size: min(...)` fallback for narrow phones.
- ❌ KPI grid at fixed columns (`grid-cols-4`) — fails at 360px.
- ❌ Form 2-col by viewport (breaks inside a narrow main column).
- ❌ Iframe / preview without `aspect-ratio` (collapses to 0 height).
- ❌ Auth split with brand panel locked open at 320px viewport.

## 9. Acceptance criteria (Phase 5)

- [ ] Breakpoints in rem.
- [ ] `--page-pad-inline`, `--section-space`, `--card-pad`, `--grid-gap`, `--header-height` exist as fluid tokens.
- [ ] `--container-reading: 70ch`, `--container-page: 90rem` declared.
- [ ] Viewport queries restricted to shell primitives (`page-shell`, `sidebar-layout`).
- [ ] Container queries used for components reused at multiple widths.
- [ ] All 9 primitives present and used.
- [ ] Modal/drawer use `dvh` not `vh`.
- [ ] Tables wrapped in `table-wrap`.
- [ ] Iframes/previews wrapped in `preview-frame` or `media-shell` with `aspect-ratio`.
- [ ] Visual QA matrix passed.
- [ ] No horizontal scroll at 320 CSS px on any tested page.

## 10. Boundary

- **Browser support / polyfills for container queries / `dvh` / `:has()`:** owned by `react-patterns`. Imported here as "assume modern; declare baseline elsewhere".
- **Stacking context / sticky / overflow diagnostic:** owned by `react-patterns`. This file declares **rules** (`table-wrap` always present); `react-patterns` debugs why a sticky header escapes a stacking context.
- **Component anatomy:** owned by `component-architect`. This file declares only layout behavior.
- **WCAG reflow at 320 CSS px:** threshold imported from `ux-audit`.
