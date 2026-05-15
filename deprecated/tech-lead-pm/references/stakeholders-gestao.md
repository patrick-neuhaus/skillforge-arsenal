# Stakeholders — Gestao e Frameworks

Referencia para gestao de stakeholders e tomada de decisao em equipe.

## Principios

1. **Cocriacao > imposicao.** Envolva o stakeholder na decisao — ele aceita melhor.
2. **Comunicacao cadenciada.** Nao espere perguntarem "como ta?" — mande update antes.
3. **Demandas nao planejadas:** "Se a gente fizer isso, o que sai do sprint atual?"
4. **Disagree and commit.** Se discordar e perder, execute o melhor possivel.

## DACI — Framework de Decisao Async

Quando precisa tomar decisao que envolve multiplas pessoas:

| Papel | Descricao |
|-------|-----------|
| **Driver** | Quem empurra a decisao pra frente (coleta info, recomenda) |
| **Approver** | UMA pessoa que decide (nao comite) |
| **Contributors** | Quem da input tecnico ou de negocio |
| **Informed** | Quem precisa saber do resultado |

### Template ClickUp

```
Decisao: [O que precisa ser decidido]
Driver: [Nome]
Approver: [Nome]
Contributors: [Nomes]
Informed: [Nomes]
Deadline: [Data]
Opcoes: [A, B, C]
Recomendacao do Driver: [Opcao + justificativa]
Decisao final: [Preenchido pelo Approver]
```

### Por que DACI funciona

Elimina o "reunionismo". O Driver faz o trabalho pesado de coletar info, o Approver decide, todo mundo sabe seu papel. Nao precisa de call pra cada decisao.

### Quando usar DACI

- Decisao que afeta mais de 1 pessoa
- Decisao tecnica que pode ser controversa
- Mudanca de prioridade, escopo, ou prazo
- Escolha de stack, ferramenta, ou abordagem

### Quando NAO usar DACI

- Decisao que so afeta voce → decide sozinho
- Decisao urgente (<2h) → decide e informa depois
- Decisao operacional trivial → Decision Zones (Green/Yellow/Red)

## Tipos de Stakeholder

| Stakeholder | O que quer | Como comunicar | Frequencia |
|-------------|-----------|----------------|------------|
| Willy (chefe) | Ver crescimento como lider | Update + duvidas de gestao | Semanal (daily 9h e 1:1) |
| Cliente | Resultado, sentir controle | Status + proximos passos | Por entrega ou semanal |
| Equipe | Clareza, autonomia, crescimento | Tasks claras + feedback + 1:1 | Diario + semanal |

## Lidando com Stakeholder que Pede Algo que Nao Faz Sentido

### Roteiro

1. **"Qual problema isso resolve?"** → talvez a solucao seja outra
2. Se nao definir o problema → **"Sem entender o problema, corro risco de construir errado"**
3. Se insistir → **"Ok, entra no lugar de [Y]. Qual prioriza?"**
4. Se custo extra → **"Isso e escopo adicional. Posso orcar separado."**

### Principio

Nunca diga "nao" direto. Diga "sim, mas no lugar de [X]" ou "sim, mas com [impacto]". Isso forca o stakeholder a priorizar, nao voce a dizer nao.

## Comunicacao por Tipo de Stakeholder

### Com Willy (chefe/mentor)

- **Formato:** conciso, com dados, mostrando raciocinio
- **O que compartilhar:** decisoes tomadas, duvidas de gestao, bloqueios que voce nao consegue resolver
- **O que NAO compartilhar:** todo detalhe operacional. Ele quer ver que voce ta no controle, nao que voce precisa de ajuda pra tudo
- **Na daily 9h:** update de 2min max. O que fez, o que vai fazer, se precisa de input dele

### Com Clientes

Use a skill **comunicacao-clientes** pra comunicacao direta. Aqui e so o framework de gestao:
- Update antes de perguntarem
- Inclua sempre: o que foi feito, o que vem a seguir, se tem bloqueio
- Se vai atrasar: avise ANTES do prazo, nao no dia

### Com a Equipe

- Transparencia sobre prioridades e mudancas
- Contexto de negocio junto com tasks tecnicas
- Feedback regular (nao so quando da merda)
- Reconhecimento publico, correcao privada
