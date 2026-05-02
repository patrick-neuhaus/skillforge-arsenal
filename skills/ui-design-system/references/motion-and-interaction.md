# 07 — `references/motion-and-interaction.md` (proposed)

> Proposed new reference. Defines motion-as-system: durations, easing partition by use, microinteractions canônicas, reduced-motion as a rule. Loaded in Phase 4.

---

# Motion and Interaction

## 1. Iron rule

`prefers-reduced-motion: reduce` is **regra**, never opcional. Every animation must declare a fallback that:
- Removes movement (no translate/scale entry).
- Keeps the meaningful change instant or short cross-fade (< 100ms).
- Preserves state changes — disabling motion never disables feedback.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
This is a default; specific motion may override with intentional cross-fade.

## 2. Duration tokens

| Token | Value | Use |
|---|---|---|
| `motion.duration.instant` | 0ms | State swaps that should not animate (disabled flag, error toggle) |
| `motion.duration.fast` | 100ms | Hover, focus-ring fade-in, tooltip show |
| `motion.duration.normal` | 200ms | Button press, modal scrim fade |
| `motion.duration.slow` | 320ms | Drawer slide, dropdown reveal, layout shifts |
| `motion.duration.decorative` | 480–800ms | Hero entry, onboarding flourish |

Anything beyond 800ms is suspect — either it's a real animation (video/Lottie) or it's slop.

## 3. Easing partition

Motion has 3 distinct uses; each gets its own easing family.

| Use | Easing | Why |
|---|---|---|
| **State** (hover, focus, press) | `ease` (`cubic-bezier(0.25, 0.1, 0.25, 1)`) | Symmetric; user expects symmetric response |
| **Layout** (sheet open, drawer slide, modal in) | `ease-out` (`cubic-bezier(0.0, 0.0, 0.2, 1)`) | Decelerates into rest; mimics physical inertia |
| **Decorative entry** (page hero, illustration reveal) | Expressive cubic-bezier (`cubic-bezier(0.34, 1.56, 0.64, 1)`) or spring | Permits overshoot/bounce when context is celebratory |

Using a decorative spring for a state hover is slop. Using `ease` for a drawer is sluggish. Use the partition.

## 4. Canonical microinteractions

### 4.1 Hover
- Property: `background`, `box-shadow`, `transform: translateY(-1px)` (rare).
- Duration: `fast`.
- Easing: `ease`.
- Reduced motion: instant background swap; no translate.

### 4.2 Press / active
- Property: `background` (darker) OR `box-shadow: inset`.
- Duration: `instant` to `fast`.
- Easing: `ease`.
- Avoid `transform: scale(0.95)` — it shifts hit targets and reads as a children's app.

### 4.3 Focus-visible
- Property: `outline` color/offset; `box-shadow: 0 0 0 3px var(--focus-ring)`.
- Duration: `fast`, can be instant (1ms) for keyboard immediacy.
- Reduced motion: instant.

### 4.4 Page / route transition
- Property: cross-fade `opacity` 0→1 on inbound; 1→0 on outbound.
- Duration: `normal`.
- Easing: `ease-out`.
- Skip if user navigates while animation runs (cancel + snap to final state).
- Reduced motion: instant.

### 4.5 Loading
- Spinner: rotate 360° linear, 1.2s cycle.
- Skeleton shimmer: linear gradient sweep, 1.5s cycle.
- Reduced motion: spinner becomes a non-animated dotted ring or text label; skeleton becomes static neutral block.

### 4.6 Layout transition (e.g. card expand, list item add)
- FLIP technique (`getBoundingClientRect` → animate `transform`).
- Duration: `slow`.
- Easing: `ease-out`.
- Reduced motion: instant snap to new position.

### 4.7 Tooltip / popover
- Show: opacity 0→1, slight `translateY(2px)→0`.
- Duration: `fast`.
- Delay before show: 400ms (Fitts) or 0ms if user just dismissed another.
- Reduced motion: instant fade only, no translate.

### 4.8 Toast / snackbar
- Slide-in from edge + fade.
- Duration: `slow`.
- Easing: `ease-out`.
- Auto-dismiss: 4–6s for info; manual for error.
- Reduced motion: fade only.

## 5. Anti-patterns

- ❌ Animation without reduced-motion fallback.
- ❌ Decorative easing (overshoot/bounce) on functional state changes.
- ❌ Long durations (>500ms) for state transitions.
- ❌ `transform: scale()` on press (hit-target instability).
- ❌ Skeleton/shimmer running during reduced motion.
- ❌ Auto-playing video without user trigger above the fold.
- ❌ Parallax on body scroll without reduced-motion guard.
- ❌ Different easing every component (no system).
- ❌ Animation hiding meaningful state change (user can't tell the form submitted because the button "wiggled and went back").

## 6. Acceptance criteria

- [ ] All 5 duration tokens declared.
- [ ] Easing partition documented and present in tokens (`motion.easing.state`, `motion.easing.layout`, `motion.easing.decorative`).
- [ ] Every animation has a `prefers-reduced-motion` fallback.
- [ ] No `transform: scale()` on interactive press states.
- [ ] No state animation > `motion.duration.normal`.
- [ ] No decorative easing on state transitions.
- [ ] All microinteractions in §4 use the canonical pattern.

## 7. Boundary

- **WCAG 2.3.3 (Animation from Interactions) compliance auditing:** `ux-audit`.
- **Motion implementation in React (Framer Motion, view transitions, CSS animations):** `react-patterns`.
- **Decorative animation for video/storytelling:** out of scope — see `animations.jsx` starter or video skills.
- **Token shape:** `design-json-schema.md` (this file declares the **policy**).
