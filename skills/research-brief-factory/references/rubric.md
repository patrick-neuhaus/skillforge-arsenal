# Rubrica - Research Brief Factory

Consulte este arquivo para avaliar se um research brief esta pronto para Deep Research ou se ainda e discovery disfarçado.

---

## Gate rapido

Antes de entregar o brief, responda:

1. Existe uma decisao que a pesquisa precisa destravar?
2. O contexto atual esta resumido em estado verificavel, nao em narrativa solta?
3. Existem evidencias locais ou foi so sensacao?
4. Os gaps dizem o que falta saber?
5. As hipoteses podem ser confirmadas ou falsificadas?
6. O fora de escopo impede a pesquisa de virar curiosidade ampla?
7. O formato esperado orienta comparacao e decisao?
8. O brief escolhe explicitamente Single Mother Research, Sequential Research Series, Parallel Research Briefs ou Discovery First?
9. Se ha 5+ areas ou 5+ hipoteses, ele prioriza profundidade ou sugere quebra?

Se 1 ou 3 falhar, nao fabrique um brief final. Rode discovery primeiro.
Se 8 falhar em brief grande, nao entregue como final. Escolha a estrategia antes.

---

## Invariantes do brief

Todo brief forte deve conter:

- Objetivo da pesquisa: o que a pesquisa deve descobrir.
- Decisao: qual escolha sera tomada depois.
- Estrategia de pesquisa: single, series, parallel ou discovery, com motivo.
- Contexto atual: estado local, sistema, projeto, restricoes e papel ativo.
- Evidencias locais: traces, incidentes, bugs, gates, loops, comparacoes ou exemplos reais.
- Gaps: o que nao sabemos ainda.
- Hipoteses: afirmacoes testaveis que a pesquisa deve pressionar.
- Restricoes: tempo, stack, permissao, ferramentas, politica interna, budget ou appetite.
- Fora de escopo: o que a pesquisa nao deve cobrir.
- Fontes desejadas: tipos de fontes, comunidades, docs, papers, repos, benchmarks, cases.
- Formato esperado: matriz, recomendacao, plano, criterios, trade-offs ou perguntas respondidas.
- Criterios de qualidade: como saber se a pesquisa foi util.

---

## Score

Use score de 0 a 100.

### 90-100: pronto para Deep Research

Caracteristicas:
- Decisao-alvo explicita.
- Evidencia local suficiente.
- Anti-escopo forte.
- Hipoteses falsificaveis.
- Estrategia de pesquisa explicita e proporcional ao tamanho do brief.
- Fontes e formato orientados a decisao.

Acao: entregar brief.

### 75-89: bom, com ressalvas

Caracteristicas:
- Decisao existe, mas alguma evidencia ou restricao esta incompleta.
- Formato esperado e claro.
- Pode gerar pesquisa util, mas ha risco de conclusao ampla demais.
- Estrategia declarada, mas ainda pode estar ampla demais para 5+ areas/hipoteses.

Acao: entregar com ressalvas ou fazer 1-2 perguntas antes.

### 60-74: discovery incompleto

Caracteristicas:
- Tema claro, decisao fraca.
- Evidencias locais insuficientes.
- Gaps misturados com curiosidade.

Acao: nao enviar para Deep Research ainda. Fazer discovery curto.

### 0-59: brief ruim

Caracteristicas:
- "Pesquise X" generico.
- Contexto bruto sem pergunta.
- Recomendacao esperada sem criterio.
- Pesquisa externa substitui observacao local.
- Brief com 5+ areas/hipoteses sem escolher profundidade, serie ou quebra paralela.

Acao: bloquear como brief final e reconstruir.

---

## Sinais de discovery

Se aparecer qualquer sinal abaixo, pause antes de montar o brief final:

- Nao ha decisao a tomar.
- Ha sensacao, mas nenhum incidente concreto.
- Nao existem exemplos bons e ruins.
- O problema muda de nome a cada explicacao.
- Patrick quer criar skill antes de manual run.
- A pesquisa externa esta sendo usada para evitar observacao local.

Perguntas corretivas:

- "Que decisao essa pesquisa precisa destravar?"
- "Qual incidente real mostrou esse problema?"
- "Quais 3 exemplos bons e 3 ruins calibram o padrao?"
- "Isso precisa virar skill agora ou primeiro fazemos uma execucao manual?"
- "O que a pesquisa nao pode responder porque depende de observacao local?"

---

## Anti-padroes

### "Pesquise X" generico

Problema: produz relatorio enciclopedico.
Correcao: transformar X em decisao, gaps e hipoteses.

### Contexto bruto sem pergunta

Problema: o pesquisador escolhe o problema por conta propria.
Correcao: declarar objetivo, decisao e formato esperado antes do contexto.

### Arquitetura do zero com stack existente

Problema: ignora restricoes reais e recomenda solucao bonita que nao cabe.
Correcao: explicitar stack, estado implementado e restricoes.

### Tres projetos misturados

Problema: a pesquisa otimiza uma media que nao serve para nenhum caso.
Correcao: separar briefs por decisao ou declarar prioridade entre projetos.

### Brief gigante sem estrategia

Problema: a ferramenta de Deep Research devolve pergunta de amplitude vs profundidade ou entrega resumo raso.
Correcao: escolher single, series, parallel ou discovery antes do prompt final. Com 5+ areas/hipoteses, priorizar profundidade ou quebrar.

### Tudo vira prompt ou skill

Problema: automatiza antes de entender a dor.
Correcao: exigir manual run, bons/ruins e criterio de recorrencia.

### Trace para tudo

Problema: ruido ganha status de evidencia.
Correcao: registrar apenas drift, bug real, gate falho, corrective loop, decisao cara ou comparacao custo/qualidade.

### Aceitar hipotese sem evidencia

Problema: pesquisa vira confirmacao de vies.
Correcao: marcar como hipotese fraca e pedir evidencia local.

### Recomendacoes sem formato

Problema: entrega bonita, mas nao acionavel.
Correcao: exigir matriz, ranking, trade-offs, next actions ou criterios de decisao.

---

## Criterios de qualidade

Um bom research brief:

- Reduz o espaco de busca.
- Protege a pesquisa contra generalidades.
- Preserva contexto local suficiente para nao reinventar diagnostico.
- Distingue fato, hipotese, gap e preferencia.
- Forca a pesquisa a voltar com decisao, nao so informacao.
- Escolhe explicitamente estrategia quando o escopo e grande.
- Deixa claro quando a resposta certa e "nao pesquise ainda".
