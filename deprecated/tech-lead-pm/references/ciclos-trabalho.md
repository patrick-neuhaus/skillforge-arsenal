# Ciclos de Trabalho — Shape Up e DORA

Referencia para ciclos de trabalho e metricas de saude do time.

## Shape Up (Basecamp) — Alternativa a Scrum pra times pequenos

Shape Up foi criado pelo Basecamp pra times de 3-15 pessoas. Principio central: **fixed time, variable scope** — o tempo e fixo, o escopo se ajusta.

### Conceitos-chave

| Conceito | Descricao |
|----------|-----------|
| **Appetite** | Quanto tempo VALE gastar num problema. Nao e estimativa (quanto leva), e aposta (quanto estou disposto a investir). |
| **Shaping** | Antes de passar pra equipe, o lider define problema + solucao rough. Nem wireframe detalhado, nem "faz ai". |
| **Betting Table** | A cada ciclo, voce e Willy apostam em quais shaped projects entram. Se nao entrou, volta pro shaping ou morre. |
| **Cooldown** | 2 semanas entre ciclos pra bugs, tech debt, exploracao. Equipe escolhe no que trabalhar. |
| **Hill Chart** | Visualizar progresso como colina — subindo = descobrindo, descendo = implementando. Se ficou no topo muito tempo, tem problema de design. |

### Sizes

- **Small Batch:** 1-2 semanas. Tasks operacionais, melhorias pontuais.
- **Big Batch:** 6 semanas. Features completas, MVPs, redesigns.

### Quando usar Shape Up vs Kanban continuo

| Tipo de trabalho | Abordagem |
|-----------------|-----------|
| Projetos de produto (features, MVPs, redesigns) | Shape Up |
| Trabalho operacional (manutencao, suporte, bugs) | Kanban continuo |

Na pratica, voce provavelmente usa os dois: Shape Up pros projetos de cliente e produto, Kanban pro fluxo operacional do dia a dia.

### Implementacao no ClickUp

1. Crie uma **pasta por ciclo** ("Ciclo 1 — Mar/Abr", "Ciclo 2 — Mai/Jun")
2. Dentro, **listas por projeto shaped**
3. **Cooldown** como lista separada
4. **Tags:** `shaped`, `building`, `cooldown`
5. **Custom field "Appetite":** Small Batch / Big Batch
6. **Custom field "Hill":** Subindo / Topo / Descendo

### Shaping — Como fazer

O shaping e responsabilidade SUA (lider), nao do junior. E o equivalente a "pensar antes de mandar fazer".

1. **Defina o problema** — nao a solucao. "Clientes reclamam que nao sabem o status do pedido" (problema) vs "Criar pagina de tracking" (solucao).
2. **Defina o appetite** — quanto tempo vale gastar nisso? 1 semana? 6 semanas? Se nao vale mais de 1 semana, e Small Batch.
3. **Crie a solucao rough** — nao wireframe detalhado. Breadboarding (fluxo de telas com campos) ou fat marker sketch (rabisco grosso).
4. **Identifique rabbit holes** — onde a equipe pode se perder? Marque como "nao fazer" ou "simplificar".
5. **Escreva o pitch** — problema, appetite, solucao, rabbit holes, no-gos.

## DORA Metrics — Medir saude do time

4 metricas que times de elite usam (do livro Accelerate):

| Metrica | O que mede | Elite | Medio |
|---------|-----------|-------|-------|
| Deployment Frequency | Quantas vezes faz deploy | Multiplas/dia | 1x/semana a 1x/mes |
| Lead Time | Commit ate producao | <1 dia | 1 semana a 1 mes |
| Change Failure Rate | Deploys que causam problema | 0-15% | 16-30% |
| MTTR | Tempo pra recuperar de falha | <1 hora | <1 dia |

### Pra time pequeno: comece com 2

1. **Lead Time** (commit a producao) — indica fluxo de trabalho
2. **Change Failure Rate** — indica qualidade

### Diagnostico

| Sintoma | Causa provavel | Acao |
|---------|---------------|------|
| Lead Time alto (>1 semana) | Gargalo no processo (review? deploy? aprovacao?) | Mapear o pipeline e encontrar o gargalo |
| Change Failure Rate alto (>30%) | Problema de qualidade (tasks mal escritas? falta de review?) | Investir em criterios de aceitacao e review |
| Ambos altos | Processo inteiro precisa de atencao | Parar e redesenhar o fluxo |

### Como medir no ClickUp

- **Lead Time:** use o campo "Time in Status" do ClickUp. Meça o tempo entre "A Fazer" e "Concluido".
- **Change Failure Rate:** crie tag "retrabalho" pra tasks que voltaram de "Concluido" pra "Fazendo".
- **Dashboard:** crie um dashboard no ClickUp com esses dois indicadores. Revise semanalmente na weekly.
