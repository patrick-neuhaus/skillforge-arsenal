# Audit de Qualidade — Wave 6.1 (foundationais)

**Data:** 2026-04-11
**Auditor:** Claude Opus 4.6 (leitura direta, sem delegação pra Haiku — decisão Patrick)
**Escopo:** 10 skills foundationais do arsenal
**Rubric aplicada:** `skills/prompt-engineer/rubric/system-prompt.yaml`
**Threshold produção:** 75/100
**Total linhas auditadas:** 2089 (média 209 linhas/skill)

---

## Resumo executivo

| # | Skill | Linhas | Score | Tier | Decisão |
|---|-------|--------|-------|------|---------|
| 1 | **trident** | 198 | **92.3** | ⭐ Produção alta | OK |
| 2 | **sdd** | 179 | **88.1** | ⭐ Produção alta | OK |
| 3 | **reference-finder** | 221 | **85.9** | Produção | OK |
| 4 | **context-tree** | 185 | **83.7** | Produção | OK / REFACTOR LIGHT |
| 5 | **maestro** | 207 | **83.2** | Produção | OK |
| 6 | **context-guardian** | 166 | **83.2** | Produção | OK |
| 7 | **pattern-importer** | 201 | **82.4** | Produção | OK |
| 8 | **prompt-engineer** | 282 | **82.1** | Produção | OK / REFACTOR LIGHT |
| 9 | **geo-optimizer** | 148 | **78.1** | Produção (borderline) | REFACTOR LIGHT |
| 10 | **skill-builder** | 302 | **77.7** | Produção (borderline) | REFACTOR LIGHT |

**Média ponderada:** 83.7/100
**Acima do threshold 75:** 10/10 (100%)
**Tier produção alta (85+):** 3/10 (trident, sdd, reference-finder)
**Borderline (75-80):** 2/10 (geo-optimizer, skill-builder)

**Nenhuma skill em tier crítico (<50).** **Nenhuma pede DEPRECATE, MERGE, ou SPLIT.**

---

## Padrões cruzados (o que aprendi auditando 10 de uma vez)

### ⚠️ Padrão 1: R005 (few-shot examples) é sistematicamente fraco

**7 das 10 skills** têm templates de output mas **faltam exemplos input→output concretos**:
- context-tree: template de entry format, zero exemplo real de "user diz X → skill cria arquivo Y"
- maestro: templates Single Skill / Multi-Skill Chain abstratos, sem execução real
- geo-optimizer: estrutura de rewrite, exemplo real só em `references/examples.md`
- skill-builder: exemplos em `references/writing-guide.md`, nada inline
- pattern-importer: pattern document template, zero exemplo de pattern extraído
- context-guardian: templates Green/Yellow/Red são exemplos de output, mas não input→output completo
- prompt-engineer: TEM exemplo Good vs Bad (único que cumpre R005 inline, +10 pts)

**Impacto:** rubric diz "1 exemplo concreto = score 100, template abstrato = 60". Média puxa pra baixo.

**Recomendação de sistema:** adicionar à checklist do skill-builder uma regra "cada SKILL.md deve ter ao menos 1 bloco `## Example` com user intent → skill output real, não abstrato". Isso vira critério de validação estrutural.

### ⚠️ Padrão 2: C001 (caps lock) varia muito e não há padrão

- **Melhores (80-95):** context-tree, pattern-importer, maestro, sdd
- **Piores (45-60):** skill-builder (45), geo-optimizer (55), prompt-engineer (55)

**Insight empírico:** os piores em CAPS são justamente as skills *meta* (sobre skills/prompts). Essas lidam com muitos termos de arte (IRON LAW, BLOCKING, REQUIRED, SKILL.md, GEO) que viram caps por hábito.

**Recomendação:** padronizar "termos de arte" como **negrito** em vez de CAPS em SKILL.md foundationais. IRON LAW → **Iron Law**, BLOCKING → **blocking**, etc. Exceção: só REQUIRED/GATE marcadores de workflow podem ser CAPS.

### ⚠️ Padrão 3: skill-builder viola o próprio limite de 250 linhas

**302 linhas quando ensina <250.** Documentado como tech debt conhecido na própria skill (anti-pattern L254: "SKILL.md over 250 lines → move content to references/").

**Não é falso positivo — é ironia real.** U002 score 35 pra skill-builder é o pior do batch, puxa o score total pra borderline 77.7.

**Recomendação:** mover Step 0 (8 questões) pra `references/step-0-pre-build-research.md`. SKILL.md retém só o pointer "Load references/step-0.md". Corta ~80 linhas. Score U002 saltaria de 35 → 80.

### ⚠️ Padrão 4: geo-optimizer não tem role/contexto explícito

**Único que viola R001 (peso 100) no batch.** Começa direto com IRON LAW sem declarar "Who is this skill, what domain".

**Outras skills cumprem:** "maestro — Skill Orchestrator", "trident — Three-pronged pipeline", "sdd — Spec Driven Development", etc.

**geo-optimizer corpo L6:** `# GEO Optimizer — Generative Engine Optimization` — isso é título, não role/contexto.

**Fix:** adicionar 2 linhas antes do IRON LAW: "geo-optimizer otimiza descriptions de skills (não de prompts) pra serem descobertas por agentes de IA. Contexto: trabalha com keyword bombing PT-BR+EN, máximo 1024 chars, GEO (Generative Engine Optimization)."

### ✅ Padrão 5: Boundaries entre skills são excelentes

**Zero overlap real detectado.** Cada skill tem "When NOT to use" + "Boundary table" claros:
- skill-builder ↔ prompt-engineer: v3 resolve overlap via tabela explícita (L287-296 skill-builder)
- context-tree ↔ context-guardian: knowledge (persistente) vs window (runtime) — 5% overlap apenas
- reference-finder ↔ pattern-importer: teoria vs prática, documentado em ambas
- trident ↔ security-audit ↔ architecture-guard: composable, documentado em trident L180-186

**Nenhum merge/split candidate.** Foundationais estão bem fatoradas.

### ✅ Padrão 6: Prefilling deprecated (C002) = 100 pra todas

Nenhuma skill usa padrão legacy "Assistant:" ou `<assistant>` tags. Todas limpas pra Claude 4.x.

---

## Detalhes por skill

### 1. trident (92.3) — ⭐ referência de qualidade

**Pontos fortes:**
- R001 (100) + R002 (95) + R003 (95): role, formato, instruções impecáveis
- R006 (100): 6 anti-patterns + 6 design principles em forma positiva
- Exemplo de disambiguation (adicionado na Wave 5) preenche R005 (95)
- 3-agent pipeline com prompts templates separados (Scanner/Verifier/Arbiter)
- Shared output contract (`bug_id` schema) garante consistência entre fases

**Findings P1:**
- C001 (75): ~15 CAPS, alguns são acrônimos de domínio (CONFIRMED, REJECTED, SUSPICIOUS são tiers válidos). Aceitável.

**Decisão:** **OK** — nada a fazer.

---

### 2. sdd (88.1) — ⭐ referência de workflow

**Pontos fortes:**
- R003 (93): phases 1.1-4.2 muito específicas
- R006 (85): 6 anti-patterns "problem → consequence" em forma positiva
- PRD format + Spec format inline (não precisa load references)
- Integração com 7 outras skills sem overlap

**Findings P1:**
- R004 (80): não cobre cenário "user rejeita PRD no gate" — qual o fluxo? Volta pra research? Refina?
- Rollback strategy mencionada em spec.md template mas não detalhada no workflow

**Decisão:** **OK** — P1 é nice-to-have.

---

### 3. reference-finder (85.9)

**Pontos fortes:**
- R004 (85): edge cases de `--solution-scout` bem documentados (nenhum/50+/local/timeout)
- R005 (88): exemplo concreto "Patrick: 'tem skill pra validar prompts?'" (único com user intent real!)
- Templates de output obrigatórios (tabela com match score)

**Findings P1:**
- C001 (70): ~12 CAPS (MOC repetido, REUSE/EXTEND/BUILD, NEVER)
- U002 (75): 221 linhas borderline, poderia extrair tech-catalog.md pra lazy load

**Decisão:** **OK** — refactor de C001 opcional.

---

### 4. context-tree (83.7)

**Pontos fortes:**
- R001 (100): role explícito perfeito
- C001 (90): só ~5 CAPS, bem controlado
- U002 (95): 185 linhas / ~1800 tokens — excelente eficiência
- 7 operations sem overlap

**Findings P1:**
- R005 (45): **CRÍTICO no próprio critério** — zero exemplo input→output concreto. Template de entry format existe mas nenhum "user diz X → context-tree cria Y"
- R004 (65): só 1 gate (--prune). Não cobre --add com duplicata detectada, --connect com 0 conexões, --query em domínio vazio

**Decisão:** **REFACTOR LIGHT** — adicionar 1 exemplo completo (~15 linhas) + documentar edge cases de --add/--connect/--query.

---

### 5. maestro (83.2)

**Pontos fortes:**
- R006 (85): 6 anti-patterns positivos
- Tabela Intent Pattern → Category → Primary Skills bem estruturada (L48-80)
- IRON LAW forte ("NEVER recommend a skill without reading its SKILL.md first")

**Findings P1:**
- R004 (70): não cobre intent totalmente fora de escopo, user profile mismatch, nenhuma skill encontrada
- R005 (60): templates Single/Multi-Chain abstratos, sem exemplo real de routing completo
- Classificação de intents ambíguos (cross-domain paralelo vs sequencial) não coberta

**Decisão:** **OK** — findings são P2, não bloqueiam uso.

---

### 6. context-guardian (83.2)

**Pontos fortes:**
- R006 (85): 6 anti-patterns positivos
- Templates Green/Yellow/Red são quase-exemplos (R005 68)
- 3 options (--check, --handoff, --budget) enxutas

**Findings P1:**
- R004 (72): não cobre "usuário não pode /clear agora" (stakeholder esperando)
- R002 (85): output de `--check` é exemplo textual, não schema normativo
- Integração com maestro: maestro pode invocar mas não está documentado quando (ex: "a cada 3+ skills na chain")

**Decisão:** **OK** — adicionar 1 edge case seria bom mas não obrigatório.

---

### 7. pattern-importer (82.4)

**Pontos fortes:**
- IRON LAW forte (.tmp cleanup) com gate explícito
- R006 (88): 6 anti-patterns bem estruturados
- C001 (85): caps controlado
- U002 (88): 201 linhas ~1900 tokens OK

**Findings P1:**
- R005 (58): pattern document template existe mas zero exemplo real de pattern extraído ("clonei X, achei padrão Y, apliquei em Z")
- R004 (78): não cobre network failures, repo deletado, permission errors, branch inexistente
- Integration com SDD mencionada na description mas não detalhada no body

**Decisão:** **OK** — nice-to-have refactor.

---

### 8. prompt-engineer (82.1)

**Pontos fortes:**
- R002 (95): output format muito estruturado, --validate workflow formal, 4 rubrics YAML
- R005 (90): **único do batch com exemplo Good vs Bad inline** (L226-253) — referência de como fazer
- Boundary table explícita com skill-builder (L275-282)
- Anti-drift rule documentada (L117-127)

**Findings P1:**
- C001 (55): ~12 CAPS (IRON LAW, NEVER, MUST, NUNCA, JAMAIS, DEPRECATED) — ironia pra skill que ensina calibração
- U002 (60): 282 linhas borderline 3000 tokens. Poderia extrair seção "Integration" + "Anti-Patterns" pra references/
- R004 (78): edge cases dispersos em 3 seções, não consolidados

**Decisão:** **OK / REFACTOR LIGHT** — caps é P1 fácil. Extração P2.

**Ironia documentada:** a skill que criou a rubric usada pra auditar tem C001 55 — pior que context-tree (90). Prompt-engineer deveria aplicar seu próprio remédio.

---

### 9. geo-optimizer (78.1) — borderline

**Pontos fortes:**
- R003 (90): workflow numerado, scoring table explícita
- Workflow 3 steps com gate explícito
- Boundary com skill-builder e prompt-engineer documentado

**Findings P1 (múltiplos):**
- **R001 (65) — VIOLAÇÃO**: não tem role/contexto header explícito. Começa direto com IRON LAW (L6 é título, não contexto). Único do batch que viola R001.
- C001 (55): ~15 CAPS (NEVER, GATE, BLOCKING, REQUIRED, NÃO, SEMPRE, GEO múltiplos, PT-BR, EN)
- R004 (60): sem handling pra description >1024 chars após rewrite, sem abort se step 3 falha, sem skip condition se score já alto

**Decisão:** **REFACTOR LIGHT** — adicionar role header (2 linhas) + reduzir caps + adicionar 3 edge cases. Estima 45 min. Score esperado pós-fix: ~85.

---

### 10. skill-builder (77.7) — borderline

**Pontos fortes:**
- R003 (92): question-style excelente, 7 steps + Step 0 com 8 questões
- R004 (90): Step 0 cobre edge cases de decisão de criação
- Handoff explícito com prompt-engineer (v3, L266-296)
- Boundary table muito detalhada (L287-296)

**Findings P0 (bloqueador estrutural):**
- **U002 (35) — CRÍTICO**: 302 linhas / ~3500+ tokens, VIOLA o próprio limite de 250 linhas. Ironia documentada como anti-pattern na própria skill (L254). Puxa score total pra borderline.
- **C001 (45)**: 60+ CAPS (SKILL x28, REQUIRED x9, IRON/LAW x8, BLOCKING x6). Pior do batch.

**Findings P1:**
- R005 (70): exemplos estão em `references/`, não inline. Skill meta não demonstra padrão que ensina
- R006 (75): anti-patterns em forma mista ("No workflow", "Copy-pasted docs") — nem sempre positivos

**Decisão:** **REFACTOR LIGHT** (prioritário) — mover Step 0 pra `references/step-0-pre-build-research.md`, corta ~80 linhas. Reduzir caps (substituir SKILL→skill, IRON LAW→Iron Law). Estima 1h. Score esperado pós-fix: ~87.

---

## Recomendações sistêmicas (não-bloqueantes)

### 1. Nova regra estrutural pra skills futuras
**Adicionar ao skill-builder Pre-Delivery Checklist:**
> `- [ ] SKILL.md tem seção "## Example" com pelo menos 1 user intent real → skill output real, não abstrato`

**Por quê:** 7 das 10 skills têm R005 <70 porque usam templates em vez de exemplos concretos. Adicionar à checklist força correção.

### 2. Padronização de caps lock em skills meta
**Convenção proposta:**
- `**Iron Law**` (negrito, não CAPS)
- `**blocking**`, `**required**` (negrito)
- `⛔ GATE:` (CAPS só no marcador, não no corpo)
- Termos de arte (SKILL.md, GEO, MOC) usar como está (acrônimos legítimos)

**Aplicar em:** skill-builder, prompt-engineer, geo-optimizer primeiro. Depois propagar.

### 3. Refactor prioritário: skill-builder move Step 0 pra references/
**Esforço:** ~30 min
**Ganho esperado:** score 77.7 → 85+
**Side effect positivo:** skill-builder deixa de violar próprio limite (para de ser piada)

---

## Próximas Waves (recomendação Patrick)

**Wave 6.1 terminada.** Todas as 10 foundationais em tier produção (todas ≥75). Nenhum refactor urgente. 3 refactors opcionais documentados.

**Wave 6.2** (30 skills de conteúdo/marketing + engenharia + auditoria, 10 por sub-wave): continuar na próxima sessão fresh. Critério calibrado: usar mesmo processo (Opus lê direto, aplica rubric, gera relatório consolidado).

**Fix aplicativo mais urgente (fora de Wave 6):**
- **skill-builder refactor light** (30 min) — maior ROI: vira de 77.7 para 85+, remove ironia estrutural, serve de referência melhor pra skills futuras.

**Fix aplicativo opcional:**
- **geo-optimizer refactor light** (45 min) — adiciona role header, corrige R001, sobe de 78.1 pra 85+.

---

## Metodologia

**Aplicação manual da rubric** (sem promptfoo end-to-end, sem ANTHROPIC_API_KEY — decisão Patrick):

1. Ler SKILL.md completo (10 arquivos, 2089 linhas total)
2. Aplicar cada critério da rubric `system-prompt.yaml` mentalmente:
   - Score 0-100 por critério
   - Tier: Core / Useful / Marginal
   - Findings P0/P1/P2
3. Calcular score ponderado usando pesos da rubric (100+95+90+85+70+60+80+60+50+70+60 = 820)
4. Comparar scores cruzando 10 skills pra detectar padrões
5. Gerar relatório único consistente

**Decisão explícita do Patrick** (pós-batch-1 do Haiku via Explore agents):
> "em vez de usar haiku, nao quer ler individualemnte uma por uma vc mesmo?"

Batch 1 do Haiku (5 skills) foi descartado. Audit refeito pelo Opus. Consistência de critério entre skills melhorou significativamente.

---

## Score médio pós-refactors sugeridos (projeção)

| Skill | Atual | Pós-refactor | Condição |
|-------|-------|--------------|----------|
| trident | 92.3 | 92.3 | — |
| sdd | 88.1 | 88.1 | — |
| reference-finder | 85.9 | 88 | se C001 caps corrigido |
| context-tree | 83.7 | 88 | se R005 exemplo adicionado + R004 edge cases |
| maestro | 83.2 | 83.2 | — |
| context-guardian | 83.2 | 83.2 | — |
| pattern-importer | 82.4 | 82.4 | — |
| prompt-engineer | 82.1 | 87 | se C001 caps + U002 extração |
| geo-optimizer | 78.1 | 85 | se R001 role + C001 caps + R004 edge cases |
| **skill-builder** | **77.7** | **87** | **se U002 Step 0 movido + C001 caps** |

**Média atual:** 83.7
**Média projetada pós-refactors opcionais:** ~86.4 (+2.7 pts)

Nenhum refactor é urgente. Todos são ROI baixo-médio. Priorizar skill-builder se houver 1h livre.
