# Templates - Research Brief Factory

Consulte este arquivo quando precisar gerar um brief copiavel para Deep Research, uma pergunta de discovery ou uma capsule de handoff.

Nao use estes templates como formulario burro. Preencha apenas com informacao relevante e corte o que nao muda a decisao.

---

## Template principal: Research brief decisorio

Copie e preencha:

<research_brief>
Titulo:
[Nome curto da decisao]

Objetivo da pesquisa:
[O que a pesquisa precisa descobrir para ajudar uma decisao real.]

Decisao a destravar:
[Depois da pesquisa, Patrick precisa escolher entre quais caminhos?]

Estrategia de pesquisa:
- Tipo: Single Mother Research | Sequential Research Series | Parallel Research Briefs | Discovery First
- Motivo: [Por que esta estrategia combina com a decisao, numero de areas e maturidade do contexto.]
- Trade-off: [Profundidade priorizada | quebra em serie | briefs paralelos | discovery antes.]
- Se a ferramenta perguntar amplitude vs profundidade: [Resposta curta e direta.]

Contexto atual:
- Sistema/projeto:
- Estado implementado:
- Papel ativo/permissao, se relevante:
- Restricoes de stack/ferramentas:
- Appetite/prazo/budget:

Evidencias locais:
- Evidencia 1:
  - Tipo: drift | bug real | gate falho | corrective loop | decisao cara | comparacao custo/qualidade
  - O que aconteceu:
  - Consequencia:
- Evidencia 2:
  - Tipo:
  - O que aconteceu:
  - Consequencia:
- Evidencia 3:
  - Tipo:
  - O que aconteceu:
  - Consequencia:

Gaps:
- [O que ainda nao sabemos e precisa de pesquisa externa.]
- [O que ainda depende de observacao local e nao deve ser terceirizado para pesquisa.]

Hipoteses falsificaveis:
- H1: [Se X for verdade, deveriamos observar Y.]
- H2: [Se X for falso, a recomendacao muda para Z.]
- H3: [Aposta de risco que a pesquisa precisa pressionar.]

Perguntas de pesquisa:
1. [Pergunta especifica ligada a uma hipotese ou gap.]
2. [Pergunta especifica ligada a decisao.]
3. [Pergunta sobre trade-off, custo, risco ou alternativa.]

Fontes desejadas:
- Docs oficiais:
- Papers/livros/frameworks:
- Repos/cases reais:
- Benchmarks/comparativos:
- Comunidades ou discussoes tecnicas:

Fora de escopo:
- [Tema que parece relacionado, mas nao ajuda a decisao.]
- [Decisao ja tomada.]
- [Pesquisa introdutoria/generica que nao deve consumir tempo.]

Formato esperado da resposta:
- Resumo executivo de 5-10 linhas.
- Matriz comparando alternativas por criterios.
- Recomendacao final com confianca: alta | media | baixa.
- Trade-offs e riscos residuais.
- Proximas acoes testaveis.
- Perguntas que continuam abertas.

Criterios de qualidade:
- A resposta precisa mudar ou confirmar uma decisao.
- A resposta deve citar onde a evidencia externa contradiz ou confirma os traces locais.
- A resposta deve separar fatos, inferencias e opinioes.
- A resposta deve dizer quando nao ha evidencia suficiente.
</research_brief>

---

## Template curto: Estrategia de pesquisa

Use antes do prompt final quando houver muitos subtemas, 5+ areas ou 5+ hipoteses.

Estrategia escolhida: [Single Mother Research | Sequential Research Series | Parallel Research Briefs | Discovery First]

Motivo:
[Uma frase explicando se existe decisao mae, dependencia sequencial, independencia dos subtemas ou falta de discovery.]

Como responder amplitude vs profundidade:
- Single Mother Research: "Priorize profundidade alta nos gaps criticos da decisao central. Faca triagem ampla apenas para mapear riscos e alternativas; deixe follow-ups no fim."
- Sequential Research Series: "Esta primeira pesquisa deve decidir as proximas pesquisas. Priorize criterios de quebra, dependencias e perguntas filhas candidatas."
- Parallel Research Briefs: "Nao comprima tudo em uma pesquisa. Gere briefs separados por subtema independente."
- Discovery First: "Nao rode Deep Research final ainda. Primeiro feche decisao, evidencia local e anti-escopo."

---

## Template curto: Discovery antes do brief

Use quando o pedido ainda nao tem decisao, evidencia ou escopo.

Antes de montar o research brief, preciso fechar 3 pontos:

1. Decisao:
Qual escolha essa pesquisa precisa destravar?

2. Evidencia local:
Qual incidente, trace, bug, gate falho, corrective loop ou comparacao real mostrou que isso importa?

3. Anti-escopo:
O que voce nao quer que a pesquisa cubra agora?

Se a resposta for "nao sei", isso ainda e discovery. A proxima acao e observar ou fazer uma execucao manual, nao Deep Research.

---

## Template: Brief operacional para fresh session

Use quando o objetivo for abrir uma nova sessao com estado e permissao preservados.

<fresh_session_brief>
Checkpoint atual:
[Onde paramos.]

Modo obrigatorio:
[executor | reviewer | orchestrator | delegate-only | prompt factory | outro]

Contexto MVP:
[Resultado minimo que ainda importa.]

Estado implementado:
- [O que ja existe.]
- [O que nao deve ser refeito.]

Objetivo desta sessao:
- [Decisao ou entrega esperada.]

Primeira acao permitida:
[Acao concreta e pequena.]

Acoes proibidas:
- [O que causaria drift.]
- [O que depende de gate ainda aberto.]

Gates abertos:
- [Validacao, aprovacao, review ou teste pendente.]

Riscos residuais:
- [Risco que a nova sessao precisa lembrar.]
</fresh_session_brief>

---

## Template: Resume capsule pos-drift

Use quando uma sessao perdeu papel, permissao, escopo ou sequencia de wave.

<resume_capsule>
ACTIVE_ROLE:
[Papel que deve continuar.]

DIRECT_WRITE_PERMISSION:
[allowed | forbidden | only-listed-files | ask-first]

NEXT_ALLOWED_ACTION:
[A unica proxima acao valida.]

NEXT_FORBIDDEN_ACTION:
[A acao tentadora que deve ser evitada.]

OPEN_GATES:
- [Gate ainda aberto.]

CURRENT_WAVE:
[Wave atual e limite de escopo.]

RESIDUAL_RISKS:
- [Risco que continua vivo.]

WHY_THIS_EXISTS:
[Qual drift ou falha este capsule esta prevenindo.]
</resume_capsule>

---

## Template: Politica de trace

Use quando o contexto veio grande demais e precisa separar evidencia de ruido.

<trace_policy>
Registrar somente:
- Drift: o agente mudou de papel, permissao ou objetivo.
- Bug real: comportamento quebrado com consequencia observavel.
- Gate falho: validacao obrigatoria falhou ou foi ignorada.
- Corrective loop: erro exigiu nova wave/correcao.
- Decisao cara: escolha com impacto em custo, arquitetura, equipe ou cliente.
- Comparacao custo/qualidade: evidencia de trade-off entre caminhos.

Nao registrar:
- Opiniao sem incidente.
- Preferencia sem consequencia.
- Conversa casual.
- Tentativa abandonada sem aprendizado.
- Contexto que nao muda decisao.
</trace_policy>

---

## Template: Pedido para Deep Research

Use este bloco como mensagem final para a ferramenta/agente de pesquisa.

Voce vai executar uma pesquisa profunda para apoiar uma decisao especifica. Nao faca uma visao geral do tema.

Use o brief abaixo como fonte principal. Priorize evidencias que confirmem, contradigam ou refinem as hipoteses. Quando uma fonte externa nao se aplicar ao contexto local, diga explicitamente por que.

Entregue:
- Resumo executivo.
- Matriz de alternativas.
- Evidencias mais fortes.
- Riscos e trade-offs.
- Recomendacao com nivel de confianca.
- Proximas acoes testaveis.

Brief:
[Cole aqui o research_brief preenchido.]
