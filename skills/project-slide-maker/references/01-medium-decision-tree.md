# Medium Decision Tree

> Mapeia `slide.type` + content → medium. Carrega na Phase 3.

## Tree

```
slide.type == 'cover' / 'hero':
  has video asset           → 'video' (MP4 background)
  branded interactive       → 'rive'
  static + tw-animate       → 'css'

slide.type == 'demo':
  drag/move/sort            → 'framer-motion' (layoutId)
  typing/sequence           → 'framer-motion' (stagger variants)
  form filling              → 'framer-motion' (filter/blur sequence)
  data animating            → 'framer-motion' (useMotionValue + useTransform)
  single state hover        → 'css'

slide.type == 'feature':
  static showcase           → 'css' (tw-animate-css)
  micro-decoration          → 'lottie' (icon)

slide.type == 'transcript' / 'closing':
  → 'css' (View Transitions API ok)

slide.type == 'page-transition':
  → 'css' (View Transitions API + AnimatePresence)
```

## Justificativa

Compilado de DR03 pattern inventory (2026-05-04, `outputs/motion-03-pattern-inventory-gemini-2026-05-04.md`):

> 9/10 casos do Patrick precisam Framer Motion. Apenas hover micro-interactions e PDF region select rodam puro CSS/DOM.

## Reduced-motion fallback (IL2 gate)

Cada medium declara fallback explícito:

| Medium | Fallback reduced-motion |
|---|---|
| video | poster image static (primeiro frame) |
| framer-motion | snap final state sem transition (`useReducedMotion()`) |
| lottie | first frame static (`autoplay={false}`) |
| rive | first state machine state |
| css | no animation, snap state direto |

Sem fallback declarado = slide não passa Phase 5 gate.
