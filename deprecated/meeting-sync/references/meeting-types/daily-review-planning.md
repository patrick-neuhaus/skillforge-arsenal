# meeting-types/daily-review-planning

Configuração específica para reuniões do tipo daily, revisão de projeto e planning.

## Quando usar este tipo

- Reunião semanal/diária de acompanhamento de projetos
- Review client-by-client de status de tasks
- Planning de próximas semanas
- Participantes típicos: Patrick + Willy + eventual Hygor ou Jonas

## Scope ClickUp

- **Space:** Desenvolvimento (`90174691251`)
- **Filtro de status:** NENHUM — buscar em todos os status
- **Sort:** `updated_at desc` — tarefas tocadas recentemente aparecem primeiro
- **Abrangência:** space inteiro (todos os clientes, a menos que `--project` especificado)

## Output esperado

- Organização **client-by-client** (ordem alfabética)
- Por cliente: tasks atualizadas + novas + decisões tomadas
- Mix típico de itens:
  - Muitos **UPDATE** (a maioria dos itens em daily é update de status)
  - Alguns **NEW_TASK** (ações novas identificadas)
  - Várias **DECISION** (definições de abordagem, prioridade, tecnologia)
  - Alguns **BLOCKER** (impedimentos que precisam ser resolvidos)
  - Poucos **INFO** (disponibilidade, contexto de prazo)
  - NOT_TASK para operacional puro

## Formato típico de transcrição

Transcrição segue geralmente cliente por cliente (Willy/Patrick passando pelo status de cada projeto):
1. Willy pergunta status do cliente X
2. Patrick relata o que foi feito + o que está travado
3. Willy comenta/decide/redireciona
4. Passam pro próximo cliente

Identificar mudança de cliente pelo nome do cliente na fala ou pelo contexto do que está sendo discutido.

## Participantes e aliases

- Patrick Neuhaus → sempre presente
- Willy Azevedo → sempre presente (gestor)
- Hygor Fragas / "Igor" → presente em algumas reuniões, assuntos técnicos
- Jonas Bialoso → presente em algumas reuniões, assuntos técnicos

## Perguntas frequentes ao Patrick após reunião deste tipo

- Task com `MEDIUM` match: "Isso é update da task X ou uma nova task?"
- Item sem dono identificado: "Quem pega isso, Hygor ou Jonas?"
- Decisão que implica ação: "Isso gera task ou fica só como decisão registrada?"