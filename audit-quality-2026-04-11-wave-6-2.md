# Audit de Qualidade — Wave 6.2 (conteúdo/marketing)

**Data:** 2026-04-11
**Auditor:** Claude Opus 4.6 (leitura direta, padrão Wave 6.1)
**Escopo:** 10 skills de conteúdo e marketing
**Rubric aplicada:** `skills/prompt-engineer/rubric/system-prompt.yaml`
**Threshold produção:** 75/100
**Total linhas auditadas:** 2816 (média 282 linhas/skill — **35% mais longas que foundationais**)

---

## Resumo executivo

| # | Skill | Linhas | Origem | Score | Decisão |
|---|-------|--------|--------|-------|---------|
| 1 | **comunicacao-clientes** | 197 | native | **85.7** | OK |
| 2 | **seo** | 166 | native | **85.5** | OK |
| 3 | **ai-seo** | 399 | community | **83.6** | REFACTOR HEAVY |
| 4 | **free-tool-strategy** | 180 | community | **83.5** | OK |
| 5 | **product-marketing-context** | 242 | community | **83.4** | OK / REFACTOR LIGHT |
| 6 | **competitor-alternatives** | 257 | community | **82.6** | REFACTOR LIGHT |
| 7 | **launch-strategy** | 354 | community | **81.4** | REFACTOR HEAVY |
| 8 | **site-architecture** | 358 | community | **81.1** | REFACTOR HEAVY |
| 9 | **sales-enablement** | 350 | community | **81.0** | REFACTOR HEAVY |
| 10 | **copy** | 313 | native | **79.0** | REFACTOR LIGHT |

**Média ponderada:** 82.7/100 (**vs 83.7 Wave 6.1**, -1 pt)
**Acima do threshold 75:** 10/10 (100%)
**Tier produção alta (85+):** 2/10 (comunicacao-clientes, seo)
**Borderline (75-80):** 1/10 (copy)
**REFACTOR HEAVY urgente:** 4/10 (ai-seo, sales-enablement, launch-strategy, site-architecture)

**Nenhuma skill abaixo de 75.** Todas em produção, mas 7 das 10 precisam refactor.

---

## Achado crítico: duas origens coexistem

Detectei empiricamente dois padrões no arsenal marketing:

### Padrão A: native skillforge-arsenal (3 skills — copy, comunicacao-clientes, seo)

- ✅ Iron Law explícita
- ✅ Workflow numerado com markers ⚠️/⛔ BLOCKING
- ✅ Seção "Anti-Patterns" explícita
- ✅ Pre-Delivery Checklist
- ✅ Português brasileiro
- ✅ Keyword bombing PT-BR + EN na description
- ❌ **Tendem a ser mais longas** (copy tem 313 linhas — viola o limite)

### Padrão B: community imports (7 skills — ai-seo, sales-enablement, launch-strategy, site-architecture, competitor-alternatives, free-tool-strategy, product-marketing-context)

- ✅ "You are an expert in..." serve como R001 mas não tem Iron Law explícita
- ✅ Frameworks estruturados, tables, muitos exemplos inline
- ✅ Casos de uso reais citados (Notion, Superhuman, SavvyCal, TRMNL) — **R005 systematically 90+**
- ✅ References via markdown relative paths
- ❌ **Sem Iron Law, sem Anti-Patterns seção explícita** — R001/R006 ~80 não 95
- ❌ Sem confirmation gates explícitos
- ❌ Em inglês (não PT-BR — mas OK, public-facing)
- ❌ **Sistematicamente longas** — 5 de 7 acima de 350 linhas

**Conclusão:** não é um bug, é design. Community imports privilegiam cobertura ampla e exemplos reais; native skills privilegiam estrutura rígida e brevidade. Os scores convergem (~81-86) mas por motivos diferentes.

---

## Padrões cruzados (cruzando 10 audits)

### ⚠️ Padrão 1: U002 (attention budget) é sistematicamente crítico

**Community imports violam limite de 250 linhas em 5 de 7 casos:**
- ai-seo: 399 linhas (+60% over limit)
- site-architecture: 358 linhas
- launch-strategy: 354 linhas
- sales-enablement: 350 linhas
- competitor-alternatives: 257 linhas

**Native também tem 1 caso:**
- copy: 313 linhas (+25%)

**6 das 10 skills Wave 6.2 acima de 250 linhas.** Score médio U002 nessas 6: ~25/100. **Este é o finding estrutural mais grave do arsenal.**

**Recomendação:** aplicar o padrão da Wave 6.1.1 (skill-builder refactor) — mover seções grandes pra `references/`. Ganho consistente observado: 77.7 → ~87 (+9.3 pts).

### ⚠️ Padrão 2: Community imports não têm Anti-Patterns explícitos

**6 das 7 community imports não têm seção "Anti-Patterns" no estilo das foundationais.** Têm "Common Mistakes" mas misturadas, não em seção dedicada no topo. R006 score ~60 nessas.

**Impacto:** baixo semanticamente (Common Mistakes serve o mesmo propósito), alto em padronização.

**Recomendação:** se convertidas pra padrão native no refactor, adicionar seção Anti-Patterns explícita. Custo: 10-15 linhas por skill. Ganho R006: 60 → 85.

### ⚠️ Padrão 3: copy viola o próprio limite (ironia #2 do arsenal)

**copy = 313 linhas**, uma das skills foundationais do arsenal, ensina triagem rigorosa mas ela mesma é **25% maior que o limite**.

**Padrão familiar:** skill-builder também violava (302 linhas → 247 pós-Wave 6.1.1). copy é o próximo candidato ao mesmo tratamento.

**Recomendação:** extrair Phase 0-2 details + Framework Selection + Phase 3 Sweeps pra references/. Target: ~220 linhas. Ganho projetado: 79.0 → ~88.

### ⚠️ Padrão 4: comunicacao-clientes roda SEM acentuação portuguesa

Todo o arquivo (197 linhas) usa texto ASCII puro sem acentos (`nao`, `reacao`, `opcoes`, `comunicacao`). **Decisão intencional ou workaround de encoding antigo?**

Se foi workaround (como o hook v1 que teve bug cp1252), é tech debt corrigível. Se intencional (para evitar problemas de encoding em displays WhatsApp), mantém. **Precisa confirmação do Patrick.**

### ✅ Padrão 5: R005 (few-shot examples) é o ponto forte dos community imports

**Community imports sistematicamente fortes em R005** (85-98):
- launch-strategy (98) — cita Superhuman, Notion, SavvyCal, Reform, TRMNL com resultados específicos
- sales-enablement (95) — 10-12 slide framework, persona cards, deck patterns
- site-architecture (92) — ASCII trees, Mermaid diagrams, URL map tables
- ai-seo (92) — Query tables, content block patterns, Princeton GEO research

**Native skills são mais fracas em R005** (55-85):
- seo (55) — só "load references"
- copy (60) — templates mas sem exemplo real
- comunicacao-clientes (85) — Tipos 1-6 com exemplos inline

**Insight:** community imports ensinam por exemplo (R005 strong), native skills ensinam por estrutura (workflow strong). Híbrido seria ideal.

### ✅ Padrão 6: product-marketing-context é fundacional pra 6 outras skills

5 das 7 community imports começam com "Check for product marketing context first: If `.agents/product-marketing-context.md` exists..." Isso cria um **meta-pattern**: product-marketing-context é precondition pra ai-seo, sales-enablement, launch-strategy, site-architecture, competitor-alternatives, free-tool-strategy.

**Integração não documentada no maestro skill-catalog.** Vale adicionar como chain pattern: "se task de marketing, rodar product-marketing-context primeiro".

---

## Detalhes por skill

### 1. comunicacao-clientes (85.7) — 🥇 top do batch

**Pontos fortes:**
- R003 (92): 6 tipos de mensagem bem definidos (update, aprovação, escopo, bad-news, cobrança, reclamação)
- R004 (88): 5 confirmation gates explícitos (Type 4, Type 5, novos clientes)
- R006 (80): 8 anti-patterns com rationale
- Boundary clara com copy (L10-15)
- Filosofia explícita "Mensagem enviada > mensagem perfeita"

**Findings P1:**
- **Arquivo sem acentos portugueses** — tech debt? Confirmar com Patrick
- R005 (85): exemplos parciais por tipo, mas poderia ter 1 exemplo input→output completo inline
- C001 (60): ~10 caps (NUNCA, SEMPRE, NAO, ACAO)

**Decisão:** **OK** — apenas confirmar encoding.

---

### 2. seo (85.5) — 🥈

**Pontos fortes:**
- R001 (90): role claro "SEO Strategist v1"
- C001 (90): caps controlado, muitas siglas legítimas (EEAT, URL, CTA)
- R006 (88): tabela de anti-patterns muito detalhada (10 items com Por quê + Correto)
- U002 (95): 166 linhas — exemplar
- Progressive loading impecável: 11 references organizadas por domínio

**Findings P1:**
- **R005 (55) — fraco**: zero exemplo input→output, tudo via "Load references/X.md"
- R004 (75): when NOT to use presente, mas não cobre edge cases

**Decisão:** **OK** — adicionar 1 exemplo curto seria bom mas não urgente.

---

### 3. ai-seo (83.6)

**Pontos fortes:**
- R005 (92) — extraordinário: Query tables, content block patterns, Princeton GEO research numbers, AI bot list
- R003 (95): Three Pillars framework, Content Types table com citation shares
- R006 (90): 10 Common Mistakes muito específicas
- R004 (88): robots.txt handling, gated content, blocked bots

**Findings P0:**
- **U002 (15) — CRÍTICO**: **399 linhas**, 60% acima do limite. Maior violação do batch.

**Findings P1:**
- Sem Iron Law estilo native (R001 80 em vez de 95)
- Sem Anti-Patterns section dedicada (tem Common Mistakes disperso)

**Decisão:** **REFACTOR HEAVY** — extrair Three Pillars detail + AI Bot Access Check + Platform Ranking Factors + Schema Markup pra references/. Target: ~220 linhas. Ganho projetado: 83.6 → ~92 (maior absoluto do batch).

---

### 4. free-tool-strategy (83.5) — 🥇 do batch community

**Pontos fortes:**
- U002 (80): 180 linhas — único community import abaixo de 250
- R003 (88): ideação framework, validation, MVP scope, evaluation scorecard
- R005 (80): tool types table com exemplos reais

**Findings P1:**
- R006 (60): sem Anti-Patterns explícito
- R004 (75): cobertura OK mas sem edge cases fortes

**Decisão:** **OK** — mais curta e enxuta das community imports.

---

### 5. product-marketing-context (83.4)

**Pontos fortes:**
- R002 (98) — **maior R002 do batch**: template markdown completo explícito (12 sections, 50+ linhas de template estruturado)
- R005 (90): template serve como few-shot
- **Skill fundacional**: 5 outras marketing skills dependem de product-marketing-context.md

**Findings P1:**
- R006 (50): sem Anti-Patterns nem Common Mistakes, tem só "Tips"
- U002 (55): 242 linhas, borderline

**Decisão:** **OK / REFACTOR LIGHT** — adicionar seção Anti-Patterns ou Common Mistakes (10 linhas) resolve R006. Score projetado pós-fix: 86.

---

### 6. competitor-alternatives (82.6)

**Pontos fortes:**
- R003 (92): 4 page formats com URL patterns, keyword targeting
- R005 (88): format examples + data file structure
- Integração clara com sales-enablement (boundary explícito)

**Findings P1:**
- **U002 (45)**: 257 linhas — borderline acima do limite
- R006 (60): sem Anti-Patterns explícitos

**Decisão:** **REFACTOR LIGHT** — extrair detailed Research Process + Ongoing Updates pra references/. Target: ~210 linhas. Ganho projetado: 82.6 → ~87.

---

### 7. launch-strategy (81.4)

**Pontos fortes:**
- R005 (98) — **maior R005 do batch**: Superhuman case, Notion case, TRMNL case, SavvyCal case, Reform case com números específicos
- R003 (95): 5 phases, ORB framework, Product Hunt strategy
- R004 (82): pre-launch, launch day, post-launch, ongoing (4 estados)

**Findings P0:**
- **U002 (18) — CRÍTICO**: **354 linhas**, 40% acima do limite

**Findings P1:**
- R006 (60): sem Anti-Patterns explícitos (mas tem muita orientação preventiva inline)

**Decisão:** **REFACTOR HEAVY** — extrair Product Hunt Launch Strategy + Post-Launch Product Marketing + Ongoing Launch Strategy pra references/. Target: ~220 linhas. Ganho projetado: 81.4 → ~90.

---

### 8. site-architecture (81.1)

**Pontos fortes:**
- R005 (92): ASCII trees, Mermaid diagrams (dois tipos), URL map table, hub-and-spoke visual
- R002 (92): Output Format section muito estruturado (4 deliverables)
- R003 (95): page hierarchy, navigation types, URL patterns, internal linking rules

**Findings P0:**
- **U002 (18) — CRÍTICO**: **358 linhas**

**Findings P1:**
- R006 (60): Common Mistakes presente mas não seção Anti-Patterns global

**Decisão:** **REFACTOR HEAVY** — extrair Visual Sitemap (Mermaid) + Internal Linking Strategy + Output Format details pra references/. Target: ~220 linhas. Ganho projetado: 81.1 → ~89.

---

### 9. sales-enablement (81.0)

**Pontos fortes:**
- R005 (95): 10-12 slide framework explícito, persona cards, deck patterns, objection categories
- R003 (92): cobertura ampla (decks, one-pagers, ROI, demo scripts, playbooks, proposals, personas)
- R002 (92): output format por asset type (tabela estruturada)

**Findings P0:**
- **U002 (20) — CRÍTICO**: **350 linhas**

**Findings P1:**
- R006 (60): sem Anti-Patterns explícitos
- Múltiplos sub-tópicos (7 asset types) poderiam ser references separadas

**Decisão:** **REFACTOR HEAVY** — mover cada asset type (Sales Deck, One-Pagers, Objection, ROI, Demo, Case Study, Proposal, Playbook, Persona Cards) pra references/sales-enablement/*.md. Target: ~220 linhas. Ganho projetado: 81.0 → ~89.

---

### 10. copy (79.0) — borderline (ironia estrutural #2)

**Pontos fortes:**
- R003 (95): 8 modes, Phase 0-4 workflow detalhado, framework selection por Schwartz
- R004 (90): Phase 0 Gate 0.0 boundary check, --framework conflict handling, audiência mista
- R006 (85): 11 anti-patterns específicos
- Boundary com comunicacao-clientes explícita
- Schwartz 5 niveis com framework mapping

**Findings P0:**
- **U002 (30) — CRÍTICO**: **313 linhas** (25% acima). Segunda skill do arsenal a violar próprio limite (primeira foi skill-builder na Wave 6.1).
- **C001 (55)**: ~20 caps isoladas (NUNCA, PARAR, BLOQUEANTE, GATE, AVISAR, NAO, CTA, RSA, VoC, B2B, B2C)

**Findings P1:**
- R005 (60): templates sim, exemplo completo input→output falta

**Decisão:** **REFACTOR LIGHT** (prioritário) — extrair Phase 0 Audience Context tables + Phase 2 Framework Selection detail + Schwartz detailed sections pra references/. Target: ~230 linhas. Ganho projetado: 79.0 → ~88.

---

## Recomendações sistêmicas (não-bloqueantes)

### 1. Campanha "U002 Refactor" pro arsenal

**4 REFACTOR HEAVY + 2 REFACTOR LIGHT em Wave 6.2**, mais **1 REFACTOR LIGHT** (skill-builder) já feito em Wave 6.1.1. Padrão:

- **skill-builder (6.1.1)** — primeira aplicação, validou o approach
- **copy** — segundo candidato óbvio, native, mesmo problema
- **ai-seo, sales-enablement, launch-strategy, site-architecture** — community imports, refactor heavy
- **competitor-alternatives** — refactor light

**Esforço agregado estimado:** ~6h para os 6 refactors (skill-builder levou 30min, os demais são similares).

**Ganho agregado projetado:** score médio Wave 6.2 subiria de 82.7 → ~87.5 (+4.8 pts no batch).

### 2. Padronização entre native e community

Community imports faltam estrutura padrão skillforge (Iron Law, Anti-Patterns, PT-BR). **3 opções:**

- **Opção A**: manter como estão (são public-facing, inglês + estrutura frouxa é ok)
- **Opção B**: aplicar padrão native durante refactor (adiciona ~10 linhas cada, ganha +5 pts R001/R006)
- **Opção C**: criar novo padrão "community skill" documentado no skill-builder pra aceitar esse shape oficialmente

**Minha recomendação:** **Opção B** — padronizar durante o refactor que já vai acontecer. Single pass, maior ganho.

### 3. product-marketing-context como precondition pattern

5 skills marketing chechkam product-marketing-context.md no início. **Isso é uma chain de fato mas não documentada.** Vale adicionar ao maestro:

- Novo chain pattern: "marketing task → invocar product-marketing-context primeiro se .agents/ não existe"
- Anotar no skill-catalog.md

### 4. Confirmar encoding de comunicacao-clientes

Arquivo todo sem acentos em português. Tech debt ou decisão consciente? Se bug, fix trivial. Se decisão, documentar no SKILL.md.

---

## Projeção pós-refactors opcionais

| Skill | Atual | Pós-refactor | Condição |
|-------|-------|--------------|----------|
| copy | 79.0 | 88 | Refactor light + extração |
| ai-seo | 83.6 | 92 | Refactor heavy |
| launch-strategy | 81.4 | 90 | Refactor heavy |
| site-architecture | 81.1 | 89 | Refactor heavy |
| sales-enablement | 81.0 | 89 | Refactor heavy |
| competitor-alternatives | 82.6 | 87 | Refactor light |
| product-marketing-context | 83.4 | 86 | Adicionar anti-patterns |
| comunicacao-clientes | 85.7 | 87 | Encoding fix (se aplicável) |
| seo | 85.5 | 88 | Adicionar 1 exemplo |
| free-tool-strategy | 83.5 | 83.5 | — |

**Média atual:** 82.7
**Média projetada pós-refactors:** ~87.6 (+4.9 pts agregado)

---

## Comparação Wave 6.1 vs Wave 6.2

| Métrica | Wave 6.1 (foundationais) | Wave 6.2 (marketing) | Delta |
|---------|--------------------------|----------------------|-------|
| Score médio | 83.7 | 82.7 | -1.0 |
| Linhas médias | 209 | 282 | **+73 (+35%)** |
| Skills acima de 250 linhas | 2 (skill-builder, prompt-engineer) | **6** | **3x mais** |
| Tier produção alta (85+) | 3 (trident, sdd, reference-finder) | 2 (comunicacao-clientes, seo) | -1 |
| REFACTOR HEAVY | 0 | **4** | **+4** |
| REFACTOR LIGHT | 2 (geo-optimizer, skill-builder) | 3 (copy, competitor, product-marketing) | +1 |
| OK | 8 | 3 | -5 |

**Conclusão:** Wave 6.2 tem problema estrutural sistêmico (linhas) que Wave 6.1 não tinha. Community imports + copy precisam de uma "passada de extração" coordenada.

---

## Metodologia

Idêntica à Wave 6.1:
1. Leitura direta de cada SKILL.md pelo Opus (sem delegação Haiku — decisão Patrick)
2. Aplicação mental da rubric `system-prompt.yaml` com pesos ponderados
3. Cross-batch analysis pra detectar padrões sistêmicos
4. Relatório consolidado com findings por skill + padrões + recomendações

**Novo insight desta wave:** a existência de dois padrões (native vs community) não foi evidente na Wave 6.1 porque todas as foundationais são native. Ver 7 community imports em sequência revelou a diferença estrutural.
