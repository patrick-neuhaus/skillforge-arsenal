# Prompt-Engineer Gaps — Auditoria Honesta da Skill Atual

**Data:** 2026-04-10
**Objetivo:** documentar onde `prompt-engineer` (versão atual) FALHA em validar conteúdo real, pra usar esses gaps como input das rubrics da Sub-fase 0B.
**Método:** aplicar manualmente o quality checklist da SKILL.md atual (linhas 97-108) + 7 princípios + lista de anti-patterns em 3 alvos. Comparar com leitura crítica paralela.

---

## Quality checklist atual do prompt-engineer

| Criterion | Ask yourself | Red flag |
|-----------|-------------|----------|
| Context/Role | Does the model know WHO it is and FOR WHAT? | Generic, personality-less output |
| Specific instructions | Clear actions or vague direction? | Model invents behavior |
| Output format | Precisely defined? | Inconsistent between runs |
| Examples (few-shot) | At least 1 input→output? | Model guesses format |
| Edge cases | Handles invalid, empty, unexpected? | Silent failure in production |
| What NOT to do | Explicit anti-patterns? Phrased positively? | Undesired behaviors |
| Attention budget | Too long? Redundant? | Diluted attention, high cost |
| Language calibration | Excess caps lock? | Overtriggering in 4.x |
| Tool management | Minimal, no overlap? | Model confuses tools |

---

## Alvo 1 — CLAUDE.md (D:\DOCUMENTOS\Github\CLAUDE.md, ~303 linhas)

### O que prompt-engineer atual CONSEGUE detectar

| Critério | Aplicado | Detectou |
|----------|----------|----------|
| Context/Role | ✅ | "Você é meu sócio técnico" — passa, role claro |
| Specific instructions | ✅ parcial | Muitas regras claras (Daily de abertura, Reporte diário). Algumas vagas ("Confronta direto") |
| Output format | ✅ | Reporte diário tem template explícito. Outras seções não precisam de format |
| Examples (few-shot) | ❌ falha em apontar | Não exige exemplo pra TODA seção; CLAUDE.md tem várias regras sem exemplo (Confrontação, Filtro de alavancagem) |
| Edge cases | ❌ N/A | Não se aplica direto a CLAUDE.md (não é prompt de chatbot que recebe inputs) |
| What NOT to do | ✅ parcial | Lista anti-patterns no Filtro/Confrontação ("não babar ovo") mas não estrutura |
| Attention budget | ⚠️ | 303 linhas — perto do limite, não detecta como problema |
| Language calibration | ⚠️ | "ANTES" e "NÃO" caps em vários pontos — não detecta calibração quebrada |
| Tool management | ❌ N/A | Não se aplica |

### O que prompt-engineer atual NÃO consegue detectar (gaps críticos)

#### Gap CRÍTICO 1: Não detecta CONTRADIÇÕES entre seções
A skill atual valida cada bloco isoladamente. CLAUDE.md tem instruções que se contradizem entre si:
- "Filtro de alavancagem aplique silenciosamente" vs "Model & Skill Router abra bloco antes de qualquer ação não-trivial" — um diz pra ficar quieto, outro diz pra falar
- "Higiene de tokens: leitura cirúrgica" vs "Confiança antes de código: 95% de confiança antes de fazer mudanças" — o primeiro estimula leitura mínima, o segundo exige leitura ampla pra atingir confiança
- "Respostas objetivas, 2 linhas" vs "Quando algo for ambíguo, pergunta antes de assumir, 2 perguntas targeted" — conflito de "responder rápido" vs "perguntar mais"

**Por que falha:** o checklist é por-prompt, não por-coleção. Não tem critério "consistência inter-seção".

#### Gap CRÍTICO 2: Não detecta GATES AUSENTES (texto vs gate físico)
A skill atual avalia se a instrução é clara, mas não pergunta "essa instrução tem reforço estrutural ou depende só de lembrança?". Isso é exatamente o que falhei nesta sessão:
- Filtro de alavancagem é texto → eu pulo
- IRON LAW seria texto → eu pularia
- Hook é estrutura → eu não pulo

**Por que falha:** o checklist assume que o validador é o operador da instrução. Pra Claude validando regras pra Claude, falta o critério "isso vai ser cumprido sem hook?".

#### Gap CRÍTICO 3: Não detecta REDUNDÂNCIA SEMÂNTICA (mesma ideia em N seções)
CLAUDE.md atual tem:
- "Filtro de alavancagem" + "Confrontação" + "Como trabalhar comigo: PENSA antes de fazer" — todas dizem variações de "não execute cego"
- "Tom e formato: Direto ao ponto" + "Como trabalhar comigo: Respostas objetivas" + "Output efficiency" (do system) — três fontes pra mesma regra

A skill detecta "redundância" como atributo do attention budget, mas só por contagem de tokens, não por semântica.

#### Gap CRÍTICO 4: Não tem critério pra MEMORY/STATE sections
CLAUDE.md tem applied learning bullets (Higiene de tokens), stakeholders recorrentes, agenda fixa. Isso não é "instrução pro modelo" — é state que o modelo lê. A skill atual não distingue, então aplica critérios errados (cobra "few-shot example" pra lista de stakeholders).

#### Gap CRÍTICO 5: Não tem critério pra ROUTING/DECISION trees
"Model & Skill Router" é uma árvore de decisão. A skill atual valida como se fosse instrução normal, mas árvores precisam de critérios próprios:
- Cobertura: cada caso possível tem branch?
- Mutuamente exclusivos? (Sonnet medium e Sonnet high se sobrepõem em "5+ arquivos OR loopou 1x" — qual prevalece?)
- Default explícito? (sim, "default 80% Sonnet medium" ✅)

**Verdict do CLAUDE.md por prompt-engineer atual:** "passa com warnings menores em attention budget".
**Verdict honesto:** **3 contradições críticas, gates ausentes em 90% das regras comportamentais, redundância semântica em 4+ seções, sem critério pra memory/routing.** Score real ~50/100.

---

## Alvo 2 — Plano (fluffy-giggling-phoenix.md v2, 555 linhas)

### O que prompt-engineer atual CONSEGUE detectar

| Critério | Aplicado | Detectou |
|----------|----------|----------|
| Context/Role | ❌ N/A | Plano não é prompt — não tem role |
| Specific instructions | ✅ | Cada fase tem ações concretas |
| Output format | ✅ parcial | Algumas fases têm output explícito (Fase 5 template), outras não |
| Examples (few-shot) | ❌ falha | Aplica critério errado — plano técnico não roda, exemplo input→output é ortogonal |
| Edge cases | ✅ → | Aplica como "failure modes", o plano cobre |
| What NOT to do | ✅ | Tem "Anti-padrões" e "O que NÃO está neste plano" |
| Attention budget | ⚠️ | 555 linhas — flag mas sem critério pra plano vs prompt |
| Language calibration | ⚠️ | "NÃO PULAR FASE 1" caps — flag genérico |
| Tool management | ❌ N/A | |

### Critérios aplicados ERRADAMENTE pelo prompt-engineer atual

#### Erro 1: Cobrar few-shot example pra plano técnico
"Examples (few-shot)" é critério de prompt operacional. Plano técnico não roda — não recebe input nem produz output. Pedir "1 input→output example" pra Fase 0B é absurdo.
**Critério correto pra plano:** "cada fase tem critério de sucesso verificável?" / "cada fase tem output concreto?"

#### Erro 2: Tratar attention budget como contagem de tokens
Plano de 555 linhas pode estar enxuto OU bloated, dependendo de redundância semântica e densidade de informação. A skill conta linhas e flag, sem analisar conteúdo.
**Critério correto pra plano:** "tem seção que pode ser removida sem perder capacidade de execução?" / "tem ideia repetida em 2+ lugares?"

#### Erro 3: Não verificar dependências entre fases
Plano tem Fase 5 que depende de Fase 0. Plano tem checkpoints humanos. Plano tem failure modes que param o fluxo. A skill atual não tem critério pra "DAG é válido?" / "checkpoint tá no lugar certo?".

#### Erro 4: Não verificar reversibilidade
Plano pode propor mudanças irreversíveis. A skill não pergunta "se Fase 3 falhar, dá pra desfazer Fase 2?". Crítico em planos de implementação.

### Gaps de cobertura específicos pra "technical-plan"

A skill atual NÃO detecta:
- **Chicken-and-egg lógico** (encontrei manualmente como F1 do auto-audit antes — a skill não pegaria)
- **Pré-requisitos não declarados** (Fase 5 depende de Fase 0, mas plano antigo não dizia)
- **Estimativa de esforço ausente** (algumas fases sem dificuldade/tempo)
- **Decisões pra humano sem formato comparável** (F11 do auto-audit)
- **Critério de parada vago** ("se der ruim, parar" — quando exatamente?)
- **Failure modes inconsistentes** (algumas fases têm, outras não)

**Verdict do plano por prompt-engineer atual:** "passa com warnings em attention budget e caps lock".
**Verdict honesto:** **plano tem 14 findings reais, 4 críticos.** A skill atual pegaria talvez 3 deles (caps lock, attention, talvez "what not to do" parcial). 11 ficam invisíveis.

---

## Alvo 3 — Routing Priorities table (skill-catalog.md, 30 linhas — Bloco 1 da Fase 5)

### O que prompt-engineer atual CONSEGUE detectar

| Critério | Aplicado | Detectou |
|----------|----------|----------|
| Context/Role | ❌ N/A | Tabela de roteamento não tem role |
| Specific instructions | ✅ | Cada linha é uma regra explícita |
| Output format | ✅ | Tabela com 3 colunas — formato claro |
| Examples (few-shot) | ❌ falha | Critério errado pra tabela; mas faltam exemplos práticos ("quando intent é X, qual linha pega?") |
| Edge cases | ❌ falha | Não cobre intent ambíguo (ex: "review esse código E também o UX" — trident OU ux-audit?) |
| What NOT to do | ✅ | Coluna "NÃO usar" é explícita |
| Attention budget | ✅ | 30 linhas, OK |
| Language calibration | ✅ | OK |
| Tool management | ❌ falha | Lista 8 skills sem dizer prioridade entre overlaps reais |

### Gaps específicos pra "iron-laws" / tabela de roteamento

A skill atual NÃO detecta:
- **Cobertura incompleta** — tabela cobre alguns overlaps mas não todos. Que outras combinações de skill ficaram fora?
- **Sobreposição de regras** — duas linhas podem pegar mesmo intent ("design review" + "auditoria de UX" — um cliente pede "revisa o frontend"; ambas matcham?)
- **Hierarquia ausente** — quando 2+ regras matcham, qual prevalece? Não tá explícito.
- **Trigger semântico** — tabela usa keywords, mas o intent real do usuário pode usar palavras diferentes. Sem coverage de variações.
- **Falsos positivos** — "DRY/KISS" matcha trident, mas e se for sobre prompt simplification? trident é sobre código.
- **Maintenance debt** — quem atualiza a tabela quando skills novas entram?

**Verdict da tabela por prompt-engineer atual:** "passa com nota máxima — bem estruturada".
**Verdict honesto:** **funciona pra casos óbvios mas tem 6 gaps de cobertura e zero hierarquia entre regras conflitantes.** Score real ~65/100.

---

## Síntese dos gaps do prompt-engineer atual

### Gaps estruturais (afetam todas as validações)

1. **Sem rubric por tipo** — mesmo checklist pra chatbot, plano técnico, CLAUDE.md, tabela de roteamento. Critérios aplicam-se erroneamente em metade dos casos.
2. **Sem critério de consistência inter-seção** — valida bloco isolado, não conjunto. Contradições entre seções passam.
3. **Sem critério de gate físico vs textual** — não pergunta "essa regra vai ser cumprida sem hook?". Gera regras que parecem boas mas viram sugestão.
4. **Sem critério de redundância semântica** — só conta tokens. Mesma ideia em 3 seções passa se cada uma for curta.
5. **Sem critério de cobertura/exclusividade pra árvores de decisão** — valida regras isoladas, não a árvore como um todo.

### Gaps por tipo

**claude-md (e similares — system prompts híbridos com memory + routing + behavioral):**
- Não distingue behavioral vs operational vs memory vs routing sections
- Aplica "few-shot example" universalmente, errado pra memory sections
- Não verifica contradições entre seções
- Não pergunta sobre gates físicos
- Não valida pruning de regras antigas (quando remover?)

**technical-plan (planos de implementação):**
- Cobra few-shot example (ortogonal pra plano)
- Não verifica DAG de dependências entre fases
- Não verifica reversibilidade
- Não verifica critérios de sucesso por fase
- Não verifica chicken-and-egg lógico
- Não verifica failure modes consistentes

**iron-laws / routing tables:**
- Não verifica cobertura (todas as combinações)
- Não verifica exclusividade (2 regras matcham mesmo intent?)
- Não verifica hierarquia entre regras conflitantes
- Não verifica triggers semânticos (variações de palavra)

**system-prompt (chatbots, agentes):**
- Esse a skill atual já cobre razoavelmente bem (é pra isso que foi feita)
- Talvez melhorar: integração com tools, calibração 4.x, cache strategy

### Critérios que a skill atual aplica erroneamente

| Critério | Quando erra | Quando acerta |
|----------|-------------|---------------|
| Few-shot example | plano técnico, memory section, routing table | system prompt de chatbot, prompt de extração |
| Output format | seções comportamentais ("Tom e formato") | extração JSON, schema |
| Edge cases | plano técnico (vira "failure modes") | chatbot com input variado |
| Tool management | planos sem tools | agente com 5+ tools |

---

## Conclusão

A skill atual é **funcional pra system prompts de chatbot e prompts de extração**, que é o domínio pra que foi originalmente desenhada. Ela é **inadequada pra**:
- CLAUDE.md (sem reference, critérios errados em 5/9)
- plano técnico/PRD (sem reference, critérios errados em 4/9)
- iron-laws / routing tables (sem reference, sem critérios de cobertura)
- system prompts híbridos com memory

**Recomendação pra Sub-fase 0B (criar rubrics):**

Criar 4 rubrics (já no plano) com:
1. **rubrics/claude-md.md** — atende os 5 gaps críticos do alvo 1. Critérios novos: contradições inter-seção, gates físicos, redundância semântica, distinção behavioral/operational/memory/routing, pruning.
2. **rubrics/technical-plan.md** — atende os 4 erros de aplicação do alvo 2. Critérios novos: DAG de dependências, reversibilidade, critérios de sucesso por fase, chicken-and-egg, failure modes consistentes, decisões humanas com formato comparável.
3. **rubrics/iron-laws.md** — atende os 6 gaps do alvo 3. Critérios novos: cobertura, exclusividade, hierarquia, triggers semânticos, falsos positivos, maintenance.
4. **rubrics/system-prompt.md** — formaliza o que já funciona, adiciona calibração 4.x e cache strategy.

**Insight meta:** essa auditoria foi possível porque tive a SKILL.md inteira do prompt-engineer na cabeça e correlacionei com os 3 alvos manualmente. Pra escalar, as rubrics precisam ser **executáveis** — listas de checks que o próprio Claude consegue rodar mecanicamente, não princípios genéricos.

**Failure mode a observar na 0B:** se ao escrever as rubrics eu perceber que cada critério novo precisa de "raciocínio profundo" pra aplicar, é sinal de que a abstração ainda tá fraca. Critério bom é "checa X, Y, Z" — verificável em 30 segundos.
