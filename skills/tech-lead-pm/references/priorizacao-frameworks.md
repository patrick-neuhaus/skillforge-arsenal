# Priorizacao — Frameworks Detalhados

Guia completo de todos os frameworks de priorizacao usados na skill.

## Framework 1: Impacto x Esforco (dia a dia)

|  | Baixo esforco | Alto esforco |
|--|---------------|-------------|
| **Alto impacto** | FAZ AGORA | PLANEJA (agenda, delega) |
| **Baixo impacto** | DELEGA ou AUTOMATIZA | NAO FAZ |

**Quando usar:** decisoes rapidas do dia a dia, triagem de demandas.
**Limite:** subjetivo. Funciona bem pra 5-10 itens, nao pra backlog grande.

## Framework 2: RICE (backlog de produto)

**Formula:** Reach x Impact x Confidence / Effort

| Componente | O que mede | Escala |
|------------|-----------|--------|
| Reach | Quantas pessoas afeta no periodo | Numero absoluto |
| Impact | Quanto muda pra cada pessoa | 0.25 (minimo) a 3 (massivo) |
| Confidence | Quao certo voce esta dos numeros | 50% a 100% |
| Effort | Pessoa-semanas de trabalho | Numero absoluto |

**Quando usar:** backlog de produto, lista de melhorias, priorizacao de features.
**Quando NAO usar:** decisoes do dia a dia (overkill), quando nao tem dados de Reach.

## Framework 3: ICE (experimentos rapidos)

**Formula:** Impact x Confidence x Ease (1-10 cada)

| Componente | Descricao | Escala |
|------------|-----------|--------|
| Impact | Quanto impacto se funcionar | 1-10 |
| Confidence | Quao certo que vai funcionar | 1-10 |
| Ease | Quao facil de implementar | 1-10 |

**Quando usar:** growth hacking, experimentos, ideias rapidas, quando nao tem dados de Reach.
**Cuidado:** scores sao subjetivos. Se tudo ta dando 8-9-10, alguem ta mentindo. Force-rank: se dois itens tem score igual, qual voce faria primeiro? Ajuste os scores.

## Framework 4: WSJF (portfolio com urgencia)

**Formula:** Cost of Delay / Job Size

**Cost of Delay** = User Value + Time Criticality + Risk Reduction

| Componente | O que mede |
|------------|-----------|
| User Value | Quanto valor entrega pro usuario |
| Time Criticality | Tem deadline? Perde valor com o tempo? |
| Risk Reduction | Reduz risco tecnico ou de negocio? |
| Job Size | Esforco relativo |

**Quando usar:** multiplos projetos competindo por recurso, precisa decidir qual vai primeiro.
**Quando NAO usar:** tasks do dia a dia (overkill). Use Impacto x Esforco.

## Framework 5: Kano Model (expectativa do usuario)

| Categoria | Se tem | Se nao tem | Exemplos |
|-----------|--------|-----------|----------|
| **Basico** | Nem nota | Reclama | Login funcionar, pagina carregar |
| **Performance** | Mais satisfeito | Menos satisfeito | Velocidade, busca precisa |
| **Encantamento** | Surpresa positiva | Nao nota | Sugestao inteligente, animacao |

**Regra pra MVP:** 100% basico, essencial de performance, ZERO encantamento.

## Framework 6: Caminho Critico (dependencias)

1. Liste todas as tarefas + dependencias
2. O caminho mais longo e o caminho critico
3. Qualquer atraso no critico atrasa o projeto inteiro
4. Foque recurso no caminho critico. Tasks fora dele tem folga.

**Quando usar:** projetos com multiplas tasks dependentes, quando precisa saber "o que atrasa TUDO se atrasar".

## Processo Pratico de Priorizacao

Use esse roteiro quando alguem disser "ta tudo urgente":

1. Liste tudo que ta "urgente"
2. Pra cada item: **"Se eu NAO fizer isso essa semana, o que acontece de CONCRETO?"**
3. Se a resposta for vaga ("pode dar problema", "seria bom ter") → nao e urgente
4. Classifique o que sobrou com o framework adequado
5. Se mais de 3 itens ficaram no topo, algo ta errado — force-rank
6. O que ficou no fundo — MATA (nao "adia", mata. Se for importante, volta sozinho)

## Guia rapido: Qual Framework Usar

| Situacao | Framework | Por que |
|----------|-----------|---------|
| Triagem rapida do dia | Impacto x Esforco | Simples, visual, rapido |
| Backlog de produto | RICE | Dados quantitativos, comparavel |
| Ideias/experimentos | ICE | Rapido, sem precisar de dados |
| Projetos competindo | WSJF | Inclui urgencia e custo de atraso |
| Entender expectativa | Kano | Separa basico de encantamento |
| Dependencias | Caminho Critico | Identifica gargalos |
