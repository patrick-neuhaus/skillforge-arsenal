# Audit de Qualidade — Wave 6.3 (engenharia)

**Data:** 2026-04-11
**Auditor:** Claude Opus 4.6 (leitura direta)
**Escopo:** 10 skills de engenharia
**Rubric aplicada:** `skills/prompt-engineer/rubric/system-prompt.yaml`
**Threshold produção:** 75/100
**Total linhas auditadas:** 1674 (média **167 linhas/skill** — 41% menor que Wave 6.2!)

---

## Resumo executivo

| # | Skill | Linhas | Score | Tier | Decisão |
|---|-------|--------|-------|------|---------|
| 🥇 | **component-architect** | 153 | **90.5** | ⭐⭐ produção alta | OK |
| 🥈 | **code-dedup-scanner** | 168 | **90.1** | ⭐⭐ | OK |
| 🥉 | **architecture-guard** | 171 | **89.8** | ⭐⭐ | OK |
| 4 | **react-patterns** | 140 | **89.8** | ⭐⭐ | OK |
| 5 | **cli-skill-wrapper** | 175 | **89.7** | ⭐ | OK |
| 6 | **ui-design-system** | 135 | **89.2** | ⭐ | OK |
| 7 | **lovable-router** | 151 | **88.8** | ⭐ | OK |
| 8 | **supabase-db-architect** | 202 | **87.6** | Produção | OK |
| 9 | **lovable-knowledge** | 161 | **87.6** | Produção | OK |
| 10 | **n8n-architect** | 218 | **87.2** | Produção | OK |

**Média ponderada:** **89.0/100** — maior de todas as waves
**Acima do threshold 75:** 10/10 (100%)
**Tier produção alta (85+):** **10/10 (100%)** — primeira wave com todas no topo
**REFACTOR LIGHT/HEAVY:** **0/10** — primeira wave com zero refactors necessários

---

## Comparação entre waves

| Métrica | Wave 6.1 (found) | Wave 6.2 (marketing) | Wave 6.3 (eng) |
|---------|------------------|----------------------|-----------------|
| Score médio | 83.7 | 82.7 | **89.0** |
| Linhas médias | 209 | 282 | **167** |
| Skills acima de 250 linhas | 2 | 6 | **0** |
| Tier produção alta (85+) | 3 | 2 | **10** |
| REFACTOR necessários | 3 | 7 | **0** |

**Wave 6.3 é significativamente superior às outras.** Insight: skills técnicas criadas por usuário técnico seguindo o padrão native skillforge tendem a ser mais enxutas e estruturalmente corretas. Marketing skills importadas trouxeram gordura; eng skills foram construídas sob medida.

---

## Achados importantes

### ✅ Padrão 1: eng skills como referência de qualidade do arsenal

**component-architect (90.5)** é o top score do arsenal INTEIRO — supera trident (92.3) ligeiramente quando comparamos só eng vs foundationais. Características que puxaram pra cima:
- Exemplo inline `❌ 11 props — too many` / `✅ Composed — each piece is simple` (R005 95)
- 7-prop rule concreto com threshold numérico
- Variant pattern com discriminated unions

**code-dedup-scanner (90.1)** também exemplar: match format completo com exemplo real de Button.tsx — cumprindo R005 que era fraco em outras skills.

### ✅ Padrão 2: Wave 6.3 skills respeitam limite de linhas universalmente

**Zero skills acima de 250 linhas.** n8n-architect é o maior com 218 — ainda dentro do threshold. Isso é exceção notável:
- Wave 6.1: 2 de 10 violavam
- Wave 6.2: 6 de 10 violavam
- Wave 6.3: **0 de 10**

Significa que o refactor sistemático das waves anteriores era de fato uma dívida técnica acumulada, não um problema inerente ao arsenal.

### ⚠️ Padrão 3: C001 (caps lock) é o único ponto fraco consistente

Pior scores em caps:
- **n8n-architect (65)** — NUNCA/REQUIRED/IRON LAW/GATE aparecem repetidos em tabelas
- **supabase-db-architect (60)** — siglas legítimas (JSONB, UUID, RLS) + NUNCA/USING(true) puxam
- **lovable-knowledge (80)** — NUNCA/NEVER/ALWAYS moderado

Ganho potencial de refactor de caps: ~1-2 pts por skill. **Não é prioritário** dado que todas já estão acima de 85.

### ⚠️ Padrão 4: R005 ainda é o critério mais fraco em média

Skills fracas em R005 (few-shot examples concretos):
- n8n-architect (75) — templates mencionados mas sem input→output
- ui-design-system (75) — mais instruções, poucos exemplos
- lovable-knowledge (75) — exemplos Good/Bad só em anti-patterns

Skills fortes em R005 (acima de 90):
- **component-architect (95)** — exemplo Card com 11 props vs composed
- **code-dedup-scanner (92)** — match format completo
- **cli-skill-wrapper (92)** — commands literais
- **supabase-db-architect (90)** — SQL concreto BOM/RUIM

**Padrão confirmado cross-waves:** R005 é sistematicamente o critério mais fraco. Skills que cumprem (component-architect, code-dedup-scanner) ficam no top.

### ✅ Padrão 5: Zero overlap real entre skills eng

Nenhuma candidata a merge/split. Boundaries impecáveis:
- **component-architect ↔ code-dedup-scanner**: "este escaneia o que existe, component-architect planeja o que criar" — documentado em ambas
- **architecture-guard ↔ react-patterns**: "shares Thin Client Iron Law. architecture-guard enforces, react-patterns teaches"
- **architecture-guard ↔ trident**: "Trident finds bugs, architecture-guard finds structural violations. Run both."
- **lovable-router ↔ lovable-knowledge ↔ supabase-db-architect**: chain clara documentada em todas

---

## Detalhes por skill (diagnóstico compacto)

### 1. component-architect (90.5) — 🥇

**Pontos fortes:**
- R005 (95): exemplo inline Good vs Bad de Card + Button
- 7-prop rule + variant pattern como fórmulas concretas
- Boundary explícita com code-dedup-scanner

**Findings:** nenhum P0/P1. Skill de referência.

---

### 2. code-dedup-scanner (90.1) — 🥈

**Pontos fortes:**
- R005 (92): match format completo com exemplo real (Button.tsx:1, 12 imports)
- Tabela Decision (REUSE/EXTEND/USE PACKAGE/EXTRACT/CREATE)

**Findings:** nenhum.

---

### 3. architecture-guard (89.8) — 🥉

**Pontos fortes:**
- Violation format estruturado com V001/V002 IDs
- Exemplo BAD vs GOOD behavior organization (árvore folders)
- 5 categorias de regras com severity P0/P1/P2

**Findings:** C001 (80) — algumas caps em contexto de IRON LAW.

---

### 4. react-patterns (89.8)

**Pontos fortes:**
- IRON LAW forte (Thin Client, Fat Server)
- Decision tree explícito (useState? useEffect? Browser API?)
- Tabela de findings com File/Issue/Pattern/Fix

**Findings:** nenhum significativo.

---

### 5. cli-skill-wrapper (89.7)

**Pontos fortes:**
- IRON LAW mensurável (CLI output < raw API bytes)
- Commands literais (tool search, tool get, tool list)
- Output Compression Strategies table

**Findings:** C001 moderado, R006 bom.

---

### 6. ui-design-system (89.2)

**Pontos fortes:**
- IRON LAW concreto (hex colors, fonts, não adjetivos)
- 7 sections de design.json explícitas
- `clamp()` rule pra fluid typography

**Findings:** R005 (75) — poderia ter exemplo de design.json completo inline.

---

### 7. lovable-router (88.8)

**Pontos fortes:**
- Classificação rápida + zona cinza explícita
- Decision matrix com 6 anti-patterns específicos
- U002 (92): 151 linhas, muito eficiente

**Findings:** R005 (70) — classificação serve como few-shot parcial.

---

### 8. supabase-db-architect (87.6)

**Pontos fortes:**
- R005 (90): SQL BOM vs RUIM inline de RLS policy
- Framework 5 camadas explícito
- 10 anti-patterns com rationale

**Findings:**
- **C001 (60)** — siglas legítimas (JSONB, UUID) + NUNCA/USING(true) puxam. Fix opcional: remover NUNCA onde não é IRON LAW.
- R004 (88): edge cases cobertos

**Decisão:** OK — C001 é fix de P2 opcional.

---

### 9. lovable-knowledge (87.6)

**Pontos fortes:**
- Boundary clara com product-discovery-prd
- Por-modo workflow (workspace/project/agents/review)
- 8 anti-patterns com Por quê/Correto

**Findings:**
- R005 (75) — exemplos Good/Bad só em anti-patterns, não inline no workflow

---

### 10. n8n-architect (87.2)

**Pontos fortes:**
- R006 (95): 13 anti-patterns com tabela Por quê/O que fazer
- 8 opções (--flow, --waves, --build, etc) sem overlap
- Wave development explícito

**Findings:**
- **C001 (65)** — maior penalty do batch. NUNCA, IRON LAW, REQUIRED aparecem repetidos em tabelas
- R005 (75) — muitos "Load references/..." sem exemplo inline
- U002 (75) — 218 linhas, próximo do limite

**Decisão:** OK — mas candidato a refactor futuro de caps. Não urgente.

---

## Decisão sistêmica: zero refactors na Wave 6.3

**Rationale:**
1. Todas as 10 skills ≥85 (tier produção alta)
2. Zero violações de limite de linhas
3. Ganhos potenciais de refactors (~1-2 pts em caps) são marginais
4. Contexto limitado deve priorizar Waves 6.4 e continuity doc
5. Padrões específicos (C001 em n8n/supabase) ficam documentados pra refactor futuro dedicado

**Opcional pra sessão futura (fora do escopo Wave 6.3):**
- n8n-architect refactor caps: 87.2 → ~89 (-10 min esforço)
- supabase-db-architect refactor caps: 87.6 → ~89 (-10 min)

---

## Projeção pós-refactors opcionais (fora de escopo)

| Skill | Atual | Projetado |
|-------|-------|-----------|
| n8n-architect | 87.2 | 89 |
| supabase-db-architect | 87.6 | 89 |
| lovable-knowledge | 87.6 | 89 |

**Média atual:** 89.0
**Média projetada pós-refactors opcionais:** ~89.6 (+0.6 pts)

Ganho marginal. **Wave 6.3 declarada completa sem refactors.**

---

## Comparação final waves 6.1 / 6.2 / 6.3

| Aspecto | Wave 6.1 | Wave 6.2 | Wave 6.3 |
|---------|----------|----------|----------|
| Média pré-refactor | 83.7 | 82.7 | **89.0** |
| Média pós-refactor | ~86.4 (proj) | ~87.5 (proj) | **89.0** (sem refactor) |
| Refactors necessários | 3 de 10 | 7 de 10 | **0 de 10** |
| Skills acima 85 | 3 | 2 | **10** |
| Skills violando limite | 2 | 6 | **0** |

Arsenal de engenharia é a parte **mais estruturalmente sã** do skillforge.
