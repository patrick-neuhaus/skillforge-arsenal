# Higiene de Tokens para Codex

- Leia cirurgicamente. Prefira buscas e trechos especificos a abrir arquivos enormes.
- Preserve contexto: se uma resposta grande pode virar arquivo/handoff, grave plano ou resumo e continue por waves.
- Se o contexto passar de ~50% em trabalho longo, gere handoff com `context-guardian`.
- Filtre outputs de shell com limites. Evite despejar logs longos no contexto.
- Se falhar duas vezes na mesma hipotese, mude estrategia antes da terceira tentativa.
- Nao carregue references inteiras de skills; leia apenas o `SKILL.md` e os arquivos explicitamente necessarios.
