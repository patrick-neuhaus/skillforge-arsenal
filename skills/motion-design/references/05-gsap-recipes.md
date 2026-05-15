# `references/05-gsap-recipes.md` — GSAP Recipes Canonical (Wave 9)

> **11 receitas GSAP** extraídas dos 4 DRs (DR-0 canonical + DR-A 10 showcases + DR-B Codrops/Awwwards + DR-C Osmo Supply). Snippets byte-perfect, contexto de uso, fallback reduced motion, browser baseline.
> **Quando usar:** Phase 1 lookup do `--full` consulta esta ref pra recipes GSAP candidatas. `--quick` tb pode usar invocando `motion-design --spec gsap-<recipe>`.
> **Boundary:** receitas core GSAP. React/Next/Astro adapters em `12-react-adapters.md`. Theoretical foundations em `06-theoretical-foundations.md`.

---

## 0. Setup canonical (qualquer recipe assume isso)

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { CustomEase } from "gsap/CustomEase";
import { SplitText } from "gsap/SplitText";
import { Flip } from "gsap/Flip";

gsap.registerPlugin(ScrollTrigger, CustomEase, SplitText, Flip);
```

**Cleanup React (sempre):** usa `useGSAP` hook do `@gsap/react` OR `gsap.context()` em mount/unmount. Detalhes em `12-react-adapters.md`.

**Reduced motion guard:** TODA recipe DEVE ter:
```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (prefersReducedMotion) {
  // snap-to-end OR alternativa segura
  return;
}
```

---

## Recipe 1 — Lenis canonical sync com GSAP

**Source:** DR-0 + DR-B (Codrops Lenis tutorial)
**Quando usar:** smooth scroll em landing/portfolio/brand site. Sincroniza Lenis com `gsap.ticker` pra ScrollTrigger funcionar correto.
**Quando NÃO usar:** SaaS operacional (smooth scroll em dashboard atrapalha keyboard navigation), mobile baixo (Lenis bypass touch nativo).

```js
import Lenis from '@studio-freight/lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  smoothTouch: false, // CRÍTICO: false em mobile
  touchMultiplier: 2,
});

// Canonical sync GSAP ticker
gsap.ticker.add((time) => {
  lenis.raf(time * 1000); // ms→s conversion
});
gsap.ticker.lagSmoothing(0); // disable lag smoothing pra Lenis

// Update ScrollTrigger no scroll
lenis.on('scroll', ScrollTrigger.update);
```

**Reduced motion fallback:**
```js
if (prefersReducedMotion) {
  // skip Lenis entirely — usa scroll nativo
  return;
}
```

**Browser baseline:** Chrome 90+, Safari 15+, Firefox 88+. Lenis funciona em todos modernos.

**Anti-pattern:** chamar `lenis.raf()` em `requestAnimationFrame` próprio. Conflita com gsap.ticker e causa jitter.

---

## Recipe 2 — CustomEase nomeado (osmo-ease canonical)

**Source:** DR-C (Osmo Supply curve nomeada)
**Quando usar:** quando tom motion = "cinematic premium" / "polish award-grade". CustomEase nomeado vira token reusável.
**Quando NÃO usar:** SaaS operacional simples (ease-out CSS basta).

```js
// Define curves nomeadas (1x no app boot)
CustomEase.create("osmo-ease", "0.625, 0.05, 0, 1");
CustomEase.create("cinematicSilk", "M0,0 C0.215,0.61 0.355,1 1,1");
CustomEase.create("hop", "M0,0 C0.05,0.7 0.1,1 0.5,1 0.6,1 0.65,0.95 0.7,0.85 0.8,0.6 1,0.5 1,1");

// Uso
gsap.to(".hero-title", {
  y: 0,
  opacity: 1,
  duration: 1.2,
  ease: "osmo-ease", // referencia nome, não inline curve
});
```

**Embasamento teórico:** Easing semantics — curve `osmo-ease (0.625, 0.05, 0, 1)` tem início desacelerado + chegada suave. Sensação: "orgânico não-mecânico, premium." Diferença vs `power3.out`: subtle mas perceptível em hero reveal.

**Reduced motion fallback:**
```js
ease: prefersReducedMotion ? "none" : "osmo-ease",
duration: prefersReducedMotion ? 0 : 1.2,
```

---

## Recipe 3 — easeReverse (GSAP 2026 feature)

**Source:** DR-0 GSAP 2026 release notes
**Quando usar:** animação onde reverse precisa easing diferente da entrada (entrada cinemática lenta, saída rápida).
**Quando NÃO usar:** animações simétricas onde forward = reverse.

```js
gsap.to(".modal-panel", {
  y: 0,
  opacity: 1,
  duration: 0.4,
  ease: "power2.out",
  easeReverse: "power3.in", // reverse usa curve diferente
});

// Quando reverte (close modal):
tl.reverse(); // automaticamente usa easeReverse
```

**Embasamento teórico:** Saída de modal/drawer/overlay deve ser MAIS rápida que entrada (Carbon, Material guidelines). Entrada = "cuidadosa, anuncia presença". Saída = "fora do caminho, libera contexto". `easeReverse` resolve sem timeline manual reverse.

**Reduced motion fallback:** ambos eases viram `none`, duration 0.

---

## Recipe 4 — Flip.fit() consecutive scrub waypoints

**Source:** DR-A (Awwwards showcase technique) + DR-B
**Quando usar:** elemento "viaja" entre 3+ posições conforme scroll progress. Cada waypoint = layout state diferente.
**Quando NÃO usar:** transição simples 2 estados (FLIP normal basta).

```js
const card = document.querySelector('.product-card');

// Captura 3 waypoints (positions ao longo da página)
const waypoint1 = document.querySelector('#waypoint-1');
const waypoint2 = document.querySelector('#waypoint-2');
const waypoint3 = document.querySelector('#waypoint-3');

// Cria timeline scrubbed pelo scroll
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".product-section",
    start: "top top",
    end: "bottom bottom",
    scrub: 1, // CRÍTICO: scrub 1 = 1s smoothing
  },
});

// Captura state inicial
const state1 = Flip.getState(card);

// Move pra waypoint 1
tl.add(() => {
  card.appendChild(waypoint1);
  Flip.fit(card, state1, { duration: 0, scale: true, rotation: true });
});

// Move pra waypoint 2 (consecutive)
tl.add(() => {
  const state2 = Flip.getState(card);
  card.appendChild(waypoint2);
  Flip.fit(card, state2, { duration: 0, scale: true });
});

// Move pra waypoint 3
tl.add(() => {
  const state3 = Flip.getState(card);
  card.appendChild(waypoint3);
  Flip.fit(card, state3, { duration: 0, scale: true });
});
```

**Embasamento teórico:** Gestalt continuity — olho do user segue trajetória contínua mesmo entre containers diferentes. `Flip.fit` consecutive scrub mantém continuidade espacial sem cortes visuais.

**Reduced motion fallback:** desliga ScrollTrigger + posiciona card direto no waypoint final.

**Browser baseline:** Chrome 76+, Safari 14+, Firefox 70+. Flip plugin paid (GSAP Bonus / GSAP Premium).

---

## Recipe 5 — Persistent canvas (Three.js scene survives Barba route swap)

**Source:** DR-B (Codrops Barba+GSAP+Three.js tutorial)
**Quando usar:** SPA com Barba.js page transitions onde Three.js scene precisa persistir entre rotas (configurador, brand site imersivo).
**Quando NÃO usar:** Lovable/Next/Astro (router próprio, não Barba). SaaS sem 3D.

```js
import barba from '@barba/core';
import * as THREE from 'three';

// Canvas + scene LIVE FORA do barba container (mounted no body, persiste)
const canvas = document.createElement('canvas');
canvas.id = 'persistent-canvas';
document.body.appendChild(canvas);

const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// Render loop independente
let frameId;
function animate() {
  frameId = requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();

// Barba transitions só atualizam scene state, não destroem
barba.init({
  transitions: [{
    name: 'fade-3d',
    leave({ current }) {
      // Fade out + atualiza camera position pra próxima rota
      gsap.to(camera.position, { z: 5, duration: 0.6, ease: "osmo-ease" });
      return gsap.to(current.container, { opacity: 0, duration: 0.6 });
    },
    enter({ next }) {
      // Atualiza scene pro contexto da rota nova
      updateSceneForRoute(next.namespace);
      return gsap.from(next.container, { opacity: 0, duration: 0.6 });
    },
  }],
});

function updateSceneForRoute(namespace) {
  // Limpa meshes antigas, adiciona novas conforme rota
  scene.children.forEach(child => scene.remove(child));
  if (namespace === 'home') addHomeMeshes(scene);
  if (namespace === 'about') addAboutMeshes(scene);
}
```

**Embasamento teórico:** Continuidade espacial entre rotas em brand site imersivo. Scene 3D = "world" que persiste, rotas = "camera shots" diferentes. Sem persistent canvas, cada rota recria scene = boot cost + flash visual.

**Reduced motion fallback:** desliga GSAP transitions Barba (instant), mas scene continua renderizando.

**Browser baseline:** Chrome 88+, Safari 14+, Firefox 80+. WebGL2 idealmente.

---

## Recipe 6 — registerEffect + Custom Elements (Telha Clarke pattern)

**Source:** DR-A (Awwwards Telha Clarke showcase)
**Quando usar:** quando padrão motion vira reusável em DOM (similar a Web Component). Decorativo/declarativo.
**Quando NÃO usar:** projeto pequeno onde 1 timeline GSAP basta.

```js
// Registra effect customizado (1x boot)
gsap.registerEffect({
  name: "scrubReveal",
  effect: (targets, config) => {
    return gsap.to(targets, {
      opacity: 1,
      y: 0,
      duration: config.duration,
      ease: config.ease,
      scrollTrigger: {
        trigger: targets,
        start: "top 80%",
        end: "top 30%",
        scrub: config.scrub || 0.5,
      },
    });
  },
  defaults: { duration: 1, ease: "osmo-ease", scrub: 0.5 },
  extendTimeline: true,
});

// Define Custom Element que usa effect
class ScrubReveal extends HTMLElement {
  connectedCallback() {
    gsap.effects.scrubReveal(this, {
      duration: this.dataset.duration || 1,
    });
  }
}
customElements.define('scrub-reveal', ScrubReveal);

// Uso no HTML (declarativo):
// <scrub-reveal data-duration="1.5">
//   <h2>Section Title</h2>
// </scrub-reveal>
```

**Embasamento teórico:** Encapsulation — pattern motion vira "tag HTML" reusável. Designer/dev junior usa tag sem precisar entender GSAP. Padrão Telha Clarke (Awwwards SOTD).

**Reduced motion fallback:**
```js
connectedCallback() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    this.style.opacity = 1; // snap final state
    return;
  }
  gsap.effects.scrubReveal(this, { duration: this.dataset.duration || 1 });
}
```

---

## Recipe 7 — SplitText word/char stagger timeline

**Source:** DR-B + DR-0
**Quando usar:** kinetic headline em hero/manifesto/launch page. Reveal por palavra/caractere.
**Quando NÃO usar:** corpo de texto, parágrafos, body copy (atrapalha leitura WCAG 2.2.2).

```js
const headline = document.querySelector('.hero-title');

// Split em palavras (preferido — char é overkill em maioria casos)
const split = new SplitText(headline, { type: "words", wordsClass: "split-word" });

gsap.from(split.words, {
  y: 40,
  opacity: 0,
  duration: 0.8,
  stagger: 0.04, // 40ms entre palavras (DR-05 recomenda 20-80ms)
  ease: "osmo-ease",
  delay: 0.3,
});

// Cleanup: split.revert() restaura HTML original (importante pra a11y/SEO)
// useGSAP hook faz isso automático
```

**Embasamento teórico:** Gestalt continuity — stagger 40ms cria ritmo "leitura natural" sem parecer fila lenta. Stagger > 80ms vira "uma palavra de cada vez", quebra fluxo. Stagger < 20ms = sincronizado, perde efeito.

**Reduced motion fallback:** snap todas palavras pro estado final, sem stagger.

**A11y:** `split.revert()` em unmount preserva texto original pra screen readers. Texto continua selecionável durante motion.

**Browser baseline:** SplitText paid plugin (GSAP Bonus). Free alternative: SplitType lib npm.

---

## Recipe 8 — Scroll-driven CSS variables com GSAP onUpdate

**Source:** DR-B (Codrops scroll progress patterns)
**Quando usar:** quando design quer expor scroll progress pra CSS (ex: gradient shifting, opacity calc, transform compose).
**Quando NÃO usar:** scroll-trigger simples (CSS scroll-driven animations API direta basta).

```js
gsap.to({ progress: 0 }, {
  progress: 1,
  scrollTrigger: {
    trigger: ".section-narrative",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.5,
  },
  onUpdate: function() {
    const progress = this.targets()[0].progress;
    document.documentElement.style.setProperty('--scroll-progress', progress);
  },
});
```

CSS consome:
```css
.gradient-bg {
  background: linear-gradient(
    to bottom,
    hsl(220, 80%, calc(20% + (var(--scroll-progress) * 40%))),
    hsl(280, 80%, calc(40% + (var(--scroll-progress) * 30%)))
  );
}

.fade-element {
  opacity: calc(1 - var(--scroll-progress));
}
```

**Embasamento teórico:** Separation of concerns — JS gerencia scroll listener (uma vez), CSS gerencia visual transformations. Mais performático que múltiplas timelines GSAP transformando properties.

**Reduced motion fallback:** desliga ScrollTrigger, força `--scroll-progress: 0` ou `1` direto.

**Browser baseline:** CSS variables = Chrome 49+, Safari 9.1+, Firefox 31+. Universal.

---

## Recipe 9 — Flip layout animation (state shift)

**Source:** DR-0 + DR-A
**Quando usar:** layout changes (sort/filter/reorder/grid→list switch) onde elementos precisam continuidade visual.
**Quando NÃO usar:** lista 500+ items (custo paint > benefício), animação simples 2 estados (CSS transition basta).

```js
const grid = document.querySelector('.products-grid');
const items = grid.querySelectorAll('.product-card');

// Filter button click
filterButton.addEventListener('click', () => {
  // 1. Captura state ANTES da mudança
  const state = Flip.getState(items);

  // 2. Aplica mudança (ex: filter remove items, sort reorder)
  applyFilter('category-A'); // toggla classes/estilos OR remove items DOM

  // 3. Anima do state antigo pro novo
  Flip.from(state, {
    duration: 0.6,
    ease: "osmo-ease",
    stagger: 0.04,
    absolute: true, // remove de fluxo durante animação
    onLeave: (elements) => gsap.to(elements, { opacity: 0, scale: 0.8, duration: 0.3 }),
    onEnter: (elements) => gsap.from(elements, { opacity: 0, scale: 0.8, duration: 0.3 }),
  });
});
```

**Embasamento teórico:** FLIP (First-Last-Invert-Play) preserva continuidade visual em layout shifts. Sem FLIP, items "saltam" entre posições = perda rastreabilidade.

**Reduced motion fallback:**
```js
Flip.from(state, {
  duration: prefersReducedMotion ? 0 : 0.6,
  // sem stagger se reduced
});
```

**A11y:** mantém foco no elemento se ele continua existindo pós-filter.

---

## Recipe 10 — MorphSVG rotational mapping

**Source:** DR-C (Osmo Supply pattern) + DR-0
**Quando usar:** ícone state change com formas que NÃO são parentes (ex: arrow → check, hamburger → close com forma orgânica).
**Quando NÃO usar:** formas simples geometricamente parentes (CSS rotate basta).

```js
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";
gsap.registerPlugin(MorphSVGPlugin);

gsap.to("#icon-arrow", {
  morphSVG: {
    shape: "#icon-check",
    type: "rotational", // CRÍTICO: rotational para morphs naturais
    map: "complexity", // mapeia pontos por complexidade (não distância)
  },
  duration: 0.6,
  ease: "osmo-ease",
});
```

**Embasamento teórico:** `type: "rotational"` + `map: "complexity"` produz morph natural sem cruzamento de paths estranho. Default `linear` map causa "spaghetti" visual em formas complexas.

**Reduced motion fallback:** snap direto pra forma final, sem morph.

**Browser baseline:** MorphSVG paid plugin (GSAP Bonus).

---

## Recipe 11 — gsap.quickTo (high-frequency updates)

**Source:** DR-C (Osmo) + DR-B
**Quando usar:** mouse parallax / cursor follower / continuous input update onde precisa interpolar valores 60fps.
**Quando NÃO usar:** trigger único (gsap.to direto basta).

```js
const xTo = gsap.quickTo(".cursor-follower", "x", { duration: 0.6, ease: "power3" });
const yTo = gsap.quickTo(".cursor-follower", "y", { duration: 0.6, ease: "power3" });

window.addEventListener("mousemove", (e) => {
  xTo(e.clientX);
  yTo(e.clientY);
});
```

**Embasamento teórico:** `quickTo` reusa tween instance entre chamadas = zero allocation overhead. Crítico em mousemove (60+ events/s). Sem `quickTo`, cria/destrói tween a cada move = GC pressure + frame drops.

**Reduced motion fallback:** desabilita listener inteiro OR snap cursor sem follow.

**Browser baseline:** GSAP 3.10+. Universal.

---

## Lookup map — recipe por contexto

| Contexto Phase 0 detectou | Recipes prioritárias |
|---|---|
| sales / landing premium | Recipe 1 (Lenis), Recipe 2 (CustomEase), Recipe 7 (SplitText) |
| portfolio creative | Recipe 1, Recipe 5 (persistent canvas), Recipe 7, Recipe 11 (cursor) |
| saas operacional | Recipe 9 (Flip layout), Recipe 3 (easeReverse modal/drawer) |
| brand site Awwwards-tier | Recipe 1, Recipe 2, Recipe 4 (Flip.fit consecutive), Recipe 5, Recipe 8 (CSS vars) |
| editorial / blog | Recipe 8 (scroll progress), Recipe 7 (kinetic headline) |
| slide deck pitch | Recipe 7 (kinetic), Recipe 2 (CustomEase pra polish) |
| e-comm | Recipe 9 (Flip filter), Recipe 11 (cursor product hover) |
| explainer scroll-narrative | Recipe 4 (Flip.fit consecutive), Recipe 8 (CSS vars), Recipe 5 (canvas se 3D) |

---

## Anti-patterns globais

1. **Importar GSAP só pra fade 150ms:** bundle size > benefício. Use CSS transition.
2. **CustomEase inline em cada call:** define 1x global, referencia por nome. Cache.
3. **Lenis sem `gsap.ticker` sync:** quebra ScrollTrigger updates.
4. **`gsap.context()` esquecido em React:** memory leak garantido. Use `useGSAP` hook.
5. **MorphSVG entre formas sem parentesco visual:** confunde user. Mantém categoria semântica.
6. **SplitText sem `revert()` cleanup:** quebra a11y/SEO no unmount.
7. **`scrub: true` em ScrollTrigger sem smoothing:** jitter em scroll fast. Use `scrub: 0.5-1`.
8. **Persistent canvas sem render loop pause em tab blur:** GPU desperdiçada.

---

## Boundary com outras skills

- **`react-patterns`** — implementação React específica (useEffect, refs, useGSAP). Esta ref dá receita core, React skill aplica em componente.
- **`ui-design-system`** — tokens CSS de duração/easing. CustomEase nomeado = token. Esta ref usa, não redefine.
- **`ux-audit`** — audita se motion paga aluguel em fluxo real. Esta ref dá receita; ux-audit decide se usar.
- **`react-patterns --audit-cross-browser`** — Lenis/GSAP em Safari iOS, Firefox quirks. Esta ref dá receita; cross-browser audita.

---

## Referências

- DR-0 GSAP canonical (1546 linhas) — `Downloads/DR GSAP/DEEP RESEARCH 0/DR_GSAP_MERGED.md`
- DR-A 10 showcases criativos (1515 linhas) — `Downloads/DR GSAP/DEEP RESEARCH A/DR_A_MERGED.md`
- DR-B Codrops/Awwwards (1080 linhas) — `Downloads/DR GSAP/DEEP RESEARCH B/DR_B_MERGED.md`
- DR-C Osmo Supply (918 linhas) — `Downloads/DR GSAP/DEEP RESEARCH C/DR_C_MERGED.md`
- gsap.com docs canonical
- @studio-freight/lenis npm
