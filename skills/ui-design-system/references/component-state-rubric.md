# 06 — `references/component-state-rubric.md` (proposed)

> Proposed new reference. Visual rubric of states a component can express, from the **design system** perspective. Anatomy, slots, variants, props belong to `component-architect`; this file declares **what visual states must exist**, **which DS tokens express them**, and **how to audit them visually**.

---

# Component State Rubric (visual)

## 1. The 17 states

| # | State | Trigger | Required for | DS tokens it consumes |
|---|---|---|---|---|
| 1 | **default** | Idle | All | `surface.*`, `on-surface-*`, `action.default` |
| 2 | **hover** | Pointer enters | Interactive (mouse) | `action.hover`, `effects.shadow.hover`, `motion.transition.fast` |
| 3 | **focus-visible** | Keyboard focus | All interactive | `focus.ring` (3:1 against every surface) |
| 4 | **active / pressed** | Mousedown / touch | Interactive | `action.active` (or inset shadow) |
| 5 | **selected** | Persistent state, "this row is chosen" | Lists, tabs, segmented controls | `action.default` (subtle), `on-action`, sometimes `decorative.secondary` |
| 6 | **disabled** | Cannot be used | Interactive | desaturated `action.disabled`, foreground meets 4.5:1 if text |
| 7 | **loading** | Async work in progress | Data-fetching, submit | `motion.spinner`, neutral surface; preserve hit target size |
| 8 | **error** | Validation/system failed | Forms, fetches | `status.error`, `status.error-foreground`, `focus.ring` shifts to error variant |
| 9 | **success** | Operation completed | Forms, async actions | `status.success` (use sparingly; transient) |
| 10 | **empty** | No content yet | Lists, inboxes, dashboards | `surface.sunken` background + illustration placeholder + primary CTA |
| 11 | **read-only** | Locked but viewable | Forms in audit mode | `surface.sunken`, no `focus.ring`, cursor `not-allowed` only on truly disabled |
| 12 | **expanded** | Disclosure open | Accordion, sidebar item | indicator rotation/animation + `aria-expanded="true"` |
| 13 | **drag** | Item being dragged | Sortable lists, kanban | `effects.shadow.lifted`, slight opacity reduction, drop targets highlighted |
| 14 | **overflow** | Content exceeds container | Long titles, table cells | `text-overflow: ellipsis` + tooltip OR scroll-wrap; never truncate without recovery |
| 15 | **async (skeleton)** | Initial paint, content not ready | Lists, cards | `surface.skeleton` (animated shimmer respecting reduced-motion) |
| 16 | **no-results** | Filter/search returned 0 | Tables, search | Distinct from empty: shows query + suggestion to broaden |
| 17 | **error-bound (boundary)** | Component crashed | Any | Component renders its own error state, not a blank box |

## 2. State coverage matrix

For each component the system ships, declare which of the 17 are **required**, **recommended**, or **N/A**.

Example for `Button`:

| State | Status | Token mapping |
|---|---|---|
| default | required | `action.default`, `on-action` |
| hover | required | `action.hover` |
| focus-visible | required | `focus.ring` |
| active | required | `action.active` |
| selected | N/A | (Buttons aren't persistently selected; ToggleButton is.) |
| disabled | required | `action.disabled` |
| loading | required | inline spinner; preserve width |
| error | recommended | only for inline async actions ("Save failed") |
| success | recommended | transient, fades in 320ms |
| empty | N/A | |
| read-only | N/A | use disabled |
| expanded | N/A | (Disclosure component instead) |
| drag | N/A | |
| overflow | required | label truncation rule |
| async (skeleton) | recommended | when entire row of CTAs is loading |
| no-results | N/A | |
| error-bound | recommended | |

The matrix is shipped as part of `design.json` under `components.<name>.states`.

## 3. Visual audit method

Per component, generate visual proof of every required state. Methods:

- **Storybook stories** named after each state.
- **Or**: a single playground page with toggle for each state.
- **Or** (lightweight): screenshot grid in `ds-audit/<component>/states/*.png`.

Audit is a **boundary-positive** activity: gaps surface as "Component X missing visual proof for state Y". This file does not prescribe the framework — only that the proof exists.

## 4. Anti-patterns

- ❌ Hover style without focus-visible style ("only mouse users".)
- ❌ Focus-ring same color as `action.default` (invisible on the action's own hover).
- ❌ Disabled state with foreground < 4.5:1 if it carries text the user might read (form labels).
- ❌ Loading state shrinks the button (layout shift on click).
- ❌ Error state encoded only by red color (must include icon or text).
- ❌ Empty state that's just `<p>No data</p>` — empty is a UX moment; provide context + recovery.
- ❌ No-results conflated with empty (different copy, different recovery).
- ❌ Truncation without tooltip or scroll-wrap (information loss).
- ❌ Skeleton that ignores reduced-motion (shimmer pulses for users who asked it not to).

## 5. Acceptance criteria

- [ ] Every shipped component has a row in `components.<name>.states`.
- [ ] Required states have a token mapping.
- [ ] Visual proof exists per required state.
- [ ] Focus-visible distinct from hover for every interactive component.
- [ ] Loading state preserves component dimensions.
- [ ] Error state uses both color + non-color cue.
- [ ] Empty and no-results are distinct with distinct copy.
- [ ] Skeleton respects `prefers-reduced-motion`.

## 6. Boundary

- **Anatomy / slots / variants / props / a11y contract:** `component-architect`.
- **Implementation patterns (React state, Suspense, ErrorBoundary):** `react-patterns`.
- **Whether each state is announced to assistive tech:** `ux-audit`.
- **Token shape:** `design-json-schema.md`.
- **Token derivation:** `color-token-algorithms.md`.
