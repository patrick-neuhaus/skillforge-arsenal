# Pattern: registerEffect + Custom Elements (Telha Clarke pattern)

> **Source:** DR-A Awwwards Telha Clarke
> **Categoria:** declarative motion / encapsulation
> **Pilar:** transversal (todos pilares)
> **Quando usar:** quando padrão motion vira reusável em DOM (similar Web Component). Time grande precisando consistência sem cada dev escrever timeline GSAP.
> **Quando NÃO usar:** projeto pequeno onde 1 timeline GSAP basta. App altamente dinâmico onde patterns mudam frequente.

---

## Snippet canonical

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// 1. Registra effect customizado (1x boot)
gsap.registerEffect({
  name: 'scrubReveal',
  effect: (targets, config) => {
    return gsap.from(targets, {
      opacity: 0,
      y: config.distance,
      duration: config.duration,
      ease: config.ease,
      scrollTrigger: {
        trigger: targets,
        start: 'top 80%',
        end: 'top 30%',
        scrub: config.scrub,
      },
    });
  },
  defaults: {
    duration: 1,
    distance: 40,
    ease: 'osmo-ease',
    scrub: 0.5,
  },
  extendTimeline: true,
});

// 2. Custom Element que usa effect
class ScrubReveal extends HTMLElement {
  connectedCallback() {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) {
      this.style.opacity = 1;
      return;
    }

    gsap.effects.scrubReveal(this, {
      duration: parseFloat(this.dataset.duration) || 1,
      distance: parseFloat(this.dataset.distance) || 40,
    });
  }
}

customElements.define('scrub-reveal', ScrubReveal);
```

## Uso HTML (declarativo)

```html
<scrub-reveal data-duration="1.5" data-distance="60">
  <h2>Section Title</h2>
  <p>Body text reveals on scroll</p>
</scrub-reveal>

<scrub-reveal>
  <img src="hero.jpg" alt="Hero" />
</scrub-reveal>
```

## Por quê funciona

- **Encapsulation:** pattern motion vira "tag HTML" reusável.
- **Consistência:** todo `<scrub-reveal>` no app = mesmo motion calibrado.
- **Designer/dev junior friendly:** usa tag sem entender GSAP timeline.
- **DOM-native:** Custom Elements são standard browser API, não framework lock-in.

## Embasamento teórico

> "registerEffect + Custom Elements porque encapsulation + consistency — pattern motion vira API DOM declarativa. Time grande aplica `<scrub-reveal>` universalmente, garantindo motion polish consistente sem cada dev escrever timeline GSAP."

## Reduced motion

Built-in no `connectedCallback`:

```js
if (prefersReduced) {
  this.style.opacity = 1; // snap final state
  return;
}
```

## Anti-pattern

- **Effect sem defaults:** força usuário passar todos params = perde simplicidade.
- **Custom Element sem reduced motion:** decorativo sempre liga = WCAG 2.3.3 falha.
- **Effect complexo demais:** vira "macro" obscuro. Mantém effect = 1 timeline simples.
- **Custom Elements em React app:** prefer hook React custom (useScrubReveal) — Custom Elements + React = friction.

## Patterns de Custom Elements úteis

### `<scrub-reveal>` — section reveal on scroll

(Snippet canonical acima)

### `<kinetic-headline>` — kinetic typography

```js
gsap.registerEffect({
  name: 'kineticHeadline',
  effect: (targets, config) => {
    const split = new SplitText(targets, { type: 'words' });
    return gsap.from(split.words, {
      y: config.distance,
      opacity: 0,
      duration: config.duration,
      stagger: config.stagger,
      ease: 'osmo-ease',
    });
  },
  defaults: { duration: 0.8, distance: 40, stagger: 0.04 },
});

class KineticHeadline extends HTMLElement {
  connectedCallback() {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    gsap.effects.kineticHeadline(this);
  }
}
customElements.define('kinetic-headline', KineticHeadline);
```

### `<magnetic-button>` — magnetic cursor effect

```js
gsap.registerEffect({
  name: 'magnetic',
  effect: (targets) => {
    const el = targets[0] || targets;
    const xTo = gsap.quickTo(el, 'x', { duration: 0.6, ease: 'power3' });
    const yTo = gsap.quickTo(el, 'y', { duration: 0.6, ease: 'power3' });

    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      xTo(x * 0.3);
      yTo(y * 0.3);
    });

    el.addEventListener('mouseleave', () => {
      xTo(0);
      yTo(0);
    });
  },
});

class MagneticButton extends HTMLElement {
  connectedCallback() {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    gsap.effects.magnetic(this);
  }
}
customElements.define('magnetic-button', MagneticButton);
```

## Browser baseline

Custom Elements: Chrome 67+, Safari 10.1+, Firefox 63+. Universal modernos.
GSAP registerEffect: GSAP 3+.

## A11y

- Custom Elements continuam DOM normal — screen readers funcionam
- Reduced motion guard built-in
- Tag semântica preservada (Custom Element renderiza filhos)

## React caveat

Custom Elements + React = friction:
- React 18 suporta Custom Elements mas com quirks
- Prefer hook React custom equivalente:

```tsx
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';

export function useScrubReveal(ref, config = {}) {
  useGSAP(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    gsap.effects.scrubReveal(ref.current, config);
  }, { scope: ref });
}

// Uso
function Section() {
  const ref = useRef(null);
  useScrubReveal(ref, { duration: 1.5 });
  return <section ref={ref}>...</section>;
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 6
- React equivalent em `references/12-react-adapters.md`
