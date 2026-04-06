---
name: copy
description: "Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."
---

# Copy v2

IRON LAW: NUNCA escreva copy sem antes classificar o contexto da audiência. Para modos de conversão direta (landing, cold-email), isso é o nível Schwartz (1-5). Para outros modos, cada um tem seu próprio sistema de classificação — veja Phase 0.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | landing, social, email, cold-email, whatsapp, blog-seo, ux, ads | auto-detect |
| `--edit` | Revisar/editar copy existente (Seven Sweeps) | false |
| `--brief` | Gerar copy brief antes de escrever | false |
| `--framework <f>` | Forçar framework: aida, pas, bab, sb7, pastor, value-eq | auto por contexto |

## Workflow

```
Copy Progress:

- [ ] Phase 0: Triagem ⚠️ REQUIRED
  - [ ] ⛔ GATE 0.0: Isto é copy de marketing/vendas? (Se não → redirecionar)
  - [ ] 0.1 Identificar modo (tabela Mode Detection) — se ambíguo: ⛔ PARAR e perguntar
  - [ ] 0.2 Classificar contexto da audiência (tabela Audience Context por modo)
  - [ ] 0.3 Definir objetivo (converter? nutrir? educar? funcional?)
  - [ ] 0.4 Classificar: B2B ou B2C? (afeta tom, prova, CTA, template)
- [ ] Phase 1: Pesquisa ⚠️ REQUIRED
  - [ ] 1.1 Load references/foundations.md (sempre)
  - [ ] 1.2 Load reference do modo (tabela Reference Mapping)
  - [ ] 1.3 Load condicional: copy-psychology.md (ver triggers)
  - [ ] 1.4 VoC: Perguntar "Tem reviews, depoimentos, ou frases exatas de clientes?"
         Se sim → usar como BASE do copy. Se não → seguir com frameworks.
  - [ ] 1.5 Se --brief: gerar copy brief → ⛔ GATE: aprovação antes de Phase 2
- [ ] Phase 2: Escrever ⚠️ REQUIRED
  - [ ] 2.1 Selecionar framework/sistema pelo modo + contexto (tabela Framework Selection)
  - [ ] 2.2 Se --framework conflita com contexto: AVISAR mismatch, perguntar se prossegue
  - [ ] 2.3 Escrever primeiro rascunho seguindo estrutura do framework/sistema
  - [ ] 2.4 Load references/headlines.md → gerar 2-3 alternativas de headline/hook
         (de pelo menos 3 categorias diferentes: benefício, dor, prova social, curiosidade, etc.)
- [ ] Phase 3: Editar ⛔ BLOQUEANTE
  - [ ] 3.0 Scan de Anti-Patterns (lista abaixo) — corrigir antes dos sweeps
  - [ ] 3.1 Load references/copy-process.md (Seven Sweeps)
  - [ ] 3.2 Rodar sweeps ADAPTADOS ao tamanho (tabela Adaptive Sweeps)
  - [ ] 3.3 Load references/power-words.md para polish no nível de palavra
- [ ] Phase 4: Apresentar ⛔ BLOQUEANTE
  - [ ] 4.1 Apresentar copy com anotações explicando as escolhas
  - [ ] 4.2 Apresentar alternativas de headline (com Quick Test aplicado)
  - [ ] 4.3 Se blog-seo: incluir SEO checklist
  - [ ] 4.4 Se ads: incluir limites de caracteres por plataforma
  - [ ] ⛔ GATE: Aprovação do usuário antes de qualquer publicação/envio
```

---

## Phase 0: Triagem

### ⛔ GATE 0.0 — Boundary Check (ANTES de tudo)

Isto é copy de marketing/vendas? Sinais de que NÃO é:

| Sinal | Redirecionar para |
|-------|-------------------|
| "mensagem pro cliente" + contexto de gestão (atraso, entrega, cobrança, status, aprovação) | **comunicacao-clientes** |
| Estratégia de marca, posicionamento, persona | **product-discovery-prd** |
| Auditoria SEO, SEO técnico, meta tags, schema | **seo** |
| Auditoria de fluxo UX (não microcopy) | **ux-audit** |
| Prompt pra IA, system prompt, agente | **prompt-engineer** |

**Heurística:** Se "cliente" + contexto de gestão (atraso, entrega, cobrança, status) → NÃO é copy. Redirecionar.

Se validar que é copy → prosseguir para 0.1.

### 0.1 — Mode Detection

| Contexto no prompt | Modo |
|-------------------|------|
| "landing page", "página de vendas", "LP", "sales page" | landing |
| "post", "LinkedIn", "Instagram", "TikTok", "carrossel", "thread" | social |
| "email", "sequence", "nurture", "welcome" | email |
| "cold email", "outbound", "prospecção" | cold-email |
| "WhatsApp", "mensagem" (sem contexto de gestão), "follow-up" | whatsapp |
| "blog", "artigo", "SEO", "conteúdo" | blog-seo |
| "botão", "erro", "onboarding", "microcopy", "UX", "empty state" | ux |
| "anúncio", "ad", "Meta Ads", "Google Ads", "criativo", "RSA" | ads |

**⛔ Se ambíguo: PARAR e perguntar.** "Texto pra onde? Landing page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX, ou Ads?"

**Se o prompt pede "outline" ou "estrutura":** anotar. Na Phase 2, entregar estrutura anotada em vez de copy completo. Na Phase 3, pular Seven Sweeps (não se aplica a outlines).

### 0.2 — Audience Context (por modo)

A classificação de audiência depende do modo. Schwartz clássico (1-5) se aplica diretamente a **landing** e **cold-email**. Os outros modos usam sistemas próprios:

| Modo | Sistema de Classificação | O que perguntar/classificar |
|------|--------------------------|----------------------------|
| **landing** | Schwartz 1-5 | Nível de consciência da audiência |
| **cold-email** | Schwartz 1-5 | Nível de consciência do prospect |
| **social** | Content Pillar + Formato | Qual pilar? (Industry 30%, BTS 25%, Educational 25%, Personal 15%, Promotional 5%). Qual formato? (Story, Contrarian, Value, Carousel, Thread) |
| **email** (sequence) | Schwartz Progressivo | Schwartz de ENTRADA (ex: 2) e Schwartz de SAÍDA (ex: 4). Cada email progride a audiência um nível. |
| **whatsapp** | Estado do Lead | Frio? Morno? Quente? No-show? Follow-up? + técnica Chris Voss |
| **blog-seo** | Buyer Stage | Awareness, Consideration, Decision, Implementation (ver copy-blog-seo.md) |
| **ux** | Estado da Interface | Onboarding, Erro, Empty State, Sucesso, Confirmação Destrutiva (NÃO usar Schwartz) |
| **ads** | Tipo de Tráfego → Schwartz | Perguntar: "Tráfego frio ou remarketing?" Frio → Schwartz 1-2. Remarketing → 3-4. Carrinho → 5. |

### Schwartz 5 Níveis (quando aplicável)

| Nível | Nome | Sinal | Framework padrão | Alternativa |
|-------|------|-------|-----------------|-------------|
| 1 | Unaware | Não sabe que tem o problema | Story / SB7 | Epiphany Bridge |
| 2 | Problem Aware | Sabe do problema, não da solução | PAS | PASTOR |
| 3 | Solution Aware | Sabe que soluções existem, não conhece você | AIDA | FAB, 4Ps |
| 4 | Product Aware | Conhece você, ainda não comprou | Value Equation | BAB |
| 5 | Most Aware | Pronto pra comprar, só precisa de motivo | Closing Framework | — |

**Regra crítica:** urgência e escassez só funcionam no nível 4-5. Em níveis 1-2, afastam.

### Schwartz 5 — Closing Framework

Para audiência Most Aware (trial usado, carrinho abandonado, remarketing quente):

1. Lembrete do valor — o que já experimentaram/viram/receberam
2. Objeção final endereçada — a ÚNICA coisa que ainda impede
3. Incentivo — desconto, bônus, extensão de trial, upgrade
4. CTA direto + urgência real — prazo ou escassez verdadeira
5. Guarantee + risk reversal — transferir risco pro vendedor

Tom: assertivo, direto, sem rodeios. Não re-educar — o lead já sabe tudo.

### 0.4 — B2B vs B2C

| Dimensão | B2B | B2C |
|----------|-----|-----|
| Decisor | Comitê, múltiplos stakeholders | Individual ou família |
| Ciclo | Longo (semanas a meses) | Curto (minutos a dias) |
| Driver | ROI, eficiência, compliance, risk-to-career | Emoção, desejo, status |
| Tom | Profissional, baseado em dados | Conversacional, emocional |
| Prova | Cases com ROI, logos, TCO comparison | Reviews, testemunhos pessoais |
| CTA | "Agende demo", "Fale com vendas" | "Compre agora", "Comece grátis" |

---

## Phase 1: Reference Loading

### Reference Mapping (modo → arquivo)

| Modo | Arquivo | Notas |
|------|---------|-------|
| landing | `references/copy-landing.md` | Templates de LP, CTA formula, CRO |
| social | `references/copy-social.md` | Templates por plataforma, content pillars |
| email | `references/copy-email.md` | Welcome sequence, subject lines, benchmarks |
| cold-email | `references/copy-email.md` (seção Cold Email) | 9 frameworks, personalização, cadência |
| whatsapp | `references/copy-whatsapp.md` | Chris Voss, estrutura, erros fatais |
| blog-seo | `references/copy-blog-seo.md` | E-E-A-T, framework de artigo, buyer stage |
| ux | `references/copy-produto.md` | Checklists por componente, tom por estado |
| ads | `references/copy-anuncios.md` | 8 angles, waves, limites de plataforma |

**Sempre carregar:** `references/foundations.md`

### Triggers de Loading Condicional

| Arquivo | Carregar QUANDO |
|---------|-----------------|
| `references/copy-psychology.md` | Schwartz ≥ 4, OU copy envolve pricing, OU objeções, OU remarketing, OU carrinho abandonado, OU CTA de conversão final |
| `references/headlines.md` | Sempre na Phase 2.4 (gerar alternativas de headline) |
| `references/power-words.md` | Sempre na Phase 3.3 (polish) |
| `references/copy-process.md` | Sempre na Phase 3 (Seven Sweeps), OU se --edit, OU se --brief |

### VoC (Step 1.4)

Perguntar ao usuário: **"Tem reviews, depoimentos, ou frases exatas de clientes?"**

- Se sim → usar frases EXATAS como BASE do copy (não como decoração). Headlines, hooks e CTAs devem derivar de VoC antes de fórmulas genéricas.
- Se não → seguir com frameworks. Anotar na apresentação: "Copy melhoraria com VoC real."

### Copy Brief (Step 1.5, se --brief)

1. Preencher campos inferíveis do contexto fornecido
2. Perguntar ao usuário os campos não inferíveis (máximo 3 perguntas targeted)
3. Apresentar brief completo
4. **⛔ GATE: aprovação do brief ANTES de prosseguir pra Phase 2.**

Template do brief está em `references/copy-process.md`.

---

## Phase 2: Framework/System Selection

A seleção depende do modo. Nem todo modo usa frameworks de vendas.

| Modo | Sistema de Escrita | Detalhes |
|------|-------------------|----------|
| **landing** | Framework por Schwartz (tabela acima) | Combinar com template de LP de copy-landing.md. Framework = arco narrativo, template = estrutura de seções. Se B2B + ticket alto: Template Enterprise. |
| **cold-email** | Framework de Cold Email | 9 frameworks em copy-email.md: QVC, PPP, Star-Story-Solution, SCQ, ACCA, 3C's, Mouse Trap, Justin Michael, Vanilla Ice Cream. Escolher por perfil do destinatário. |
| **social** | Template de Post por formato | Story Post, Contrarian, Thread, Carousel (copy-social.md). Escolher pelo objetivo do post. |
| **email** (sequence) | Framework como arco geral | Framework principal pro arco (PAS, AIDA), mas cada email pode usar framework diferente conforme Schwartz progride de entrada → saída. |
| **whatsapp** | Estrutura de Mensagem + Chris Voss | Saudação → Contexto → Valor → Prova → CTA conversacional. Técnicas: Tactical Empathy, Mirroring, Labeling, Calibrated Questions, No-oriented questions. |
| **blog-seo** | Framework de Artigo SEO | 6 componentes de copy-blog-seo.md: H1, Introdução, Body H2/H3, Conteúdo Original, Internal Links, CTA. |
| **ux** | Checklist por Componente | Botões, Forms, Erros, Empty States, Success States (copy-produto.md). Tom adaptado ao estado da interface. |
| **ads** | Angles por Emoção-Alvo | 8 angles de copy-anuncios.md: Pain Point, Outcome, Social Proof, Curiosity, Comparison, Urgency, Identity, Contrarian. Respeitar limites de caracteres por plataforma. |

### Audiência Mista / Stack de Frameworks

Se a audiência cobre múltiplos níveis Schwartz (ex: sales page longa, remarketing misto):

1. Classificar Schwartz de ENTRADA e de SAÍDA
2. Usar Stack de Frameworks:
   - Seções 1-3: framework do nível de entrada (ex: PAS pra nível 2)
   - Seções 4-6: framework intermediário (ex: FAB/AIDA pra nível 3)
   - Seções 7+: framework do nível de saída (ex: Value Equation pra nível 4-5)

### Schwartz 3 — Comparação Competitiva

Para Schwartz 3 (Solution Aware), o lead está COMPARANDO alternativas. O copy DEVE incluir diferenciação: seção de comparação (vs. concorrentes), posicionamento claro, prova específica.

### Conflito --framework × Contexto

Se o usuário forçar um framework que não combina com o contexto:
> "PAS é otimizado pra [nível X], sua audiência é [nível Y]. [Framework recomendado] seria mais eficaz. Quer que eu use PAS mesmo assim ou prefere [recomendado]?"

Executar o que o usuário decidir, mas anotar o mismatch na apresentação.

---

## Phase 3: Edição

### 3.0 — Scan de Anti-Patterns

Antes dos Seven Sweeps, scan binário (tem ou não tem):

- [ ] Claims genéricas sem prova ("o melhor do mercado", "world-class", "líder")
- [ ] Corporativês ("alavancar", "solução robusta", "seamless", "sinergia")
- [ ] Feature dump sem benefício (testar "o que significa que...")
- [ ] CTA ausente, fraco, ou enterrado
- [ ] Tom inconsistente entre seções
- [ ] Urgência/escassez em audiência Schwartz 1-2
- [ ] Headlines de urgência em Schwartz 1-2

Corrigir anti-patterns ANTES de entrar nos sweeps.

### 3.1-3.3 — Seven Sweeps (Adaptativo)

| Tamanho do output | Sweeps a aplicar |
|-------------------|-----------------|
| **< 50 palavras** (WhatsApp, microcopy, ads curtos) | Sweep 1 (Clarity) + Sweep 3 (So What) |
| **50-200 palavras** (email, ads longos, posts curtos) | Sweeps 1, 2, 3, 5, 7 |
| **> 200 palavras** (LP, sales page, artigos) | Todos os 7 Sweeps |
| **Múltiplos outputs** (sequences, série de ads) | Full Sweeps nos 2 mais críticos. Sweeps 1-3 nos demais. |
| **--edit sem contexto de audiência** | Pular Schwartz. Aplicar sweeps relevantes ao tamanho. |

**Os 7 Sweeps:**

| # | Sweep | Pergunta-chave |
|---|-------|----------------|
| 1 | **Clarity** | Está claro sem esforço cognitivo? |
| 2 | **Voice & Tone** | Tom combina com a marca e o canal? |
| 3 | **So What** | Cada afirmação tem benefício explícito? |
| 4 | **Prove It** | Claims têm prova concreta? |
| 5 | **Specificity** | Números, prazos, detalhes específicos? |
| 6 | **Heightened Emotion** | Faz sentir? Usar: linguagem sensorial, antes/depois emocional, Life Force 8 (copy-psychology.md), Pratfall Effect. |
| 7 | **Zero Risk** | Removeu barreiras? Garantia, trust elements perto do CTA? |

---

## Anti-Patterns

- Escrever copy sem classificar contexto da audiência
- Usar urgência/escassez pra audiências Unaware (Schwartz 1-2)
- Corporativês ("alavancar", "solução robusta", "seamless")
- Feature dump sem benefício (teste "o que significa que...")
- CTA ausente ou enterrado no fim
- Tom inconsistente entre seções
- Claims genéricas sem prova ("o melhor do mercado", "world-class")
- Escrever pra todo mundo = não escrever pra ninguém
- Aplicar framework de vendas (AIDA, PAS) em modo UX (microcopy é funcionalidade)
- Forçar Schwartz em modos onde não se aplica (social orgânico, UX)
- Seven Sweeps completo em copy de 30 caracteres

## Quando NÃO usar

| Situação | Use em vez disso |
|-----------|-----------------|
| Comunicação com clientes (atraso, cobrança, status) | **comunicacao-clientes** |
| Estratégia de marca / posicionamento | **product-discovery-prd** |
| Auditoria SEO / SEO técnico | **seo** |
| Auditoria de fluxo UX (não microcopy) | **ux-audit** |
| Prompt engineering pra IA | **prompt-engineer** |

## Integrations

- **SEO** — copy escreve o conteúdo, seo otimiza a estrutura e os metadados
- **UX Audit** — ux-audit revisa fluxos, copy escreve a microcopy
- **Comunicação Clientes** — comunicação cuida das mensagens com clientes, copy cuida do marketing
- **Product Discovery PRD** — PRD define o que construir, copy vende

## Design Principles

1. Classificação de audiência ANTES da escolha do framework — adaptada por modo
2. VoC (Voz do Cliente) > linguagem inventada — use as palavras do seu cliente
3. Clareza > criatividade — sempre
4. Especificidade > generalidade — números, nomes, datas
5. Benefícios > features — ponte "o que significa que..."
6. Teste > opinião — A/B é o único árbitro
7. Edição não é opcional — Seven Sweeps (adaptativo) é o padrão mínimo
