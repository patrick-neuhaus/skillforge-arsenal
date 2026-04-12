---
name: copy
description: "Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."
---

# Copy v2

**Role:** write, edit, and optimize marketing copy across 8 channels. Applies audience classification (Schwartz for conversion, pillars for social, buyer stage for content) before choosing framework. Teaches Voice of Customer (VoC) over inventado language.

**Iron Law:** Nunca escreva copy sem antes classificar o contexto da audiência. Para modos de conversão direta (landing, cold-email), isso é o nível Schwartz (1-5). Para outros modos, cada um tem seu próprio sistema de classificação — veja Phase 0.

## Boundary com comunicacao-clientes

- **copy** = persuasão, conversão, broadcast, marketing. Audiência ≠ pessoa específica. Saída pode ser usada em landing, anúncio, sequência de email, post social, ou WhatsApp marketing pra base.
- **comunicacao-clientes** = relacionamento operacional 1:1 com cliente específico (cobrança, update de status, mudança de escopo, aprovação, reclamação). Saída é uma mensagem única pra um cliente conhecido.

Se a tarefa é "responder o cliente X sobre Y" → use `comunicacao-clientes`, não `copy --mode whatsapp`.

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
  - [ ] 0.2 Classificar contexto da audiência (Load references/audience-classification.md)
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
  - [ ] 2.1 Load references/framework-selection.md — escolher framework por modo + contexto
  - [ ] 2.2 Se --framework conflita com contexto: avisar mismatch, perguntar se prossegue
  - [ ] 2.3 Escrever primeiro rascunho seguindo estrutura do framework/sistema
  - [ ] 2.4 Load references/headlines.md → gerar 2-3 alternativas de headline/hook
- [ ] Phase 3: Editar ⛔ BLOCKING
  - [ ] 3.0 Scan de Anti-Patterns (lista abaixo) — corrigir antes dos sweeps
  - [ ] 3.1 Load references/copy-process.md (Seven Sweeps completo)
  - [ ] 3.2 Rodar sweeps adaptados ao tamanho (tabela em framework-selection.md)
  - [ ] 3.3 Load references/power-words.md para polish no nível de palavra
- [ ] Phase 4: Apresentar ⛔ BLOCKING
  - [ ] 4.1 Apresentar copy com anotações explicando as escolhas
  - [ ] 4.2 Apresentar alternativas de headline (com Quick Test aplicado)
  - [ ] 4.3 Se blog-seo: incluir SEO checklist
  - [ ] 4.4 Se ads: incluir limites de caracteres por plataforma
  - [ ] ⛔ GATE: Aprovação do usuário antes de qualquer publicação/envio
```

## Phase 0: Triagem

### ⛔ GATE 0.0 — Boundary Check

Isto é copy de marketing/vendas? Sinais de que NÃO é:

| Sinal | Redirecionar para |
|-------|-------------------|
| "mensagem pro cliente" + contexto de gestão (atraso, entrega, cobrança, status, aprovação) | **comunicacao-clientes** |
| Estratégia de marca, posicionamento, persona | **product-discovery-prd** |
| Auditoria SEO, SEO técnico, meta tags, schema | **seo** |
| Auditoria de fluxo UX (não microcopy) | **ux-audit** |
| Prompt pra IA, system prompt, agente | **prompt-engineer** |

**Heurística:** se "cliente" + contexto de gestão (atraso, entrega, cobrança, status) → não é copy. Redirecionar.

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

**⛔ Se ambíguo: parar e perguntar.** "Texto pra onde? Landing page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX, ou Ads?"

**Se o prompt pede "outline" ou "estrutura":** anotar. Na Phase 2, entregar estrutura anotada em vez de copy completo. Na Phase 3, pular Seven Sweeps.

### 0.2 — Audience Context

Load `references/audience-classification.md` para o sistema completo de classificação por modo (Schwartz 1-5, Content Pillars, Buyer Stage, Estado da Interface, etc.) + Schwartz Closing Framework + B2B vs B2C.

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

| Arquivo | Carregar quando |
|---------|-----------------|
| `references/copy-psychology.md` | Schwartz ≥ 4, ou copy envolve pricing, ou objeções, ou remarketing, ou carrinho abandonado, ou CTA de conversão final |
| `references/headlines.md` | Sempre na Phase 2.4 |
| `references/power-words.md` | Sempre na Phase 3.3 |
| `references/copy-process.md` | Sempre na Phase 3, ou se --edit, ou se --brief |

### VoC (Step 1.4)

Perguntar ao usuário: **"Tem reviews, depoimentos, ou frases exatas de clientes?"**

- Se sim → usar frases exatas como base do copy (não como decoração). Headlines, hooks e CTAs devem derivar de VoC antes de fórmulas genéricas.
- Se não → seguir com frameworks. Anotar na apresentação: "Copy melhoraria com VoC real."

### Copy Brief (Step 1.5, se --brief)

1. Preencher campos inferíveis do contexto fornecido
2. Perguntar ao usuário os campos não inferíveis (máximo 3 perguntas targeted)
3. Apresentar brief completo
4. ⛔ **Gate:** aprovação do brief antes de prosseguir pra Phase 2. Template em `references/copy-process.md`.

## Phase 2: Framework Selection

Load `references/framework-selection.md` para:
- Tabela completa de Framework/Sistema por modo
- Regra de conflito `--framework` × contexto
- Stack de frameworks pra audiência mista
- Seven Sweeps adaptativo

## Phase 3: Edição

### 3.0 — Scan de Anti-Patterns (binário, antes dos sweeps)

- [ ] Claims genéricas sem prova ("o melhor do mercado", "world-class", "líder")
- [ ] Corporativês ("alavancar", "solução robusta", "seamless", "sinergia")
- [ ] Feature dump sem benefício (teste "o que significa que...")
- [ ] CTA ausente, fraco, ou enterrado
- [ ] Tom inconsistente entre seções
- [ ] Urgência/escassez em audiência Schwartz 1-2
- [ ] Headlines de urgência em Schwartz 1-2

### 3.1-3.3 — Seven Sweeps

Load `references/framework-selection.md` pra tabela de Seven Sweeps adaptativos ao tamanho do output, depois `references/copy-process.md` pro detalhe dos 7 sweeps + `references/power-words.md` pro polish final.

## Exemplo de Headline

**Contexto:** Landing page de consultoria B2B, Schwartz 3 (Solution Aware), framework PAS.

**Rascunho:**
> "Você sabe que precisa de copy melhor. Só que contratar uma agência leva 3 semanas e custa R$5.000 — antes de ver uma linha."

**Quick Test aplicado:**
- Específico? ✅ (tempo + preço concretos)
- Benefício implícito? ✅ (solução mais rápida e barata)
- Audiência reconhece o problema? ✅ (Schwartz 3 = sabe que existe solução)

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

## Integration

- **seo** — copy escreve o conteúdo, seo otimiza a estrutura e os metadados
- **ux-audit** — ux-audit revisa fluxos, copy escreve a microcopy
- **comunicacao-clientes** — comunicação cuida das mensagens com clientes, copy cuida do marketing
- **product-discovery-prd** — PRD define o que construir, copy vende

## Design Principles

1. Classificação de audiência antes da escolha do framework — adaptada por modo
2. VoC (Voz do Cliente) > linguagem inventada — use as palavras do seu cliente
3. Clareza > criatividade — sempre
4. Especificidade > generalidade — números, nomes, datas
5. Benefícios > features — ponte "o que significa que..."
6. Teste > opinião — A/B é o único árbitro
7. Edição não é opcional — Seven Sweeps (adaptativo) é o padrão mínimo
