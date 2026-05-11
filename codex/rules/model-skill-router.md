# Model & Skill Router para Codex

No Codex, o modelo default do Patrick e `gpt-5.5` com reasoning effort `medium`.

## Regra principal

Antes de trocar de modelo, aumente reasoning effort. Para tarefas complexas, prefira `gpt-5.5` high/xhigh antes de mudar para modelos menores ou especializados.

## Heuristica

- `gpt-5.5 medium`: default para coding, arquitetura moderada, analise e execucao.
- `gpt-5.5 high`: feature multi-arquivo, schema change, debug com varias hipoteses, plano tecnico relevante.
- `gpt-5.5 xhigh`: decisao cara, migracao de ecossistema, bug sistemico, arquitetura multi-sistema.
- `gpt-5.4` ou `gpt-5.4-mini`: tarefas menores quando custo/velocidade importam e risco e baixo.
- Subagents: usar somente quando Patrick pedir delegacao/parallel agents ou quando o sistema permitir explicitamente.

## Skill routing

- Skill obvia + intent claro: use direto.
- 2+ skills, agent ou workflow: use `maestro`.
- Nenhuma cobre: `reference-finder --solution-scout` antes de construir.

## Interrupcoes obrigatorias

- Task estrategica: sugerir alinhar com Willy.
- Terceira iteracao sem uso real: "Tu ta melhorando algo que nunca usou. Usa primeiro, depois melhora com feedback real."
- Pedido operacional que e de Hygor/Jonas: confrontar antes de Patrick assumir.
