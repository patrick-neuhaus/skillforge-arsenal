# `references/03-narrativo-editorial.md` — Pilar 3: Motion Narrativo, Editorial e Atmosférico

> Motion **guiado por scroll ou tempo**: scrollytelling, parallax, hero entry, ambient backgrounds, sticky narrative frames. Cabe em landing, editorial, product story, campaign. Em SaaS operacional **sai de fininho**. Scroll-driven Animations + GSAP + sticky CSS são a base.

## 1. Quando este pilar entra

| Contexto | Aplicabilidade | Cuidado |
|---|---|---|
| Landing institucional / brand site | Alta — primeira dobra + storytelling | Não esconder CTA, não atrasar leitura |
| Editorial / long-form / blog | Média — progress indicators, reveal sutil | Não distrair da leitura |
| Product story / launch | Alta — explainer scrollytelling | Avaliar se mobile aguenta |
| SaaS operacional | Baixa — só progress bar de scroll em docs internas | Nada de parallax em dashboard |
| Showcase de design system | Média — demonstrar motion como demo | Demo sempre tem `pause` |
| Documentação técnica | Baixa — apenas reading progress | — |

## 2. Catálogo de padrões

### 2.1 Hero section animations

Primeira dobra com reveal, sequência ou loop curto.

| Padrão | Quando | Duração | Risco |
|---|---|---|---|
| Headline staggered fade-in | Landing | 400–800ms (split em palavras) | Atrasa leitura se > 1s |
| Visual key art reveal | Brand site | 600–1200ms | Esconder CTA crítico |
| Background loop ambient | Hero contínuo | Loop 8–15s | Distrai da mensagem se chamativo |
| Number/metric count-up | KPI hero | 800–1500ms | Repetir em cada visita = tédio |
| Logo wall scroll | Social proof | Marquee 30–60s linear | Loop infinito = pause obrigatório |

**Regra hero:** mensagem-chave + CTA legíveis em ≤ 1s. Motion serve a leitura, não compete.

### 2.2 Scrollytelling

Narrativa progressiva guiada pelo scroll.

| Padrão | Quando | Técnica |
|---|---|---|
| Sticky frame + scrolling text | Explainer com visual fixo | `position: sticky` + sections de texto rolando |
| Step-by-step diagram reveal | Tutorial visual progressivo | IntersectionObserver + Motion ou GSAP ScrollTrigger |
| Camera "zoom" simulado | Approach progressivo no asset | CSS `transform: scale()` ligado a scroll progress |
| Layered parallax narrative | Profundidade narrativa | CSS scroll-driven OU GSAP |
| Text-as-camera (text moves through 3D scene) | Brand premium / experimental | WebGL + scroll progress |

**Regra crítica:** scrollytelling **nunca sequestra o scroll**. Usuário tem que conseguir descer ignorando a animação. Se animação some/aparece em loop sem progresso, está quebrada.

### 2.3 Scroll effects (sem narrativa)

| Padrão | Quando | Técnica preferida |
|---|---|---|
| Section reveal (fade+up) | Cada seção entra no viewport | IntersectionObserver + CSS class toggle (preferido) ou Motion `whileInView` |
| Parallax suave | Hero ou seção destaque | CSS scroll-driven (`scroll-timeline`) com fallback ou GSAP |
| Reading progress bar | Long-form | CSS `animation-timeline: scroll()` ou JS scroll listener throttled |
| Pin + animate | GSAP-style sticky animation | GSAP ScrollTrigger (Motion's `useScroll` é alternativa lightweight) |
| Image reveal on scroll | Editorial galleries | clip-path animado via scroll progress |

**Tier de risco parallax:**
- ✅ Translação leve (≤ 30px range) → ok
- ⚠️ Translação grande (100px+) → pode causar enjoo (vestibular WCAG 2.3.3)
- ❌ Camera-style 3D parallax sem `prefers-reduced-motion` → exclusivo, viola

### 2.4 Ambient backgrounds

| Padrão | Quando | Técnica | Custo |
|---|---|---|---|
| CSS gradient shift | Hero brand | `background-position` animado | Bx |
| Animated gradient mesh | Premium brand | CSS conic/radial multi + animation | Bx-Md |
| Particle field | Tech/SaaS hero | Canvas 2D ou tsParticles lib | Md |
| Blob morph background | Creative brand | SVG morph loop | Bx-Md |
| Noise/grain texture | Editorial premium | SVG `feTurbulence` ou WebGL shader | Md-Al |
| WebGL shader scene | Brand premium / immersive | Three.js + custom shader | Al |

**Regra:** ambient nunca atrasa LCP. Carregar **depois** do hero crítico estar interativo. Lazy + IntersectionObserver.

### 2.5 Sticky narrative frames

Visual fixo + texto rolando.

| Variante | Bom uso | Mau uso |
|---|---|---|
| Single sticky image + scrolling text | Comparison, explainer | Conteúdo curto que cabe em 1 dobra |
| Sticky video + caption progress | Product demo | Mobile com vídeo grande (data) |
| Stacked sticky cards | Step-by-step process | Mais que 5 steps (fadiga) |

**Técnica:** `position: sticky; top: 0; height: 100vh` + sections de texto com `min-height: 100vh` ao redor.

### 2.6 Reading / Progress indicators

```css
.progress-bar {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--brand);
  transform-origin: left;
  animation: progress linear;
  animation-timeline: scroll();
}
@keyframes progress {
  to { transform: scaleX(1); }
  from { transform: scaleX(0); }
}
```

Fallback JS pra browsers sem `animation-timeline` (Safari ainda não cobriu 100%): scroll listener com `requestAnimationFrame`.

## 3. Decisão técnica

```
Sequência ligada ao scroll progress?
  ├─ Suporte browser ok pra alvo? (Chrome 115+, Edge 115+, FF 110+ behind flag)
  │   ├─ Sim → CSS scroll-driven animations (`animation-timeline: scroll()` / `view()`)
  │   └─ Não OU complexidade alta → GSAP ScrollTrigger
  ├─ React + state-driven? → Motion (`useScroll`, `whileInView`)
  └─ Simples reveal on enter? → IntersectionObserver + CSS class toggle (mais barato)

Hero entry?
  ├─ Texto staggered → CSS `@keyframes` com `animation-delay` por palavra OU Motion stagger
  └─ Visual reveal → CSS clip-path/mask OU SVG path

Parallax?
  ├─ Range pequeno → CSS scroll-driven simple
  └─ Múltiplas camadas + 3D → GSAP ou WebGL (último recurso)
```

## 4. Bom uso vs mau uso (DR-05)

| ✅ Bom | ❌ Mau |
|---|---|
| Headline reveal acelerando mensagem | Headline reveal atrasando leitura |
| Sticky explainer com visual fixo | Sticky em mobile sem fallback |
| Reading progress bar discreta | Progress bar gritante competindo com conteúdo |
| Ambient gradient sutil | Background loop chamativo atrás de texto |
| Parallax ≤ 30px | Parallax pesado causando enjoo |
| Scroll-driven em landing | Scroll-driven em SaaS operacional |

## 5. Mobile + perf

- Scrollytelling complexo em mobile → considerar versão simplificada ou pular animação
- WebGL scenes → exclusivo mobile premium, com toggle off por default
- Parallax mobile → desativar por completo OU range muito menor (15px)
- Vídeo background → `<video autoplay muted playsinline>` + `poster` + lazy load + tamanho mobile separado

## 6. Reduced motion (crítico neste pilar)

```css
@media (prefers-reduced-motion: reduce) {
  /* Parallax: desligar completamente */
  .parallax { transform: none !important; }

  /* Scroll-driven: snap-to-state */
  .scroll-fade { opacity: 1 !important; transform: none !important; }

  /* Ambient: desligar loop */
  .ambient-loop { animation: none !important; }

  /* Hero entry: ir direto pro estado final */
  .hero-stagger > * { animation: none !important; opacity: 1 !important; }
}
```

WCAG 2.3.3 (Animation from Interactions): toda animação não-essencial disparada por scroll/hover deve ser desligável.

## 7. Spec template

```
Padrão: <hero entry / scrollytelling / parallax / ambient / sticky / progress>
Pilar: 3 (narrativo/editorial)
Trigger: <viewport-enter / scroll-progress / time-loop>
Range scroll: <em vh ou px>
Camadas (parallax): <N>
Duração: <ms para entry / loop>
Reduced motion: <comportamento explícito>
Mobile: <ativo / simplificado / desligado>
Técnica: <CSS scroll-driven / IntersectionObserver / GSAP ScrollTrigger / Motion useScroll>
Browser baseline + fallback: <X>
Critério de aceite:
  - [ ] LCP não atrasado pela animação
  - [ ] Mobile testado (touch scroll funciona)
  - [ ] reduced-motion testado
  - [ ] Não sequestra scroll
  - [ ] CTA crítico continua acessível
```

## 8. Boundary

- **`ui-design-system`** — tokens de duração/easing pra hero entry (não duplicar). Tokens fluidos `--hero-entry-stagger`.
- **`ux-audit`** — audita se motion narrativo "paga aluguel" no contexto. Se atrapalha tarefa = finding.
- **`react-patterns`** — implementação React (`IntersectionObserver`, `useScroll`, lazy load do GSAP). Suporte browser de `animation-timeline`.
- **`component-architect`** — se sticky frame ou progress bar viram componente, anatomia mora lá.
