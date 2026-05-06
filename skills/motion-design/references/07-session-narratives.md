# `references/07-session-narratives.md` — Session Narratives → Motion Language (Wave 9)

> **Mapeamento contexto → motion language.** 7 tipos de site/material × audiência × ação primária = motion language calibrada. Skill `--full` consulta esta ref no Phase 1 lookup pra match session narrative com recipes/patterns priorizados.
> **Quando usar:** Phase 1 lookup. Cruza session narrative card (Phase 0 output) contra esta ref pra ranking inicial.
> **Boundary:** mapeamento contexto → motion. Recipes técnicas em `05-gsap-recipes.md`. Foundations conceptuais em `06-theoretical-foundations.md`.

---

## 1. Princípio do mapeamento

Cada contexto pede **motion language diferente**. Não existe "motion universal". Mesma técnica que encanta em hero brand creative atrapalha em SaaS dashboard.

**3 dimensões da motion language:**
1. **Tom** — minimal técnico / cinematic premium / lúdico criativo / brutalist editorial / corporate clássico
2. **Densidade** — quanto motion ornamental aceitável (% vs operacional)
3. **Tolerância experimental** — risco de motion que envelhece rápido

---

## 2. Mapa por tipo de site

### 2.1 Sales / Landing institucional

**Contexto típico:**
- Audiência: B2B decisor (CMO, CEO, Head of Growth) ou B2C premium
- Ação: book demo / start trial / agendar call
- Time-on-page alvo: 2-5 min
- Conversion-driven: cada motion serve conversão, não espetáculo

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | minimal técnico (B2B SaaS) ou cinematic premium (B2B enterprise / B2C luxo) |
| Densidade | 60% operacional + 40% decorativo |
| Tolerância experimental | Baixa-média (não pode envelhecer em 1 ano) |

**Patterns prioritários:**
- Hero layered reveal staggered (400-800ms)
- Kinetic headline curta (split em palavras)
- Section enter stagger leve (250-400ms)
- Count-up discreto em métricas sociais
- CTA highlight pulse contextual
- Reading bar OR scroll progress
- Page transition cross-fade leve

**Patterns a evitar:**
- 3D pesado WebGL (custo bundle vs ROI conversion)
- Character animations lúdicas (B2B sério não combina)
- Scrollytelling pesado (atrasa CTA)
- Parallax forte (vestibular + mobile perf)

**Recipes priorizados (de `05-gsap-recipes.md`):**
- Recipe 1 (Lenis canonical) — smooth scroll diferencial
- Recipe 2 (CustomEase osmo-ease) — polish premium
- Recipe 7 (SplitText stagger) — kinetic headline
- Recipe 11 (gsap.quickTo) — cursor follower premium

**Frases template:**
> "Hero layered reveal 600ms + CustomEase osmo-ease porque sales premium = primeira dobra acelera mensagem + CTA, motion polish diferencia de SaaS genérico ease-out."

---

### 2.2 Portfolio (designer / agency / studio)

**Contexto típico:**
- Audiência: clientes potenciais (CMOs, founders) + peers (designers, agencies)
- Ação: book consultation / hire / inspire (peer review)
- Time-on-page alvo: 5-15 min (deep exploration)
- Awwwards-tier expectativa: motion É o produto

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | cinematic premium ou brutalist editorial ou lúdico criativo (depende personalidade brand) |
| Densidade | 30% operacional + 70% decorativo |
| Tolerância experimental | Alta (envelhecer em 1-2 anos é OK pra portfolio refresh) |

**Patterns prioritários:**
- Persistent canvas Three.js (Recipe 5)
- Page transition Barba+GSAP cinematográfico
- Cursor follower custom (Recipe 11)
- Hero scrollytelling com camera moves
- Kinetic typography manifesto
- Image gallery FLIP transitions
- WebGL shader backgrounds

**Patterns a evitar:**
- Skeleton loading mundano (não passa "wow")
- Microinteractions corporate clássicas
- Motion 100% operacional (parece SaaS)

**Recipes priorizados:**
- Recipe 1 (Lenis) — premium smooth scroll
- Recipe 5 (persistent canvas) — Three.js continuity
- Recipe 4 (Flip.fit consecutive) — scrollytelling
- Recipe 11 (gsap.quickTo) — cursor parallax

**Frases template:**
> "Persistent canvas Three.js + page transition Barba porque portfolio audience espera motion award-grade — sem 3D imersivo, perde competição visual contra peers."

---

### 2.3 SaaS operacional / Dashboard / Admin

**Contexto típico:**
- Audiência: usuários recorrentes (operam app diariamente)
- Ação: completar tarefas operacionais (CRUD, filter, export)
- Time-on-page alvo: várias sessões/dia, minutos cada
- Eficiência > espetáculo: motion atrapalha = abandono

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | minimal técnico DOMINANTE ou corporate clássico |
| Densidade | 90% operacional + 10% decorativo |
| Tolerância experimental | Zero — pattern testado obrigatório |

**Patterns prioritários:**
- Microinteractions (press 80ms, hover 120ms, focus ring 100ms)
- Skeleton loading (não shimmer chamativo)
- Toast slide+fade (180-260ms)
- Modal backdrop+panel (200-320ms entry, 150-200ms exit)
- Drawer slide (220-360ms)
- FLIP reorder em listas (Recipe 9)
- Empty state ilustração simples (Lottie sem character lúdico)

**Patterns a evitar:**
- Hero kinetic typography pesado (não tem hero)
- Parallax scrolling
- 3D / WebGL (perf custo sem ROI operational)
- Character mascots animados
- Scrollytelling
- Background ambient loops
- Motion > 320ms em UI repetitiva (100+/dia)

**Recipes priorizados:**
- Recipe 3 (easeReverse pra modal/drawer)
- Recipe 9 (Flip layout em listas)

**Frases template:**
> "Microinteractions 80-180ms + easeReverse pra modal/drawer porque SaaS operational user vê interface 100+ vezes/dia — qualquer motion > 320ms vira friction acumulada = abandono produto."

---

### 2.4 Slide deck (pitch / sales presentation)

**Contexto típico:**
- Audiência: investidores / clientes alvo presenciais
- Ação: compreensão narrativa + decisão
- Time-on-page alvo: 5-30s por slide
- Storytelling-driven: motion serve narrativa, não decoração

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | cinematic premium ou minimal técnico (depende audience) |
| Densidade | 20% operacional + 80% decorativo (storytelling) |
| Tolerância experimental | Média (deck 1 ano de vida típico) |

**Patterns prioritários:**
- Kinetic headline word-reveal (Recipe 7)
- Section enter stagger (250-450ms)
- Number count-up em métricas
- Logo reveal curto (300-800ms)
- Image reveal staggered
- Sticky narrative frames (deck educacional)
- Gradient wash background sutil

**Patterns a evitar:**
- 3D Three.js (overhead deck format)
- Persistent canvas (slide é discreto, não SPA)
- Character mascots
- Scrollytelling longa (deck é discreto por slide)
- Motion ornamental sem mensagem (vira distração de venda)

**Recipes priorizados:**
- Recipe 2 (CustomEase polish)
- Recipe 7 (SplitText kinetic headline)

**Frases template:**
> "Kinetic headline word-reveal + CustomEase osmo-ease em slide pitch porque audience tem 5-15s por slide — motion deve REVELAR mensagem, não competir com leitura."

---

### 2.5 Brand site (creative / institutional brand)

**Contexto típico:**
- Audiência: brand discovery + peer recognition
- Ação: brand recall / portfolio sample / cultural alignment
- Time-on-page alvo: 3-10 min
- Brand expression dominante: motion É a personality

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | DEPENDE personalidade brand — cinematic premium / lúdico criativo / brutalist editorial |
| Densidade | 30% operacional + 70% decorativo |
| Tolerância experimental | Alta (refresh em 1-2 anos OK) |

**Patterns prioritários:**
- Hero kinetic typography manifesto
- Animated logos (intro splash + reveal hero)
- Morphing brand shapes (blob ambient, liquid hover)
- Character mascots (se brand é lúdico)
- Doodle / hand-drawn elements (creator brand)
- Scrollytelling brand story
- WebGL shader backgrounds
- Page transition cinematográfico

**Patterns a evitar:**
- Microinteractions SaaS-style (perde personalidade)
- Skeleton loading mundano
- Default ease-out genérico
- Motion sem identidade brand

**Recipes priorizados:**
- Recipe 1 (Lenis premium scroll)
- Recipe 2 (CustomEase nomeada brand-specific)
- Recipe 5 (persistent canvas se 3D brand-aligned)
- Recipe 6 (registerEffect + Custom Elements brand-specific)

**Frases template:**
> "CustomEase nomeada 'cinematicSilk' + persistent canvas com WebGL shader porque brand site é a personality — motion ornamental serve identidade, não conversão imediata."

---

### 2.6 Editorial / Blog / Long-form / Docs

**Contexto típico:**
- Audiência: leitor focado (long-form attention)
- Ação: ler / compreender / compartilhar
- Time-on-page alvo: 5-20 min
- Reading-driven: motion não pode COMPETIR com texto

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | brutalist editorial ou minimal técnico |
| Densidade | 70% operacional + 30% decorativo |
| Tolerância experimental | Baixa (leitor abandona se motion atrapalha) |

**Patterns prioritários:**
- Reading progress bar (Recipe 8 com CSS scroll-driven)
- Scroll-driven CSS vars pra gradient sutil
- Section enter sutil (somente uma vez por seção)
- Image reveal on scroll (clip-path)
- Self-drawing path em ilustrações editoriais
- Sticky narrative frames (explainer com visual fixo)
- Hover preview em links

**Patterns a evitar:**
- Hero kinetic typography (texto principal é o body)
- Background loops chamativos
- Parallax pesado (atrapalha reading flow)
- 3D / character animations
- Section reveal staggered repetidamente (irrita leitor)

**Recipes priorizados:**
- Recipe 8 (scroll-driven CSS vars) — progress + ambient sutil

**Frases template:**
> "Reading progress bar discreta + section reveal único (250ms) porque editorial = user em modo reading — motion ornamental atrapalha leitura linear, mas progress bar AJUDA orientação."

---

### 2.7 E-commerce / Loja produto

**Contexto típico:**
- Audiência: comprador comparando produtos
- Ação: add cart / buy now / wishlist
- Time-on-page alvo: 3-10 min (browsing) + 1-2 min (decision)
- Conversion-driven: motion serve product trust + decision

**Motion language calibrada:**

| Dimensão | Calibração |
|---|---|
| Tom | minimal técnico (mass market) ou cinematic premium (luxo / artesanal) |
| Densidade | 70% operacional + 30% decorativo (decorativo só em produto reveal) |
| Tolerância experimental | Baixa-média |

**Patterns prioritários:**
- Microinteractions cart (add 200ms + count-up badge)
- Image gallery zoom on hover
- Product 3D orbit (configurador) — Recipe 5 leve
- AR try-on (joalheria, óculos, móveis)
- FLIP filter/sort em grid produtos (Recipe 9)
- Quick view modal (200-280ms)
- Wishlist heart fill animation
- Skeleton loading em listagens

**Patterns a evitar:**
- Hero kinetic typography pesado (atrapalha browsing)
- Character mascots não-relacionados ao produto
- Scrollytelling (e-comm é browse + decide, não narrative)
- Page transition lenta (interrompe browse)

**Recipes priorizados:**
- Recipe 9 (Flip filter grid)
- Recipe 11 (cursor product hover)
- Recipe 5 (persistent canvas se configurador 3D)

**Frases template:**
> "FLIP filter + microinteractions cart porque e-comm = browse rápido + decision — motion deve servir comparison + trust signal sem atrapalhar."

---

## 3. Calibração por audiência

### 3.1 B2B Enterprise austero

- Tom: corporate clássico OR minimal técnico
- Evitar: lúdico, character, brutalist
- Easing: ease-out, power2.out (não osmo-ease custom)
- Reduced motion: strict

### 3.2 B2B SaaS moderno

- Tom: minimal técnico
- Aceitar: leves toques cinematic em hero
- Easing: power2.out, easeReverse pra modais
- Reduced motion: strict

### 3.3 B2C Premium / luxo

- Tom: cinematic premium DOMINANTE
- Aceitar: 3D produto, persistent canvas
- Easing: CustomEase nomeada
- Reduced motion: respeitar mas não destruir experiência

### 3.4 B2C Mass market

- Tom: minimal técnico (mobile-first)
- Aceitar: microinteractions vibrantes
- Easing: ease-out, power2.out
- Reduced motion: strict

### 3.5 Creator / Designer brand

- Tom: lúdico criativo OR brutalist editorial
- Aceitar: experimental WebGL, character animations
- Easing: CustomEase exotic, elastic, back.out
- Reduced motion: respeitar com fallback significativo

### 3.6 Dev / Designer audience técnica

- Tom: minimal técnico OR brutalist editorial
- Aceitar: motion polish que demonstra técnica
- Easing: CustomEase com nome citável (osmo-ease, hop)
- Reduced motion: strict (audience aware)

---

## 4. Calibração por ação primária

| Action | Motion priorities | Anti-pattern |
|---|---|---|
| Comprar agora | CTA highlight pulse + product reveal cinematic | Storytelling longo |
| Agendar call / book demo | Calendar widget reveal + CTA prominence | Hero pesado atrasando CTA |
| Baixar lead magnet | Form reveal smooth + download confirmation | Modal pesado |
| Assinar newsletter | Inline form expansion sutil | Modal interrompe leitura |
| Ler artigo | Reading progress + image reveals | Hero motion competindo body |
| Brand awareness | Storytelling progressivo + brand expressions | Conversion-pressure motion |
| Inspect product (e-comm) | 3D orbit + zoom + gallery FLIP | Page transition atrapalha browse |

---

## 5. Combinações comuns (cheat sheet)

### Sales premium B2C luxo
- Tom: cinematic premium
- Recipes: 1+2+7+11 (Lenis + CustomEase + SplitText + cursor)
- Tolerância: alta (motion É vendedor)

### SaaS B2B operacional
- Tom: minimal técnico
- Recipes: 3+9 (easeReverse modal/drawer + Flip layout)
- Tolerância: zero (motion = ferramenta)

### Portfolio designer Awwwards-tier
- Tom: cinematic premium ou brutalist
- Recipes: 1+5+11 (Lenis + persistent canvas + cursor)
- Tolerância: alta (motion É produto)

### Slide deck pitch B2B
- Tom: cinematic premium minimal
- Recipes: 2+7 (CustomEase + SplitText kinetic)
- Tolerância: média

### Brand site creative agency
- Tom: lúdico criativo OR brutalist
- Recipes: 5+6 (persistent canvas + registerEffect Custom Elements)
- Tolerância: alta

### Editorial premium long-form
- Tom: brutalist editorial
- Recipes: 8 (scroll-driven CSS vars)
- Tolerância: zero (reading flow sagrado)

### E-comm luxury
- Tom: cinematic premium
- Recipes: 5+9+11 (3D orbit + FLIP + cursor)
- Tolerância: média

---

## 6. Anti-patterns mapeamento

1. **Aplicar motion language errada:** brutalist editorial em slide pitch B2B sério = quebra trust.
2. **Ignorar audiência:** creator brand motion lúdico em audience B2B enterprise = desalinhamento.
3. **Tom único pra tudo:** "cinematic premium" não é universal — em SaaS operational vira overhead.
4. **Confundir tipo + audiência:** sales pra B2C luxo ≠ sales pra B2B SaaS — motion language muda.

---

## 7. Boundary com outras skills

- **`product-marketing-context`** — define posicionamento brand. Esta ref usa posicionamento pra calibrar motion.
- **`ui-design-system`** — tokens motion (duration/easing). Esta ref informa quais tokens fazem sentido por contexto.
- **`copy`** — define mensagem. Esta ref calibra motion AROUND mensagem.

---

## 8. Manutenção desta ref

- ADD novo tipo de site só quando 3+ projetos não couberam nos 7 atuais
- Refinar combinações conforme Patrick testa Wave 1 em 3 inputs reais
- Revisar trimestralmente alinhamento com tendências Awwwards/Codrops
