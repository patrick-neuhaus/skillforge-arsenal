# Pattern: Osmo-style button effects (50+ patterns)

> **Source:** DR-C Osmo Supply Button Pack
> **Categoria:** microinteractions / brand polish
> **Pilar:** 1 (funcional/estrutural) + 2 (vetorial/branding)
> **Quando usar:** botões CTA premium em landing/portfolio/brand site. Calibrado pra "polish award-grade".
> **Quando NÃO usar:** SaaS operacional repetido (overhead em UI 100+/dia), B2B enterprise austero (bounce/elastic quebra trust).

---

## Variant 1 — Hover lift + shadow

```css
.btn-lift {
  transition: transform 250ms cubic-bezier(0.625, 0.05, 0, 1),
              box-shadow 250ms cubic-bezier(0.625, 0.05, 0, 1);
  will-change: transform;
}

.btn-lift:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.btn-lift:active {
  transform: translateY(0) scale(0.98);
  transition-duration: 80ms;
}

@media (hover: hover) and (pointer: fine) {
  .btn-lift:hover { /* hover só em devices c/ ponteiro fino */ }
}

@media (prefers-reduced-motion: reduce) {
  .btn-lift { transition: none; }
}
```

**Quando usar:** CTA principal landing, primary action.

---

## Variant 2 — Magnetic button (cursor follower)

```js
import { gsap } from 'gsap';

const button = document.querySelector('.btn-magnetic');
const xTo = gsap.quickTo(button, 'x', { duration: 0.6, ease: 'power3' });
const yTo = gsap.quickTo(button, 'y', { duration: 0.6, ease: 'power3' });

button.addEventListener('mousemove', (e) => {
  const rect = button.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;
  xTo(x * 0.3); // magnetic strength = 0.3
  yTo(y * 0.3);
});

button.addEventListener('mouseleave', () => {
  xTo(0);
  yTo(0);
});

// Reduced motion
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
  button.removeEventListener('mousemove', /* handler */);
}
```

**Quando usar:** hero CTA premium, brand site signature button. Apenas devices c/ ponteiro fino.

**Anti-pattern:** magnetic em mobile (touch sem mousemove) = inútil overhead.

---

## Variant 3 — Border draw on hover

```html
<button class="btn-border-draw">
  Click me
  <svg class="border-svg" viewBox="0 0 200 50">
    <rect x="1" y="1" width="198" height="48" fill="none" stroke="currentColor" stroke-width="2" />
  </svg>
</button>
```

```css
.btn-border-draw {
  position: relative;
  background: transparent;
  border: none;
}

.border-svg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.border-svg rect {
  stroke-dasharray: 500;
  stroke-dashoffset: 500;
  transition: stroke-dashoffset 600ms ease-out;
}

.btn-border-draw:hover .border-svg rect {
  stroke-dashoffset: 0;
}

@media (prefers-reduced-motion: reduce) {
  .border-svg rect { transition: none; stroke-dashoffset: 0; }
}
```

**Quando usar:** brand site editorial, portfolio agency. Tom "self-drawing" elegante.

---

## Variant 4 — Background gradient shift

```css
.btn-gradient-shift {
  background: linear-gradient(120deg, #6366f1 0%, #8b5cf6 50%, #6366f1 100%);
  background-size: 200% 100%;
  background-position: 0% 0%;
  transition: background-position 400ms cubic-bezier(0.625, 0.05, 0, 1);
}

.btn-gradient-shift:hover {
  background-position: 100% 0%;
}
```

**Quando usar:** brand site moderno, fintech premium, AI/SaaS landing.

---

## Variant 5 — Icon morph state (rotational)

```html
<button class="btn-icon-morph" aria-label="Open menu">
  <svg viewBox="0 0 24 24">
    <path id="icon-path" d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" />
  </svg>
</button>
```

```js
import { gsap } from 'gsap';
import { MorphSVGPlugin } from 'gsap/MorphSVGPlugin';

gsap.registerPlugin(MorphSVGPlugin);

const button = document.querySelector('.btn-icon-morph');
let isOpen = false;

button.addEventListener('click', () => {
  isOpen = !isOpen;
  gsap.to('#icon-path', {
    morphSVG: {
      shape: isOpen ? 'M6 6l12 12M6 18L18 6' : 'M3 6h18M3 12h18M3 18h18',
      type: 'rotational',
    },
    duration: 0.4,
    ease: 'power2.inOut',
  });
});
```

**Quando usar:** menu hamburger ↔ close, play ↔ pause.

---

## Variant 6 — Press compress + spring back

```css
.btn-press {
  transition: transform 100ms ease-out;
}

.btn-press:active {
  transform: scale(0.96);
  transition-duration: 80ms;
}

/* Spring back via JS pra control finer */
```

```js
import { gsap } from 'gsap';

const button = document.querySelector('.btn-press');

button.addEventListener('mousedown', () => {
  gsap.to(button, { scale: 0.96, duration: 0.08, ease: 'power2.out' });
});

button.addEventListener('mouseup', () => {
  gsap.to(button, { scale: 1, duration: 0.4, ease: 'elastic.out(1, 0.5)' });
});
```

**Quando usar:** botões interativos importantes onde tato matters. CTA hero.

---

## Variant 7 — Liquid CTA (SVG turbulence filter)

```html
<svg width="0" height="0">
  <filter id="liquid-filter">
    <feTurbulence id="turbulence" type="fractalNoise" baseFrequency="0.02" numOctaves="2" />
    <feDisplacementMap in="SourceGraphic" scale="20" />
  </filter>
</svg>

<button class="btn-liquid">Hover me</button>
```

```css
.btn-liquid {
  filter: url(#liquid-filter);
  transition: filter 400ms ease-out;
}

.btn-liquid:hover #turbulence {
  /* Animar baseFrequency via JS */
}
```

```js
gsap.to('#turbulence', {
  attr: { baseFrequency: 0.05 },
  duration: 0.6,
  ease: 'power2.out',
});
```

**Quando usar:** brand creative agency, fintech premium, design experimental.

**Anti-pattern:** liquid em SaaS B2B serioso = quebra trust.

---

## Variant 8 — Text reveal on hover

```html
<button class="btn-text-reveal">
  <span class="text-default">Hover me</span>
  <span class="text-hover">Click here</span>
</button>
```

```css
.btn-text-reveal {
  position: relative;
  overflow: hidden;
}

.text-default,
.text-hover {
  display: block;
  transition: transform 300ms cubic-bezier(0.625, 0.05, 0, 1);
}

.text-hover {
  position: absolute;
  inset: 0;
  transform: translateY(100%);
}

.btn-text-reveal:hover .text-default {
  transform: translateY(-100%);
}

.btn-text-reveal:hover .text-hover {
  transform: translateY(0);
}
```

**Quando usar:** brand site polish, portfolio.

---

## Decision tree — qual variant escolher

```
Tom session narrative?
├─ Minimal técnico (B2B SaaS) → Variant 1 (lift), Variant 6 (press)
├─ Cinematic premium (sales premium) → Variant 4 (gradient), Variant 8 (text reveal)
├─ Lúdico criativo (creator brand) → Variant 2 (magnetic), Variant 7 (liquid)
├─ Brutalist editorial → Variant 3 (border draw)
└─ Funcional state change → Variant 5 (icon morph)
```

## Reduced motion fallback (todas variants)

```css
@media (prefers-reduced-motion: reduce) {
  .btn-lift,
  .btn-magnetic,
  .btn-border-draw,
  .btn-gradient-shift,
  .btn-icon-morph,
  .btn-press,
  .btn-liquid,
  .btn-text-reveal {
    transition: none !important;
    animation: none !important;
    transform: none !important;
  }
}
```

## A11y crítico todos buttons

- `:focus-visible` indicator obrigatório
- `aria-label` em icon-only buttons
- Keyboard activation (Enter/Space) funcionando
- Estado disabled `pointer-events: none` + `aria-disabled`
- Reduced motion respeitado (snap-to-state)

## DIY vs Osmo decision

Ver `references/09-osmo-comparable.md` sec 3 — quando comprar Osmo Member faz sentido vs DIY.

**Resumo:** se Patrick faz 1+ projeto Webflow/mês, Osmo Member €25/mês amortiza com 1 projeto. DIY se brand-specific OR projeto único.

## Browser baseline

- CSS transitions/transforms: universal
- SVG morphSVG: requer GSAP MorphSVG plugin (paid)
- Magnetic: GSAP universal
- Liquid filter SVG: Chrome/Safari/Firefox modernos

## Boundary

- Pilar 1 microinteractions em `references/01-funcional-estrutural.md`
- Foundations easing em `references/06-theoretical-foundations.md` sec 4
- DIY vs Osmo em `references/09-osmo-comparable.md`
