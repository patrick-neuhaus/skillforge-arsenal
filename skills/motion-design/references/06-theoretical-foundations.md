# `references/06-theoretical-foundations.md` — Theoretical Foundations Motion (Wave 9)

> **4 fundamentos teóricos** que justificam decisões motion: Gestalt, Attention Economy, Scroll Psychology, Easing Semantics. Cada princípio com aplicação prática + frase template "X porque Y".
> **Quando usar:** Phase 3 do `--full` consulta esta ref pra gerar embasamento teórico das propostas. Output Patrick lê + cita em vendas como diferencial.
> **Boundary:** foundations conceptuais. Frases prontas estilo copy-paste em `11-validation-prompts.md`. Recipes técnicas em `05-gsap-recipes.md`.

---

## 1. Gestalt principles aplicados a motion

### 1.1 Continuity (continuidade)

**Princípio:** Olho humano segue trajetórias contínuas, prefere caminhos lineares/curvos suaves a saltos.

**Aplicação motion:**
- Stagger reveal de palavras em headline = trajetória horizontal de leitura
- FLIP layout animation = elementos "viajam" entre posições (não saltam)
- Scrollytelling sticky frame = visual fixo ENQUANTO texto rola = continuidade espacial
- Page transition shared element = item da lista "vira" hero da próxima rota

**Frase template:**
> "Vou usar [stagger reveal / FLIP / shared element] aqui porque continuity gestalt mantém olho do user em trajetória linear, evitando saltos cognitivos que quebram leitura."

**Anti-pattern:**
> "Não usaria [hard cut / fade simples / pop-in random] aqui porque quebra continuidade — user perde rastro do que aconteceu."

### 1.2 Common fate (destino comum)

**Princípio:** Elementos que se movem juntos são percebidos como grupo/relacionados.

**Aplicação motion:**
- Cards entrando em stagger (mesmo direção, mesmo timing offset) = "estes pertencem juntos"
- Logo wall scroll horizontal contínuo = "social proof em conjunto"
- Filter chips entrando juntos = "filtros relacionados"

**Frase template:**
> "Stagger uniforme em [cards/logos/chips] porque common fate gestalt sinaliza grupo coeso — user percebe como categoria, não items isolados."

### 1.3 Closure (fechamento)

**Princípio:** Cérebro completa formas/sequências incompletas.

**Aplicação motion:**
- Self-drawing path SVG (logo reveal traçado) = user "vê" forma completa antes terminar
- Loader circular (arc desenhando) = user antecipa círculo completo = sensação progresso
- Reveal staggered onde último elemento = CTA = closure aponta pro click

**Frase template:**
> "Self-drawing path no logo porque closure gestalt — cérebro do user completa forma antes mesmo do path acabar = sensação de descoberta + memorabilidade."

### 1.4 Proximity (proximidade)

**Princípio:** Elementos próximos espacialmente são percebidos como relacionados.

**Aplicação motion:**
- Tooltip aparece próximo do trigger = relação clara
- Toast aparece próximo do action que disparou = causalidade visual
- Modal abre centrado em viewport (não próximo ao botão) = quebra proximity intencional pra mudança contexto

**Frase template:**
> "Dropdown abre a partir do trigger (não centrado) porque proximity gestalt — origem física informa relação. User não procura onde apareceu."

### 1.5 Anti-pattern Gestalt

NUNCA mover elementos não-relacionados em sincronia (vira common fate falso). Ex: hero title staggered junto com sidebar items = user pensa que estão relacionados quando não estão.

---

## 2. Attention Economy

### 2.1 Princípio central

User tem **atenção finita**. Cada motion compete por essa atenção. Decisão crítica: motion AJUDA leitura/foco OU COMPETE com conteúdo principal?

### 2.2 First fold attention budget

**Pesquisa (Nielsen Norman):** user decide ficar/sair em 3-5 segundos na primeira dobra. Motion na hero tem 1 job: ACELERAR mensagem-chave + CTA. NÃO competir com leitura.

**Regra dura:** mensagem-chave + CTA legíveis em ≤ 1 segundo. Motion serve leitura, NÃO atrasa.

**Frase template:**
> "Hero reveal em 800ms porque attention economy primeiro contato — user precisa entender mensagem em ≤1s. Motion mais lento atrasa decisão = abandono."

**Anti-pattern:**
> "Não usaria hero loop ambient + kinetic typography pesado + 3D scene aqui porque cada motion compete pela atenção limitada do user — resultado: user vai embora antes entender o que oferecemos."

### 2.3 Operational vs decorative attention

**Operational motion** (feedback, loading, transition) = atenção REQUERIDA. User PRECISA perceber pra continuar tarefa.

**Decorative motion** (ambient, brand reveal, hover effect) = atenção CONCEDIDA. User aceita olhar se contexto permite.

**Calibração:**
- SaaS dashboard: 90% operational + 10% decorative max
- Landing page: 60% operational + 40% decorative
- Brand site: 30% operational + 70% decorative
- Slide deck: 20% operational + 80% decorative (storytelling)

**Frase template:**
> "Em SaaS operacional uso microinteractions discretas + skeleton loading. Decorative motion (ambient, hero loop) sai de fininho porque competiria com tarefa do user."

### 2.4 Distraction tax

Cada motion ornamental cobra "tax" cognitivo. 5 motions ornamentais = user processa cada um = fadiga + abandono.

**Regra:** se animar 100+ vezes/dia, motion = 0 OR ≤100ms. Vide craft gate `01-funcional-estrutural.md`.

**Frase template:**
> "Press feedback em 80ms porque user clica isso 100+ vezes/dia. Motion mais longo = distraction tax acumulado = friction."

---

## 3. Scroll Psychology

### 3.1 Modos de scroll do user

| Modo | Comportamento | Implicação motion |
|---|---|---|
| **Skimming** (escaneando) | Scroll rápido, busca visual ancora | Motion precisa SECTION ENTRANCE óbvia (não sutil demais) |
| **Reading** (lendo) | Scroll lento, conteúdo absorvido | Motion deve EVITAR competir com leitura linha-a-linha |
| **Searching** (procurando) | Scroll com Cmd+F mental | Motion não pode ESCONDER conteúdo via reveal demorado |
| **Hunting** (caçando CTA) | Scroll buscando preço/botão | Motion deve REVELAR CTA rápido |

**Frase template:**
> "Section reveal staggered curto (250ms) porque user em modo skimming — precisa percepção rápida 'tem section aqui'. Reveal lento perderia ancora visual."

### 3.2 Vestibular triggers (WCAG 2.3.3)

Movimentos que disparam náusea/desconforto vestibular:
- **Parallax forte** (deslocamentos > 100px relativos ao viewport)
- **Camera-style 3D parallax** (zoom + tilt + pan combinados)
- **Auto-scroll** (sequestra controle do user)
- **Rotação contínua** > 1Hz
- **Zoom contínuo** sem trigger user

**Regra dura:** TODA animação não-essencial disparada por scroll/hover deve ser desligável via `prefers-reduced-motion: reduce`.

**Frase template:**
> "Parallax range ≤30px porque vestibular — deslocamentos maiores disparam náusea em ~5% dos users (WCAG 2.3.3). Premium é experiência confortável, não show ofensivo."

### 3.3 Scroll velocity vs animation timing

User scroll velocity varia: trackpad slow (~500px/s) vs mousewheel fast (~3000px/s) vs keyboard PageDown (~viewport/click).

**Implicação:** ScrollTrigger sem `scrub` smoothing = jitter em scroll fast. ScrollTrigger com `scrub: 0.5-1` = catchup suave.

**Frase template:**
> "ScrollTrigger com scrub: 0.5 porque user scroll velocity varia 6x entre input methods. Smoothing previne jitter visual em mousewheel rápido sem atrasar trackpad lento."

### 3.4 Sticky narrative pattern

Sticky frame + texto rolando = pattern narrativo poderoso (DR-05 + DR-B). Mas:
- Mensagem PRECISA sobreviver sem motion (fallback estático)
- Não exagerar pinning (max 5 capítulos = ~5 viewports)
- Mobile: considerar versão simplificada

**Frase template:**
> "Sticky frame com 3 capítulos porque scroll psychology — user lê narrativa progressiva. Mais que 5 capítulos = fadiga; menos que 2 = motion overhead sem benefício narrative."

---

## 4. Easing Semantics

### 4.1 Curves transmitem sensações

| Curve | Sensação | Quando usar |
|---|---|---|
| **linear** | Mecânico, robótico, contínuo | Loops infinitos (skeleton, spinner) |
| **ease-out** | Natural chegada, "pousa" | Entradas, reveals (default) |
| **ease-in** | Acelera saindo, "lança" | Saídas (modal close, drawer dismiss) |
| **ease-in-out** | Suave 2 lados, "respiração" | Estados toggle, autoplay loops |
| **power3.out** | Punchy, decisivo | Botão press, CTA highlight |
| **back.out(1.7)** | Overshoot lúdico | Confirmação positiva (success check) |
| **elastic.out** | Bouncy, brincalhão | Decorativo, brand creative |
| **expo.out** | Cinematic premium | Hero reveal, premium brand |
| **CustomEase "osmo-ease"** | Orgânico não-mecânico | Award-grade premium |
| **CustomEase "hop"** | Bounce orgânico custom | Brand creative com personalidade |

### 4.2 Tom de motion → easing escolhido

| Tom session narrative | Easing recomendado |
|---|---|
| minimal técnico (B2B SaaS) | ease-out, power2.out |
| cinematic premium (brand sales) | osmo-ease, expo.out, CustomEase nomeado |
| lúdico criativo (creator brand) | back.out, elastic.out, hop |
| brutalist editorial (editorial premium) | linear (intencional), ease-in-out simples |
| operational (dashboards) | ease-out (entrance), ease-in (exit) — easeReverse pattern |

**Frase template:**
> "CustomEase osmo-ease (0.625, 0.05, 0, 1) aqui porque tom session narrative = cinematic premium. Curve orgânica não-mecânica match expectativa Awwwards-tier; power2.out seria genérico SaaS."

### 4.3 Asymmetric easing (entrance vs exit)

**Princípio:** entrada e saída raramente devem usar mesmo easing.
- **Entrada:** ease-out — anuncia presença, "pousa"
- **Saída:** ease-in OR power3.in — fora do caminho, "decola"

GSAP 2026 `easeReverse` resolve sem timeline manual.

**Frase template:**
> "Modal entrance ease-out 320ms + exit ease-in 200ms via easeReverse porque saída deve ser MAIS rápida que entrada — Carbon/Material guidelines convergem nisso. User quer voltar ao contexto, não esperar fade-out lento."

### 4.4 Anti-pattern easing

- **Linear em UI feedback:** parece mecânico/quebrado. Use `ease-out`.
- **Bounce/elastic em SaaS sério:** quebra confiança. Use `power2.out`.
- **CustomEase complexo em microinteraction press:** overhead injustificado. Use `power2.out` simples.
- **Default ease (sem especificar):** GSAP usa `power1.out` — OK mas raramente "polish award-grade". Specifique sempre.

---

## 5. Síntese — combinando 4 foundations

Decisão motion award-grade = aplicar 4 foundations simultaneamente:

### Exemplo: Hero reveal em landing premium

**Phase 3 proposal usando 4 foundations:**

```
Vou usar headline staggered word-reveal (40ms stagger) + CustomEase osmo-ease + duração 1.2s em hero porque:

1. Gestalt continuity: stagger 40ms cria trajetória horizontal de leitura — olho segue palavra-em-palavra sem saltar.
2. Attention economy: hero é primeira dobra, user decide em 3s — 1.2s deixa CTA + headline lidos antes de scroll.
3. Scroll psychology: user provavelmente entrando modo skimming — reveal precisa ser óbvio (não sutil) pra ancorar atenção.
4. Easing semantics: osmo-ease (0.625, 0.05, 0, 1) match tom 'cinematic premium' do session narrative — diferencia de SaaS genérico ease-out.

Não usaria:
- Linear easing porque parece mecânico/genérico — perde diferencial premium.
- Hero loop ambient simultâneo porque competiria atenção da headline.
- Stagger > 80ms porque vira "uma palavra de cada vez", quebra fluxo de leitura.
```

---

## 6. Boundary com outras skills

- **`ux-audit`** — audita se motion paga aluguel no fluxo real. Esta ref justifica decisões; ux-audit valida na prática.
- **`ui-design-system`** — tokens (duration/easing) baseados nestes foundations. Esta ref dá embasamento; DS materializa em CSS vars.
- **`react-patterns`** — implementação foundations virou code. Cross-browser caveats.
- **`copy`** — kinetic typography overlap; copy decide MENSAGEM, motion decide REVEAL.

---

## 7. Referências bibliográficas

- **Gestalt psychology:** Wertheimer, Koffka, Köhler (1920s) — princípios visuais aplicados a motion contemporâneo.
- **Attention Economy:** Herbert Simon (1971) "Designing Organizations for an Information-Rich World"
- **Nielsen Norman Group:** "How Long Do Users Stay on Web Pages?" (5-10s decision)
- **WCAG 2.3.3:** Animation from Interactions — guideline reduced motion
- **Carbon Design System / Material Design / Atlassian Motion:** convergência industry guidelines
- **Easing curves:** Robert Penner equations (1990s) + GSAP CustomEase extensions
- **Scroll psychology:** Jakob Nielsen "Eyetracking Research" + DR-05 sintese
- **DR-05-animations.md:** sintese local em `Downloads/Skill de Design/deep research/DR-05-animations.md`
- **DR-A/B/C GSAP merged:** showcases reais aplicando foundations

---

## 8. Manutenção desta ref

- ADD foundation novo só quando padrão real apareceu 3+ vezes nas decisões `--full`
- Remover foundation que nunca foi citado em proposta `--full` por 90 dias
- Revisão trimestral
