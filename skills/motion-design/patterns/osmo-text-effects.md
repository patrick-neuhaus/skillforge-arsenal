# Pattern: Osmo-style text effects (30+ patterns)

> **Source:** DR-C Osmo Supply text effects collection
> **Categoria:** kinetic typography / brand expression
> **Pilar:** 2 (vetorial/branding) + 3 (narrativo/editorial)
> **Quando usar:** headlines, manifestos, slogans rotativos, hero text reveal. Brand polish award-grade.
> **Quando NÃO usar:** corpo de texto, parágrafos, body copy, termos legais (atrapalha leitura WCAG 2.2.2).

---

## Variant 1 — Word stagger reveal (canonical)

```js
import { SplitText } from 'gsap/SplitText';
const split = new SplitText('.headline', { type: 'words' });
gsap.from(split.words, {
  y: 40,
  opacity: 0,
  stagger: 0.04,
  duration: 0.8,
  ease: 'osmo-ease',
});
```

Ver `patterns/splittext-stagger.md` pra detalhamento completo.

---

## Variant 2 — Letter swap loop (slogan rotativo)

```html
<h1 class="headline-rotate">
  We make
  <span class="rotator">
    <span>websites</span>
    <span>brands</span>
    <span>experiences</span>
  </span>
  awesome.
</h1>
```

```js
import { gsap } from 'gsap';

const slots = document.querySelectorAll('.rotator span');
const tl = gsap.timeline({ repeat: -1 });

slots.forEach((slot, i) => {
  tl.to(slot, { y: -100, opacity: 0, duration: 0.4, ease: 'power3.in' }, i * 2);
  tl.fromTo(
    slots[(i + 1) % slots.length],
    { y: 100, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.4, ease: 'power3.out' },
    i * 2 + 0.4
  );
});

// Reduced motion: pause loop
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
  tl.kill();
}
```

**Quando usar:** brand site, tagline rotativo manifesto.

**Anti-pattern WCAG 2.2.2:** loop > 5s precisa pause control. Adicionar `<button>` toggle play/pause.

---

## Variant 3 — Text scrub reveal on scroll

```js
import { SplitText } from 'gsap/SplitText';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

const split = new SplitText('.scroll-reveal', { type: 'words' });

gsap.from(split.words, {
  opacity: 0.2, // partial dim, não 0
  stagger: 0.05,
  scrollTrigger: {
    trigger: '.scroll-reveal',
    start: 'top 80%',
    end: 'bottom 30%',
    scrub: 0.5,
  },
});
```

**Quando usar:** editorial premium, manifesto long-form. Texto "ilumina" conforme scroll.

---

## Variant 4 — Marquee horizontal contínuo

```html
<div class="marquee">
  <div class="marquee-track">
    <span>WORD</span> <span>WORD</span> <span>WORD</span>
    <span>WORD</span> <span>WORD</span> <span>WORD</span>
  </div>
</div>
```

```css
.marquee {
  overflow: hidden;
  white-space: nowrap;
}

.marquee-track {
  display: inline-flex;
  gap: 2rem;
  animation: marquee 30s linear infinite;
  will-change: transform;
}

@keyframes marquee {
  to { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .marquee-track { animation: none; }
}
```

**Quando usar:** brand banner, fintech ticker, social proof logos.

**Anti-pattern WCAG 2.2.2:** marquee contínuo > 5s precisa pause. Adicionar pause-on-hover OR button.

```css
.marquee:hover .marquee-track { animation-play-state: paused; }
```

---

## Variant 5 — Variable font weight pulse

```css
@font-face {
  font-family: 'BrandFont';
  src: url('font-variable.woff2') format('woff2-variations');
  font-weight: 100 900;
}

.headline-pulse {
  font-family: 'BrandFont';
  animation: weight-pulse 4s ease-in-out infinite;
}

@keyframes weight-pulse {
  0%, 100% { font-variation-settings: 'wght' 400; }
  50% { font-variation-settings: 'wght' 700; }
}

@media (prefers-reduced-motion: reduce) {
  .headline-pulse { animation: none; }
}
```

**Quando usar:** brand site moderno com variable font, slogan highlight.

---

## Variant 6 — Typewriter effect

```js
const text = 'Welcome to the future';
const target = document.querySelector('.typewriter');
let i = 0;

const interval = setInterval(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    target.textContent = text;
    clearInterval(interval);
    return;
  }

  target.textContent = text.slice(0, i++);
  if (i > text.length) clearInterval(interval);
}, 50); // 50ms por char
```

**Quando usar:** brand creator/dev, retrô-tech aesthetic, terminal feel.

**Anti-pattern:** typewriter em conteúdo crítico — atrasa leitura sem benefício.

---

## Variant 7 — Glitch / distortion text

```css
@keyframes glitch {
  0%, 100% { text-shadow: 0 0 0 transparent; }
  10% { text-shadow: -2px 0 0 #ff0080, 2px 0 0 #00ffff; }
  20% { text-shadow: 2px 0 0 #ff0080, -2px 0 0 #00ffff; }
  30% { text-shadow: 0 -2px 0 #ff0080, 0 2px 0 #00ffff; }
  /* ... */
}

.headline-glitch {
  animation: glitch 200ms steps(2) infinite;
}

@media (prefers-reduced-motion: reduce) {
  .headline-glitch { animation: none; }
}
```

**Quando usar:** brand experimental, gaming, cyberpunk aesthetic.

**Anti-pattern:** glitch contínuo em SaaS sério — quebra trust completamente.

---

## Variant 8 — Liquid morph text

Combina SVG morph com text path. Complexo. Ver Codrops tutorials.

---

## Variant 9 — 3D text rotation

```css
.headline-3d {
  perspective: 1000px;
}

.headline-3d span {
  display: inline-block;
  transform-origin: 50% 50% -50px;
  animation: rotate3d 4s linear infinite;
}

@keyframes rotate3d {
  to { transform: rotateY(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .headline-3d span { animation: none; }
}
```

**Quando usar:** brand experimental, decorative hero, ludic creative.

---

## Variant 10 — Text-on-path animation

```html
<svg viewBox="0 0 500 200">
  <path id="textPath" d="M 50 100 Q 250 0 450 100" fill="none" />
  <text>
    <textPath href="#textPath" startOffset="0">
      Curved text reveal
      <animate
        attributeName="startOffset"
        from="100%"
        to="0%"
        dur="2s"
        fill="freeze"
      />
    </textPath>
  </text>
</svg>
```

**Quando usar:** brand creative, editorial layouts artísticos.

---

## Decision tree — qual variant escolher

```
Tom session narrative + section?
├─ Sales premium hero → Variant 1 (word stagger), Variant 5 (variable weight)
├─ Brand creative manifesto → Variant 2 (rotator), Variant 9 (3D), Variant 10 (path)
├─ Editorial premium long-form → Variant 3 (scroll scrub)
├─ Fintech/tech ticker → Variant 4 (marquee)
├─ Brand experimental gaming → Variant 7 (glitch)
├─ Creator/dev retrô → Variant 6 (typewriter)
└─ B2B SaaS minimal → Variant 1 simples (sem stagger pesado)
```

## Reduced motion (todas variants)

Snap final state OR pause loop. NEVER continuar motion contínuo.

## A11y crítico

- WCAG 2.2.2: motion contínuo > 5s precisa pause control
- WCAG 2.3.1: flashing > 3x/segundo proibido (Variant 7 glitch atenção)
- SplitText `revert()` em unmount preserva texto
- Screen readers veem texto completo (não fragmentos)

## DIY vs Osmo

Osmo Supply tem 30+ text effects calibrados. Se Patrick faz Webflow + 1+ projeto/mês, Osmo Member amortiza. DIY se brand-specific.

## Browser baseline

- SplitText: GSAP paid
- Variable fonts: Chrome 62+, Safari 11+, Firefox 62+
- SVG textPath animation: universal
- CSS animations: universal

## Boundary

- SplitText pattern em `patterns/splittext-stagger.md`
- Foundations gestalt em `references/06-theoretical-foundations.md` sec 1
- Pilar 2 vetorial/branding em `references/02-vetorial-branding.md`
