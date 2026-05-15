# meeting-types/1on1-stakeholder

Configuração para reuniões 1-on-1 entre Patrick e um stakeholder de cliente específico (comercial, marketing, operação, etc.).

## Quando usar este tipo

- Reunião com 1 stakeholder (Enzo/Artemis Comercial, Hélio/Artemis Marketing, Rafael/AWControl, Delai/AWControl, Júlio/Artemis, etc.)
- Foco num único cliente/área
- Stakeholder traz demandas novas + status + dúvidas técnicas
- Participantes: Patrick + stakeholder (às vezes + Willy ou dev)

## Scope ClickUp

- **Folder único do cliente** mencionado na transcrição (não space inteiro)
- Se stakeholder é de múltiplas áreas (ex: Enzo = Artemis Comercial + às vezes LeadGen), escopar nas lists relevantes
- Sort: `updated_at desc`, sem filtro de status
- Considera backlog + tasks ativas do cliente pra cruzar com demandas novas

## Output esperado

- Organização **project-focused**: 1 cliente, seções por área/list ou por prioridade
- Mix típico de itens:
  - **Muitos NEW_TASK** — stakeholder traz demandas novas (é o padrão de 1-on-1)
  - **Poucos UPDATE** — alguns status updates sobre tasks em andamento
  - **Várias DECISION** — stakeholder decide escopo, prioridade, abordagem
  - **Alguns INFO** — contexto de mercado, concorrência, prazos externos
  - NOT_TASK pra operacional que aparecer

## Formato típico de transcrição

1. Pequeno small talk
2. Stakeholder revisa o que foi feito desde a última vez (gera UPDATE)
3. Stakeholder apresenta documento/lista de demandas novas (gera NEW_TASK em lote)
4. Patrick discute viabilidade técnica de cada demanda (gera DECISION sobre escopo)
5. Priorização do que sai na próxima semana
6. Fechamento com próximos passos

## Participantes e aliases

Exemplos comuns:
- Enzo Campos → Artemis Comercial
- Hélio Costa Jr → Artemis Marketing
- Júlio Cezar → Artemis (geral, especialmente SEO)
- Rafael (AWControl) → Athié
- Delai (AWControl) → Athié
- Marcelo → Galáxia

Sempre checar `project-aliases.md` pra folder correto.

## Particularidades

- **IL-9 direto** aplica pesado: todas as tasks novas caem em cliente de Hygor ou Jonas, Patrick não deve ficar sozinho na execução
- **IL-9 reverso** aplica quando demanda exige infra tech-lead (DB, integração nova, arquitetura) — Patrick precisa entrar como co-assignee
- Prioridades vêm do stakeholder, não do Patrick — registrar a ordem que o stakeholder disse (ex: "o #1 é lead scoring")
- Due dates geralmente vagas ("essa semana", "próxima") — pedir confirmação antes de gravar
- **Respeitar capacidade do dev:** se stakeholder pede 5 coisas pra "essa semana" e dev tem OOO → confrontar antes de aprovar todas

## Perguntas frequentes ao Patrick após reunião deste tipo

- "Qual das N demandas é realmente pra essa semana vs backlog?"
- "Dev X (Hygor/Jonas) tem capacidade essa semana ou precisa adiar parte?"
- "Demanda Y tem infra tech-lead (DB, etc.) — tu entra como co-assignee?"
- "Stakeholder falou X 'já tá pronto' mas não achei task — criar `[CONFIG]` pra registro?"