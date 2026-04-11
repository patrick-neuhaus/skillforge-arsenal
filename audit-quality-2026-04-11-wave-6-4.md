# Audit de Qualidade — Wave 6.4 (auditoria + utils + docs)

**Data:** 2026-04-11
**Auditor:** Claude Opus 4.6 (leitura direta)
**Escopo:** 10 skills de auditoria, gestão, utilitários e documentos
**Rubric:** `skills/prompt-engineer/rubric/system-prompt.yaml`
**Total linhas auditadas:** 1919 (média **192 linhas/skill**)

---

## Resumo executivo

| # | Skill | Linhas | Score | Decisão |
|---|-------|--------|-------|---------|
| 🥇 | **schedule** | 135 | **91.0** | OK |
| 🥈 | **security-audit** | 222 | **89.5** | OK |
| 🥉 | **pdf** | 231 | **89.5** | OK |
| 4 | **product-discovery-prd** | 181 | **89.0** | OK |
| 5 | **xlsx** | 199 | **89.0** | OK |
| 6 | **vps-infra-audit** | 196 | **89.0** | OK |
| 7 | **ux-audit** | 205 | **88.5** | FIX ENCODING (como comunicacao-clientes) |
| 8 | **docx** | 175 | **88.5** | OK |
| 9 | **pptx** | 173 | **88.0** | OK |
| 10 | **tech-lead-pm** | 202 | **87.5** | OK |

**Média:** **88.8/100** — muito próxima da Wave 6.3 (89.0)
**Acima do threshold 75:** 10/10
**Tier produção alta (85+):** **10/10**
**REFACTOR estrutural (linhas):** 0/10

**Único fix identificado:** ux-audit está sem acentos portugueses (mesmo bug de encoding do comunicacao-clientes que fixei na Wave 6.2).

---

## Comparação final entre todas as waves

| Wave | Domínio | Média | Linhas médias | Refactors |
|------|---------|-------|---------------|-----------|
| **6.1** | Foundationais | 83.7 | 209 | 3/10 |
| **6.2** | Marketing/Content | 82.7 | 282 | 7/10 |
| **6.3** | Engenharia | **89.0** | **167** | 0/10 |
| **6.4** | Auditoria/Utils/Docs | **88.8** | 192 | 1/10 (encoding only) |

**Insight final:** o arsenal se divide em duas metades:
- **Marketing/Content + Foundationais (refactorados)**: médias 83-87, precisavam de extração sistemática
- **Engenharia + Auditoria/Utils**: médias 88-89, estruturalmente prontas

A diferença é origem (native vs community) + domínio (técnico vs conteúdo).

---

## Achados importantes

### ✅ Padrão 1: pipelines 3-agent são top do arsenal

**security-audit (89.5)** e **vps-infra-audit (89.0)** seguem o padrão trident (92.3) — pipelines de 3 agentes (Scanner/Verifier/Arbiter ou Collector/Analyzer/Architect). Características compartilhadas:

- Workflow com fases ⚠️ REQUIRED + ⛔ BLOCKING explícitos
- Output contracts entre agentes documentados em references/
- Max 15-25 findings (evita colapso em ruído)
- Gates de confirmação antes de aplicar qualquer mudança
- Re-inspeção independente entre agents

**Lição:** quando o problema suporta adversarial verification, pipelines 3-agent produzem as skills mais robustas.

### ✅ Padrão 2: Anthropic skills (pdf/docx/pptx/xlsx) são consistentemente boas

Scores entre 88.0 e 89.5. Características:

- R005 (95-92): exemplos inline de código (pypdf, openpyxl, PptxGenJS)
- R006 (90-95): anti-patterns em tabela com "Por quê/Faça isso"
- Quick Reference tables bem estruturadas
- Progressive loading via references/
- Licença proprietária documentada

**pdf (89.5) é o top das Anthropic skills** — mais anti-patterns (10+), checklists específicos, e IRON LAW mensurável (backup antes de destrutivo).

### ⚠️ Padrão 3: ux-audit está sem acentos portugueses

Arquivo de 205 linhas todo em ASCII puro (`nao`, `experiencia`, `usabilidade`, `interface`, `acessibilidade`). Mesmo bug de encoding que comunicacao-clientes tinha na Wave 6.2 (foi fixado).

**Causa provável:** sessões antigas onde o encoding cp1252 do Windows quebrou acentos durante edit/write.

**Fix:** mesmo tratamento aplicado em comunicacao-clientes — rewrite completo restaurando acentuação. Ganho: qualidade do texto em português sobe, nenhum efeito negativo.

### ✅ Padrão 4: schedule é a TOP do arsenal após foundationais

**schedule (91.0)** — terceira maior skill score do arsenal (após component-architect 90.5 e trident 92.3). Por quê:

- IRON LAW mensurável: "self-contained description, future runs have no session"
- U002 excelente (135 linhas, ~1400 tokens)
- R005 forte: exemplos cron patterns + template de prompt
- 4 options (--create/--recurring/--once/--list) sem overlap
- Boundaries claras com n8n-architect + tech-lead-pm

Skill enxuta, focada, bem-executada. Referência de como deve ser uma skill pequena.

### ⚠️ Padrão 5: tech-lead-pm é o único abaixo de 88

**tech-lead-pm (87.5)** — puxado pra baixo por:
- C001 (75): muitos CAPS em tabela de módulos
- R005 (82): templates em references/, não inline
- U002 (82): 202 linhas próximo do limite

Não urgente. Ficaria 90+ com redução de caps. Candidato a refactor light futuro opcional.

---

## Fix aplicado: ux-audit encoding

Mesmo processo do comunicacao-clientes da Wave 6.2. Arquivo reescrito mantendo estrutura/conteúdo, só adicionando acentuação portuguesa correta.

Score pós-fix projetado: 88.5 → 88.8 (ganho marginal, é qualidade textual).

---

## Decisão sistêmica Wave 6.4

**Zero refactors estruturais.** Uma correção de encoding (ux-audit).

Todas as 10 skills estão em tier produção alta (≥85). Ganhos potenciais de refactors adicionais são marginais (~1-2 pts) e o contexto deve ser priorizado pra continuity doc + commit final.

---

## Estado final do arsenal após Wave 6

| Categoria | Skills | Score médio | Limite violado | Tier alto |
|-----------|--------|-------------|----------------|-----------|
| Foundationais | 10 | 83.7 (→86.4 pós-refactor) | 2 (→0) | 3 |
| Marketing/Content | 10 | 82.7 (→87.5 pós-refactor) | 6 (→0) | 2 (→ várias) |
| Engenharia | 10 | 89.0 | 0 | 10 |
| Auditoria/Utils/Docs | 10 | 88.8 | 0 | 10 |
| **Total (40)** | — | **86.1** média | **8 antes / 0 depois** | ~25/40 |

**40 skills, 0 violações de limite após waves 6.1-6.4, média global ~86.**

---

## Metodologia

Mesma das waves anteriores. Leitura direta pelo Opus, aplicação mental da rubric com pesos ponderados, cross-batch analysis pra detectar padrões.

**Novidade Wave 6.4:** foi a wave mais rápida porque 9 de 10 skills estavam em bom estado. O único trabalho real foi o encoding fix.
