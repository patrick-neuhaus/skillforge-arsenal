# Pattern: Scroll-driven CSS variables

> **Source:** DR-B Codrops scroll progress patterns
> **Categoria:** scroll-driven / progressive enhancement
> **Pilar:** 3 (narrativo/editorial)
> **Quando usar:** quando design quer expor scroll progress pra CSS (gradient shifting, opacity calc, transform compose) sem múltiplas timelines GSAP.
> **Quando NÃO usar:** scroll-trigger simples (CSS scroll-driven animations API direta basta), animation 1-shot (não precisa progress contínuo).

---

## Snippet canonical — JS-driven (compatibility ampla)

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReduced) {
  // Snap progress final
  document.documentElement.style.setProperty('--scroll-progress', '0');
} else {
  gsap.to({ progress: 0 }, {
    progress: 1,
    scrollTrigger: {
      trigger: '.section-narrative',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 0.5,
    },
    onUpdate: function() {
      const progress = this.targets()[0].progress;
      document.documentElement.style.setProperty('--scroll-progress', progress);
    },
  });
}
```

## CSS consume

```css
/* Gradient shift baseado em scroll */
.gradient-bg {
  background: linear-gradient(
    to bottom,
    hsl(220, 80%, calc(20% + (var(--scroll-progress, 0) * 40%))),
    hsl(280, 80%, calc(40% + (var(--scroll-progress, 0) * 30%)))
  );
}

/* Opacity calc */
.fade-element {
  opacity: calc(1 - var(--scroll-progress, 0));
}

/* Transform compose */
.parallax-layer {
  transform:
    translateY(calc(var(--scroll-progress, 0) * -50px))
    scale(calc(1 + var(--scroll-progress, 0) * 0.1));
}

/* Filter blur progressive */
.blur-on-scroll {
  filter: blur(calc(var(--scroll-progress, 0) * 10px));
}
```

## Snippet alternativo — CSS scroll-driven nativo (modern browsers)

```css
@keyframes scroll-progress {
  to { --scroll-progress: 1; }
}

@property --scroll-progress {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

:root {
  animation: scroll-progress linear;
  animation-timeline: scroll();
}

@media (prefers-reduced-motion: reduce) {
  :root {
    animation: none;
  }
}
```

## Por quê funciona

- **Separation of concerns:** JS gerencia scroll listener (uma vez), CSS gerencia visual transformations.
- **Performance:** mais barato que múltiplas timelines GSAP transformando properties.
- **CSS power:** `calc()` + CSS variables permite transformações compostas elegantes.
- **Compositor-friendly:** browser pode usar GPU compositor pra transforms baseados em CSS vars.

## Embasamento teórico

> "Scroll-driven CSS variables porque separation of concerns — JS gerencia scroll listener (uma vez), CSS gerencia visual transformations. Mais performático que múltiplas timelines GSAP transformando properties direto."

## Reduced motion

Snap `--scroll-progress: 0` (ou `1` se preferir final state). CSS variables respeitam reduced motion automaticamente quando usados em `transform/opacity` properties.

## Anti-pattern

- **Animar layout properties via CSS vars:** `width/height/top/left` causa layout thrash.
- **CSS vars em filter pesado:** `blur()` com scroll causa GPU usage alta — moderar amplitude.
- **Scroll listener próprio sem ScrollTrigger:** miss optimizations Lenis sync.

## Performance

- CSS variable updates = barato (compositor-friendly)
- `scrub: 0.5` smoothing previne jitter
- Tabular: 1 listener JS scroll = 100s de animations CSS dependentes

## Browser baseline

- CSS variables: Chrome 49+, Safari 9.1+, Firefox 31+ (universal)
- `@property`: Chrome 85+, Safari 16.4+, Firefox 128+
- CSS scroll-driven: Chrome 115+, Edge 115+, Firefox 110+ (flag), Safari TP

## A11y

- Reduced motion: snap final state
- Conteúdo legível durante scroll progressive
- Sem dependence em motion pra entender conteúdo

## Casos de uso award-grade

### 1. Hero gradient cinematic shift
Hero com gradient mudando lentamente conforme user scroll = ambient sutil sem competir mensagem.

### 2. Progressive blur on parallax
Foreground blur conforme background pulled com scroll = depth premium.

### 3. Color theme shift entre sections
Section A azul → Section B violeta via CSS variable cores controladas por scroll progress.

### 4. Reading progress visual
`width: calc(var(--scroll-progress) * 100%)` em barra fixa.

## React adapter

```tsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function ScrollDrivenSection() {
  const ref = useRef(null);

  useGSAP(() => {
    gsap.to({ progress: 0 }, {
      progress: 1,
      scrollTrigger: {
        trigger: ref.current,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.5,
      },
      onUpdate: function() {
        ref.current?.style.setProperty('--scroll-progress', this.targets()[0].progress);
      },
    });
  }, { scope: ref });

  return <section ref={ref} className="scroll-narrative">...</section>;
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 8
- Foundations scroll psychology em `references/06-theoretical-foundations.md` sec 3
