# `references/02-vetorial-branding.md` — Pilar 2: Motion Vetorial, Ilustrativo e de Branding

> Motion que **comunica marca**: logos animados, ícones com gestos, kinetic typography, characters, mascotes, doodles. Eleva percepção de valor em landing, hero, splash. Quase sempre **fora** de SaaS operacional. SVG + dotLottie + Rive são as 3 técnicas dominantes.

## 1. Quando este pilar entra

| Contexto | Aplicabilidade | Cuidado |
|---|---|---|
| Landing institucional | Alta — diferenciação de marca | Não atrasar leitura do hero |
| Produto visual / brand-heavy | Alta — coração da experiência | Pode dominar se mal calibrado |
| Design system showcase | Média — animar ícones e logos como demo | Ícones do DS sempre coerentes em motion |
| SaaS operacional | Baixa — apenas logo splash + ícones funcionais | Não usar character/doodle em dashboard |
| Documentação técnica | Baixa — diagramas vetoriais com line animation | Não usar kinetic type em corpo de texto |
| Template demonstrativo | Média — depende da intenção do template | — |

## 2. Catálogo de padrões

### 2.1 Line animation / Self-drawing SVG

Linhas que se traçam ou percorrem trajeto.

| Padrão | Quando | Duração | Técnica |
|---|---|---|---|
| Logo reveal | Splash, hero entry | 800–1500ms | SVG `stroke-dasharray` + `stroke-dashoffset` animado |
| Signature draw | Manifesto, autoria | 1200–2500ms | SVG path animation |
| Map/diagram trace | Onboarding, explainer | 600–1200ms por trecho | SVG + WAAPI ou Motion |
| Connector lines (diagram) | Mostrar relação | 400–600ms por linha | SVG + stagger |
| Underline reveal on link | Hover state | 200ms | CSS `transform-origin: left` + scaleX |

**Pattern base:**
```css
.draw-path {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: draw 1500ms ease-out forwards;
}
@keyframes draw {
  to { stroke-dashoffset: 0; }
}
```

**Regra:** path de logo nunca > 2.5s. Atrasa primeira leitura. Pra paths longos (mapa, ilustração), divida em segmentos cascatados.

### 2.2 Morphing

Forma A → forma B com lógica visual.

| Padrão | Bom uso | Mau uso |
|---|---|---|
| Menu ↔ close (hambúrguer ↔ X) | Estados semanticamente parentes | Morph entre formas sem relação |
| Play ↔ pause | Toggle player | Morph "decorativo" sem causalidade |
| Logo reveal A → final | Brand intro | Logo morfa toda hora em nav |
| Blob ambient morph | Hero background | Morph que distrai do CTA |

**Técnica:**
- 2 formas SVG com **mesmo número de pontos** + `d` interpolável → CSS variables ou WAAPI
- Formas com geometria diferente → Motion (`<motion.path>` com shape-tween) ou GSAP MorphSVG
- Loop ambient → SVG + `animate` ou Motion repeat

### 2.3 Animated logos

| Variante | Quando | Duração | Frequência |
|---|---|---|---|
| Splash boot | Primeira carga do app | 1200–2000ms | 1x por sessão (memoizar) |
| Hero entry | Landing page topo | 800–1500ms | 1x por visita |
| Hover/focus em header | Discovery sutil | 200–300ms | A cada interação |
| Loading state | Aguardando boot | Loop 1500–2500ms | Enquanto carrega |
| Social signature | OG image, vídeo | Variável | Asset estático em maioria |

**Anti-pattern:** logo no header animar a cada page load em SPA. Vira ruído. Anime 1x por sessão.

### 2.4 Kinetic typography / Expressive type

Texto em movimento; voz, ênfase, ritmo.

| Padrão | Bom uso | Mau uso |
|---|---|---|
| Headline reveal staggered | Hero, manifesto | Corpo de texto, parágrafos |
| Word/letter swap loop | Slogan rotativo | Termo crítico, label de UI |
| Slide in on scroll | Sequência narrativa | Dashboard com KPIs |
| Marquee | Brand banner, fintech ticker | Conteúdo essencial à leitura |
| Variable font weight pulse | Brand expression | Texto que precisa ser legível |

**Técnica:**
- Letter-by-letter → split em spans (manual ou SplitText/SplitType lib) + Motion stagger
- Word swap → CSS `@keyframes` com `content` ou React state com `<AnimatePresence>`
- Variable font → `font-variation-settings` animável

**Regra crítica de a11y:** texto que se move ou pisca > 5s deve ter botão pause (WCAG 2.2.2). Texto crítico para leitura nunca em motion contínuo.

### 2.5 Character animations / Mascotes

| Variante | Bom uso | Mau uso |
|---|---|---|
| Onboarding companion | Acolher novo usuário | Não usar em dashboard sério |
| Empty state mascot | "Sem dados? Aqui tá vazio" | Empty state em dado financeiro crítico |
| Tutorial guide | Explicar feature lúdica | Compliance/legal/financeiro |
| Brand homepage character | Identidade lúdica | B2B enterprise austero |

**Técnica:**
- **Rive** quando precisa interatividade (state machine, hover→reaction, drag) → runtime real-time, light asset
- **dotLottie** quando precisa loop simples ou ícone/character standalone → fácil integrar, comunidade vasta
- **SVG rigging** quando precisa controle pixel-perfect e bundle pequeno
- **Vídeo** quando precisa fotorrealismo ou efeitos não-vetorizáveis (raro)

### 2.6 Doodle / Hand-drawn

| Padrão | Quando | Técnica |
|---|---|---|
| Sketch underline | Highlight orgânico | SVG path frame-by-frame |
| Wiggle stroke | Brand creator | CSS `@keyframes` jitter sutil |
| Frame-by-frame wobble | Stop-motion estética | Sprite sheet OU Lottie |

**Anti-pattern:** doodle em B2B enterprise. Quebra confiança/seriedade.

## 3. Decisão técnica (3 runtimes principais)

```
Animação vetorial nasce em ferramenta visual? → dotLottie (After Effects → bodymovin → .lottie/.json)
Precisa interatividade complexa (state machine, hover→state, drag→reaction)? → Rive
Precisa controle máximo + bundle mínimo + acessibilidade fácil? → SVG nativo + CSS/WAAPI
Animação > 5s ou complexa demais pra render web? → Vídeo (mp4/webm) com fallback
```

| Técnica | Tamanho típico | Interatividade | Acessibilidade | Quando |
|---|---|---|---|---|
| SVG inline + CSS | <5 KB | Limitada | Excelente (DOM) | Logos simples, line, morph leve |
| dotLottie | 10–80 KB | Eventos básicos | Boa (com label) | Animações complexas exportadas de AE |
| Rive | 5–50 KB | Alta (state machine) | Boa (com aria) | Characters interativos, microinteractions premium |
| WebGL/Canvas | Variável | Total | Manual (ARIA + alt) | Particles, shaders, processuals |
| Vídeo (mp4) | 200KB–2MB | Nenhuma | Track legendas | Última opção, fotorrealismo |

## 4. Reduced motion + a11y

- Animação **decorativa** (logo loop, ambient) → desligar completamente em `prefers-reduced-motion: reduce`
- Animação **funcional** (logo reveal único, ícone que muda estado) → ir direto pro estado final, sem transição
- Texto kinetic > 5s → pause obrigatório (WCAG 2.2.2)
- Flashing > 3 vezes/segundo → proibido (WCAG 2.3.1)
- Lottie/Rive precisam declarar `aria-label` ou estar em região decorativa (`aria-hidden="true"`)

## 5. Spec template

```
Padrão: <line/morph/logo/kinetic/character/doodle>
Pilar: 2 (vetorial/branding)
Asset: <SVG inline / .lottie / .riv / vídeo>
Tamanho: <KB>
Duração total: <ms ou loop>
Trigger: <visible/hover/click/scroll-progress>
Reduced motion: <off/snap-to-end>
Critério de aceite:
  - [ ] Asset < <budget> KB
  - [ ] Roda 60fps em mobile médio
  - [ ] aria-label ou aria-hidden declarado
  - [ ] Pause disponível se loop > 5s
  - [ ] Reduced motion testado
```

## 6. Boundary

- **`ui-design-system`** — define escala de tipografia que kinetic type pode usar; tokens de cor pra logo/ícone. Esta ref usa.
- **`component-architect`** — se ícone animado vira componente reutilizável, anatomia é dele.
- **`react-patterns`** — implementação Lottie/Rive em React (lazy load, intersection observer pra trigger no viewport).
- **`ux-audit`** — audita se kinetic type compromete leitura ou se mascote está fora de contexto.
