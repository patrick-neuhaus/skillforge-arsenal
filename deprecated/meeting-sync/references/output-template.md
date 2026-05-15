# output-template

Template do arquivo diário `.md` gerado pela skill após sync com ClickUp.

## Emoji legend

| Emoji | Significado |
|-------|-------------|
| ✅ | Concluído |
| ⚠️ | Em revisão / atenção |
| 🔴 | Urgente / fazer hoje |
| 🟡 | Normal |
| ⚪ | Baixa / sem foco |
| 🔒 | Bloqueado |
| 🔀 | Delegado / gerou task |
| 🆕 | Task nova criada nesta reunião |
| 🗑️ | Apagada / duplicata |

Emojis combinam: `🔴🔒` = urgente mas bloqueado, `✅🔀` = concluído e gerou outra.
Não usar 🔥 (redundante com 🔴) nem emojis decorativos em headers de cliente.

## Template

```markdown
# 📋 Daily — DD/MM/YYYY ([dia da semana])
**Tipo:** [daily-review-planning | outro]
**Participantes:** [lista]

| Emoji | Significado |
|-------|-------------|
| ✅ | Concluído |
| ⚠️ | Em revisão / atenção |
| 🔴 | Urgente / fazer hoje |
| 🟡 | Normal |
| ⚪ | Baixa / sem foco |
| 🔒 | Bloqueado |
| 🔀 | Delegado / gerou task |
| 🆕 | Task nova |
| 🗑️ | Apagada / duplicata |

---

## [Cliente A]  ← ordem alfabética

### [Área/Lista]

[EMOJI] **[PREFIXO] Título da task** (ID: `TASKID`)
→ [Assignee] | [prioridade] | [contexto 1 linha]

---

## [Cliente B]

...

---

## Decisões

- **[Cliente]:** [decisão tomada na reunião]

---

## Bloqueios

- **[ID task]** — [descrição do bloqueio + próximo passo]

---

## Descartados (NOT_TASK)

- "[trecho da transcrição]" — [motivo: operacional puro / sem ação / informação]

---

## RESUMO DO DIA

| | Criadas | Atualizadas | Concluídas |
|--|---------|-------------|------------|
| Total | N | N | N |

**Por responsável:**
- [Nome]: N tasks ([detalhes])
```

## Regras de geração

1. Clientes em ordem **alfabética** sempre
2. Tasks por área/lista dentro do cliente
3. Incluir ID do ClickUp sempre (facilita rastreabilidade)
4. 1 linha de contexto por task (de onde veio, por que importa)
5. Seção Decisões: apenas o que foi **decidido**, não o que foi discutido
6. Seção Bloqueios: só o que está **ativamente bloqueando** hoje
7. NOT_TASK descartados: incluir trecho literal + motivo claro

## Onde salvar

`C:\Users\Patrick Neuhaus\Desktop\Daily\YYYY-MM\DD.md`

Exemplo: reunião de 14/04/2026 → `Desktop/Daily/2026-04/14.md`