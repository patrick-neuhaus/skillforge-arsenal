# Plano v3 — Validação via rubric `technical-plan.yaml`

**Data:** 2026-04-10
**Arquivo validado:** `C:\Users\Patrick Neuhaus\.claude\plans\fluffy-giggling-phoenix.md` (~700 linhas)
**Tipo:** technical-plan
**Validador:** prompt-engineer v3 (rubric aplicada manualmente — promptfoo precisa de ANTHROPIC_API_KEY configurada, ainda não foi configurada nesta máquina)
**Threshold:** 75/100

---

## Score por critério (rubric/technical-plan.yaml)

| ID | Critério | Score | Tier | Notas |
|----|----------|-------|------|-------|
| **R001** | DAG de dependências entre fases | **95** | Core | Cada wave declara pré-req explícito ("Pré-requisito: Wave X completa"). Diagrama no final. -5 porque Wave 4 declara depender de "1, 2, 2.5, 3" mas não explica por quê depende da 2.5 (poderia rodar antes). |
| **R002** | Reversibilidade | **70** | Core | Wave 2 (hook) tem rollback implícito (deletar arquivo), Wave 5 (validação retroativa) é não-destrutiva. Mas Wave 1.4 (refatorar prompt-engineer SKILL.md) e Wave 2.5 (resolver contradições CLAUDE.md) não declaram rollback explícito. -30. |
| **R003** | Critério de sucesso por fase | **85** | Core | A maioria das waves tem critério verificável. "ccinspect lint não retorna erros", "score >= 75", "git status clean". Wave 2.4 e 7.2 dependem de Patrick aprovar (subjetivo mas marcado como checkpoint). -15 porque Wave 6 sub-waves (audit qualidade) usam "decisão clara" como critério, vago. |
| **R004** | Chicken-and-egg lógico | **100** | Core | Resolvido na v3. Sub-fase 1.5 valida o plano APÓS rubric existir. Sub-fase 0A original já tinha apontado e v3 resolveu invertendo ordem. Zero loops lógicos detectados. |
| **R005** | Failure modes consistentes | **80** | Useful | Tabela consolidada de failure modes no fim do plano (7 cenários cobertos). Cada Wave crítica menciona seu próprio failure mode. -20 porque Wave 4, Wave 7 e algumas sub-waves de Wave 6 não declaram explicitamente. |
| **R006** | Decisões pra humano com formato comparável | **90** | Useful | A decisão sobre `--skill-prompt` foi apresentada como Opção A vs Opção B com recomendação justificada. Decisões fundamentais (D1-D4) têm rationale. -10 porque algumas escolhas pequenas dentro das waves não têm comparação. |
| **R007** | Estimativa de esforço | **75** | Useful | Cada wave tem estimativa (Alta/Média/Baixa). Tempo estimado pra Wave 1 (~4-6h). -25 porque Waves 2.5, 4, 5 não têm estimativa numérica. |
| **M001** | "O que NÃO está neste plano" explícito | **100** | Marginal | Seção dedicada com 9 itens. Excelente. |
| **M002** | Checkpoints humanos marcados | **100** | Marginal | Tabela explícita de checkpoints humanos obrigatórios + emoji ⛔ pra GATEs. Excelente. |

---

## Score agregado

**Cálculo ponderado** (peso × score, dividido pela soma dos pesos):

| Critério | Peso | Score | Contribuição |
|----------|------|-------|--------------|
| R001 | 100 | 95 | 9500 |
| R002 | 90 | 70 | 6300 |
| R003 | 95 | 85 | 8075 |
| R004 | 100 | 100 | 10000 |
| R005 | 70 | 80 | 5600 |
| R006 | 60 | 90 | 5400 |
| R007 | 50 | 75 | 3750 |
| M001 | 30 | 100 | 3000 |
| M002 | 40 | 100 | 4000 |
| **Soma** | **635** | — | **55625** |

**Score final: 55625 / 635 = 87.6/100 [Core tier]**

**Recomendação:** ✅ APROVADO (≥75)

---

## Comparação v2 → v3

| Métrica | Plano v2 | Plano v3 |
|---------|----------|----------|
| Score (rubric technical-plan) | ~60/100 (auto-audit manual estimou) | **87.6/100** |
| Findings P0 | 4 críticos | 0 críticos remanescentes |
| Findings P1 | 7 importantes | 4 importantes (reversibilidade parcial) |
| Linhas | 555 | ~700 (mais detalhado mas mais estruturado) |
| Chicken-and-egg lógicos | 1 (Fase 0 imaginada) | 0 |
| Reusa ferramentas existentes? | Não | Sim (ccinspect + promptfoo) |

**Subiu 27 pontos.** Confirma que rubric específica detecta problemas que checklist genérica não detectava.

---

## Findings P0 (corrige antes de fechar)

**Nenhum P0 remanescente.** Os 4 P0 do plano v2 foram resolvidos:
- F1 (chicken-and-egg) → resolvido na Sub-fase 0A (validar primeiro, criar guide depois)
- F2 (hook técnico) → pré-requisito explícito de ler docs
- F4 (all-negatives IL) → reframe positivo aplicado nas IL-1 a IL-7
- F8 (overlap --score vs --validate) → `--score` absorvido em `--validate`

---

## Findings P1 (corrige se possível)

### P1.1 — Wave 1.4 sem plano de rollback
**Critério:** R002 (Reversibilidade)
**Issue:** Refatorar `prompt-engineer/SKILL.md` não declara como reverter se quebrar.
**Fix sugerido:** Adicionar nota: "Antes de editar SKILL.md, criar branch git ou copy do arquivo. Se rubric retornar comportamento errado, restaurar do backup."
**Severity:** P1

### P1.2 — Wave 2.5 sem plano de rollback explícito
**Critério:** R002 (Reversibilidade)
**Issue:** Resolver as 3 contradições do CLAUDE.md atual envolve edits diretos sem backup mencionado.
**Fix sugerido:** "Antes de aplicar correções, copiar CLAUDE.md.bak. Se score cair em vez de subir, restaurar."
**Severity:** P1

### P1.3 — Wave 6 sub-waves com critério vago
**Critério:** R003 (Critério de sucesso verificável)
**Issue:** "Decisão clara (OK/refactor/merge/split/gap)" — quem decide o que é "claro"? Sem critério objetivo.
**Fix sugerido:** "Decisão clara = entrada em tabela do audit-quality-{wave}.md com: (a) classificação, (b) rationale 1 frase, (c) esforço estimado em horas. Se faltar qualquer um, não é clara."
**Severity:** P1

### P1.4 — Estimativas de tempo numéricas faltando
**Critério:** R007 (Estimativa de esforço)
**Issue:** Waves 2.5, 4, 5 não têm tempo estimado em horas/min, só dificuldade qualitativa.
**Fix sugerido:** Adicionar coluna "Tempo estimado" na tabela final do plano com horas/min por wave.
**Severity:** P1

---

## Findings P2 (tech debt)

### P2.1 — Wave 4 dependência declarada mas não justificada
**Critério:** R001 (DAG de dependências)
**Issue:** "Pré-requisito: Wave 1, 2, 2.5, 3 completas" mas Wave 4 (Phase 0 + solution-scout) tecnicamente poderia rodar logo após Wave 1.
**Fix:** Justificar a dependência ou mover Wave 4 pra logo após Wave 1.
**Severity:** P2

### P2.2 — Wave 7.2 (testes E2E) com 5 testes mas sem critério de aceitação per-test
**Critério:** R003
**Issue:** Cada teste tem "esperado" mas não tem "como medir" objetivamente.
**Fix:** Adicionar pra cada teste: "Como verificar: <comando ou observação concreta>".
**Severity:** P2

---

## Insight meta da validação

A validação foi feita aplicando a rubric `technical-plan.yaml` mentalmente — promptfoo não rodou de verdade porque `ANTHROPIC_API_KEY` não está configurada nesta máquina. **Implicação:** o setup do prompt-engineer v3 ainda precisa de uma sub-fase 1.4.5: "configurar API key promptfoo" pra que `--validate` rode end-to-end.

**Insight novo (gap pra documentar em `gaps/`):** a rubric `technical-plan.yaml` não tem critério "ferramentas requeridas estão configuradas no ambiente?". Plano que assume ferramentas configuradas pode quebrar na primeira execução. Vou criar gap.

**Output esperado quando promptfoo rodar de verdade:** mesmo formato deste documento, gerado automaticamente pelo `promptfoo eval`. Por enquanto, a versão manual serve como ground truth pra calibrar a rubric.

---

## Status final

**APROVADO COM RESSALVAS.** Score 87.6/100 (acima do threshold de 75). 4 findings P1 a corrigir antes da execução completa. 2 findings P2 como tech debt.

**Próximas ações:**
1. Aplicar P1.1 e P1.2 (notas de rollback) — pode ser feito imediatamente no plano file
2. Aplicar P1.3 (critério verificável de Wave 6) — refinar texto de "decisão clara"
3. Aplicar P1.4 (estimativas numéricas) — adicionar coluna de tempo
4. Documentar gap "ferramentas configuradas" em `gaps/`
5. Configurar ANTHROPIC_API_KEY pra promptfoo rodar de verdade (sub-fase 1.4.5 nova)
