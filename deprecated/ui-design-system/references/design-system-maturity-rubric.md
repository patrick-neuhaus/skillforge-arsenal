# 08 — `references/design-system-maturity-rubric.md` (proposed)

> Proposed new reference. Powers the `--audit` mode of the SKILL. Defines 3 maturity levels × 7 dimensions; produces a scorecard + remediation plan.

---

# Design System Maturity Rubric

## 1. The 3 levels

| Level | Name | Heuristic |
|---|---|---|
| **L0** | Embryonic | Tokens exist as raw hex/font lists; consumers reference them inconsistently; no primitives. |
| **L1** | Adolescent | Tokens organized by role; named primitives exist; some components documented; gaps in motion/states/governance. |
| **L2** | Mature | Full token system (color roles, fluid spacing, breakpoints in rem); 9 primitives in use; states matrix per component; motion-as-system; documented governance and ownership. |

Most projects start at L0. The SKILL's job in `--audit` is to score where they are on each dimension, not just overall.

## 2. The 7 dimensions

For each dimension below, score L0 / L1 / L2.

### 2.1 Color
- **L0** — Hex codes scattered in code; no `colors.roles`; no contrast log.
- **L1** — `colors.primary/neutral/accent` exist; some contrast tested.
- **L2** — Semantic role groups (`action`, `brand`, `focus`, `surface`, `decorative`); foreground measured on every approved real pair; `focus.ring` first-class; status colors managed (not derived); edge cases handled.

### 2.2 Typography
- **L0** — Sizes inline as `text-xl`, `text-2xl`; line-height ad-hoc; `Inter` everywhere.
- **L1** — Type scale present; line-heights distinguish body (1.5+) and heading (1.1–1.25).
- **L2** — Modular scale via `clamp()` for fluid sizing; `ch`-based reading width; weight scale; rare display weight reserved for headings; vertical rhythm tokenized.

### 2.3 Spacing
- **L0** — `gap-3`, `mt-7`, `pl-2.5` — no scale.
- **L1** — Scale present (4 or 8 base); gaps consistent within components.
- **L2** — Fluid wrappers (`--page-pad-inline`, `--section-space`, `--card-pad`, `--grid-gap`) declared; rhythm tokens consumed by primitives; no inline magic numbers.

### 2.4 Primitives
- **L0** — `<div className="grid grid-cols-...">` repeated; no shared shell.
- **L1** — A handful of layout components exist; coverage incomplete.
- **L2** — All 9 named primitives present (`page-shell`, `responsive-grid`, `cluster`, `stack`, `sidebar-layout`, `form-grid`, `table-wrap`, `preview-frame`, `media-shell`); container queries used in components, viewport queries in shell.

### 2.5 Components
- **L0** — Buttons in 4 places, each slightly different; no inventory.
- **L1** — Component library present; visual states partial; props undocumented.
- **L2** — `components.<name>.states` table per component; required visual states proven; layout behavior declared; anatomy documented in `component-architect`.

### 2.6 Motion
- **L0** — `transition: all 0.2s ease` everywhere; no reduced-motion fallback.
- **L1** — Duration tokens exist; some reduced-motion support.
- **L2** — Duration + easing partition (state / layout / decorative); reduced-motion mandatory and tested; no `transform: scale()` on press; canonical microinteractions in place.

### 2.7 Governance
- **L0** — No owner; tokens edited freely; no review.
- **L1** — A maintainer exists; loose conventions documented in README.
- **L2** — Token changes go through review; consumers tracked; deprecation has a process; new components have an admission criterion (states, motion, contrast, primitives used).

## 3. Scoring output

The audit emits:

```
{
  "level": "L1",                 // overall = lowest dimension level
  "dimensions": {
    "color":      { "level": "L1", "gaps": ["focus-ring not first-class", "no contrast log for raised surface"] },
    "typography": { "level": "L1", "gaps": ["no fluid clamp on H1/H2"] },
    "spacing":    { "level": "L0", "gaps": ["no fluid tokens", "magic numbers in section padding"] },
    "primitives": { "level": "L0", "gaps": ["no named primitives; ad-hoc grid in 14 places"] },
    "components": { "level": "L1", "gaps": ["no visual proof for empty/no-results/error states on Table"] },
    "motion":     { "level": "L0", "gaps": ["no reduced-motion fallback in 6 components", "scale press on Button"] },
    "governance": { "level": "L0", "gaps": ["no owner declared", "ad-hoc token additions"] }
  },
  "topRemediations": [
    "Introduce primitives: page-shell, responsive-grid, sidebar-layout (impact: 14 ad-hoc grids unified)",
    "Add reduced-motion media query at root",
    "Extract --page-pad-inline, --section-space, --card-pad as fluid tokens",
    "Promote focus.ring to first-class color token; test 3:1 against all 4 surfaces",
    "Document Table empty/no-results/error states + add visual proof"
  ]
}
```

## 4. Boundary

- **WCAG findings** that surface during audit (e.g. "alt text missing on image carousel"): hand off to `ux-audit`.
- **Component anatomy gaps** (slot missing, variant inconsistent): hand off to `component-architect`.
- **Build/baseline gaps** (no PostCSS, no `target: 'es2022'`): hand off to `react-patterns`.
- **DS adherence gaps** (using shadcn but bypassing primitives): `design-system-audit`.
