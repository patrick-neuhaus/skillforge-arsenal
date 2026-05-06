# `references/09-osmo-comparable.md` — Osmo Supply Comparable + DIY vs Comprar Matrix (Wave 9)

> **30+ patterns Osmo Supply** mapeados + custo replicação DIY vs Osmo Member (€20-25/mês) vs Lifetime (€750). Ajuda Patrick decidir Make vs Buy em projetos.
> **Quando usar:** quando session narrative pede pattern Osmo (button hover premium, text effect cinematographic, scroll narrative). Phase 2 decision considera matrix.
> **Boundary:** focado Osmo Supply specifically. Outras alternatives commerciais em `08-case-studies.md` Pattern E (custom). Recipes técnicas em `05-gsap-recipes.md`.

---

## 1. Osmo Supply overview

**Site:** osmo.supply
**Founders:** small team Webflow/GSAP focused
**Modelo:**
- **Member:** €25/mês ou €20/mês anual = acesso 30+ patterns + button pack + text effects
- **Lifetime:** €750 = acesso vitalício
- **Course:** €199 standalone = curso GSAP+Webflow
- **Button Pack standalone:** €100 (50 buttons) OR €50 unlock 50 included via Member
- **Free tier:** 5-10 patterns sample

**Stack:** Webflow + GSAP + Lenis + custom shaders
**CustomEase nomeada:** "osmo-ease" (0.625, 0.05, 0, 1) virou referência industry

**Resource count (DR-C divergência):**
- Claude DR-C contou: 165 production-ready
- ChatGPT DR-C contou: 176 (incluindo Button Pack slots active)
- Diferença ≈ button pack WIP

---

## 2. Inventário Osmo (categorizado)

### 2.1 Button effects (~50 patterns)

**Categorias:**
- Hover lift + shadow (10+ variants)
- Cursor magnetic (5+ variants)
- Liquid CTA hover (SVG turbulence filter)
- Border draw on hover (SVG path)
- Background gradient shift (CSS vars)
- Icon morph state (rotational MorphSVG)
- Text reveal on hover (split + stagger)
- Press compress + spring back

**Cost DIY:** ~30 min - 2h cada, depende complexidade
**Cost Osmo:** Member access OR €100 Button Pack standalone

---

### 2.2 Text effects (~30 patterns)

**Categorias:**
- SplitText word stagger reveal
- Letter-by-letter reveal
- Variable font weight pulse
- Marquee horizontal/vertical
- Scrub reveal on scroll
- Typewriter effect
- Text-on-path animation
- Glitch / distortion text
- Liquid morph text
- 3D text rotation

**Cost DIY:** ~30 min - 4h cada
**Cost Osmo:** Member

---

### 2.3 Scroll narrative patterns (~25 patterns)

**Categorias:**
- Sticky scrollytelling
- Pin + animate sequences
- Scroll-driven CSS vars
- Section reveal staggered
- Image sequence on scroll
- Layered parallax narrative
- Reading progress bar
- Section pin with horizontal scroll
- Camera path following scroll
- Marquee linked to scroll velocity

**Cost DIY:** ~1-8h cada, alguns muito complexos
**Cost Osmo:** Member

---

### 2.4 Page transitions (~15 patterns)

**Categorias:**
- Barba+GSAP cinematographic
- Barba+GSAP fade simple
- View Transitions API
- Slide direction-aware
- Curtain reveal
- Logo morph transition

**Cost DIY:** ~2-8h cada
**Cost Osmo:** Member

---

### 2.5 Hover / cursor effects (~20 patterns)

**Categorias:**
- Cursor follower variations
- Magnetic effect
- Image distortion on hover (WebGL)
- Card tilt 3D faux
- Reveal mask on hover
- Color invert on hover
- Cursor trail effect

**Cost DIY:** ~30min - 4h cada
**Cost Osmo:** Member

---

### 2.6 Loading / boot patterns (~10 patterns)

**Categorias:**
- Logo reveal splash
- Progress bar with brand
- Skeleton variations
- Boot animation cinematic

**Cost DIY:** ~1-3h cada
**Cost Osmo:** Member

---

### 2.7 Background / ambient (~15 patterns)

**Categorias:**
- Gradient mesh animado
- Particle field
- Shader noise
- Blob morph
- Liquid gradient

**Cost DIY:** ~2-12h cada (shader pode ser pesado)
**Cost Osmo:** Member

---

## 3. DIY vs Comprar — Matrix de decisão

### 3.1 Quando DIY faz sentido

| Cenário | Por quê DIY |
|---|---|
| Projeto único / one-off | Subscription Osmo não amortiza |
| Pattern muito específico | Osmo tem genérico, projeto precisa custom |
| Time interno aprendendo GSAP | DIY = aprendizado paga depois |
| Brand-specific motion | Osmo é genérico, brand precisa identidade |
| Cliente paga R$5k+ pelo motion | DIY = margem maior |
| Projeto > 6 meses lifecycle | Tempo amortiza investimento |

### 3.2 Quando comprar Osmo Member faz sentido

| Cenário | Por quê comprar |
|---|---|
| Múltiplos projetos / mês | €25/mês amortiza com 1 projeto |
| Time que opera Webflow primário | Osmo é Webflow-native |
| Projeto rápido (deadline curto) | DIY paga prazo, Member paga produtividade |
| Cliente quer "look Osmo-tier" | Osmo entrega já calibrado |
| Pattern complexo (Flip.fit consecutive) | DIY exige expertise, Osmo entrega refinado |

### 3.3 Quando Lifetime €750 faz sentido

| Cenário | Por quê Lifetime |
|---|---|
| Operação contínua > 30 meses | Lifetime = €25 × 30 = breakeven |
| Time fixo Webflow agency | ROI longo prazo claro |
| Múltiplos clientes recorrentes | Cada projeto usa = amortiza |
| Patrick fluxo atual | Pode amortizar se Webflow continuar relevante |

### 3.4 Quando Course €199 standalone faz sentido

| Cenário | Por quê Course |
|---|---|
| Aprendizado solo | Cheaper than Member se só quer aprender |
| Sem necessidade templates production | Course ensina técnica, não entrega templates |
| Junior dev onboarding | Course = onboarding GSAP+Webflow |

---

## 4. Custos replicação por categoria (DIY estimativa)

### Tabela tempo replicação DIY (dev junior → sênior)

| Pattern | DIY junior | DIY sênior | Osmo entrega |
|---|---|---|---|
| Button hover lift simples | 30 min | 10 min | ✅ ready |
| Button magnetic + cursor | 4h | 1.5h | ✅ ready |
| Liquid CTA SVG turbulence | 8h | 3h | ✅ ready |
| SplitText word stagger | 1h | 30 min | ✅ ready |
| Marquee linked scroll | 3h | 1h | ✅ ready |
| Sticky scrollytelling 3 chapters | 12h | 4h | ✅ ready |
| Persistent canvas Three.js + Barba | 24h+ | 8h | ✅ ready |
| Cursor follower variations | 1-4h | 30min-2h | ✅ ready |
| Image distortion WebGL | 16h | 6h | ✅ ready |
| Custom shader noise bg | 12h | 4h | ✅ ready |

### Cálculo Patrick (R$ por hora)

Patrick freelancer estimativa: R$200/h. Hygor/Jonas: R$80-120/h.

| Pattern | DIY Patrick | DIY Hygor | Osmo investment |
|---|---|---|---|
| Sticky scrollytelling 3ch | R$800 | R$1440 | €25/mês ≈ R$140 |
| Persistent canvas | R$1600 | R$2880 | €25/mês |
| Liquid CTA | R$600 | R$1080 | €25/mês |
| 5 patterns simultâneos projeto | R$3000+ | R$5000+ | €25/mês |

**Conclusão:** 1 projeto premium com 5+ patterns Osmo já amortiza Member 6+ meses.

---

## 5. Osmo limitations (NÃO substitui DIY em todos casos)

### 5.1 Genérico vs brand-specific

Osmo é GENÉRICO calibrado. Brand-specific precisa adapter:
- Cores brand → CSS vars
- Easing brand → CustomEase nomeada brand
- Tom brand → adaptar duração / amplitude

**Exemplo:** Osmo button hover usa "osmo-ease". Brand premium pode querer "luxe-ease (0.7, 0, 0.3, 1)" — adapter manual.

### 5.2 Webflow-first

Osmo nasceu Webflow. React/Next/Astro = adapter manual:
- Remove Webflow CMS bindings
- Adapta pra useGSAP hook
- Reescreve markup pra JSX

**Custo adapter:** ~30 min - 2h por pattern.

### 5.3 Performance assumptions

Osmo patterns assumem desktop modern. Mobile + Save-Data:
- Verificar bundle cost
- Adicionar reduced motion fallback (Osmo as vezes light)
- Testar Safari iOS especificamente (Lenis quirks)

### 5.4 Não substitui Three.js custom

Osmo cobre patterns 80% — não substitui:
- Configurador 3D produto custom
- AR / WebXR experiences
- Custom shaders brand-specific
- Integration backend / real-time data

---

## 6. Competitors Osmo (DR-C mapeou 12)

### 6.1 Templates marketplace

| Service | Price | Foco |
|---|---|---|
| **Osmo Supply** | €25/mês | Webflow + GSAP, 30+ patterns |
| **Motion.page** | €15/mês | Framer + Webflow templates |
| **gFLUO** | €20/mês | GSAP-focused (mais técnico, less curated) |
| **Lofti UI** | €12/mês | Generic UI animations (less premium) |
| **Flowbase** | €19/mês | Webflow components (less motion-focused) |
| **Refokus** | Custom | Agency outputs, not templates |

### 6.2 Course / education

| Service | Price | Foco |
|---|---|---|
| **Osmo Course** | €199 | GSAP + Webflow específico |
| **GSAP official courses** | $99-299 | GSAP master técnico |
| **Frontend Masters GSAP** | $39/mês | Subscription mais ampla |
| **Codrops articles** | Free | Tutorials individuais |

### 6.3 Custom build agencies

Para casos onde nem Osmo nem DIY couber:
- Stripe agencies referenced (Awwwards SOTD)
- Patrick own services (compete or partner)

---

## 7. Decision tree — qual usar

```
Projeto novo precisando motion polish:
├─ Stack = Webflow?
│   ├─ Sim
│   │   ├─ Patrick faz Webflow > 1x/mês? → Osmo Member €25/mês
│   │   ├─ Webflow ocasional (1-2x/ano)? → DIY OR free tier Osmo
│   │   └─ Webflow agency com pipeline? → Osmo Lifetime €750
│   └─ Não (React/Next/Astro/Vue)
│       ├─ Pattern muito específico Osmo? → Compra + adapter (€25 + 1-2h)
│       ├─ Pattern simples? → DIY (Patrick faz rápido)
│       └─ Pattern complexo + tempo curto? → Osmo + adapter
├─ Stack = Lovable (React+Vite)?
│   └─ Use recipes próprios `05-gsap-recipes.md` + react adapter `12-react-adapters.md`
│      Osmo seria adapter overhead pra cada pattern
└─ Stack = Custom Three.js / WebXR / shader brand?
    └─ DIY obrigatório (Osmo não cobre)
```

---

## 8. Cassie Evans testimonial (DR-C)

GSAP team member Cassie Evans elogiou Osmo Supply publicamente — "templates de qualidade rara, técnica refinada". Validação industry-tier.

**Implicação:** Osmo NÃO é "snippet collection generic" — é production-tier curado.

---

## 9. Quando Patrick deve recusar Osmo

- **Cliente paga muito alto + brand-specific:** R$50k projeto = motion deveria ser custom Patrick, não template generic.
- **Audience Awwwards-tier expectativa:** Osmo é production-ready, não experimental award-grade.
- **Stack não-Webflow + tempo abundante:** custo adapter Osmo > DIY pra Lovable/Next.
- **Skill development goal:** se Patrick quer DOMINAR GSAP, DIY paga aprendizado.

---

## 10. Frase template para cliente sobre escolha

**Quando justificar usar Osmo (cliente perguntou):**

> "Escolhi Osmo Supply pra esses 5 patterns porque o template é production-tested + reduced motion já calibrado, dá pra adaptar pra brand colors em 30min cada. DIY levaria 8h+ por pattern com risco maior de bugs cross-browser. Investment €25/mês amortiza em 1 projeto."

**Quando justificar DIY (cliente perguntou):**

> "Esse motion vai ser brand-specific Patrick custom porque audience [X] espera identidade visual diferenciada — Osmo entrega genérico calibrado. DIY garante CustomEase nomeada com sua marca + animação que não vou ver em outro site."

---

## 11. Boundary com outras skills

- **`reference-finder --solution-scout`** — quando duvidar entre Osmo / DIY / outra alternativa, scout encontra alternatives.
- **`pattern-importer`** — importa pattern open source de outras refs (não Osmo paid).

---

## 12. Manutenção desta ref

- Refresh trimestral (Osmo lança templates novos, preços mudam)
- ADD competitor novo se surgir relevante
- Atualizar custos DIY conforme Patrick Wave 1 testes informarem tempo real
- Re-validar pricing Osmo (€25/mês confirma quarterly)
