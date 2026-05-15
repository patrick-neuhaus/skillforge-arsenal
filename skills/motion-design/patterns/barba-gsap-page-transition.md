# Pattern: Barba.js + GSAP page transition

> **Source:** DR-A + DR-B (Awwwards stack pattern B)
> **Categoria:** page transitions / SPA continuity
> **Pilar:** 3 (narrativo/editorial)
> **Quando usar:** site multi-page (não SPA framework) precisando page transitions cinematográficas. Webflow + GSAP + Barba é stack canônica Awwwards-tier.
> **Quando NÃO usar:** Lovable/Next/Astro (router próprio). Site single-page. SaaS dashboard.

---

## Setup

```bash
npm install @barba/core gsap
```

```html
<!-- HTML structure obrigatória -->
<body data-barba="wrapper">
  <main data-barba="container" data-barba-namespace="home">
    <!-- conteúdo página home -->
  </main>
</body>
```

## Snippet canonical — fade transition

```js
import barba from '@barba/core';
import { gsap } from 'gsap';

// Reduced motion gate
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

barba.init({
  transitions: [{
    name: 'fade',
    leave({ current }) {
      if (prefersReduced) return Promise.resolve();
      return gsap.to(current.container, {
        opacity: 0,
        duration: 0.4,
        ease: 'power2.in',
      });
    },
    enter({ next }) {
      if (prefersReduced) return Promise.resolve();
      return gsap.from(next.container, {
        opacity: 0,
        duration: 0.4,
        ease: 'power2.out',
      });
    },
  }],
});
```

## Snippet — cinematic transition (curtain reveal)

```js
barba.init({
  transitions: [{
    name: 'curtain',
    leave({ current }) {
      if (prefersReduced) return Promise.resolve();

      const tl = gsap.timeline();
      tl.to('.curtain', {
        scaleY: 1,
        duration: 0.6,
        ease: 'power3.in',
        transformOrigin: 'top',
      });
      tl.to(current.container, { opacity: 0, duration: 0.1 });
      return tl;
    },
    enter({ next }) {
      if (prefersReduced) return Promise.resolve();

      const tl = gsap.timeline();
      tl.from(next.container, { opacity: 0, duration: 0.1 });
      tl.to('.curtain', {
        scaleY: 0,
        duration: 0.6,
        ease: 'power3.out',
        transformOrigin: 'bottom',
      });
      return tl;
    },
  }],
});
```

## Snippet — namespace-specific transition

```js
barba.init({
  transitions: [
    {
      name: 'home-to-work',
      from: { namespace: 'home' },
      to: { namespace: 'work' },
      leave({ current }) {
        return gsap.to(current.container, {
          xPercent: -100,
          duration: 0.6,
          ease: 'osmo-ease',
        });
      },
      enter({ next }) {
        return gsap.from(next.container, {
          xPercent: 100,
          duration: 0.6,
          ease: 'osmo-ease',
        });
      },
    },
    // Default fallback
    {
      name: 'default',
      leave({ current }) {
        return gsap.to(current.container, { opacity: 0, duration: 0.4 });
      },
      enter({ next }) {
        return gsap.from(next.container, { opacity: 0, duration: 0.4 });
      },
    },
  ],
});
```

## ScrollTrigger refresh em route change

```js
import { ScrollTrigger } from 'gsap/ScrollTrigger';

barba.hooks.afterEnter(() => {
  ScrollTrigger.refresh();
  window.scrollTo(0, 0);
});
```

## Persistent canvas integration

Ver `patterns/persistent-canvas.md` — canvas persiste entre rotas, Barba só atualiza scene state.

## Por quê funciona

- **Continuity entre rotas:** transição cinematográfica preserva sensação de "site coeso", não páginas isoladas.
- **No reload:** Barba intercepta links + faz fetch async = instant feel.
- **Namespace targeting:** transições diferentes por contexto (home→work ≠ work→detail).
- **GSAP timeline orchestration:** complete control sobre timing.

## Embasamento teórico

> "Barba+GSAP page transition cinematográfica porque continuity gestalt entre rotas — user percebe site como experiência única, não páginas isoladas. Reload tradicional quebra essa percepção."

## Reduced motion

Skip transition GSAP, mas Barba ainda intercepta link (instant page change).

```js
if (prefersReduced) return Promise.resolve(); // skip animation, prossegue
```

## Anti-pattern

- **Transition > 800ms:** user navega 3+ vezes/sessão = friction acumulada.
- **Sem ScrollTrigger refresh:** posições stale na página nova.
- **Sem `window.scrollTo(0, 0)`:** página nova carrega no scroll position antigo.
- **Barba em SPA framework (React/Next):** conflita com router próprio.
- **Sem namespace fallback:** rota nova sem transition = crash.

## Performance

- Asset preload via `barba.hooks.beforeLeave` pra próxima rota
- Cache HTML pages (Barba faz default)
- Avoid heavy animations during fetch (user esperando = frustração)

## Browser baseline

Chrome 60+, Safari 10+, Firefox 55+. Universal.

## A11y

- Focus management: focus pro main content da rota nova
- Screen reader announce route change (use `aria-live` region OR Barba afterEnter hook)
- History API funciona (back button)
- Reduced motion respeitado

## React caveat

NÃO usar Barba em Next.js / Lovable. Use:
- Next.js: View Transitions API + GSAP fallback
- Lovable React Router: framer-motion `<AnimatePresence>` OU GSAP custom
- Astro: View Transitions nativo

## Boundary

- Persistent canvas em `patterns/persistent-canvas.md`
- Page transitions React em `references/12-react-adapters.md`
- Foundations continuity gestalt em `references/06-theoretical-foundations.md` sec 1.1
