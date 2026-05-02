# `references/04-espacial-imersivo.md` — Pilar 4: Motion Espacial, Imersivo e Experimental

> Motion **3D, WebGL, AR/VR, shaders, real-time render**. Pilar mais caro em complexidade, performance e a11y. Cabe em produto visual, configurador 3D, hero premium, experimentos brand. Quase **nunca** em SaaS operacional. Three.js + WebGL + WebXR são a base. Faux 3D (CSS 3D transforms) é a versão "barata" deste pilar.

## 1. Quando este pilar entra

| Contexto | Aplicabilidade | Custo de oportunidade |
|---|---|---|
| Configurador de produto (carro, móvel, joia) | Alta — 3D real entrega valor | Alto investment, alto retorno |
| Brand premium / hero experimental | Média — diferenciação | Pode envelhecer rápido |
| Showcase de design system | Baixa — apenas se DS é "spatial-first" | Quase nunca |
| AR de produto (try-on óculos, móveis em casa) | Alta — caso justifica | Muito alto custo |
| SaaS operacional | Baixa — apenas faux 3D leve em ícones | Sair de fininho |
| Landing institucional B2B | Baixa — geralmente não justifica | — |
| Documentação técnica | Mínima — apenas em docs de spatial product | — |

**Regra:** se o produto não é visual/espacial por natureza, este pilar é luxo. Avaliar ROI real (conversão, engagement, prova) antes de implementar.

## 2. Catálogo de padrões

### 2.1 WebGL / 3D real-time

| Padrão | Quando | Técnica |
|---|---|---|
| Configurador 360° | Inspecionar produto (carro, sapato) | Three.js + GLTF model + OrbitControls |
| Hero 3D scene | Landing premium, brand experiment | Three.js + custom shader OU React Three Fiber |
| Material showcase | Texturas, finishes, cores | Three.js PBR materials |
| Spatial portfolio | Designer / studio sites | R3F + Drei utilities |
| Product reveal animation | Lançamento, e-comm premium | Camera animation + lighting |
| Particle systems | Tech/abstract brand | Three.js Points OR shader-based |

**Stack típica:**
- **Three.js** — bare metal, controle máximo, bundle ~150KB gzipped
- **React Three Fiber (R3F)** — Three.js declarativo em React, bundle ~30KB + Three.js
- **Drei** — utilities em cima de R3F (`<OrbitControls>`, `<useGLTF>`, etc)
- **Spline** — design tool exportando 3D pra web sem código (caro em runtime)

**Asset:**
- GLTF/GLB compactado com Draco ou meshopt
- Tamanho-alvo: < 2 MB pra hero, < 5 MB pra configurador
- Texturas: KTX2/Basis pra GPU compression
- LOD (Level of Detail) pra mobile

### 2.2 AR / VR via WebXR

| Padrão | Quando |
|---|---|
| AR try-on (óculos, makeup) | E-comm beauty/fashion |
| AR room placement (móvel) | Furniture e-commerce |
| VR walkthrough (imóvel) | Real estate, turismo |
| 360° photo/video tour | Hospitality, eventos |

**Stack:**
- WebXR Device API + Three.js + custom logic
- iOS: depende do AR Quick Look (`<a rel="ar">`) ou Safari WebXR (limitado)
- Android Chrome: WebXR full
- Fallback obrigatório: vídeo 360 ou imagens

### 2.3 Faux 3D (CSS 3D transforms)

Ilusão de volume **sem** WebGL. 90% dos casos práticos de "3D na web".

| Padrão | Técnica | Custo |
|---|---|---|
| Card flip | `transform: rotateY()` + `backface-visibility` | Bx |
| Tilt on hover (parallax-like) | CSS `perspective` + JS mouse position | Bx-Md |
| Cube navigation | `transform: rotateY()` em container 3D | Md |
| Layered depth | Multiple translateZ()  layers | Bx |
| 3D button press | `transform: translateZ(-2px) rotateX(2deg)` | Bx |

**Regra:** CSS 3D resolve > 90% dos casos de "queremos 3D". Use Three.js apenas quando precisa **renderizar geometria real** ou cenas dinâmicas.

### 2.4 Isometric animation

Perspectiva isométrica fixa. Sem 3D real.

| Padrão | Quando | Técnica |
|---|---|---|
| Animated isometric explainer | SaaS B2B explicando arquitetura | SVG isométrico + Motion/GSAP |
| Building/system reveal | Infra, plataforma | SVG layers stagger |
| Workflow diagram in 3D look | Process visualization | SVG + Lottie |

**Anti-pattern:** isométrico em mobile pequeno (< 360px). Detalhe se perde, virar grid simples ou seção de texto.

### 2.5 Liquid / Glassmorphic / Neumorphic motion

| Padrão | Quando | Técnica |
|---|---|---|
| Blob morphing background | Brand creative | SVG morph + filters |
| Glassmorphism transitions | Premium UI showcase | `backdrop-filter` + transforms |
| Neumorphic press | Showcases (não use em UI real) | CSS shadow inset/outset transitions |
| Liquid CTA hover | Fintech premium | SVG turbulence filter animado |
| Shader liquid (water, fire) | Brand experimental | WebGL shader (fragment shader) |

**Aviso:** glassmorphism + neumorphism têm **problema de contraste sério**. Se for usar, garantir 4.5:1 em texto sobre o efeito. Animar o efeito sem cuidado quebra contraste em frames intermediários.

### 2.6 Real-time collaborative 3D

| Padrão | Quando |
|---|---|
| Multi-user 3D editor | Figma 3D, Spline collab |
| Sales demo with shared cursor in 3D | Enterprise sales tool |
| 3D whiteboard | Design review |

**Stack:** WebRTC ou WebSocket + Yjs/Liveblocks pra estado + R3F renderer. Custo de implementação: muito alto. Justifica apenas em produto core 3D-collab.

## 3. Decisão técnica

```
Precisa renderizar geometria 3D real (modelo, cena dinâmica, customização)?
  ├─ Sim
  │   ├─ Caso 1 (estático ou semi-estático)? → Three.js + GLTF + OrbitControls
  │   ├─ Caso 2 (React app)? → R3F + Drei
  │   ├─ Caso 3 (designer-led)? → Spline (cuidado com perf)
  │   └─ Caso 4 (AR/VR)? → WebXR + Three.js
  └─ Não
      ├─ Quero ilusão de profundidade barata? → CSS 3D transforms (faux 3D)
      ├─ Quero estética isométrica? → SVG isométrico + Motion/GSAP
      ├─ Quero efeito visual fluido (blob, liquid)? → SVG turbulence OU shader simples
      └─ Quero parallax 3D simulado? → CSS perspective + JS mouse
```

## 4. Performance (críticos neste pilar)

### Targets mínimos

| Cenário | FPS alvo | Tempo de boot | Tamanho asset |
|---|---|---|---|
| Hero 3D desktop | 60 | < 2s pra interativo | < 2 MB total |
| Hero 3D mobile médio | 30 | < 3s | < 1 MB |
| Configurador desktop | 60 | < 4s | < 5 MB |
| Configurador mobile | 30 | < 6s OU fallback estático | < 2 MB OU desligar |
| AR experience | 30+ | < 3s | < 3 MB |

### Otimizações obrigatórias

- **Lazy load** Three.js — não carregar se viewport não chegar na cena
- **Compress models** com Draco/meshopt
- **Compress textures** com KTX2/Basis
- **LOD** (mesh com menos polígonos pra mobile)
- **Pixel ratio cap** — `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`
- **Suspend on tab blur** — pause render loop quando tab inativa
- **Frustum culling** — não renderizar fora da câmera (Three.js faz default)
- **Reduce shadows** — sombras dinâmicas matam mobile

### Core Web Vitals impact

- LCP: 3D não pode ser LCP (lazy load fora do hero crítico)
- CLS: cena 3D ocupar dimensão fixa pra não causar layout shift
- INP: interação 3D > 200ms = problema (mobile principalmente)

## 5. Acessibilidade (críticos)

WebGL/3D é uma **dark zone** pra a11y. Esforço deliberado obrigatório:

- **Alternative content**: imagem estática + descrição textual sempre disponível
- **Keyboard navigation**: configurador 3D precisa permitir rotação por teclado (setas)
- **Screen reader**: aria-label descrevendo cena + estado atual
- **Reduced motion**: desligar auto-rotate, parallax, idle animations
- **Reduced data**: respeitar `Save-Data` header — não carregar 3D se ativo
- **Focus indication**: hotspots clicáveis em 3D precisam de equivalente focável no DOM
- **Pause control**: idle animations sempre têm pause

## 6. Bom uso vs mau uso (DR-05)

| ✅ Bom | ❌ Mau |
|---|---|
| Configurador de carro com inspeção real | Hero 3D em SaaS B2B sem motivo |
| AR try-on de óculos | AR random em landing institucional |
| Faux 3D em hover de card | Three.js full scene pra animar 1 botão |
| Isométrico em explainer SaaS | Isométrico em mobile pequeno sem fallback |
| Glassmorphism com contraste preservado | Glassmorphism animado quebrando contraste |
| Particle system leve (< 200 particles) | 3000 particles em mobile médio |

## 7. Spec template

```
Padrão: <webgl-hero / configurator / faux-3d / isometric / liquid / ar-vr>
Pilar: 4 (espacial/imersivo)
Asset (3D): <GLTF/GLB tamanho>
Texturas: <KTX2 tamanho>
Stack: <Three.js / R3F+Drei / Spline / SVG isométrico / CSS 3D>
Dispositivo alvo: <desktop / mobile médio / mobile baixo>
FPS alvo: <60/30>
Tempo boot alvo: <s>
Reduced motion: <auto-rotate off / pause idle / fallback estático>
Reduced data: <fallback imagem se Save-Data>
A11y:
  - aria-label da cena: <texto>
  - keyboard equivalente: <setas / tab pra hotspots>
  - alternative content: <link / imagem estática>
Critério de aceite:
  - [ ] FPS ≥ alvo em dispositivo médio
  - [ ] Boot ≤ alvo
  - [ ] LCP NÃO afetado (lazy load fora hero crítico)
  - [ ] Funciona com keyboard
  - [ ] Reduced motion testado
  - [ ] Save-Data respeitado
  - [ ] Mobile baixo: fallback estático ativo
```

## 8. Quando recusar este pilar

Recuse implementar se:
- Não é produto visual/espacial por natureza
- Mobile é > 60% do tráfego e perf não cabe
- Time não tem capacidade de manutenção (Three.js evolui rápido)
- Não há fallback aceitável pra browsers antigos / dispositivos baixos
- A11y não está no plano (3D sem a11y = decisão excludente)

Recomende **faux 3D + isométrico SVG** quando real 3D não justifica.

## 9. Boundary

- **`ui-design-system`** — define paleta/tokens; cenas 3D consomem cores como hex/HSL. Reduced-motion regras.
- **`react-patterns`** — implementação R3F, lazy load, code split, SSR de 3D (challenge), browser support WebXR.
- **`ux-audit`** — audita se 3D paga ROI no fluxo. Configurador difícil de operar = finding.
- **`component-architect`** — se viewer 3D vira componente (`<ProductViewer />`), anatomia/props lá.
- **`design-system-audit`** — não cobre 3D especificamente; raro overlap.
