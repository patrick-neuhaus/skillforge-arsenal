# Pattern: Lenis + GSAP canonical sync

> **Source:** DR-0 + DR-B (Codrops Lenis tutorial)
> **Categoria:** smooth scroll infrastructure
> **Pilar:** 3 (narrativo/editorial)
> **Quando usar:** landing/portfolio/brand site precisando smooth scroll premium + ScrollTrigger sincronizado.
> **Quando NÃO usar:** SaaS operacional (atrapalha keyboard nav), mobile baixo (Lenis bypass touch nativo prejudica).

---

## Snippet canonical

```js
import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Reduced motion gate
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (prefersReduced) {
  // skip Lenis — usa scroll nativo
} else {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
    smoothTouch: false, // CRÍTICO: false em mobile
    touchMultiplier: 2,
  });

  // Canonical sync
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);

  lenis.on('scroll', ScrollTrigger.update);
}
```

## Por quê funciona

- **Continuity engine:** Lenis garante scroll suave consistente entre sections — sem isso, ScrollTrigger animations parecem "saltar" em scroll fast.
- **Sync canônico:** `gsap.ticker.add` + `lenis.raf` em mesma frame = ScrollTrigger updates byte-perfect com scroll Lenis.
- **`lagSmoothing(0)`:** desliga GSAP lag smoothing pra Lenis ter controle total.

## Embasamento teórico

> "Lenis canonical sync porque GSAP é continuity engine — Lenis providencia scroll input suave + GSAP ticker dá frame timing. Sem sync, ScrollTrigger lê scroll position desatualizado = jitter visual."

## Reduced motion

Skip Lenis inteiro. Scroll nativo respeitado. `prefers-reduced-motion: reduce` = user explicitamente pediu menos motion.

## Anti-pattern

- **`requestAnimationFrame` próprio chamando lenis.raf:** conflita com gsap.ticker = jitter.
- **Lenis em SaaS dashboard:** keyboard navigation (PageDown, Tab) com smooth scroll vira slow + frustrante.
- **Lenis com `smoothTouch: true`:** mobile users esperam scroll nativo touch — bypass causa "pegajoso".

## Browser baseline

Chrome 90+, Safari 15+, Firefox 88+. Universal modernos.

## A11y

- Reduced motion respeitado (skip completo)
- Keyboard navigation continua funcionando (não bypass)
- Focus indicator preserved

## React adapter

Ver `references/12-react-adapters.md` sec 8 — pattern `useLenis()` hook.

## Boundary

- Recipes detalhadas em `references/05-gsap-recipes.md` Recipe 1
- Foundations em `references/06-theoretical-foundations.md` sec 3.3 (scroll velocity)
