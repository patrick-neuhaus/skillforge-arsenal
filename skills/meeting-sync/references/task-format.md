# task-format

Formato padrão para criação e atualização de tasks no ClickUp — workspace Desenvolvimento.

## Prefixos de título

| Prefixo | Quando usar |
|---------|-------------|
| `[FEATURE]` | Nova funcionalidade que adiciona capacidade ao produto |
| `[BUG]` | Comportamento incorreto que precisa ser corrigido |
| `[AJUSTE]` | Melhoria pequena, refinamento, ajuste de existente |
| `[MELHORIA]` | Melhoria significativa mas não nova feature |
| `[AUTOMAÇÃO]` | Workflow automático novo ou modificação de automação |
| `[INFRA]` | Setup de servidor, CI/CD, banco, configuração de infra |
| `[CONFIG]` | Configuração/ajuste de algo já implementado (ex: horário de envio, grupo de destino) |
| `[REUNIÃO]` | Container de time tracking de reunião (tag "reunião" — excluído do filtro padrão) |

**Regra:** task SEM prefixo some no filtro padrão do Patrick. Sempre prefixar.

## Checklist de criação (obrigatório — 5 itens)

Antes de `clickup_create_task`, verificar todos:

1. **Título com prefixo** da tabela acima (ex: `[BUG] Campo PGR não extrai validade`)
2. **`status: "a fazer"`** explícito — sem isso, task cai em backlog e desaparece
3. **`assignees`** — aplicar IL-9 (direto e reverso, ver abaixo) antes de confirmar
4. **`due_date`** definida — sem data, task vira fantasma no backlog
5. **Descrição** com:
   - **Contexto:** de onde veio esse pedido (reunião, cliente, urgência)
   - **O que fazer:** ação concreta e clara
   - **Critérios de aceitação:** como saber que está pronto

## Kanban

```
Backlog → A Fazer → Fazendo → Revisão → Bloqueado → Concluído
```

- Task nova: sempre em `A Fazer` (nunca direto em Backlog)
- Ao mover pra `Bloqueado`: adicionar comment explicando motivo
- Ao mover pra `Concluído`: critérios de aceitação cumpridos?

## IL-9 — dois sentidos

### IL-9 direto: não puxar Patrick pra task delegável

Se cliente é de Hygor/Jonas (ver tabela abaixo) e a task é delegável (dev puro) → **confronto vocal** antes de adicionar Patrick como co-assignee. Frase padrão: "Essa task é do [Hygor/Jonas], assigna nele sozinho ou tu tá fazendo junto por algum motivo específico?"

### IL-9 reverso: não deixar Hygor/Jonas sozinho numa task que exige tech-lead

Se a task cai em cliente de Hygor/Jonas MAS exige componente que só Patrick sabe fazer (DB setup, decisão arquitetural, integração nova não-trivial, debug em produção) → **confronto vocal** antes de deixar Hygor/Jonas sozinho como assignee. Frase padrão: "Essa task tem infra que geralmente é tua — Hygor/Jonas sozinho com tua ajuda pontual, ou tu entra como co-assignee?"

**Trigger do reverso:** palavras-chave na descrição ou transcrição como "colocar no banco", "infra nova", "decidir arquitetura", "integração com X novo", "debug em prod". Se aparecer qualquer uma delas + cliente Hygor/Jonas → confronto obrigatório.

## Divisão de assignee por cliente

| Cliente | Owner principal | IL-9 aplicável |
|---------|-----------------|----------------|
| Athié / AWControl / SupplyMep | Hygor | Direto + reverso |
| GaláxIA | Hygor | Direto + reverso |
| JRG Corp | Hygor | Direto + reverso |
| Marine Telematics | Hygor | Direto + reverso |
| Artemis Marketing | Hygor | Direto + reverso |
| Artemis Comercial | Hygor | Direto + reverso |
| Plus IoT | Jonas | Direto + reverso |
| Barry Callebaut | Jonas | Direto + reverso |
| Gascat | Jonas | Direto + reverso |
| Artemis Operação | Jonas | Direto + reverso |
| Artemis SEO | Patrick | N/A — Patrick é owner |

**Exceções (não confrontar):** Patrick explicitamente disse "eu vou fazer" OU task é claramente tech lead (code review, decisão arquitetural) OU Patrick já confirmou ser co-assignee antes da reunião.

## Pós-criação obrigatório

Rodar `clickup_filter_tasks` com `statuses: ["backlog"]` pra confirmar que a task criada não caiu em backlog por engano.