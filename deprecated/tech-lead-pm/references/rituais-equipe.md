# Rituais de Equipe — Templates e Guias

Rituais minimos para equipe de 3-5 pessoas. Foco em consistencia, nao perfeicao.

## Weekly Sync (obrigatorio, 1x/semana, 30min)

Substitui a daily sincrona como ritual principal. Daily async e suficiente pro dia a dia; a weekly e onde alinha a semana.

### Formato

1. O que cada um entregou essa semana (5min)
2. O que ta planejado pra proxima semana (5min)
3. Bloqueios e decisoes pendentes (10min)
4. Prioridades que mudaram (5min)
5. Uma coisa que podemos melhorar (5min)

### Dicas

- Comece no horario, termine no horario. 30min max.
- Se alguem nao tem nada pra reportar, pula. Nao force.
- Registre decisoes no ClickUp, nao na cabeca.

## Daily Async (obrigatorio, diario)

### Formato

Cada pessoa manda no ClickUp ou grupo ate as 10h:
1. O que fiz ontem?
2. O que vou fazer hoje?
3. To bloqueado em algo?

### Regras

- Duracao: 0min do seu tempo se ninguem ta bloqueado
- Se alguem ta bloqueado: resolve na hora ou agenda 15min
- Se alguem nao manda: cobre. Consistencia importa.
- Formato de texto, nao call. Respeita o tempo de todos.

## 1:1 Semanal (obrigatorio, 1x/semana com cada pessoa, 30min)

### Roteiro

1. **Como ta?** (pessoal, 2min) — nao pule isso
2. **O que ta funcionando?** — reforce o positivo
3. **O que ta travando?** — bloqueios, frustracoes
4. **Feedback** (nos dois sentidos) — use SCI
5. **Proxima semana** — alinhamento de expectativas

### Regras criticas

- NAO e status update. Pra isso tem a daily/weekly.
- 1:1 e sobre a PESSOA, nao sobre a task.
- Pra Jonas: mais proximo de mentoria (ensinar, guiar, pedir pra ele explicar o raciocinio)
- Pra Hygor: mais proximo de parceria (alinhar, decidir junto, dar autonomia)

### Perguntas uteis

- "O que eu poderia fazer diferente pra te ajudar?"
- "Tem algo que ta te incomodando que a gente nao falou?"
- "Como voce avalia sua propria semana de 1 a 5?"
- "Tem algo que voce quer aprender que nao ta tendo chance?"

## Retro Quinzenal (recomendado, a cada 2 semanas, 30min)

### Formato

1. **O que deu certo?** (10min)
2. **O que deu errado?** (10min)
3. **O que mudamos?** (10min) — 1 acao concreta. Nao 10. Uma.

### Regras

- Peca feedback sobre SUA gestao. Isso gera confianca e te ajuda a crescer.
- Registre a acao concreta no ClickUp como task.
- Na retro seguinte, verifique se a acao da retro anterior foi feita.
- Se nao foi feita, questione: era importante ou so pareceu urgente na hora?

## Implementacao no ClickUp

### Estrutura sugerida

- **Lista "Rituais"** — tasks recorrentes pra cada ritual
- **Tags:** `ritual`, `1:1`, `retro`, `weekly`
- **Custom field "Tipo":** `ritual` pra filtrar no kanban
- **Automacao:** task recorrente que cria automaticamente

### Tracking de 1:1

Crie um Doc no ClickUp por pessoa com historico de 1:1s:
```
## 1:1 com [Nome] — [Data]
### Como ta
[notas]
### O que ta funcionando
[notas]
### O que ta travando
[notas]
### Feedback dado
[notas]
### Feedback recebido
[notas]
### Acoes
- [ ] [acao 1]
- [ ] [acao 2]
```
