---
name: ui-design-system
description: PROPOSED v2 — Generates and audits design tokens, primitives, breakpoints, motion and visual state systems for any project. Owns color tokens by semantic role (action/brand/focus/surface/decorative), foreground measured on real pairs, macro×micro responsive architecture, named layout primitives, motion-as-system, and design-system maturity. Imports WCAG thresholds from ux-audit; defers component anatomy to component-architect; defers build/baseline to react-patterns. Use when starting a new product, defining tokens from a brand seed, auditing visual maturity, or applying tokens to code. Modes — `--generate` (default), `--audit`, `--apply`, `--identity`.
---

> **PROPOSAL FILE.** This is a markdown proposal for the rewritten `ui-design-system/SKILL.md`. It does not replace the live skill until reviewed.

# UI Design System (v2 — proposed)

## Iron Laws (3)

1. **Concrete inputs only.** Never invent visual decisions from abstract descriptions ("modern", "premium"). Require: brand seed color (hex/oklch), font family or screenshot, product type (operational SaaS / landing / docs / template / video), one reference UI (URL, screenshot, or existing project). If any are missing, **stop and ask**. Do not proceed.

2. **Tokens by semantic role, not by chromatic family alone.** Cor, espaço e motion vivem por **papel funcional** (action, brand, focus, surface, decorative — for color; shell vs component — for layout; state vs layout vs decorative — for motion). Chromatic families (`primary`, `accent`, `neutral`) ainda existem como fonte; papéis semânticos são o que componentes consomem.

3. **Foreground measured on the real pair.** Never approve a token decision against the abstract seed. Always measure contrast on the **rendered pair** (`primary × primary-foreground`, `surface × on-surface`, `focus-ring × surface-adjacent`). Importa limiares de `ux-audit` (WCAG 2.2 AA: 4.5:1 texto normal; 3:1 texto grande, ícones de UI, focus ring; 24×24 hit target; reflow 320 CSS px).

## Modes

| Mode | When | Output |
|---|---|---|
| `--generate` (default) | New project, new brand, new direction | `design.json` + Tailwind config + CSS variables + 3 example components rendered with the tokens |
| `--audit` | Existing project, measuring visual maturity | Maturity scorecard (3 levels × 7 dimensions) + ranked gaps + remediation plan. Loads `design-system-maturity-rubric.md`. |
| `--apply` | Tokens approved, ready to wire to code | Targeted edits to `tailwind.config.*`, `:root` CSS variables, base components. **Requires Phase 5 approval.** |
| `--identity` | Mini brand exercise (logo concept, single palette, 2 fonts) | Tiny identity brief. Loads `mini-identity-guide.md`. Not the full pipeline. |

## Pipeline (6 phases)

### Phase 1 — Inputs and product type

Collect:
- Brand seed (hex or OKLCH).
- Optional secondary brand color, accent.
- Type system source (font family + reference URL, or "use system stack").
- **Product type**: operational SaaS, landing page, documentation, template/demo, video. Affects density, type scale, motion.
- One reference UI (URL/screenshot/codebase).
- Constraints: dark mode required? brand-locked? accessibility target above AA?

If any of seed / fonts / product type / reference is missing — **stop, ask, do not infer**.

### Phase 2 — Color space and roles → load `color-token-algorithms.md`

- Choose color space: **OKLCH for derivation engine + WCAG measured for foreground + HCT (Material) as semantic-role benchmark**. Justify if deviating.
- Define **5 semantic role groups**: action, brand, focus, surface, decorative.
- Map seed → roles via `deriveColorTokens(seed, mode)` (algorithm in `color-token-algorithms.md`).
- Validate against the **8 edge cases** (dark purple, light yellow, saturated red, saturated blue, green, neutral gray, near-white, near-black). If seed falls in an edge case, follow the case-specific recipe.
- Keep `success/warning/error/info` **manual or harmonized** — never derived as `+120°` from seed.

### Phase 3 — Token generation → load `design-json-schema.md` + `responsive-design-system.md`

Produce `design.json`:
- `colors.roles` (action / brand / focus / surface / decorative) with `default`, `foreground`, `hover`, `active`, `disabled`, and `focus-ring` as **first-class token** (not buried in `input.focus`).
- `colors.contrast`: every meaningful pair tested + ratio recorded.
- `typography.scale`: modular scale, line-heights for body (1.5+) and headings (1.1–1.25), measure target via `ch`.
- `spacing.scale`: 4px or 8px base, fluid wrappers for page-pad, section-space, card-pad, grid-gap.
- `responsive.breakpoints` in **rem** (20/30/48/64/80/120 — sm/md/lg/xl/2xl/3xl).
- `responsive.fluid`: `--page-pad-inline`, `--section-space`, `--card-pad`, `--grid-gap`, `--header-height`, `--sidebar-expanded` as `clamp()` formulas.
- `responsive.containers`: `reading: 70ch`, `page: 90rem`, `page-wide: 120rem`.
- `primitives` (9 named): `page-shell`, `responsive-grid`, `cluster`, `stack`, `sidebar-layout`, `form-grid`, `table-wrap`, `preview-frame`, `media-shell`.
- `components.<name>.responsive`: layout behavior rule per component (e.g. "Button full-width when container ≤30rem", "Sidebar 3 regimes: drawer / rail / persistent").

### Phase 4 — States, motion, microinteractions → load `component-state-rubric.md` + `motion-and-interaction.md`

- For each major component, declare the visual states present (default, hover, focus-visible, active, pressed, selected, disabled, loading, error, success, empty, read-only, expanded, drag, overflow, async, no-results) and which token each state uses.
- Motion as system: durations (fast 100ms, normal 200ms, slow 320ms, decorative 480ms), easing curves with use partition (state / layout / decorative entry).
- Reduced motion is **regra**, not dica: every animation declares its `prefers-reduced-motion: reduce` fallback.

### Phase 5 — Review ⛔ BLOCKING

Run **all** of:
- Contrast on every approved real pair (text/foreground, focus-ring on every surface it lands on).
- Hit target ≥ 24×24 CSS px on all interactive primitives.
- Reflow at 320 CSS px (no horizontal scroll on shell).
- Zoom 200% / 400% (text reflow, no clipping).
- Reduced motion fallback exists for every animation.
- Visual QA matrix: 320 / 360 / 390 / 430 / 768 / 1024 / 1280 / 1366 / 1440 / 1920 viewports + ultrawide spot check.
- States matrix: long text, empty, loading, error, no-results.
- Edge case validation if seed is extreme.

**Block on any failure.** Present scorecard. Wait for human approval before Phase 6.

### Phase 6 — Apply (`--apply` only, after approval)

- Emit `tailwind.config.*` (or equivalent).
- Emit `:root` CSS variables file.
- Emit 3 example components (Button, Input, Card) rendered with the tokens.
- Note any code paths to follow up (e.g. "Existing inline `#3b82f6` usages in `apps/web/src/...` to migrate").

## Audit mode (`--audit`)

Loads `design-system-maturity-rubric.md`. Produces:
- 3-level diagnosis per dimension (cor / tipografia / spacing / primitives / componentes / motion / governança).
- Ranked gaps, top 5 remediations.
- Boundary check: any finding that's pure WCAG goes back to `ux-audit`; any finding about component anatomy goes to `component-architect`.

## Anti-patterns (block these)

- ❌ "Make it modern/premium" with no concrete input.
- ❌ Token decisions from the seed alone, without measuring foreground pair.
- ❌ Brute complement (`+180°` HSL) as accent without semantic justification.
- ❌ `success/warning/error` derived as `+120°` rotations of the seed.
- ❌ Breakpoints in pure px without rem fallback.
- ❌ Layout primitives unnamed (`<div className="grid grid-cols-...">` repeated everywhere).
- ❌ Motion without `prefers-reduced-motion`.
- ❌ Focus ring as a sub-property of `input` instead of a first-class color token.
- ❌ Audit without rubric ("looks fine to me").
- ❌ Pixel-only sizes ignoring user font size.
- ❌ Encyclopedia drift: adding tokens with no consumer.

## Pre-delivery checklist

- [ ] Seed, fonts, product type, reference all collected.
- [ ] Color space chosen and justified (OKLCH + WCAG + HCT).
- [ ] 5 semantic role groups present in `colors.roles`.
- [ ] `focus-ring` is a first-class token; 3:1 ratio met against every surface it lands on.
- [ ] All approved pairs measured ≥ 4.5:1 (or 3:1 for large text/UI graphics).
- [ ] Breakpoints in rem.
- [ ] 9 layout primitives present.
- [ ] Tokens fluidos completos (`page-pad-inline`, `section-space`, `card-pad`, `grid-gap`, `header-height`).
- [ ] Containers nomeados (`reading: 70ch`, `page: 90rem`).
- [ ] Component-level responsive rules declared (full-width threshold, sidebar regimes, table-wrap).
- [ ] Reduced motion fallback for every animation.
- [ ] Visual QA matrix passed (≥10 viewports, zoom 200%, reduced motion on/off).
- [ ] States declared per component and tokenized.
- [ ] Edge case validated if seed is extreme.

## Boundary table (positive routing)

| Symptom | Skill |
|---|---|
| "Audit a11y on this page" | `ux-audit` |
| "Define WCAG criteria" | `ux-audit` (canonical) |
| "Document component anatomy / slots / variants / props / a11y contract" | `component-architect` |
| "Container queries — does this browser support them? Polyfill?" | `react-patterns` |
| "Vite / Browserslist / build target" | `react-patterns` |
| "Set up Playwright + axe + visual regression" | `react-patterns` |
| "Are we using shadcn/Material/Chakra correctly?" | `design-system-audit` |
| "Generate the design tokens / breakpoints / primitives / motion / state-tokens / maturity scorecard" | **this skill** |
| "Translate one brand color into a full token system" | **this skill** |

## Integration notes

- This skill **owns** tokens, primitives, breakpoints, motion-as-system, visual state rubric, maturity rubric.
- This skill **imports** WCAG thresholds (4.5:1, 3:1, 24×24, reflow 320, prefers-reduced-motion) from `ux-audit`.
- This skill **defers** component anatomy/slots/variants/props/a11y contracts to `component-architect`.
- This skill **defers** build target / baseline / polyfills / test infra to `react-patterns`.
- This skill **does not** rewrite copy, run discovery, or produce PRDs.
