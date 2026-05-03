# 07 - `references/motion-and-interaction.md`

> Defines motion-as-system: durations, easing partition by use, canonical microinteractions, reduced-motion as a rule. Loaded in Phase 4.

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

Motion has 4 distinct uses; each gets its own easing family.

| Use | Easing | Why |
|---|---|---|
| **State responsive** (hover, focus, press) | `motion.easing.state-responsive`: `ease` or `cubic-bezier(0.25, 0.1, 0.25, 1)` | Symmetric; user expects immediate response |
| **Layout enter** (sheet open, drawer/modal in, popover show) | `motion.easing.layout-enter`: `ease-out` / `cubic-bezier(0.0, 0.0, 0.2, 1)` | Decelerates into rest; fast first frame |
| **Layout exit** (sheet close, drawer/modal out) | `motion.easing.layout-exit`: `ease-in` only for exits / `cubic-bezier(0.4, 0.0, 1, 1)` | Speeds away after user already decided |
| **Decorative** (page hero, illustration reveal) | `motion.easing.decorative`: expressive cubic-bezier or spring | Permits overshoot/bounce when context is celebratory |

Using a decorative spring for a state hover is slop. Using `ease` for a drawer is sluggish. Use the partition.

## 4. Canonical microinteractions

### 4.1 Hover
- Property: `background`, `box-shadow`, `transform: translateY(-1px)` (rare).
- Duration: `fast`.
- Easing: `ease`.
- Reduced motion: instant background swap; no translate.

### 4.2 Press / active
- Property: `background` (darker), `box-shadow: inset`, or `transform: scale(0.97-0.99)`.
- Duration: `instant` to `fast`.
- Easing: `motion.easing.state-responsive`.
- `scale(0.97-0.99)` is allowed for short press feedback when it does not shift layout, shrink the hit target, or run in high-frequency operational flows. Avoid `scale(0.95)` or bouncy press states.
- Reduced motion: background/shadow swap only.

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
- ❌ Exaggerated or permanent `transform: scale()` on press (hit-target instability).
- ❌ Skeleton/shimmer running during reduced motion.
- ❌ Auto-playing video without user trigger above the fold.
- ❌ Parallax on body scroll without reduced-motion guard.
- ❌ Different easing every component (no system).
- ❌ Animation hiding meaningful state change (user can't tell the form submitted because the button "wiggled and went back").

## 6. Acceptance criteria

- [ ] All 5 duration tokens declared.
- [ ] Easing partition documented and present in tokens (`motion.easing.state-responsive`, `motion.easing.layout-enter`, `motion.easing.layout-exit`, `motion.easing.decorative`).
- [ ] Every animation has a `prefers-reduced-motion` fallback.
- [ ] Press scale, when used, stays in `scale(0.97-0.99)` and has a non-motion fallback.
- [ ] No state animation > `motion.duration.normal`.
- [ ] No decorative easing on state transitions.
- [ ] All microinteractions in §4 use the canonical pattern.

## 7. Boundary

- **WCAG 2.3.3 (Animation from Interactions) compliance auditing:** `ux-audit`.
- **Motion implementation in React (Framer Motion, view transitions, CSS animations):** `react-patterns`.
- **Decorative animation for video/storytelling:** out of scope — see `animations.jsx` starter or video skills.
- **Token shape:** `design-json-schema.md` (this file declares the **policy**).
