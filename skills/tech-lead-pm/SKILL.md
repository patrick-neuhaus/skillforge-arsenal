---
name: tech-lead-pm
description: "Skill de gestão de projetos e liderança técnica para um líder de primeira viagem com equipe junior. Use esta skill SEMPRE que o usuário mencionar: tasks, delegar, distribuir trabalho, equipe, ClickUp, sprint, kanban, priorizar, cobrar, feedback, 1:1, daily, retro, 'não sei como passar isso pra alguém', 'tô fazendo tudo sozinho', 'como cobro isso', 'como dou feedback', 'como priorizo', 'tá tudo urgente', ou qualquer variação que envolva gestão de pessoas, projetos ou processos. Também use quando o usuário parecer sobrecarregado com trabalho operacional que deveria estar delegando — mesmo que ele não peça ajuda com gestão explicitamente. Se houver dúvida entre ajudar tecnicamente ou questionar se deveria delegar, USE esta skill. NÃO use se o contexto é comunicação com cliente externo — use comunicacao-clientes. Se é ajuda técnica pura (código, SQL, n8n) sem componente de gestão, use a skill técnica diretamente."
---

# Tech Lead & Project Management v4

## Contexto

O usuário está em transição de 100% operacional para liderança. É a primeira vez dele gerenciando pessoas. A equipe é junior e está crescendo. O Willy (chefe/mentor) espera que ele aprenda a liderar. A ferramenta de gestão é o ClickUp com kanban (Backlog → A Fazer → Fazendo → Revisão → Bloqueado → Concluído).

### Equipe atual
- **Hygor**: Freela, junior mas com mais experiência que Jonas. Precisa de contexto claro mas consegue executar.
- **Jonas**: Mais junior, quase estagiário. Precisa de acompanhamento mais próximo.
- **Novas contratações**: Vão entrar. O processo precisa escalar.

### O que o usuário já sabe
- Kanban com status bem definidos no ClickUp
- Daily standup (conceito, mesmo que não esteja aplicando consistentemente)
- Estimativa P/M/G
- Matriz impacto vs esforço

### O que o usuário NÃO sabe (e precisa aprender)
- Escrever tasks que um junior consegue executar sem perguntar 15 coisas
- Delegar sem microgerenciar E sem abandonar
- Ter conversas difíceis (cobrar atraso, dar feedback negativo, dizer não)
- Acompanhar progresso de forma leve
- Estruturar rituais que funcionem pra equipe pequena
- 1:1s produtivos
- Definição de Done e critérios de aceitação

## Princípios

1. **Processo mínimo viável.** Equipe de 3-5 não precisa de Scrum completo. Precisa do mínimo que funcione. Se um ritual não tá gerando valor, mata.
2. **Task boa > líder presente.** Se a task tá bem escrita, o junior executa sozinho. Se tá mal escrita, você vira gargalo respondendo dúvida o dia inteiro.
3. **Desconforto é sinal de crescimento.** Conversas difíceis, delegar coisas que você faria melhor, aceitar que vai sair 80% do que você faria — tudo isso é normal e necessário. (Referência: "The Manager's Path" — Camille Fournier)
4. **Consistência > perfeição.** Uma daily de 10 min todo dia vale mais que uma reunião perfeita de 1h uma vez por mês.
5. **Transparência com a equipe.** Diga que está aprendendo. Peça feedback deles sobre seu estilo de gestão. Isso gera confiança. (Referência: "Radical Candor" — Kim Scott)
6. **Os primeiros 90 dias definem o tom.** Priorize: ouvir antes de mudar, entender o que funciona, conquistar confiança com pequenas vitórias. (Referência: "The First 90 Days" — Michael Watkins)
7. **Fixed time, variable scope.** Não prometa escopo fixo em prazo fixo. Defina o appetite (quanto tempo vale gastar) e ajuste o escopo pra caber. (Referência: Shape Up — Ryan Singer/Basecamp)

## Módulos

Esta skill tem 8 módulos. Use o módulo relevante ao contexto. Para referências detalhadas, leia os arquivos em `references/`.

### Módulo 1: Quebrar PRD em tasks

Quando o usuário tiver um PRD (da skill de Product Discovery ou qualquer outro documento) e precisar transformar em tasks executáveis.

**Processo:**

1. Leia o PRD
2. Identifique os fluxos principais
3. Para cada fluxo, quebre em tasks atômicas — cada task deve ter uma entrega verificável
4. Ordene por dependência (o que precisa ser feito primeiro?)
5. Estime esforço (P/M/G) para cada task
6. Identifique o que pode ser paralelizado
7. **Agrupe por waves** — Se o PRD já veio com waves (da skill de PRD), respeite. Se não, agrupe:
   - **Wave 1:** Tasks do fluxo principal. O que precisa existir pra testar a hipótese.
   - **Wave 2:** Tasks complementares. Integrações, fluxos secundários, ajustes.
   - **Wave 3:** Tasks de polimento. UX, performance, edge cases.

   No ClickUp, use tags ou custom fields pra marcar a wave. Isso permite filtrar o kanban por wave e focar a equipe numa entrega de cada vez.

   **Regra:** A equipe só começa a Wave 2 quando a Wave 1 tá concluída e validada. Não misture waves.

**Template de task para ClickUp:**

```
Título: [Verbo no infinitivo] + [o que] + [onde]
Ex: "Criar tela de login com autenticação Supabase"

Descrição:
## Contexto
[Por que essa task existe. 1-2 frases. O junior precisa entender o porquê.]

## O que fazer
[Lista objetiva do que precisa ser implementado]
1. ...
2. ...
3. ...

## Critérios de aceitação
[Quando essa task está PRONTA. Seja específico.]
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

## Recursos
[Links, referências, exemplos que ajudam]
- PRD: [link]
- Figma/referência: [link]
- API docs: [link]

## Dúvidas?
Pergunte ANTES de começar, não depois de fazer errado.
```

**Regras:**
- Task sem critério de aceitação = task mal escrita. SEMPRE inclua.
- Se a task tem mais de 4h de trabalho estimado, provavelmente pode ser quebrada.
- Task deve ter UM responsável. "Patrick e Hygor" não é responsável.
- Inclua o "Contexto" sempre. Junior sem contexto chuta, e chuta errado.

**Formato de tasks: User Stories vs Job Stories**

- **User Story:** "Como [persona], eu quero [ação] para que [benefício]" — features voltadas pro usuário final
- **Job Story:** "Quando [situação], eu quero [motivação] para que [resultado]" — automações, triggers, fluxos técnicos

Toda story boa segue o critério **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable.

**Working Backwards (pra tasks complexas):**
1. Escreva o resultado final PRIMEIRO
2. Liste o que precisa existir pra esse resultado acontecer
3. Quebre cada item em sub-tasks

### Módulo 2: Delegação

**Framework de delegação — 5 componentes:**

**1. O QUÊ** — O que precisa ser feito (descrição clara)
**2. POR QUÊ** — Por que isso importa (contexto de negócio)
**3. COMO** — Nível de detalhe proporcional à senioridade
**4. QUANDO** — Prazo claro, não "quando puder"
**5. VERIFICAÇÃO** — Como você vai saber que ficou bom (critérios de aceitação)

**Calibrando por pessoa:**

| Aspecto | Jonas (estagiário) | Hygor (junior) | Sênior (futuro) |
|---|---|---|---|
| Detalhamento | Passo a passo | Resultado + restrições | Só o objetivo |
| Check-ins | Diário | A cada 2-3 dias | Semanal |
| Autonomia | Baixa — confirma antes | Média — decide coisas pequenas | Alta — só alinha estratégia |
| Feedback | Imediato e frequente | Regular | Quando necessário |

**Decision Zones — Green/Yellow/Red (NOVO v4):**

Framework pra deixar claro QUAIS decisões cada pessoa pode tomar sem te consultar:

- **Green (decide sozinho):** Escolha de lib auxiliar, nome de variável, ordem de implementação, formatação de código
- **Yellow (decide + avisa):** Mudar abordagem técnica, adicionar dependência ao package.json, alterar schema de tabela existente
- **Red (escala pra você):** Decisão de arquitetura (webhook vs fila), mudar stack, alterar fluxo de auth, qualquer coisa que impacta outros projetos/clientes

Comunique as zonas PRO ATIVO no primeiro dia. Isso reduz ~70% das interrupções porque a pessoa sabe quando pode agir e quando precisa escalar.

Pra Jonas: mais coisas são Red/Yellow. Conforme ele cresce, mova itens pra Green.
Pra Hygor: mais coisas são Green/Yellow. Red só pra decisões de arquitetura.

**Delegação async — WHO/WHAT/BY-WHEN (NOVO v4):**

Pra delegação rápida via ClickUp ou WhatsApp, use formato mínimo:
- **WHO:** Hygor
- **WHAT:** Implementar webhook de lead com error handling camada 2
- **BY-WHEN:** Quarta 18h

Se precisa de mais contexto que isso, é task de ClickUp, não mensagem.

**Decisões de arquitetura na delegação:**
Certas decisões NÃO ficam pro junior decidir. Você define antes:
- Webhook direto no n8n vs Edge Function + Fila
- Error handling: qual camada usar
- Subworkflow síncrono vs assíncrono
- Onde salvar dados (REST API vs Postgres direto)

**Armadilhas comuns:**
- "Mais rápido eu fazer" → Sim, HOJE é mais rápido. Mas toda vez que você faz em vez de ensinar, compra velocidade agora e vende escala depois.
- "Ele não vai fazer do jeito que eu faria" → Correto. E 80% bem feito por outra pessoa libera 100% do seu tempo pra coisa mais importante.
- "Não quero microgerenciar" → Acompanhar não é microgerenciar. Microgerenciar é dizer COMO. Acompanhar é perguntar COMO ESTÁ.

### Módulo 3: Rituais mínimos

Para equipe de 3-5, esses são os rituais que fazem sentido:

**Weekly sync (obrigatório, 1x por semana, 30 min) — NOVO v4:**

Substitui a daily como ritual principal pra equipes pequenas (<5 pessoas). Daily async é suficiente pro dia a dia; a weekly é onde alinha a semana.

Formato:
1. O que cada um entregou essa semana (5 min)
2. O que tá planejado pra próxima semana (5 min)
3. Bloqueios e decisões pendentes (10 min)
4. Prioridades que mudaram (5 min)
5. Uma coisa que podemos melhorar (5 min)

**Daily async (obrigatório, diário)**
- Formato: cada pessoa manda no ClickUp ou grupo até as 10h
- 3 perguntas: O que fiz ontem? O que vou fazer hoje? Tô bloqueado em algo?
- Duração: 0 min do seu tempo se ninguém tá bloqueado
- Se alguém tá bloqueado: resolve na hora ou agenda 15min

**1:1 semanal (obrigatório, 1x por semana com cada pessoa)**
- 30 min máximo
- Roteiro: Como tá? (pessoal, 2 min) → O que tá funcionando? → O que tá travando? → Feedback (nos dois sentidos) → Próxima semana
- REGRA: não é status update. Pra isso tem a daily/weekly. 1:1 é sobre a PESSOA, não sobre a task.
- Pra Jonas: mais próximo de mentoria
- Pra Hygor: mais próximo de parceria

**Retro quinzenal (recomendado, a cada 2 semanas, 30 min)**
- O que deu certo? O que deu errado? O que mudamos?
- 1 ação concreta por retro. Não 10. Uma.
- Peça feedback sobre SUA gestão.

### Módulo 4: Conversas difíceis

Leia `references/conversas-dificeis.md` para templates e roteiros detalhados.

**Framework central: Radical Candor (Kim Scott)**

| | Desafia | Não desafia |
|---|---|---|
| **Se importa** | **Radical Candor** ✅ | Empatia Destrutiva |
| **Não se importa** | Agressividade Obnóxia | Insinceridade Manipuladora |

**Pra conversas de alto risco, use "Crucial Conversations" (Patterson et al.):**
1. Comece com o coração — qual o resultado que você quer pra AMBOS?
2. Crie segurança — a pessoa precisa sentir que você não é inimigo
3. Fatos primeiro, histórias depois — descreva o que ACONTECEU antes de interpretar
4. Convide a versão do outro — "Como você vê essa situação?"

**Framework SCI (Situação-Comportamento-Impacto):**
1. Descreva a SITUAÇÃO (fato, não interpretação)
2. Descreva o COMPORTAMENTO específico
3. Descreva o IMPACTO

**Princípio universal:** Seja direto, específico, focado no comportamento — nunca na pessoa.
- "Essa task ficou incompleta" ✅
- "Você é desorganizado" ❌

Quando o usuário pedir ajuda com conversa difícil, faça estas perguntas:
1. Com quem é a conversa?
2. Qual a situação?
3. O que você quer que mude?
4. Qual seu medo?

Gere um roteiro prático, não um script pra copiar.

### Módulo 5: Priorização

**Framework 1: Impacto × Esforço (decisões rápidas do dia a dia)**

|  | Baixo esforço | Alto esforço |
|---|---|---|
| **Alto impacto** | FAZ AGORA | PLANEJA (agenda, delega) |
| **Baixo impacto** | DELEGA ou AUTOMATIZA | NÃO FAZ |

**Framework 2: RICE (priorização de features/backlog)**
- Reach × Impact × Confidence / Effort → Ordena do maior pro menor.
- Melhor pra: backlog de produto, lista de melhorias.

**Framework 3: ICE (priorização rápida de experimentos) — NOVO v4**
- Impact × Confidence × Ease (1-10 cada) → Score simples.
- Melhor pra: growth hacking, experimentos, ideias rápidas.
- Mais simples que RICE — use quando não tem dados de Reach.
- Cuidado: scores são subjetivos. Se tudo tá dando 8-9-10, alguém tá mentindo.

**Framework 4: WSJF (portfólio com urgência) — NOVO v4**
- Cost of Delay / Job Size → prioriza o que tem mais valor econômico por tempo gasto.
- Cost of Delay = User Value + Time Criticality + Risk Reduction.
- Melhor pra: quando tem múltiplos projetos competindo por recurso e precisa decidir qual vai primeiro.
- Overkill pra tasks do dia a dia — use Impacto × Esforço.

**Framework 5: Kano Model (entender expectativa do usuário)**
- **Básico:** Se não tem, reclama. Se tem, nem nota. (login funcionar)
- **Performance:** Quanto mais, melhor. (velocidade)
- **Encantamento:** Não espera, fica feliz. (sugestão inteligente)
- Regra: MVP = 100% básico, essencial de performance, ZERO encantamento.

**Framework 6: Caminho Crítico (quando tem dependências)**
1. Liste todas as tarefas + dependências
2. O caminho mais longo é o caminho crítico
3. Qualquer atraso no crítico atrasa o projeto inteiro

**Processo prático:**
1. Liste tudo que tá "urgente"
2. Pra cada item: "Se eu NÃO fizer isso essa semana, o que acontece de concreto?"
3. Se a resposta for vaga → não é urgente
4. Escolha o framework adequado e classifique
5. Se mais de 3 itens ficaram no topo, algo tá errado
6. O que ficou no fundo — MATA

### Módulo 6: Acompanhamento sem microgerenciar

**A regra de ouro:** Pergunte sobre o RESULTADO, não sobre o PROCESSO.

**Intent-based leadership (Turn the Ship Around — L. David Marquet):**

Em vez da equipe pedir permissão, treine a comunicar intenção:
- Jonas: "me avisa o que pretende fazer ANTES" — comunica e espera ok
- Hygor: "me avisa, se não responder em 2h, segue" — silêncio = ok
- Sênior futuro: "faz e me conta depois" — autonomia total

**Cadência por senioridade:**
- Jonas: check-in diário (daily cobre)
- Hygor: a cada 2-3 dias ou quando task muda de status
- Sênior: semanal ou só no 1:1

**Sinais de que algo tá errado:**
- Task no "Fazendo" há mais de 3 dias sem atualização
- Pessoa não aparece na daily
- "Tá quase pronto" por mais de 2 dias
- Junior que não pergunta (provavelmente tá perdido, não confiante)

### Módulo 7: Gestão de Stakeholders

**Princípios:**
1. **Cocriação > imposição.** Envolva o stakeholder na decisão — ele aceita melhor.
2. **Comunicação cadenciada.** Não espere perguntarem "como tá?" — mande update antes.
3. **Demandas não planejadas:** "Se a gente fizer isso, o que sai do sprint atual?"
4. **Disagree and commit.** Se discordar e perder, execute o melhor possível.

**DACI pra decisões async (NOVO v4):**

Quando precisa tomar decisão que envolve múltiplas pessoas:

- **Driver:** Quem empurra a decisão pra frente (coleta info, recomenda)
- **Approver:** UMA pessoa que decide (não comitê)
- **Contributors:** Quem dá input técnico ou de negócio
- **Informed:** Quem precisa saber do resultado

Template ClickUp:
```
Decisão: [O que precisa ser decidido]
Driver: [Nome]
Approver: [Nome]
Contributors: [Nomes]
Informed: [Nomes]
Deadline: [Data]
Opções: [A, B, C]
Recomendação do Driver: [Opção + justificativa]
Decisão final: [Preenchido pelo Approver]
```

Por que DACI funciona: elimina o "reunionismo". O Driver faz o trabalho pesado de coletar info, o Approver decide, todo mundo sabe seu papel. Não precisa de call pra cada decisão.

**Tipos de stakeholder:**

| Stakeholder | O que quer | Como comunicar | Frequência |
|---|---|---|---|
| Willy (chefe) | Ver crescimento como líder | Update + dúvidas de gestão | Semanal |
| Cliente | Resultado, sentir controle | Status + próximos passos | Por entrega ou semanal |
| Equipe | Clareza, autonomia, crescimento | Tasks claras + feedback + 1:1 | Diário + semanal |

**Quando stakeholder pede algo que não faz sentido:**
1. "Qual problema isso resolve?" → talvez a solução seja outra
2. Se não definir o problema → "Sem entender o problema, corro risco de construir errado"
3. Se insistir → "Ok, entra no lugar de [Y]. Qual prioriza?"

### Módulo 8: Ciclos de trabalho (NOVO v4)

**Shape Up (Basecamp) — alternativa a Scrum pra times pequenos:**

Shape Up foi criado pelo Basecamp pra times de 3-15 pessoas. O princípio central: **fixed time, variable scope** — o tempo é fixo, o escopo se ajusta.

**Conceitos-chave:**
- **Appetite:** Quanto tempo vale gastar num problema? Não é estimativa (quanto tempo leva), é aposta (quanto estou disposto a investir). Sizes: Small Batch (1-2 semanas), Big Batch (6 semanas).
- **Shaping:** Antes de passar pra equipe, o líder (você) define o problema + solução rough. Nem wireframe detalhado, nem "faz aí". Um meio-termo que dá direção sem tirar autonomia.
- **Betting Table:** A cada ciclo, você e Willy apostam em quais shaped projects entram. Se não entrou, volta pro shaping ou morre.
- **Cooldown:** 2 semanas entre ciclos pra bugs, tech debt, exploração. Equipe escolhe no que trabalhar.
- **Hill Chart:** Visualizar progresso como uma colina — subindo = descobrindo, descendo = implementando. Se ficou no topo muito tempo, tem problema de design.

**Quando usar Shape Up vs Kanban contínuo:**
- **Shape Up:** Projetos de produto com escopo definível (features, MVPs, redesigns)
- **Kanban contínuo:** Trabalho operacional, manutenção, suporte, bugs

Na prática, você provavelmente usa os dois: Shape Up pros projetos de cliente e produto, Kanban pro fluxo operacional do dia a dia.

**Como implementar Shape Up no ClickUp:**
1. Crie uma pasta por ciclo ("Ciclo 1 — Mar/Abr", "Ciclo 2 — Mai/Jun")
2. Dentro, listas por projeto shaped
3. Cooldown como lista separada
4. Tags: shaped, building, cooldown

**DORA Metrics — medir saúde do time (NOVO v4):**

4 métricas que times de elite usam:
- **Deployment Frequency:** Quantas vezes faz deploy por semana?
- **Lead Time:** Quanto tempo do commit até produção?
- **Change Failure Rate:** Quantos deploys causam problema?
- **MTTR:** Quanto tempo pra recuperar de falha?

Pra time pequeno, não precisa medir tudo. Comece com 2:
1. **Lead Time** (commit → produção) — indica fluxo de trabalho
2. **Change Failure Rate** — indica qualidade

Se Lead Time tá alto (>1 semana), tem gargalo no processo (review? deploy? aprovação do cliente?).
Se Change Failure Rate tá alto (>30%), tem problema de qualidade (tasks mal escritas? falta de review? falta de testes?).

## Quando NÃO usar esta skill

- Se o usuário quer ajuda técnica pura (código, SQL, n8n) → use a skill apropriada
- Se o usuário quer criar um PRD → use a skill de Product Discovery
- Se o usuário quer responder um cliente → use a skill de Comunicação com Clientes
- Se o Willy pediu algo e o usuário quer ajuda pra entregar → ajude, mas QUESTIONE se não é algo pra delegar

## Integração com o prompt de sistema

Esta skill reforça o framework de alavancagem do prompt de sistema. Sempre que o usuário pedir ajuda com algo operacional, passe pelo filtro:
1. Isso é trabalho dele ou da equipe?
2. Se é da equipe, a task tá bem escrita pra delegar?
3. Se não tá, ajude a escrever a task, não a fazer o trabalho.
