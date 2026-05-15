# Exemplos - Research Brief Factory

Consulte este arquivo quando precisar calibrar o que e um brief bom, um brief ruim ou um caso de teste para Deep Research.

---

## Principio central

Deep Research bom comeca com diagnostico local, decisao-alvo, anti-escopo, evidencias locais e hipoteses falsificaveis. Nao comeca com curiosidade aberta.

Esta skill nao executa pesquisa. Ela transforma contexto operacional baguncado em um brief decisorio para outra sessao, ferramenta ou agente de pesquisa profunda.

---

## Exemplos bons

### 1. AO/Maestro Deep Research

**Situacao:** Patrick queria investigar como melhorar AO/Maestro com base em cursos, traces e falhas reais.

**Estrutura boa:**
- Contexto do sistema: qual ecossistema esta sendo analisado e quais componentes importam.
- Aprendizados dos cursos: conceitos ja absorvidos, sem pedir para a pesquisa redescobrir o basico.
- Evidencias reais dos traces: exemplos de drift, custo, falha de gate, loop corretivo ou comparacao de qualidade.
- Gaps: o que ainda nao esta claro localmente.
- Hipoteses: afirmacoes testaveis, nao opinioes soltas.
- O que pesquisar: perguntas externas especificas.
- Nao quero: decisoes ja tomadas, docs genericas, conteudo introdutorio.
- Formato esperado: matriz, recomendacao, trade-offs, criterios de decisao.

**Por que funciona:** a pesquisa externa entra para resolver incerteza real, nao para substituir observacao local.

### 1.1 AO/Maestro grande demais: amplitude vs densidade

**Situacao:** o brief AO/Maestro juntou muitas areas e hipoteses. A ferramenta de Deep Research perguntou se deveria cobrir mais areas com menos densidade ou menos areas com profundidade maior.

**Resposta correta:**
- Estrategia: Single Mother Research adversarial.
- Decisao mae: como evoluir AO/Maestro sem reforcar drift, custo inutil ou bypass de gate.
- Trade-off: menos areas, profundidade alta nos gaps criticos.
- Triagem: mapear areas perifericas so para detectar riscos e follow-ups.
- Follow-ups: listar no fim pesquisas filhas candidatas, sem tentar resolver tudo agora.

**Mensagem curta para a ferramenta:**
"Use Single Mother Research. Priorize profundidade alta nos gaps criticos da decisao mae; faca triagem ampla apenas para nao perder riscos relevantes. Nao tente cobrir todas as areas com a mesma densidade. Termine com follow-ups/pesquisas filhas candidatas."

**Por que funciona:** a decisao central continuava unica, mas o escopo tinha inchado. Quebrar cedo demais perderia o raciocinio mae; cobrir tudo raso produziria relatorio bonito e pouco acionavel.

### 2. MktOps fresh session

**Situacao:** era preciso abrir uma nova sessao com estado operacional preservado.

**Estrutura boa:**
- Checkpoint atual: onde o projeto parou.
- Modo obrigatorio: executor, reviewer, orchestrator, delegate-only ou outro papel ativo.
- Contexto MVP: qual resultado minimo ainda importa.
- Estado implementado: o que ja existe e nao deve ser refeito.
- Objetivos: o que a proxima sessao precisa decidir ou produzir.
- Primeira acao sugerida: proximo passo permitido.
- Proibicoes: o que nao pode fazer agora.

**Por que funciona:** brief operacional precisa estado atual, restricoes e proximo passo permitido. Sem isso, a proxima sessao inventa direcao.

### 3. Resume capsule pos-drift

**Situacao:** uma sessao desviou de papel, permissao ou escopo e precisava retomar sem repetir o erro.

**Estrutura boa:**
- ACTIVE_ROLE: papel atual que deve ser preservado.
- DIRECT_WRITE_PERMISSION: se pode editar diretamente ou apenas delegar.
- NEXT_ALLOWED_ACTION: unica proxima acao valida.
- NEXT_FORBIDDEN_ACTION: acao tentadora que causaria drift.
- OPEN_GATES: validacoes ou aprovacoes ainda abertas.
- CURRENT_WAVE: wave atual e limite de escopo.
- RESIDUAL_RISKS: riscos que seguem vivos mesmo depois da correcao.

**Por que funciona:** handoff bom preserva permissao, nao so contexto.

---

## Exemplos ruins e correcao

### Ruim 1. "Melhorar prompt/instrucoes" virou edicao documental

**Sintoma:** o pedido parecia discovery, mas o modelo comecou a editar AGENTS.md, SKILL.md ou rules.

**Faltou no brief:**
- Declarar se o objetivo e discovery, pesquisa externa ou mudanca de docs.
- Anti-escopo: nao editar documentos agora.
- Gate de confirmacao antes de alterar arquivo instrucional.

**Correcao:** antes de fabricar o brief, perguntar:
"Isso e discovery, pesquisa externa ou mudanca de docs?"

### Ruim 2. Trace amplo virou ruido

**Sintoma:** tudo virou evidencia: opiniao, conversa casual, tentativa sem consequencia, preferencia vaga.

**Faltou no brief:**
- Politica de trace.
- Criterio do que conta como evidencia local.
- Separacao entre sinal forte e contexto narrativo.

**Correcao:** usar `trace_policy`:
- Registrar drift.
- Registrar bug real.
- Registrar gate falho.
- Registrar corrective loop.
- Registrar decisao cara.
- Registrar comparacao custo/qualidade.
- Ignorar ruido que nao muda decisao.

### Ruim 3. Criar skill cedo demais

**Sintoma:** uma intuicao virou skill antes de existir repeticao suficiente.

**Faltou no brief:**
- Evidencia de recorrencia.
- Bons e ruins concretos.
- Manual run anterior.

**Correcao:** gate minimo antes de propor skill:
- 3 exemplos bons.
- 3 exemplos ruins.
- 1 tentativa manual executada.
- Decisao clara de por que prompt avulso, checklist ou doc nao basta.

---

## Test cases

### Forte

**Input:** "Tenho 4 traces de AO onde o modelo saiu de orchestrator para executor, 2 gates falharam, e preciso pesquisar como desenhar handoffs que preservam permissao."

**Esperado:** brief com decisao-alvo, evidencias locais, hipoteses sobre permissao/role drift, fontes desejadas e anti-escopo contra editar docs imediatamente.

### Fraco

**Input:** "Pesquisa melhores praticas de Deep Research."

**Esperado:** recusar o brief generico e perguntar qual decisao a pesquisa precisa destravar.

### Sem evidencia

**Input:** "Acho que a skill de pesquisa vai ser util."

**Esperado:** tratar como discovery, pedir incidentes reais e perguntar se houve manual run.

### Contexto demais

**Input:** colagem longa com conversa, traces, planos e decisoes misturadas.

**Esperado:** comprimir em diagnostico local, separar evidencia de ruido, declarar gaps e descartar material que nao muda a decisao.

### Decisao estrategica: AO proprio vs nativo

**Input:** "Quero pesquisar se construo AO proprio ou uso recursos nativos do Codex/Claude."

**Esperado:** brief decisorio com criterios de custo, controle, confiabilidade, manutencao, lock-in, capacidade nativa e ponto de alinhamento com Willy antes de decisao final.
