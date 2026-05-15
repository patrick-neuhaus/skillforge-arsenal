# `references/10-discovery-prompts.md` — Phase 0 Discovery Prompts (Wave 9)

> **Perguntas template Phase 0** calibradas por input type. Skill `--full` consulta esta ref no Phase 0 pra extrair session narrative com mínimo Q&A possível. Anti-pattern: fazer 12 perguntas sempre.
> **Quando usar:** apenas Phase 0 `--full`. `--quick` pula Phase 0 inteira.
> **Boundary:** perguntas pra DESCOBRIR contexto. Frases pra JUSTIFICAR decisões em `11-validation-prompts.md`.

---

## 1. Princípios das perguntas Phase 0

### 1.1 Mom Test aplicado

Perguntas seguem Rob Fitzpatrick "Mom Test":
- ❌ Pergunta sobre futuro/opinião: "Você acharia legal um motion premium?" (todo mundo diz sim)
- ✅ Pergunta sobre passado/comportamento: "Em projetos anteriores, qual motion realmente moveu a agulha em conversão?"

### 1.2 Especificidade > generalidade

- ❌ "Qual seu público?"
- ✅ "Quem é a pessoa específica que tem que ver isso e ficar impressionada? Cargo? Empresa exemplo?"

### 1.3 Cortar Q&A quando session narrative já cristalizado

Se Patrick respondeu 2 perguntas e já tem: tipo + audiência + action + tom = SUFICIENTE. Não fazer mais 6.

---

## 2. Banco de perguntas (12 total — skill escolhe N)

### Q1. Mensagem-chave (sempre — fundamental)

```
O que o user PRECISA entender em 5 segundos quando abre <site/section>?
1 frase máximo, sem feature list.
```

**Por quê:** define hierarquia visual + onde motion deve ACELERAR comunicação.

### Q2. Audiência primária (sempre — fundamental)

```
Quem é a pessoa específica que tem que ficar impressionada?
- Cargo: <CEO B2B / dev sênior / designer / leigo / etc>
- Empresa exemplo: <ex: COO da Nike, dev tech lead Stripe>
- Decision power: <decisor / influenciador / executor>
```

**Por quê:** B2B enterprise austero ≠ creator brand lúdico ≠ designer Awwwards-grade. Tom motion DEPENDE.

### Q3. Tipo de site (sempre — fundamental)

```
Categoria DR-05 + Awwwards qual encaixa?
- sales (lead gen / SaaS landing)
- portfolio (designer / agency)
- saas operacional (dashboard / app)
- brand site (institutional creative)
- slide deck (pitch / sales presentation)
- e-comm (loja produto)
- editorial (blog / docs / long-form)
- outro: <especifica>
```

**Por quê:** mapa direto pra references priorizadas no lookup map (`07-session-narratives.md`).

### Q4. Action primária (frequente — pula só se obvious)

```
O que esse motion precisa fazer o user disparar?
- comprar agora (purchase)
- agendar call (book demo)
- baixar lead magnet (download)
- assinar newsletter (subscribe)
- ler artigo (engage long)
- só awareness (brand recall)
- outro: <especifica>
```

**Por quê:** action determina urgência motion. "Comprar agora" pede CTA highlight imediato; "awareness" tolera storytelling longo.

### Q5. Stack técnica (auto-detect se input = repo, senão pergunta)

```
Qual stack alvo da implementação?
- Lovable (React + Vite)
- Next.js (SSR caveats)
- Astro (island OR pure GSAP)
- Webflow (custom code only)
- Vanilla / framework-less
- Outra: <especifica>

Se aplicável: GSAP já instalado? Lenis já instalado? React Three Fiber?
```

**Por quê:** stack adapter em `12-react-adapters.md`. Lovable = useGSAP hook; Next = dynamic import GSAP plugins; Webflow = vanilla GSAP.

### Q6. Tom de motion (frequente — define easing/duração)

```
Qual tom motion match com brand/contexto?
- minimal técnico (B2B SaaS sério, dashboards)
- cinematic premium (sales premium, awards-tier brand)
- lúdico criativo (creator brand, character-driven)
- brutalist editorial (editorial premium, intentional rough)
- corporate clássico (enterprise B2B conservador)
- outro: <especifica>
```

**Por quê:** match direto com easing semantics em `06-theoretical-foundations.md` sec 4.2.

### Q7. Restrições performance (situacional — só se mobile/perf relevante)

```
Restrições importantes?
- Mobile baixo é prioridade? (% tráfego mobile, target device tier)
- Save-Data importa? (cliente mercado emergente)
- LCP target? (default ≤ 2.5s, premium ≤ 1.5s)
- Bundle budget? (default JS ≤ 200KB gzipped, premium ≤ 100KB)
```

**Por quê:** restrições afetam cobertura recipes. Recipe 5 (persistent canvas Three.js) inviável em mobile baixo.

### Q8. A11y compliance level (situacional — só se cliente exige WCAG)

```
Compliance level WCAG?
- AA strict (legal compliance — gov, health, banking)
- AA flexível (default web)
- AAA aspirational (raríssimo, opcional)

Reduced motion strict?
- snap-to-end obrigatório
- alternativa significativa OK
- só desligar fine
```

**Por quê:** AA strict afeta opções (kinetic typography > 5s precisa pause; parallax > 30px disparador vestibular).

### Q9. Referências visuais (frequente — calibra expectativa)

```
Tem 1-3 sites/refs que servem de norte? Awwwards / Codrops / Osmo / Behance?

Se sim: cola URLs.
Se não: descreve em 1 frase o "feeling" que quer transmitir.
```

**Por quê:** match score Phase 1 lookup melhora muito com refs concretas. 3 URLs Awwwards específicas dão ranking imediato.

### Q10. Section foco (sempre — define escopo Phase 1)

```
Qual section/elemento primário pra motion?
- hero (primeira dobra)
- scroll narrative (storytelling sequencial)
- interaction (botão / form / CTA)
- page transition (route change)
- loading (skeleton / spinner / progress)
- microinteraction (hover / press / focus)
- background ambient (passive)
- outro: <especifica>

Tem outras sections secundárias OR foco único?
```

**Por quê:** section foco filtra references na Phase 1. Hero = `03-narrativo-editorial`; microinteraction = `01-funcional-estrutural`.

### Q11. Frequência uso (situacional — só se microinteraction/UI repetitivo)

```
Esse elemento user vê/interage quantas vezes?
- 100+ vezes/dia (UI componente repetido)
- dezenas/dia (dashboard recorrente)
- ocasional (botão CTA secundário)
- raro/único (hero load, splash)
```

**Por quê:** craft gate `01-funcional-estrutural.md` calibração. 100+/dia = motion ≤100ms ou zero. Raro = delight permitido.

### Q12. Origem ação (situacional — só se microinteraction)

```
O que dispara o motion?
- ponteiro (click/hover mouse)
- teclado (focus/Enter/Space)
- sistema (route-change automático, async response)
- scroll
- gesture (touch swipe / drag)
- timer (auto / idle)
```

**Por quê:** keyboard trigger = motion deve ser instantâneo (não atrasar accessibility). Scroll trigger = scrub-friendly.

---

## 3. Calibração profundidade Q&A por input type

### Input = URL site público (1-2 perguntas após confirmação contexto base)

```
1. Q1 (mensagem-chave) — confirma o que WebFetch extraiu
2. Q3+Q6 combinadas — "Tipo de site + tom motion?"
```

Pula: Q2 (audiência inferida do site), Q4 (action visível), Q5 (não é implementação direta), Q7-Q12 (sem restrições visíveis).

### Input = Figma URL (2-3 perguntas)

```
1. Q1 (mensagem-chave) — confirma frame principal
2. Q3+Q6 combinadas — tipo + tom
3. Q10 (section foco) — qual frame específico

Se Figma tem 3+ páginas: pergunta extra sobre escopo.
```

### Input = GitHub repo (3-5 perguntas — input rico)

```
1. Q5 (stack — confirma auto-detect)
2. Q1 (mensagem-chave do projeto)
3. Q3+Q2 combinadas — tipo + audiência
4. Q10 (section foco — qual page/component)
5. Q6 OR Q7 — tom OR restrições perf

Se monorepo OR > 50 pages: pergunta extra sobre escopo.
```

### Input = PDF deck (2-3 perguntas)

```
1. Q1 — confirma narrative beats extraídos
2. Q2+Q4 combinadas — audiência + action (deck é pra quem? pra fazer o quê?)
3. Q6 — tom (slide deck pitch ≠ slide deck educational)
```

### Input = Notion/Tome URL (2-3 perguntas)

```
1. Q1 — confirma tema central
2. Q2 — audiência
3. Q10 — qual section/feature foco
```

### Input = Briefing texto livre (3-5 perguntas)

```
1. Q1 (mensagem-chave) — sempre
2. Q2 (audiência) — sempre
3. Q3 (tipo) — sempre
4. Q4 (action) — sempre
5. Q5 (stack) — sempre

Se ainda ambíguo após 5: Q6+Q10.
```

---

## 4. Frases pivot — quando Q&A travou

### Patrick respondeu vago

```
"Beleza, tu disse <resposta vaga>. Pra calibrar motion preciso mais específico:
[concretiza com 2 opções fechadas: 'tipo X ou tipo Y?']"
```

### Patrick contradiz info anterior

```
"Espera — tu disse <X> antes mas agora <Y>. Qual vale? Pode ter mudado o escopo OR tô interpretando errado."
```

### Patrick não sabe responder

```
"Tudo bem não saber. Vou propor com baseline conservador:
- Tom: minimal técnico (mais seguro)
- Tipo inferido: <X baseado em outros sinais>
Confirma OR me corrige?"
```

### Patrick quer pular Phase 0

```
"Phase 0 leve OK — vou inferir do <input> + propor direto.
Se proposta Phase 3 não bater, voltamos refinar. Tu pode pular discovery e ir direto pro lookup?"
```

---

## 5. Validação Phase 0 → Phase 1

Antes Phase 1 lookup, skill confirma session narrative card preenchido:

```
=== Session Narrative ===
Tipo: <preenchido>
Mensagem-chave: <preenchido>
Audiência: <preenchido>
Action primária: <preenchido OR "n/a se brand awareness puro">
Stack: <preenchido>
Tom motion: <preenchido>
Section foco: <preenchido>
Restrições: <preenchido OR "nenhuma específica">
Referências: <links se Patrick passou OR "nenhuma">
========================

Confirma? (sim → Phase 1 / corrige X → ajusto)
```

**Mínimo aceitável pra Phase 1:**
- Tipo (obrigatório)
- Audiência (obrigatório)
- Tom motion (obrigatório)
- Section foco (obrigatório)

Se algum mínimo não preenchido, Phase 0 NÃO encerra. Skill faz pergunta extra targeted.

---

## 6. Anti-patterns Phase 0

1. **Fazer 12 perguntas sempre:** vira ceremônia. Calibra por input type.
2. **Aceitar resposta vaga:** "tipo um motion premium" não é session narrative. Pivot pra concreto.
3. **Não confirmar inferências do auto-detect:** input rico (repo/Figma) extrai info — confirmar com Patrick antes prosseguir.
4. **Fazer Phase 0 longa em input simples:** URL + 1 frase já basta. Cortar.
5. **Não escutar pivot do Patrick:** se ele diz "skip Phase 0", respeita (modo `--quick`).
6. **Inferir tom motion sem perguntar:** sempre pergunta tom — isso muda easing semantics drasticamente.

---

## 7. Boundary com outras skills

- **`product-discovery-prd`** — discovery completo de produto (waves/personas/hipóteses). Phase 0 motion-design é discovery LIGHT focado em motion, não produto.
- **`ux-audit`** — audita fluxo existente. Phase 0 motion-design assume vai PROPOR motion novo.
- **`copy`** — descobre mensagem em texto. Phase 0 motion-design CONFIRMA mensagem-chave (não cria).

---

## 8. Manutenção desta ref

- ADD pergunta nova só quando 3+ Phase 0 falharam por falta dela
- Remover pergunta nunca usada em 30 dias
- Calibração Patrick Wave 1 testes — ajustar profundidade por input type baseado em tempo real
