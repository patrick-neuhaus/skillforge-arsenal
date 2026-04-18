---
name: meeting-sync
description: "Processar transcrição de reunião (daily, planning, review), extrair action items, cruzar com ClickUp, criar/atualizar tasks e gerar resumo markdown. Use quando: 'peguei a transcrição da daily', 'extrai tasks da reunião', 'cruza com o ClickUp', 'sincroniza reunião', 'o que saiu da call', 'action items da reunião', 'resume a daily', 'gravação da reunião', 'Fireflies', 'transcrição + tasks'. Triggers EN: meeting transcript, extract action items, sync meeting notes, daily standup summary. NÃO use pra agendar reuniões (use schedule) nem pra comunicar decisões ao cliente (use comunicacao-clientes)."
argument-hint: "[texto colado] | --file <path> | --type daily-review-planning | --dry-run | --project <name> | --date YYYY-MM-DD | --summary-only"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, mcp__*clickup*
---

# meeting-sync

Processa transcrição de reunião, extrai action items, cruza com ClickUp e gera resumo diário em markdown.

## IRON LAW

**NUNCA executar ações no ClickUp sem aprovação explícita do Patrick.** A skill PROPÕE — Patrick DECIDE. Phase 3 é sempre BLOCKING. Reunião gera interpretação, não fato confirmado.

## Options

| Flag | Default | Descrição |
|------|---------|-----------|
| `--file <path>` | texto colado | Lê transcrição de arquivo local |
| `--type <name>` | daily-review-planning | Carrega references/meeting-types/<name>.md |
| `--dry-run` | false | Só extrai e propõe, não oferece execução |
| `--project <name>` | all | Limita a um cliente específico |
| `--summary-only` | false | Gera só resumo .md, sem sync ClickUp |
| `--date YYYY-MM-DD` | today | Data da reunião |

## Phase 0: Acquire

1. Identifica input: texto colado no chat OU `--file <path>` → Read file
2. Extrai metadata: data da reunião (via `--date` ou detecta na transcrição), participantes, tipo
3. Carrega `references/meeting-types/<type>.md` (default: daily-review-planning)
4. **Se transcrição > 80K chars:** anuncia "Transcrição longa — processando cliente a cliente" → Phase 1 processa um cliente por vez, aguarda confirmação antes de avançar

### Heurística de meeting-type mismatch (Fix F)

- **Se transcrição não encaixa no `--type` passado** (ex: `--type daily-review-planning` mas transcrição é claramente 1-on-1 com stakeholder) → flagar para Patrick + perguntar se quer mudar de tipo antes de Phase 1.
- **Se `--type` não passado E transcrição parece 1-on-1** (≤2 participantes E ≤1 cliente mencionado E sem revisão client-by-client) → perguntar tipo antes de Phase 1. Default `daily-review-planning` só se sinais convergem.
- **Flag a data como assunção se não identificável:** se `--date` não passado E transcrição sem timestamp explícito → declarar "assumindo data de hoje (YYYY-MM-DD) — confirma?" antes de Phase 2.

## Phase 1: Extract

1. Carrega `references/extraction-patterns.md`
2. Carrega `references/project-aliases.md` — mapeia nomes informais a clientes/folders
3. Lê a transcrição e classifica cada item:
   - **NEW_TASK** — ação nova identificada que não existe no ClickUp
   - **UPDATE** — mudança de status/progresso em algo existente
   - **DECISION** — decisão tomada (registrar, não criar task)
   - **INFO** — informação contextual (registrar, não criar task)
   - **BLOCKER** — impedimento em task existente
   - **NOT_TASK** — operacional puro (timesheet, mensagem isolada, conversa) — descartar com motivo
4. Agrupa itens por cliente em ordem alfabética

## Phase 2: Match

Para cada UPDATE ou potencial NEW_TASK:
1. `clickup_search` no Space Desenvolvimento (`90174691251`) — **SEM filtro de status**, `sort: updated_at desc`
2. **Se search retornar 0 OU erro de server** → fallback `clickup_filter_tasks` com `list_ids: [<id_esperado>]`, `order_by: updated`, `reverse: true`, `include_closed: true` (ver references/extraction-patterns.md seção "Phase 2 fallback strategy")
3. `clickup_get_task` com `detail_level: detailed` — ler descrição + dependências antes de decidir match
4. Algoritmo de match (detalhes em references/extraction-patterns.md):
   - **HIGH (>80%):** 3+ keywords match + mesmo folder → propõe UPDATE
   - **MEDIUM (50-80%):** 2 keywords match + tema próximo → apresenta as 2 opções (UPDATE ou NEW)
   - **LOW (<50%):** <2 keywords ou folder errado → propõe NEW_TASK
   - **Anti-false-match:** nome-match HIGH mas folder/list diferente do contexto OU stakeholder de domínio diferente → rebaixar pra LOW (ver extraction-patterns.md)
5. **Regra de ouro:** `dateUpdated ≠ date_created`. Sempre verificar `date_created` antes de afirmar que task não existia.
6. **Claims de memória** (ex: "Hygor indisponível X-Y") precisam de verificação antes de usar como constraint: buscar tasks/comentários recentes que confirmem. Se não achar → perguntar Patrick. NUNCA afirmar como fato.

## Phase 3: Propose ⛔ BLOCKING

Apresenta proposta completa por cliente (ordem alfabética). Formato:

```
# Proposta Sync — [Tipo] [Data]

## [Cliente]

### 🆕 Tasks a CRIAR
| # | Prefixo + Título | Assignee | Prioridade | Due | Confiança |
|---|------------------|----------|------------|-----|-----------|

Descrição proposta (#N): contexto + o que fazer + critério de aceitação
Trecho transcrição: "..."

### 🔄 Tasks a ATUALIZAR
| # | ID | Nome atual | O que muda | Match | Confiança |

### 💡 Decisões
- ...

### 🚫 Descartados (NOT_TASK / INFO)
- "trecho" — motivo

---
✅ Aprovar tudo | 🔢 Aprovar parcial (listar IDs) | ❌ Rejeitar | ✏️ Editar
```

**⛔ AGUARDAR aprovação explícita. Não prosseguir até Patrick responder.**

## Phase 4: Execute

Só após aprovação explícita. Para cada item aprovado:

**Criar task** — checklist obrigatório (ver references/task-format.md):
1. Prefixo correto no título (ver tabela em task-format.md)
2. `status: "a fazer"` explícito (sem isso cai em backlog)
3. `assignees` definido — **IL-9 direto:** se task cai em cliente de Hygor/Jonas, **confronto vocal obrigatório** antes de incluir Patrick
4. **IL-9 reverso:** se task exige infra/componente que só Patrick sabe fazer (DB setup, decisão arquitetural, integração nova) mas cai em cliente de Hygor/Jonas → **confronto vocal obrigatório**: "Hygor sozinho com tua ajuda pontual, ou tu entra como co-assignee?". NUNCA assumir Hygor sozinho quando a task tem peça tech-lead.
5. `due_date` definida (perguntar se não souber)
6. Descrição: contexto + o que fazer + critérios de aceitação

**Atualizar task** — aplicar mudanças exatas aprovadas (status, comment, due_date, assignee).

**Verificação pós-execução:** `clickup_filter_tasks` com `statuses: ["backlog"]` → confirmar que nenhuma task caiu lá por engano.

## Phase 5: Summary

1. Carrega `references/output-template.md`
2. Gera arquivo `Desktop/Daily/YYYY-MM/DD.md`:
   - Header: data + tipo da reunião
   - Por cliente (ordem alfabética): status com emojis + ID + título + 1 linha de contexto
   - Seção de decisões importantes
   - Seção de bloqueios
   - Footer: NOT_TASK descartados com motivos
3. Exibe resumo compacto inline no chat

## Anti-patterns

1. Buscar só tasks com status `complete/done` — perde metade das updates
2. Confundir `dateUpdated` com `date_created` — task não foi criada hoje
3. Classificar item operacional (timesheet, mensagem avulsa) como NEW_TASK
4. Criar task sem prefixo, status `a fazer`, due_date ou assignee
5. Assumir que task não existe sem buscar descrição (nome curto engana)
6. Executar no ClickUp sem aprovação (viola IRON LAW)
7. Carregar todas as references de uma vez — carregar só as necessárias por fase
8. Afirmar claim de memória (indisponibilidade, prazo passado) sem verificar no ClickUp primeiro
9. Nome-match HIGH com task de domínio diferente (ex: task Marketing com demanda Comercial) → propor UPDATE errado

## When to ask vs assume

**Perguntar antes de propor:**
- Tipo de reunião não explicitado e transcrição não tem cara clara de daily-review-planning
- Item ambíguo: HIGH match com 1 task mas conteúdo divergente na descrição
- Task que ficaria assignada a Patrick em cliente de Hygor/Jonas (IL-9 direto)
- Task de cliente de Hygor/Jonas que exige infra tech-lead (IL-9 reverso)
- Claim de memória (alguém indisponível, task já existe) sem match imediato no ClickUp

**Assumir e seguir:**
- `--type daily-review-planning` como default se não especificado E transcrição não contradiz
- HIGH match (3+ keywords + mesmo folder + domínio coerente) → propor UPDATE
- LOW match (<2 keywords OU domínio divergente) → propor NEW_TASK
- Item operacional óbvio → NOT_TASK com motivo

**NUNCA assumir aprovação do Patrick.** Phase 3 é sempre BLOCKING.