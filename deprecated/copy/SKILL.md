---
name: copy
description: "Write, edit, audit, and optimize marketing copy across 9 channels. Modes: Landing Page, Sales Page, VSL, Social (Instagram/LinkedIn/TikTok/X/Threads/YouTube/Reddit), Email, Cold Email, WhatsApp/Telegram, Blog/SEO, Review Site (afiliado), UX/Microcopy, Ads (Meta/Google/TikTok/LinkedIn/Reddit/YouTube/Click-to-WhatsApp). Cross-canal sub-tipos: VSL (Jon Benson 8 parts), launch (PLF/Perfect Webinar/5-day challenge), saas-plg (activation/trial-to-paid/churn), webinar (Brunson Big Domino). Frameworks: AIDA, PAS, BAB, StoryBrand SB7, PASTOR, Hormozi Value Equation, Schwartz 5 awareness + 5 sophistication levels. Pais fundadores: Schwartz, Bencivenga, Collier, Bird, Caples, Forde, Masterson, Ogilvy, Halbert, Sugarman + Escola BR (Olivetto, Conrado, Erico, Sobral, Icaro). Psicologia: Cialdini 6+1, Pre-Suasion, Kahneman S1/S2, Ariely 5 vieses, Heath SUCCESs. Flags: --audit (analisa copy externo, nao escreve), --variants N (gera A/B), --locale br|us (forca cultura), --skip-anti-ai, --brief, --edit, --framework. Sweep #8 Anti-AI default ON. Compliance: FTC dark patterns, LGPD/GDPR opt-in, Anvisa saude, CVM financas. Use SEMPRE em: 'escreve copy', 'cria post', 'legenda pro Instagram', 'caption', 'texto de anuncio', 'copy pra Meta Ads', 'pagina de vendas', 'headline pra landing', 'email de vendas', 'sequencia de email', 'VSL', 'video de vendas', 'lancamento', 'PLF', 'Perfect Webinar', 'roteiro de webinar', 'review afiliado', 'review de produto', 'X review', 'is X worth it', 'best X', 'comparison page', 'X vs Y review', 'buying guide', 'extrai copy desse site', 'audita copy', 'analisa esse anuncio', 'compara essas 2 versions', 'gera 3 variants', 'A/B variants', 'melhora esse texto', 'reescreve', 'write copy', 'ad copy', 'sales page', 'email sequence'. NAO use pra mensagem 1:1 com cliente especifico → use comunicacao-clientes. NAO use pra pagina 'We vs Them' da PROPRIA marca → use competitor-alternatives. NAO use pra pitch deck/one-pager/objection handling → use sales-enablement. NAO use pra positioning/ICP → use product-marketing-context. NAO use pra GTM/Product Hunt → use launch-strategy."
---

# Copy v3

**Role:** write, edit, audit, and optimize marketing copy across 9 channels with cross-canal sub-types. Applies audience classification (Schwartz awareness 1-5 + sophistication 1-5 for conversion, pillars for social, buyer stage for content) before choosing framework. Teaches Voice of Customer (VoC) over inventado language. Default Sweep #8 anti-AI ON.

**Iron Law:** Nunca escreva copy sem antes classificar o contexto da audiencia. Para modos de conversao direta (landing, cold-email, review-site, ads), isso e o nivel Schwartz awareness (1-5) + estagio sophistication do mercado (1-5). Para outros modos, cada um tem seu proprio sistema de classificacao — veja Phase 0.

## Boundary com outras skills

| Skill | Quando redirecionar |
|---|---|
| **comunicacao-clientes** | 1:1 com cliente conhecido (cobranca, status, atraso, escopo, aprovacao) — copy = broadcast/marketing |
| **competitor-alternatives** | Pagina "We vs Them" da PROPRIA marca posicionando — review-site = review 3rd-party afiliado |
| **sales-enablement** | Pitch deck, one-pager, demo script, objection handling, talk track |
| **product-marketing-context** | Positioning, ICP, target audience, persona — copy USA o output |
| **launch-strategy** | Planejamento GTM, Product Hunt, waitlist — copy escreve sequencias DEPOIS |
| **ai-seo** | Otimizacao tecnica pra LLM citation (GEO/AEO) — copy escreve conteudo, encadeia em blog-seo |
| **ux-audit** | Audita fluxo UX completo — copy escreve microcopy especifico |
| **seo** | Auditoria SEO tecnica, keyword research — copy escreve conteudo |
| **prompt-engineer** | Prompt pra IA, system prompt — copy = marketing humano |
| **product-discovery-prd** | PRD, discovery, user stories — copy escreve depois |

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | landing, social, email, cold-email, whatsapp, blog-seo, review-site, ux, ads | auto-detect |
| `--audit` | Analisa copy externo (NAO escreve) — extrai patterns/frameworks/Schwartz nivel | false |
| `--variants <N>` | Gera N versoes A/B do mesmo copy | 1 |
| `--locale <l>` | br ou us — forca contexto cultural (default detecta pelo prompt) | auto |
| `--skip-anti-ai` | Pula Sweep #8 Anti-AI (use pra audit copy externo nao-IA) | false |
| `--edit` | Revisar/editar copy existente (Seven Sweeps) | false |
| `--brief` | Gerar copy brief antes de escrever | false |
| `--framework <f>` | Forcar framework: aida, pas, bab, sb7, pastor, value-eq | auto por contexto |

## Workflow

```
Copy Progress:

- [ ] Phase 0: Triagem ⚠️ REQUIRED
  - [ ] ⛔ GATE 0.0: Isto e copy de marketing/vendas? (Se nao → redirecionar — ver tabela Boundaries)
  - [ ] 0.1 Identificar modo (tabela Mode Detection) — se ambiguo: ⛔ PARAR e perguntar
  - [ ] 0.2 Classificar contexto da audiencia (Load references/audience-classification.md)
  - [ ] 0.3 Definir objetivo (converter? nutrir? educar? funcional? auditar?)
  - [ ] 0.4 Classificar: B2B ou B2C? (afeta tom, prova, CTA, template)
  - [ ] 0.5 Detectar sub-tipo cross-canal (VSL/launch/saas-plg/webinar) — opcional, ativa refs adicionais
  - [ ] 0.6 Detectar flag --audit → bypass Phase 2 (escrever) → Phase 2-A (analisar)
  - [ ] 0.7 Detectar locale (br/us) — afeta tom e referencias
- [ ] Phase 1: Pesquisa ⚠️ REQUIRED
  - [ ] 1.1 Load references/foundations.md (sempre)
  - [ ] 1.2 Load reference do modo (tabela Reference Mapping)
  - [ ] 1.3 Load condicional: copy-psychology.md (ver triggers)
  - [ ] 1.4 VoC: Perguntar "Tem reviews, depoimentos, ou frases exatas de clientes?"
         Se sim → usar como BASE do copy. Se nao → seguir com frameworks.
  - [ ] 1.5 Se --brief: gerar copy brief → ⛔ GATE: aprovacao antes de Phase 2
  - [ ] 1.6 Se sub-tipo cross-canal detectado: carregar refs adicionais (ex: launch → email + landing + social)
- [ ] Phase 2: Escrever ⚠️ REQUIRED (skip se --audit)
  - [ ] 2.1 Load references/framework-selection.md — escolher framework por modo + contexto
  - [ ] 2.2 Se --framework conflita com contexto: avisar mismatch, perguntar se prossegue
  - [ ] 2.3 Escrever primeiro rascunho seguindo estrutura do framework/sistema
  - [ ] 2.4 Load references/headlines.md → gerar 2-3 alternativas de headline/hook
  - [ ] 2.5 Se --variants N: gerar N versoes (mesmo angle ou angles diferentes)
- [ ] Phase 2-A: Auditar (apenas se --audit) ⚠️ REQUIRED
  - [ ] 2A.1 Identificar framework usado no copy externo (AIDA/PAS/SB7/etc)
  - [ ] 2A.2 Identificar nivel Schwartz awareness + sophistication
  - [ ] 2A.3 Identificar VoC vs linguagem inventada
  - [ ] 2A.4 Avaliar CRO 7 dimensoes (clareza/relevancia/proposta/friccao/distracao/confianca/urgencia)
  - [ ] 2A.5 Diagnose: o que funciona, o que nao, fixes especificos
- [ ] Phase 3: Editar ⛔ BLOCKING (skip se --audit)
  - [ ] 3.0 Scan de Anti-Patterns (lista abaixo) — corrigir antes dos sweeps
  - [ ] 3.1 Load references/copy-process.md (Seven Sweeps + #8 Anti-AI completo)
  - [ ] 3.2 Rodar sweeps adaptados ao tamanho (tabela em framework-selection.md)
  - [ ] 3.3 Sweep #8 Anti-AI default ON (skip so se --skip-anti-ai)
  - [ ] 3.4 Load references/power-words.md para polish no nivel de palavra
- [ ] Phase 4: Apresentar ⛔ BLOCKING
  - [ ] 4.1 Apresentar copy com anotacoes explicando as escolhas
  - [ ] 4.2 Apresentar alternativas de headline (com Quick Test aplicado)
  - [ ] 4.3 Se blog-seo OU review-site: incluir SEO checklist + Schema markup
  - [ ] 4.4 Se ads: incluir limites de caracteres por plataforma
  - [ ] 4.5 Se compliance aplicavel (saude/financas/dados): adicionar disclaimers
  - [ ] ⛔ GATE: Aprovacao do usuario antes de qualquer publicacao/envio
```

## Phase 0: Triagem

### ⛔ GATE 0.0 — Boundary Check

Isto e copy de marketing/vendas? Sinais de que NAO e (ver tabela Boundaries acima).

**Heuristica:** se "cliente" + contexto de gestao (atraso, entrega, cobranca, status) → nao e copy. Redirecionar.

### 0.1 — Mode Detection

| Contexto no prompt | Modo |
|-------------------|------|
| "landing page", "pagina de vendas", "LP", "sales page", "pricing", "about" | landing |
| "VSL", "video de vendas", "video sales letter", "roteiro de webinar" | landing (sub-tipo VSL) |
| "post", "LinkedIn", "Instagram", "TikTok", "carrossel", "thread", "X", "Twitter", "Threads", "Reddit", "YouTube Shorts", "reel" | social |
| "email", "sequence", "sequencia", "nurture", "welcome", "drip", "autoresponder", "newsletter" | email |
| "cold email", "outbound", "prospeccao", "frio", "outreach B2B" | cold-email |
| "WhatsApp", "Zap", "Telegram", "Click-to-WhatsApp", "drip whatsapp", "mensagem" (sem contexto de gestao) | whatsapp |
| "blog", "artigo", "SEO", "conteudo", "best of" (informativo), "vs" (informativo) | blog-seo |
| "review afiliado", "X review", "is X worth it", "vale a pena", "comparison X vs Y" (afiliado), "best X" (afiliado), "buying guide" | review-site |
| "botao", "CTA", "erro", "onboarding", "microcopy", "UX", "empty state", "push notification", "SMS", "AI consent" | ux |
| "anuncio", "ad", "Meta Ads", "Google Ads", "TikTok Ads", "LinkedIn Ads", "Reddit Ads", "YouTube TrueView", "Click-to-WhatsApp Ads", "criativo", "RSA", "PMax" | ads |

**⛔ Se ambiguo: parar e perguntar.** "Texto pra onde? Landing/VSL, Social, Email, Cold Email, WhatsApp, Blog/SEO, Review Site, UX, ou Ads?"

**Se prompt pede "outline" ou "estrutura":** anotar. Phase 2 entrega estrutura, Phase 3 pula sweeps.

### 0.2 — Audience Context

Load `references/audience-classification.md` para:
- Schwartz Awareness 1-5 (consciencia do leitor)
- Schwartz Sophistication 1-5 (saturacao do mercado)
- Sistema por modo (Content Pillars, Buyer Stage, Estado da Interface, etc)
- Tom BR vs US (locale)
- B2B vs B2C

### 0.5 — Sub-type Detection (cross-canal)

Detectar se intent ativa workflow cross-canal:

| Sub-tipo | Trigger | Refs ativados |
|---|---|---|
| **VSL** | "VSL", "video de vendas", "roteiro vendas vídeo" | copy-landing.md (VSL section) + copy-process.md |
| **launch** | "lancamento", "PLF", "Formula de Lancamento", "open cart", "5-day challenge", "high-ticket coaching application" | copy-email.md (Launch section) + copy-landing.md + copy-anuncios.md + copy-social.md |
| **saas-plg** | "SaaS PLG", "activation email", "trial-to-paid", "churn copy", "expansion email" | copy-email.md (SaaS section) + copy-landing.md (Pricing section) |
| **webinar** | "webinar", "Perfect Webinar", "Brunson", "Big Domino" | copy-landing.md (VSL/Brunson) + copy-process.md |

### 0.6 — --audit flag (analise copy externo)

Se `--audit` ativo, pulamos Phase 2 (escrever) e Phase 3 (editar). Vamos pra Phase 2-A (analisar).

Output: diagnose estruturado, NAO copy reescrito.

### 0.7 — Locale detection

| Sinal | Locale |
|---|---|
| Cliente PT-BR explicito, mercado BR, WhatsApp/Pix/CVM/Anvisa, "Brasil" | br |
| Cliente US, "USA", "American audience", "$" sem "R$" | us |
| Sem sinal claro | br (default — Patrick) |

Locale afeta:
- Tom (caloroso BR vs distante US)
- Hiperboles (aceitas BR vs evitadas US)
- Compliance (LGPD/Anvisa BR vs FTC US)
- Referencias culturais (BBB/futebol BR vs Star Wars US)
- Canais (WhatsApp dominante BR vs marginal US)

## Phase 1: Reference Loading

### Reference Mapping (modo → arquivo)

| Modo | Arquivo | Notas |
|------|---------|-------|
| landing | `references/copy-landing.md` | LP templates, CTA, CRO, VSL completo, SaaS Pricing |
| social | `references/copy-social.md` | TikTok hooks, LinkedIn document, Threads, Shorts, Reddit |
| email | `references/copy-email.md` | Sequences, Beehiiv/Settle/ARM, Apple MPP, SaaS, Launch |
| cold-email | `references/copy-email.md` (Cold Email) | 9 frameworks, personalizacao, cadencia |
| whatsapp | `references/copy-whatsapp.md` | Chris Voss, PIX, LGPD, Click-to-WA BR, Telegram, Kwai |
| blog-seo | `references/copy-blog-seo.md` | E-E-A-T, AI Overview, GEO, Pillar/Hub/Cluster |
| review-site | `references/copy-review-site.md` | Single review, comparison, best-of, buying guide, FTC disclosure, Schema |
| ux | `references/copy-produto.md` | Voice/tone matrices, AI features, error fluxos criticos, a11y, push/SMS |
| ads | `references/copy-anuncios.md` | Meta Advantage+, PMax, TikTok, Reddit, TrueView, LinkedIn TL |

**Sempre carregar:** `references/foundations.md`

### Triggers de Loading Condicional

| Arquivo | Carregar quando |
|---------|-----------------|
| `references/copy-psychology.md` | Schwartz ≥ 4, copy envolve pricing/objecoes/remarketing/carrinho/CTA conversao final |
| `references/headlines.md` | Sempre na Phase 2.4 |
| `references/power-words.md` | Sempre na Phase 3.4 |
| `references/copy-process.md` | Sempre na Phase 3, ou se --edit, ou se --brief, ou se --audit |

### VoC (Step 1.4)

Perguntar ao usuario: **"Tem reviews, depoimentos, ou frases exatas de clientes?"**

- Se sim → usar frases EXATAS como base do copy. Headlines, hooks e CTAs devem derivar de VoC antes de formulas genericas.
- Se nao → seguir com frameworks. Anotar: "Copy melhoraria com VoC real."

### Copy Brief (Step 1.5, se --brief)

1. Preencher campos inferiveis do contexto fornecido
2. Perguntar ao usuario campos nao inferiveis (max 3 perguntas targeted)
3. Apresentar brief completo
4. ⛔ Aprovacao do brief antes de prosseguir pra Phase 2. Template em `references/copy-process.md`.

## Phase 2: Framework Selection

Load `references/framework-selection.md` para:
- Tabela completa de Framework/Sistema por modo
- Regra de conflito `--framework` × contexto
- Stack de frameworks pra audiencia mista
- Seven Sweeps adaptativo

## Phase 2-A: Audit Mode (--audit)

Quando `--audit` ativo, pular Phase 2 (escrever) e Phase 3 (editar). Output:

```
## Audit Report: [tipo de copy] — [URL ou trecho]

### Framework detectado
[AIDA / PAS / SB7 / PASTOR / nenhum claro]

### Nivel Schwartz
- Awareness: [1-5] — [justificativa]
- Sophistication: [1-5] — [justificativa]

### VoC vs Linguagem inventada
[Mostra quotes e classifica]

### CRO 7 dimensoes (1-5 cada)
- Clareza: X/5
- Relevancia: X/5
- Proposta de Valor: X/5
- Friccao: X/5
- Distracao: X/5
- Confianca: X/5
- Urgencia: X/5

### Pontos fortes
[O que funciona]

### Problemas (priorizados)
1. [P0/P1/P2] — [issue] — [fix concreto]
2. ...

### Patterns extraiveis (swipe file)
[Hooks, transicoes, CTAs que vale guardar]
```

## Phase 3: Edicao

### 3.0 — Scan de Anti-Patterns (binario, antes dos sweeps)

- [ ] Claims genericas sem prova ("o melhor do mercado", "world-class", "lider")
- [ ] Corporativês ("alavancar", "solucao robusta", "seamless", "sinergia")
- [ ] Feature dump sem beneficio (teste "o que significa que...")
- [ ] CTA ausente, fraco, ou enterrado
- [ ] Tom inconsistente entre secoes
- [ ] Urgencia/escassez em audiencia Schwartz 1-2
- [ ] Promessa milagrosa em saude/financas (Anvisa/CVM violation)

### 3.1-3.4 — Seven Sweeps + #8 Anti-AI

Load `references/framework-selection.md` pra tabela de sweeps adaptativos ao tamanho. Depois `references/copy-process.md` pro detalhe dos 8 sweeps + `references/power-words.md` pro polish final.

**Sweep #8 Anti-AI = default ON.** Skip so com `--skip-anti-ai`.

## Exemplo de Headline

**Contexto:** Landing page de consultoria B2B, Schwartz 3 (Solution Aware), Sophistication 3 (mecanismo unico), framework PAS.

**Rascunho:**
> "Voce sabe que precisa de copy melhor. So que contratar uma agencia leva 3 semanas e custa R$5.000 — antes de ver uma linha. Aqui fazemos diferente: brief em 1h, primeira versao em 48h, com nosso framework de Schwartz + VoC."

**Quick Test aplicado:**
- Especifico? ✅ (tempo + preco concretos)
- Beneficio implicito? ✅ (solucao mais rapida e barata)
- Audiencia reconhece o problema? ✅ (Schwartz 3 = sabe que existe solucao)
- Mecanismo unico? ✅ (Sophistication 3 — "framework Schwartz + VoC")
- Sweep #8 Anti-AI? ✅ (sem em-dash overload, sem "in essence", sem "leverage")

## Anti-Patterns

- Escrever copy sem classificar contexto da audiencia
- Usar urgencia/escassez pra audiencias Unaware (Schwartz 1-2)
- Sophistication 1 headline em mercado sophistication 4 (parece raso)
- Corporativês ("alavancar", "solucao robusta", "seamless")
- Feature dump sem beneficio (teste "o que significa que...")
- CTA ausente ou enterrado no fim
- Tom inconsistente entre secoes
- Claims genericas sem prova ("o melhor do mercado", "world-class")
- Escrever pra todo mundo = nao escrever pra ninguem
- Aplicar framework de vendas (AIDA, PAS) em modo UX (microcopy e funcionalidade)
- Forcar Schwartz em modos onde nao se aplica (social organico, UX)
- Seven Sweeps completo em copy de 30 caracteres
- Skip Sweep #8 Anti-AI sem motivo (Claude smell e bug recorrente)
- Promessa milagrosa em saude/financas (Anvisa/CVM violation)
- Review afiliado sem disclosure FTC visivel
- Copy review sem cons (parece ad)

## Quando NAO usar (resumo das Boundaries)

| Situacao | Use em vez disso |
|----------|------------------|
| Comunicacao com clientes (atraso, cobranca, status) | **comunicacao-clientes** |
| "We vs Them" da PROPRIA marca | **competitor-alternatives** |
| Pitch deck, one-pager, demo script | **sales-enablement** |
| Estrategia de marca / positioning / ICP | **product-marketing-context** |
| GTM, Product Hunt, waitlist | **launch-strategy** |
| LLM citation / GEO / AEO | **ai-seo** |
| Auditoria SEO tecnica | **seo** |
| Auditoria de fluxo UX (nao microcopy) | **ux-audit** |
| Prompt engineering pra IA | **prompt-engineer** |
| PRD / discovery / user stories | **product-discovery-prd** |

## Integration

- **seo / ai-seo** — copy escreve conteudo, seo otimiza estrutura/metadados, ai-seo otimiza pra LLM citation
- **ux-audit** — ux-audit revisa fluxos, copy escreve a microcopy
- **comunicacao-clientes** — comunicacao cuida das mensagens com clientes, copy cuida do marketing
- **product-discovery-prd** — PRD define o que construir, copy vende
- **launch-strategy** — launch-strategy planeja GTM, copy escreve as sequencias
- **competitor-alternatives** — competitor-alternatives = SUA marca vs concorrente. copy review-site = review 3rd-party afiliado
- **sales-enablement** — pitch deck/one-pager. copy = marketing massa
- **product-marketing-context** — copy USA o output (positioning, ICP)

## Design Principles

1. Classificacao de audiencia antes da escolha do framework — adaptada por modo (Schwartz awareness + sophistication)
2. VoC (Voz do Cliente) > linguagem inventada — use as palavras do seu cliente
3. Clareza > criatividade — sempre
4. Especificidade > generalidade — numeros, nomes, datas (Bencivenga)
5. Beneficios > features — ponte "o que significa que..."
6. Teste > opiniao — A/B e o unico arbitro (Caples)
7. Edicao nao e opcional — Seven Sweeps + #8 Anti-AI (adaptativo) e o padrao minimo
8. Compliance (FTC/LGPD/Anvisa/CVM) e gate, nao opcional
9. BR e default contextual (100% clientes Patrick) — Tom BR aceito, Compliance BR sempre
10. Cross-canal sub-tipos (VSL/launch/saas-plg/webinar) ativam refs adicionais — orquestracao Phase 0