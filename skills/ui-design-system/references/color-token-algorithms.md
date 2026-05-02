# 04 — `references/color-token-algorithms.md` (proposed)

> Proposed new reference file for `ui-design-system/references/color-token-algorithms.md`. Distills DR-01 into an executable rubric: color space, semantic roles, derivation algorithm, edge cases, acceptance criteria. Loaded in Phase 2 of the SKILL pipeline.

---

# Color Token Algorithms

This reference defines **how** to translate a brand seed into a full token system. SKILL.md decides **when** to invoke it; the schema (`design-json-schema.md`) defines the output shape.

## 1. Color spaces and what each one buys you

| Space | Strength | Weakness | Role in this skill |
|---|---|---|---|
| **OKLCH** | Perceptually uniform; lightness L is monotonic; predictable hue rotations; `chroma` is independent of L | Browser support recent; some chromas out of sRGB gamut | **Derivation engine**: hue/chroma/lightness math happens here |
| **WCAG (sRGB relative luminance)** | Authoritative for accessibility; what auditors measure | Not perceptually uniform; says nothing about aesthetic harmony | **Foreground gate**: every approved pair is measured here, on the rendered pair |
| **HCT (Material 3)** | Tone is calibrated to **perceived contrast**; Material's role mapping (primary/onPrimary/container/onContainer) is mature | Less common in libs; tied to Material conventions | **Semantic role benchmark**: when in doubt about role mapping, compare to HCT's tone targets (primary 40, onPrimary 100, primaryContainer 90, onPrimaryContainer 10) |
| HSL | Familiar to developers | Lightness collapses on yellow/cyan; not perceptually uniform | **Avoid as derivation engine.** Use only as a debugging view. |
| LCH (Lab-based) | Predates OKLCH; similar properties | Less hue-stable than OKLCH | Acceptable substitute if OKLCH unavailable. |

**Rule:** Derivation in OKLCH. Foreground in WCAG. Role-naming benchmarked against HCT.

## 2. Semantic role groups (5)

Tokens consumed by components are organized by **role**, not chromatic family. Chromatic families (`primary`, `accent`, `neutral`) remain as **source palettes**; roles are what UI consumes.

### 2.1 `action` — interactive primary action

- `action.default` — the primary CTA fill.
- `action.foreground` — text/icon on `action.default`. Measured pair ≥ 4.5:1.
- `action.hover` — slightly darker/more chromatic than default.
- `action.active` / `action.pressed` — even darker; or inset shadow alternative.
- `action.disabled` — desaturated, foreground meets 4.5:1 OR component is non-text.
- `action.focus-ring` — see §2.3.

### 2.2 `brand` — recognition only, not action

- `brand.accent` — used in marketing surfaces, illustrations, decorative moments.
- `brand.accent-foreground` — text on brand accent if used.
- **Not** the same as `action.default`. A muted brand color can be `brand.accent` while `action.default` is a more saturated derived hue.

### 2.3 `focus` — first-class

- `focus.ring` — single token. Must achieve **3:1 contrast against every surface it lands on** (not just the page background). If the focus ring lands on `surface.raised` and `surface.sunken` and `surface.overlay` — test against all three.
- Implementation: `outline: 2px solid var(--focus-ring); outline-offset: 2px;` with a non-`transparent` outline-offset background.

### 2.4 `surface` — backgrounds, layered

- `surface.page` — base canvas.
- `surface.raised` — cards, popovers, lifted modules. Slightly lighter (light theme) or slightly lighter with subtle elevation (dark theme).
- `surface.sunken` — wells, inputs, code blocks. Slightly darker than `page`.
- `surface.overlay` — modal backdrops, drawers. Includes alpha.
- Each surface has its `on-*` foreground (`on-surface-page`, `on-surface-raised`).

### 2.5 `decorative` — non-functional color

- `decorative.secondary` — chips, badges, sidebar indicators, tag fills.
- Decorative colors **do not need 4.5:1 contrast** if they don't carry text/icons. They DO need 3:1 if they carry icons or convey state.

### 2.6 Why role over family

A "primary blue" might be too saturated for a CTA fill (action) but perfect for a brand accent. Conflating them ("our primary is `#0066ff`, use it everywhere") is what produces unreadable buttons and washed-out logos. Roles let `action.default` derive from the seed via a chroma/lightness adjustment, while `brand.accent` keeps the seed verbatim.

## 3. Algorithm: `deriveColorTokens(seed, mode)`

Pseudocode. Implementations may use `culori`, `chroma-js`, or native browser `CSS.supports('color', 'oklch(...)')`.

```
input: seed (any color), mode = "light" | "dark"
output: design.json colors block

# Step 1: parse seed → OKLCH (L, C, H)
seedOklch = toOklch(seed)
# Validate gamut; warn if out of sRGB
if !inSrgbGamut(seedOklch): warn("seed is out of sRGB; will be clipped")

# Step 2: detect edge case
edge = classifyEdgeCase(seedOklch)   # see §5
if edge: applyEdgeCaseRecipe(seedOklch, edge); return

# Step 3: build action role
# Target: WCAG 4.5:1 against a chosen action.foreground
# Try white foreground first
candidate = seedOklch
fgWhite = oklch(1, 0, 0)
if contrast(candidate, fgWhite) >= 4.5:
  action.default = candidate
  action.foreground = white
else:
  # darken until 4.5:1
  candidate.L = solveForContrast(candidate, fgWhite, target=4.5)
  if candidate.L < 0.30:
    # too dark; use light foreground but slightly increase chroma instead of darkening further
    action.default = boost(candidate)
    action.foreground = oklch(0.18, candidate.C * 0.2, candidate.H)
  else:
    action.default = candidate
    action.foreground = white
# hover/active
action.hover = adjust(action.default, deltaL = -0.04, deltaC = +0.02)
action.active = adjust(action.default, deltaL = -0.08, deltaC = +0.02)
action.disabled = adjust(action.default, deltaL = +/-0.10, deltaC × 0.3)

# Step 4: brand role
brand.accent = seedOklch  # raw seed — preserve recognition
brand.accent-foreground = pickForeground(brand.accent)

# Step 5: focus ring
# Must achieve 3:1 against every surface; usually solved by mid-tone of seed hue
focus.ring = solveFocusRing(seedHue, surfaces=[page, raised, sunken, overlay])

# Step 6: surfaces (mode-aware)
if mode == "light":
  surface.page    = oklch(0.99, 0, 0)
  surface.raised  = oklch(1.00, 0, 0)
  surface.sunken  = oklch(0.97, 0, 0)
  surface.overlay = oklch(0.20, 0, 0, alpha=0.5)
else:
  surface.page    = oklch(0.16, 0, 0)
  surface.raised  = oklch(0.20, 0, 0)
  surface.sunken  = oklch(0.13, 0, 0)
  surface.overlay = oklch(0.05, 0, 0, alpha=0.7)
on-surface-* = solvePerSurface(surface.*, target=4.5)

# Step 7: decorative
decorative.secondary = adjust(seedOklch, L=0.92 (light) | 0.30 (dark), C × 0.4)

# Step 8: status — DO NOT derive
status.success = MANUAL or harmonized green (~140°)
status.warning = MANUAL or harmonized yellow (~85°)
status.error   = MANUAL or harmonized red (~25°)
status.info    = MANUAL or harmonized blue (~240°)

# Step 9: validate every approved pair
for pair in approvedPairs:
  ratio = wcagContrast(pair.fg, pair.bg)
  record(pair, ratio)
  if ratio < target: fail(pair)
```

Output is the `colors` block of `design.json`, plus a `colors.contrast` log of every measured pair.

## 4. Why not brute complement / triadic / `+120°`

- **Brute complement (`+180°`)** ignores chroma and lightness; produces high-contrast pairs that are aesthetically jarring (red×green at full chroma).
- **Triadic (`+120° / +240°`)** picks colors with no functional relationship to action/brand. A triadic accent has no claim to be "the call-to-action color" or "the focus ring color".
- **Status colors (`success/warning/error`) derived from seed** break user expectation. Users learn green=success across the web; deriving green from an orange seed gives muddy olive that fails the heuristic.
- **Recommended:** use seed hue ± a small rotation (15–30°) for accents, full freedom for status (manual hex, then harmonized chroma/lightness to match seed's saturation profile).

## 5. Edge cases (8)

For each: detection, why default algorithm fails, recipe.

### 5.1 Dark purple seed (e.g. `#3b1f6b`, OKLCH ~ `0.30 0.13 290`)

- **Detect:** `L < 0.40 && C > 0.05`.
- **Failure:** `action.default = seed` is already too dark; white foreground gives huge contrast (~9:1) but UI feels heavy. Hover by darkening fails (already at floor).
- **Recipe:** Lift `L` to ~0.45 for `action.default`; preserve hue; hover by lifting another ~0.04 (counter-direction); active by reducing chroma. Brand stays at original.

### 5.2 Light yellow seed (e.g. `#f5d76e`, OKLCH ~ `0.87 0.14 95`)

- **Detect:** `L > 0.80`.
- **Failure:** White foreground fails badly (~1.4:1). Black foreground borderline (~7:1) but contrast vs hover/active weak.
- **Recipe:** Darken seed to L≈0.65 for `action.default`; black foreground; hover by darkening; brand.accent keeps raw seed (used on white surface where it can shine without text).

### 5.3 Saturated red seed (e.g. `#ff2d2d`, OKLCH ~ `0.62 0.25 25`)

- **Detect:** Hue ∈ [10°, 40°] && C > 0.20.
- **Failure:** Conflicts with `status.error`. Users will read every red button as "danger".
- **Recipe:** Either: (a) shift action hue to ~50° (orange), or (b) keep red and dedicate `status.error` to a deeper, less chromatic red (`L=0.50, C=0.18`). Document choice.

### 5.4 Saturated blue seed (e.g. `#1d4ed8`, OKLCH ~ `0.45 0.22 264`)

- **Detect:** Hue ∈ [240°, 280°] && C > 0.15.
- **Failure:** Conflicts with default browser link color and `status.info`. Plain `<a>` becomes invisible against `action.default`.
- **Recipe:** Style links explicitly (`text-decoration` + slight underline offset); do not rely on color alone for link discrimination; keep `status.info` distinct.

### 5.5 Green seed (e.g. `#10b981`, OKLCH ~ `0.70 0.16 162`)

- **Detect:** Hue ∈ [120°, 170°].
- **Failure:** Conflicts with `status.success`. "Save" buttons read as "completed" cues.
- **Recipe:** Either shift `status.success` away (toward 140° if seed is at 162°), or keep both and rely on iconography to disambiguate. Document.

### 5.6 Neutral gray seed (e.g. `#6b7280`, OKLCH ~ `0.55 0.01 250`)

- **Detect:** `C < 0.03`.
- **Failure:** No hue to derive from; algorithm produces grayscale tokens with no recognition.
- **Recipe:** Ask user for an **accent hue** as second input. Use neutral as `surface.*` and `on-surface-*` source; use accent for `action.default`, `focus.ring`, `brand.accent`.

### 5.7 Near-white seed (e.g. `#fafafa`, `L > 0.96`)

- **Detect:** `L > 0.95`.
- **Failure:** Cannot serve as `action.default` (no contrast to anything).
- **Recipe:** Reject as seed. If user insists, use as `surface.page` and require a separate `action` seed.

### 5.8 Near-black seed (e.g. `#0a0a0a`, `L < 0.10`)

- **Detect:** `L < 0.12`.
- **Failure:** Default algorithm produces an invisible token (no headroom).
- **Recipe:** Reject as seed; use as `on-surface` or text. Require separate seed for action/brand.

## 6. Acceptance criteria (Phase 5 gate)

- [ ] All approved pairs in `colors.contrast` ≥ 4.5:1 (text), 3:1 (large text, UI graphics).
- [ ] `focus.ring` ≥ 3:1 against `surface.page`, `surface.raised`, `surface.sunken`, `surface.overlay`.
- [ ] No status color derived from seed without explicit override note.
- [ ] No `action.default = brand.accent` unless seed has been validated as suitable for both roles (rare).
- [ ] Edge case applied if seed matched a case in §5.
- [ ] Dark mode tokens generated and validated separately if requested.
- [ ] Every token has at least one consumer (no orphan tokens).
- [ ] Foreground tested on **rendered pair**, not the abstract seed.

## 7. Boundary

- **WCAG thresholds (4.5, 3, 24×24, reflow):** owned by `ux-audit`. Imported here.
- **Token shape (`design.json`):** owned by `design-json-schema.md`.
- **Component-level use of tokens (which token lives in which slot):** owned by `component-architect`.
- **OKLCH/CSS gamut detection in browser:** owned by `react-patterns`.

## 8. References inside the skill

- `design-json-schema.md` — output shape.
- `responsive-design-system.md` — independent; tokens here feed primitives there.
- `component-state-rubric.md` — declares which `action.*`/`focus.*` tokens hover/focus/disabled states consume.
- `motion-and-interaction.md` — references `action.hover` timing.
