---
name: context-guardian
description: "Monitor, analyze, and manage context window usage. Generate handoff documents, alert when approaching limits, estimate budget remaining, and optimize context consumption. Use when user asks: 'quanto de contexto usei?', check context, analyze context window, 'tá pesado?', 'preciso limpar?', 'hora do /clear?', monitor context usage, manage window, 'gera um handoff', 'salva o estado antes do /clear', create handoff document, estimate context budget, 'a conversa tá longa', 'o Claude tá ficando burro', 'as respostas pioraram', detect context bloat, 'resume o que fizemos', generate summary for clear. Essential between SDD phases and in long skill chains. Also: 'quanta janela sobrou?', optimize context, verify window budget, 'antes de dar /clear', 'to sem contexto'."
---

# Context Guardian — Gestão de Context Window

IRON LAW: NEVER let context usage exceed 50% without alerting. Quality degrades silently past this threshold — the user won't notice until the output is already bad. Alert EARLY, not late.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--check` | Estimate current context usage and report | default |
| `--handoff` | Generate handoff document for /clear transition | - |
| `--budget <n>` | Set context budget for current task (default: 40%) | 40% |

## Workflow

```
Context Guardian Progress:

- [ ] Step 1: Assess ⚠️ REQUIRED
  - [ ] 1.1 Estimate current context usage
  - [ ] 1.2 Classify status (green/yellow/red)
  - [ ] 1.3 Identify biggest context consumers
- [ ] Step 2: Recommend
  - [ ] 2.1 If green → continue, report budget remaining
  - [ ] 2.2 If yellow → warn, suggest strategies
  - [ ] 2.3 If red → recommend /clear, offer --handoff
- [ ] Step 3: Handoff (if --handoff or red status)
  - [ ] 3.1 Generate handoff document
  - [ ] 3.2 Save to file
  - [ ] ⛔ GATE: User confirms handoff before /clear
```

## Step 1: Assess

### Estimating Context Usage

Context window usage is hard to measure exactly. Use these heuristics:

| Signal | Interpretation |
|--------|---------------|
| Conversation has 5-10 exchanges | ~20-30% used |
| Conversation has 10-20 exchanges | ~30-50% used |
| Conversation has 20+ exchanges | ~50%+ likely — check carefully |
| Large files were read (>500 lines) | Add ~5-10% per file |
| Multiple tool calls with large outputs | Add ~3-5% per call |
| Skills with heavy references loaded | Add ~5-10% per skill |

### Status Classification

| Status | Usage | Action |
|--------|:-----:|--------|
| 🟢 Green | <30% | Continue normally |
| 🟡 Yellow | 30-45% | Warn. Can continue but plan exit |
| 🔴 Red | >45% | Recommend /clear. Offer handoff |

### Biggest Consumers

Identify what's eating context:
1. **Long file reads** — files >200 lines loaded into conversation
2. **Tool call outputs** — grep/glob results, git diffs
3. **Skill references** — heavy skills (SDD, Trident) load multiple references
4. **Conversation history** — back-and-forth exchanges accumulate
5. **MCP responses** — JSON-heavy MCP tools bloat significantly more than CLI tools

Load `references/window-management.md` for detailed strategies.

## Step 2: Recommend

### Green (continue)
```
🟢 Context: ~[X]% usado. Budget restante: ~[Y]%.
Continue trabalhando. Próximo checkpoint em ~[N] exchanges.
```

### Yellow (warn)
```
🟡 Context: ~[X]% usado. Entrando em zona de atenção.
Estratégias:
1. Evite ler arquivos grandes — peça trechos específicos
2. Minimize tool calls com outputs longos
3. Considere /clear se a próxima tarefa é pesada
4. Se continuar: gere handoff preventivo com --handoff
```

### Red (recommend /clear)
```
🔴 Context: ~[X]% usado. Qualidade pode estar degradando.
Recomendação: /clear agora.
Execute: context-guardian --handoff para salvar estado antes.
```

## Step 3: Handoff

Load `references/handoff-templates.md` for template by scenario.

### Handoff Document Structure

```markdown
# Handoff: [data] — [tarefa em andamento]

## Estado Atual
- **Tarefa:** [o que está sendo feito]
- **Fase:** [em qual fase/step está]
- **Progresso:** [o que já foi feito vs o que falta]

## Decisões Tomadas
- [decisão 1 — por que]
- [decisão 2 — por que]

## Arquivos Modificados
- [path] — [o que foi feito]
- [path] — [o que foi feito]

## Próximos Passos
1. [próximo passo imediato]
2. [passo seguinte]
3. [passo final]

## Contexto Crítico
[Qualquer informação que NÃO está nos arquivos e seria perdida no /clear.
Ex: decisões verbais do usuário, trade-offs discutidos, bugs encontrados que ainda não foram fixados.]

## Como Retomar
Após /clear, cole este handoff como primeiro prompt:
"Estou retomando trabalho. Leia o handoff abaixo e continue de onde paramos: [cola handoff]"
```

### Save Location

Save handoff to: `handoff-[YYYY-MM-DD]-[brief-desc].md` in the project root or working directory.

⛔ **GATE:** Present handoff to user. Confirm before recommending /clear.

## Anti-Patterns

- **Alerting too late:** Alert at 30-40%, not at 60% when damage is done
- **Handoff too vague:** "We were working on stuff" is useless. Include paths, decisions, next steps
- **Handoff too detailed:** Don't copy file contents into the handoff — reference paths instead
- **Ignoring MCP bloat:** MCP tool responses are significantly heavier than CLI outputs. Flag this
- **Not saving handoff to file:** Verbal handoffs die with /clear. Always save to .md file
- **Over-checking:** Don't run --check every 2 exchanges. Check at natural breakpoints

## Pre-Delivery Checklist

- [ ] Status classification is reasonable (green/yellow/red)
- [ ] If handoff: all modified files listed
- [ ] If handoff: decisions documented with WHY
- [ ] If handoff: next steps are actionable
- [ ] If handoff: "how to resume" section included
- [ ] Handoff saved to file (not just shown in conversation)

## When NOT to use

- Short conversation (<5 exchanges) → no need to check
- Already at the end of the task → just finish instead of checking
- Using /clear between SDD phases → SDD handles its own handoffs via prd.md/spec.md

## Integration

- **SDD** — between phases: SDD uses prd.md/spec.md as natural handoffs, but context-guardian adds awareness
- **Maestro** — in long chains (3+ skills), maestro can invoke context-guardian between skills
- **All skills** — any skill can call context-guardian --check mid-workflow when feeling degradation
