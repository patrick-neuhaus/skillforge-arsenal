# `references/08-case-studies.md` — Case Studies (Wave 9)

> **40+ case studies reais** dos 4 DRs GSAP: 10 showcases criativos (DR-A) + 30 Awwwards (DR-B) + 24 Codrops tutorials (DR-B). Cada case com técnica usada + lesson learned + por quê funcionou.
> **Quando usar:** Phase 1 lookup do `--full` busca cases comparáveis ao session narrative. Phase 3 cita cases como evidência de proposta.
> **Boundary:** examples REAIS production. Recipes técnicas em `05-gsap-recipes.md`. Patterns isolados em `patterns/`.

---

## 1. Showcases criativos (DR-A — 10 sites premium)

### Case 1.1 — Hatom Protocol

**Tipo:** brand site DeFi premium
**Audiência:** crypto-native sophisticated
**Stack:** Next.js + GSAP + R3F
**Motion signature:**
- Hero scrollytelling 3D com persistent canvas
- Scroll-driven camera moves (Three.js + GSAP timeline)
- Kinetic typography reveal por section
- Custom shader backgrounds (noise + particle field)

**Lesson learned:** persistent canvas Three.js sobrevivendo entre sections via GSAP timeline scrubbed = continuidade visual award-grade. Motion é narrativa, não decoração.

**Por quê funcionou:** audience DeFi sophisticated espera diferencial visual; motion entrega trust signal "produto sério, design serious".

**Aplicar quando:** brand site crypto/DeFi/luxury que precisa diferencial vs concorrentes genéricos.

---

### Case 1.2 — Made With GSAP showcase

**Tipo:** showcase plataforma GSAP oficial
**Audiência:** devs frontend buscando ref
**Stack:** Vanilla GSAP + Lenis
**Motion signature:**
- Page transition Barba+GSAP suave
- Hero card stack reveal com Flip
- Filter FLIP em grid de showcase items
- Hover preview com cursor follower

**Lesson learned:** showcase de plataforma deve DEMONSTRAR técnica sem virar excessive — cada motion vira "exemplo replicável".

**Por quê funcionou:** audience técnica respeita restraint — motion gratuito perderia credibilidade da plataforma.

**Aplicar quando:** site institutional dev-tool ou plataforma técnica.

---

### Case 1.3 — Telha Clarke

**Tipo:** brand site arquitetura premium
**Audiência:** clientes high-end + peers arquitetos
**Stack:** Vue + GSAP + Custom Elements
**Motion signature:**
- registerEffect + Custom Elements pattern (Recipe 6)
- Kinetic typography manifesto pesado
- WebGL shader backgrounds
- Page transition cinematográfico
- Ambient particle field

**Lesson learned:** Custom Elements + GSAP effects torna motion patterns DECLARATIVOS — designer/dev junior usa tag `<scrub-reveal>` sem precisar entender GSAP timeline.

**Por quê funcionou:** brand premium arquitetura match motion award-grade Awwwards-tier.

**Aplicar quando:** brand site creative agency ou arquitetura/design studio premium.

---

### Case 1.4 — Apple product pages (Vision Pro / iPhone)

**Tipo:** sales premium B2C luxo
**Audiência:** consumer premium + tech enthusiasts
**Stack:** Custom (não-GSAP), mas técnicas replicáveis
**Motion signature:**
- Hero scrollytelling com video sequences
- Sticky frame + scrolling text overlay
- Image-sequence cinema (sprite frame frame)
- Layered reveal staggered

**Lesson learned:** product storytelling cinematográfico via image-sequence + sticky = imersão sem 3D real custo. Apple usa técnica há anos.

**Por quê funcionou:** audience premium aceita 5-10s por section pra storytelling — motion serve narrative do produto.

**Aplicar quando:** sales premium product launch / B2C luxo com produto físico complexo.

---

### Case 1.5 — Stripe Connect homepage

**Tipo:** sales B2B SaaS moderno
**Audiência:** dev + decisor técnico
**Stack:** Next.js + Custom (não-GSAP)
**Motion signature:**
- Microinteractions calibradas (hover, focus)
- Section reveal sutil one-time
- Code snippet animations
- Smooth scroll com Intersection Observer

**Lesson learned:** SaaS B2B moderno = motion DISCRETO de polish, não espetáculo. Cada animation passa "produto profissional".

**Por quê funcionou:** dev audience valoriza performance + clarity — motion ostensivo perderia trust técnico.

**Aplicar quando:** SaaS B2B targeting dev/decisor técnico.

---

### Case 1.6 — Linear (linear.app)

**Tipo:** SaaS landing premium B2B
**Audiência:** product manager + engineering lead
**Stack:** Next.js + Framer Motion
**Motion signature:**
- Hero kinetic typography minimal
- Background gradient mesh sutil
- Section reveal staggered curto
- Microinteractions calibradas
- Smooth scroll nativo

**Lesson learned:** Linear estabeleceu padrão "minimal technical premium" — motion existe mas é INVISÍVEL como aircraft well-engineered.

**Por quê funcionou:** audience PM/EM valoriza calmness + sophistication.

**Aplicar quando:** SaaS B2B competindo com Notion/Figma/Linear-tier.

---

### Case 1.7 — Vercel ship landing pages

**Tipo:** event launch / product reveal
**Audiência:** dev community
**Stack:** Next.js + Framer Motion + custom WebGL
**Motion signature:**
- Hero WebGL shader animado
- Kinetic headline split letter-by-letter
- Section transition page-flip
- Particles ambient

**Lesson learned:** event launch = motion pode ser EXPERIMENTAL (vai durar ~30 dias), tolerância alta pra wow factor.

**Por quê funcionou:** audience dev curiosa por técnica nova + contexto event = aceita experimental.

**Aplicar quando:** product launch landing page ephemeral.

---

### Case 1.8 — Awwwards SOTD (Site of the Day) median

**Tipo:** portfolio agency / creative studio
**Audiência:** peer designers + clientes premium
**Stack:** Misto (40% Webflow+GSAP+Barba, 35% Next/Nuxt+R3F, 20% Astro+GSAP, 5% custom)
**Motion signature comum:**
- Lenis canonical smooth scroll
- Persistent canvas Three.js
- Page transition cinematic
- Cursor follower custom
- Kinetic typography

**Lesson learned:** Awwwards-tier converge em ~5 motion patterns universais. Diferenciação está NA EXECUÇÃO + brand-specific touches, não em técnica nova.

**Por quê funciona:** audience expects motion award-grade — sem isso, perde competição visual.

**Aplicar quando:** portfolio agency querendo entrar Awwwards.

---

### Case 1.9 — Codrops featured tutorials (frontend exploration)

**Tipo:** technical exploration / experiment
**Audiência:** devs aprendendo técnicas
**Stack:** Vanilla GSAP + Three.js + custom
**Motion signature:**
- Experimental técnicas isoladas
- Cada tutorial = 1 técnica focused
- Documentação clara
- Performance varia (foco é técnica, não optimization)

**Lesson learned:** Codrops = laboratório técnicas. Não copia diretamente pra production sem adaptar reduced motion + perf.

**Por quê funciona:** dev audience busca exploração técnica, aceita demos sem polish completo.

**Aplicar quando:** referência técnica isolada OU showcase técnico pra dev audience.

---

### Case 1.10 — Osmo Supply (osmo.supply)

**Tipo:** template marketplace + design system
**Audiência:** Webflow / GSAP devs buscando templates
**Stack:** Webflow + GSAP + custom
**Motion signature:**
- 30+ patterns canonical (button packs, text effects, scroll, etc)
- CustomEase "osmo-ease" nomeada universalmente
- Quality bar consistente em todo site
- Mix free + paid templates

**Lesson learned:** Osmo estabeleceu vocabulário motion comum em mercado Webflow. CustomEase nomeada virou cita standard.

**Por quê funciona:** preencheu lacuna entre Codrops (técnico) e Awwwards (showcase) — Osmo é "production-ready templates".

**Aplicar quando:** referência pra avaliar Make vs Buy decisão (DIY vs Osmo). Detalhes em `09-osmo-comparable.md`.

---

## 2. Awwwards-tier sites (DR-B — 30 cases categorizados)

### 2.1 Stack Pattern A: GSAP+Lenis+Three.js+Vue/Nuxt (~35% Awwwards)

**Sites exemplo:**
- Hatom Protocol (DeFi)
- Studio375 (creative agency)
- Silent House (architecture)
- OGAKI (creative studio)
- Planetoño (brand creative)

**Motion comum:**
- Lenis canonical smooth scroll
- Persistent canvas Three.js / R3F
- Page transition cinematic
- Cursor follower
- Kinetic typography

**Quando aplicar:** creative agency / brand premium / architecture studio.

---

### 2.2 Stack Pattern B: GSAP+Webflow+Barba (~25% Awwwards)

**Sites exemplo:**
- Telha Clarke (DR-A)
- Made With GSAP showcase
- Many Webflow Made-with showcases
- Some agency portfolios

**Motion comum:**
- Barba page transitions
- GSAP ScrollTrigger
- registerEffect + Custom Elements
- Lenis smooth scroll

**Quando aplicar:** agencies que mantém Webflow stack mas precisam motion award-grade.

---

### 2.3 Stack Pattern C: GSAP DOM-only (~20% Awwwards)

**Sites exemplo:**
- Linear-style minimal sites
- Editorial premium
- Some SaaS landing premium

**Motion comum:**
- ScrollTrigger DOM transformations
- SplitText kinetic typography
- FLIP layout animations
- Sem 3D / WebGL

**Quando aplicar:** SaaS B2B premium ou editorial onde 3D seria overkill.

---

### 2.4 Stack Pattern D: Custom (não-GSAP) (~15% Awwwards)

**Sites exemplo:**
- Apple product pages
- Vercel ship pages
- Some Apple-tier B2C

**Motion comum:**
- Custom rAF + Intersection Observer
- WebGL custom shaders
- Image sequences (sprite frame)
- Framer Motion (React)

**Quando aplicar:** quando bundle budget é crítico OU motion é tão custom que GSAP overhead não compensa.

---

### 2.5 Stack Pattern E: Astro+GSAP (~5% emergente)

**Sites exemplo:**
- Performance-first creative sites
- Static-first portfolios

**Motion comum:**
- Astro islands com GSAP
- View Transitions API + GSAP fallback
- Lighter bundle vs SPA

**Quando aplicar:** portfolio static-first ou content-heavy site precisando performance + motion.

---

## 3. Codrops featured tutorials (DR-B — 24 técnicas)

### 3.1 Categoria: Scroll-driven narrative

- **Sticky scrollytelling** (image transitions on scroll)
- **Persistent 3D scene** (Three.js + ScrollTrigger pin)
- **Scroll-linked SVG path drawing**
- **Camera path following scroll**

### 3.2 Categoria: Interaction primitives

- **Cursor follower variations** (10+ variations)
- **Magnetic button effect**
- **Custom hover reveals**
- **Drag interactions com physics**

### 3.3 Categoria: Page transitions

- **Barba.js + GSAP timeline orchestration**
- **View Transitions API + fallback**
- **Shared element transitions**
- **Slide direction-aware transitions**

### 3.4 Categoria: Text effects

- **SplitText word stagger variations**
- **Kinetic typography manifesto**
- **Text-on-path animation**
- **Variable font weight pulse**

### 3.5 Categoria: WebGL effects

- **Shader noise backgrounds**
- **Image distortion on hover (RGB shift)**
- **Particle systems leves**
- **Custom material PBR**

### 3.6 Categoria: Layout animations

- **FLIP filter/sort grids**
- **Flip.fit consecutive scrub waypoints**
- **Layout shift transitions**

---

## 4. Lessons learned cross-cutting (10 takeaways)

### Lesson 1 — "Shell motion" thesis (DR-B)

Motion award-grade não está só em hero — está nos SHELLS (loaders, menus, footers, contact pages). Sites Awwwards-tier polish os shells tanto quanto hero.

**Aplicar:** ao auditar projeto, verificar se shells (loader, footer, menu, 404, contact) tem motion polish ou são deixados genéricos.

### Lesson 2 — "Anti-demo" framing (DR-B)

Motion award-grade NÃO é demo de técnica — é narrativa cohesiva onde técnica desaparece. Demo motion = "olha que legal!"; award-grade = "que site interessante."

**Aplicar:** se motion chama atenção pra SI MESMO, não tá award-grade. Refator pra servir narrative.

### Lesson 3 — GSAP é "continuity engine" (DR-B)

GSAP não é animation library — é continuity engine. Sustenta percepção de site COESO entre sections, rotas, interactions, com timing harmônico.

**Aplicar:** definir GSAP CustomEase nomeada usado universalmente = identidade motion brand.

### Lesson 4 — Polish = anti-IA frontier (DR-C)

Motion award-grade = fronteira anti-IA em mercado AI-saturado. AI gera site genérico; polish motion não pode ser gerado AI.

**Aplicar:** vendas premium = mostrar motion polish como diferencial vs sites AI-gerados.

### Lesson 5 — Scrollytelling > 5 capítulos = fadiga

Sticky narrative com 6+ capítulos perde audience. Limit em 3-5 max.

### Lesson 6 — Mobile precisa fallback simplificado

Awwwards-tier desktop ≠ mobile experience. Mobile precisa simplificar OU desligar motion pesado.

### Lesson 7 — Reduced motion não é opção, é obrigação

WCAG 2.3.3 + ~5% audience com vestibular sensitivity. Sem fallback significativo = exclusão.

### Lesson 8 — Performance budget é design decision

Hero 3D com 5MB bundle = LCP perdido = abandono. Performance NÃO é optimization após design — é constraint inicial.

### Lesson 9 — Motion design system > snippets isolados

Sites Awwwards-tier tem motion system implícito (durations, easings, curves nomeadas). Snippets isolados em projeto = inconsistência percebida.

### Lesson 10 — Browser quirks ainda matam motion

Lenis quirks Safari iOS + Three.js mobile + Firefox CSS scroll-driven gaps. Cross-browser audit ainda obrigatório em 2026.

---

## 5. Lookup map — case por contexto

| Session narrative | Cases priorizados |
|---|---|
| Sales premium B2C luxo | Apple product pages, Vercel ship, Hatom |
| Sales B2B SaaS moderno | Stripe Connect, Linear, Vercel |
| Portfolio agency creative | Studio375, OGAKI, Silent House, Telha Clarke |
| Brand site institutional | Hatom, Telha Clarke, Planetoño |
| Slide deck pitch | (mostly internal — refer Apple keynote pattern) |
| Editorial long-form | (mostly Codrops scroll-driven tutorials) |
| E-comm luxury | Apple shop, premium fashion brands |
| SaaS landing premium | Linear, Stripe, Vercel |

---

## 6. Anti-patterns case study application

1. **Copy 1:1 sem adapter:** Hatom DeFi motion em SaaS B2B = desalinhamento.
2. **Awwwards mobile sem checar:** Awwwards usually shows desktop screenshot. Mobile pode ser disaster.
3. **Esquecer reduced motion:** sites Awwwards às vezes não tem strict fallback. NÃO replicar.
4. **Performance assumption:** Awwwards desktop powerful machine. Mobile mid-range pode quebrar.

---

## 7. Boundary com outras skills

- **`pattern-importer`** — importa patterns de open source. Esta ref descreve cases conceptuais; pattern-importer adapta código.
- **`reference-finder --solution-scout`** — busca refs externas. Esta ref TEM refs já curadas dos 4 DRs.

---

## 8. Manutenção desta ref

- ADD novo case study só quando 3+ projetos Patrick mencionaram OR Awwwards SOTD com técnica nova
- Atualizar trimestralmente (Awwwards muda ranking, sites podem sair do ar)
- Re-validar links ao adicionar (deeplinks frequentemente quebram)
