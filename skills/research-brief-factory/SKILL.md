---
name: research-brief-factory
description: "Transforma contexto operacional baguncado em research brief decisorio para Deep Research. Use SEMPRE que o usuario pedir: montar prompt de Deep Research, preparar pesquisa profunda, transformar traces em brief, organizar contexto para pesquisa, definir o que pesquisar, validar hipoteses, estruturar evidencias locais, diagnosticar gaps, criar anti-escopo, pedir AO/Maestro Deep Research, pesquisar cursos/metodologias/frameworks/ferramentas com decisao-alvo. NAO executa pesquisa; gera o brief/prompt. Se o pedido for 'pesquisa X generico', force diagnostico local antes."
---

# Research Brief Factory

IRON LAW: Nunca gere prompt de Deep Research sem decisao-alvo, anti-escopo e evidencia local. Sem esses tres, gere discovery primeiro, porque pesquisa aberta vira curiosidade cara.

## Boundary

Esta skill fabrica briefs decisorios para ferramentas de Deep Research. Ela nao executa a pesquisa, nao navega fontes e nao transforma resultado de pesquisa em implementacao.

Use o padrao Linear: diagnostico local -> decisao -> hipoteses -> brief -> checklist.

## Workflow

```
Research Brief Factory Progress:

- [ ] Step 1: Triagem REQUIRED BLOCKING
  - [ ] 1.1 Identificar decisao-alvo
  - [ ] 1.2 Identificar anti-escopo
  - [ ] 1.3 Identificar evidencia local
  - [ ] GATE: se faltar qualquer um dos tres, perguntar max 3 coisas
- [ ] Step 2: Diagnostico local REQUIRED
  - [ ] 2.1 Separar contexto atual, aprendizados, traces e gaps
  - [ ] 2.2 Marcar evidencias vs suposicoes
  - [ ] 2.3 Separar projetos se houver mais de um
- [ ] Step 3: Hipoteses e falsificacao REQUIRED
  - [ ] 3.1 Converter duvidas em hipoteses testaveis
  - [ ] 3.2 Definir o que confirmaria/refutaria cada hipotese
  - [ ] 3.3 Priorizar hipoteses pela decisao-alvo
- [ ] Step 4: Decidir estrategia de pesquisa REQUIRED
  - [ ] 4.1 Contar areas, subtemas e hipoteses
  - [ ] 4.2 Escolher Single Mother Research, Sequential Research Series, Parallel Research Briefs ou Discovery First
  - [ ] 4.3 Se houver 5+ areas ou 5+ hipoteses, priorizar profundidade ou sugerir quebra
- [ ] Step 5: Gerar brief REQUIRED
  - [ ] 5.1 Load `references/templates.md` para formatos completos
  - [ ] 5.2 Load `references/examples.md` se precisar calibrar com exemplos bons/ruins
  - [ ] 5.3 Entregar prompt de Deep Research ou prompt de discovery
- [ ] Step 6: Validar BLOCKING
  - [ ] 6.1 Load `references/rubric.md` para score detalhado quando o brief for critico
  - [ ] 6.2 Rodar pre-delivery checklist
```

## Step 1: Triagem REQUIRED BLOCKING

Antes de escrever qualquer prompt, responda:

1. Qual decisao o Patrick quer tomar depois da pesquisa?
2. O que a pesquisa nao deve cobrir, mesmo parecendo relacionado?
3. Que evidencias locais ja existem: traces, cursos, logs, conversas, docs, outputs, falhas repetidas?

Se faltar decisao-alvo, anti-escopo ou evidencia local, pergunte no maximo 3 coisas:

```
Antes de montar Deep Research, faltam pecas que mudam a qualidade:
1. Qual decisao voce quer tomar com essa pesquisa?
2. O que fica explicitamente fora do escopo?
3. Qual evidencia local temos alem da sua intuicao?
```

Se a resposta ainda nao trouxer os tres elementos, gere um **prompt de discovery**, nao um prompt de Deep Research.

## Step 2: Diagnostico local

Extraia e rotule os blocos abaixo. Nao despeje contexto bruto; compacte em evidencias acionaveis.

| Bloco | Pergunta que guia |
|---|---|
| Objetivo | Que resultado pratico a pesquisa precisa desbloquear? |
| Decisao | Que escolha concreta sera feita depois? |
| Contexto atual | Onde o sistema/projeto/processo esta agora? |
| Aprendizados locais | O que cursos, uso real ou tentativas anteriores ja ensinaram? |
| Evidencias dos traces | Que fatos observados sustentam o problema? |
| Gaps | O que ainda nao sabemos e impede decisao? |
| Hipoteses | O que acreditamos que pode ser verdade? |
| Restricoes | Stack, tempo, equipe, budget, ferramentas, clientes, compliance |
| Fora de escopo | O que nao pesquisar para evitar dispersao? |
| Fontes desejadas | Que tipos de fonte a pesquisa deve priorizar? |
| Formato esperado | Como o resultado precisa voltar para ser usado? |
| Criterios de qualidade | Como saber que a pesquisa ficou boa? |

Se houver 2+ projetos, crie uma secao por projeto. Misturar projetos cria hipoteses falsas.

## Step 3: Hipoteses falsificaveis

Transforme pergunta aberta em hipotese testavel:

- Ruim: "Pesquisar como melhorar prompts."
- Bom: "Hipotese: briefs com decisao-alvo + anti-escopo + evidencia local reduzem respostas genericas em pesquisas de skill design. Refutar se exemplos bons do mercado nao usam esses elementos."

Para cada hipotese, inclua:

- **Aposta:** o que achamos que e verdade.
- **Evidencia local:** o que ja aponta nessa direcao.
- **Busca externa:** que tipo de fonte pode confirmar/refutar.
- **Criterio de falsificacao:** que achado faria mudar de ideia.
- **Impacto na decisao:** o que muda se for verdadeira/falsa.

## Step 4: Estrategia de pesquisa

Antes de gerar o prompt final, escolha explicitamente uma estrategia. Isso evita brief gigante que a ferramenta de Deep Research devolve como pergunta de "amplitude vs profundidade".

Use este criterio:

| Estrategia | Quando usar | Output esperado |
|---|---|---|
| Single Mother Research | Existe uma decisao central; subtemas servem essa decisao | Um prompt mae, triagem ampla, profundidade nos gaps criticos e follow-ups no fim |
| Sequential Research Series | A primeira pesquisa precisa decidir quais pesquisas vem depois | Prompt mae + lista de pesquisas filhas candidatas com criterio de disparo |
| Parallel Research Briefs | Subtemas sao independentes e nao dependem da mesma decisao | Briefs separados, um por decisao/subtema |
| Discovery First | Falta decisao, evidencia local ou anti-escopo | Prompt de discovery, nao Deep Research final |

Se houver 5+ areas, 5+ subtemas ou 5+ hipoteses, nao aceite amplitude maxima por default. Escolha uma destas saidas:

- **Profundidade priorizada:** reduzir areas, manter a decisao central e pedir analise adversarial dos gaps mais criticos.
- **Quebra explicita:** gerar serie sequencial ou briefs paralelos quando os subtemas nao cabem em uma decisao mae.
- **Discovery:** se a lista grande existe porque a decisao ainda esta nebulosa.

Quando a ferramenta perguntar "amplitude ou profundidade?", responda com a estrategia escolhida antes de continuar.

## Step 5: Output

Load `references/templates.md` e escolha o menor template que resolve o caso:

- Gates passaram -> gerar **Research brief decisorio** e, se o usuario for colar em ferramenta externa, anexar o **Pedido para Deep Research**.
- Gates falharam -> gerar **Discovery antes do brief**, com no maximo 3 perguntas quando estiver conversando com Patrick.
- Fresh session ou handoff -> usar os templates operacionais apenas se o objetivo for preservar papel, permissao ou estado.
- Brief grande -> declarar a **estrategia de pesquisa** antes do prompt final.

O output final deve conter, no minimo:

- decisao-alvo;
- estrategia de pesquisa escolhida e motivo;
- contexto atual e restricoes;
- evidencias locais separadas de suposicoes;
- gaps que a pesquisa deve fechar;
- hipoteses falsificaveis;
- anti-escopo com motivo;
- fontes desejadas;
- formato esperado da resposta;
- criterios de qualidade.

Nao copie template inteiro se uma versao curta destrava a decisao. O brief precisa ser copiavel, mas nao burocratico.

## Exemplos de calibracao

Bons sinais:
- AO/Maestro Deep Research com decisao, contexto e gaps claros.
- MktOps fresh session com checkpoint, estado, restricoes e proximo passo.
- Resume capsule com `ACTIVE_ROLE`, `DIRECT_WRITE_PERMISSION`, `NEXT_ALLOWED_ACTION`, `NEXT_FORBIDDEN_ACTION`, `OPEN_GATES`, `CURRENT_WAVE`, `RESIDUAL_RISKS`.

Sinais ruins:
- "Melhora esse prompt/instrucoes" sem dor estabilizada.
- Trace amplo demais sem separar evidencia de ruido.
- Criar skill antes da dor aparecer repetidamente.

Load `references/examples.md` para exemplos completos quando estiver calibrando output.

## Anti-patterns

- **Pesquisar X generico** -> primeiro transforme em decisao-alvo.
- **Despejar contexto bruto** -> compacte por evidencia, gap e hipotese.
- **Pedir arquitetura do zero quando stack existe** -> preserve restricoes locais.
- **Misturar 3 projetos** -> separe hipoteses e evidencias por projeto.
- **Transformar tudo em prompt/skill** -> questione se e tooling/processo.
- **Trace para tudo** -> trace so entra se sustenta decisao ou hipotese.
- **Aceitar hipotese sem evidencia** -> marque como suposicao e defina falsificacao.
- **Pedir recomendacoes sem formato** -> defina como o resultado sera usado.
- **Executar a pesquisa** -> esta skill para no brief.

## Pre-delivery checklist

- [ ] Decisao-alvo aparece em 1 frase concreta?
- [ ] Anti-escopo esta explicito e com motivo?
- [ ] Evidencias locais foram separadas de suposicoes?
- [ ] Gaps respondem a decisao, nao curiosidade solta?
- [ ] Hipoteses sao falsificaveis?
- [ ] Estrategia de pesquisa escolhida: single, series, parallel ou discovery?
- [ ] Se ha 5+ areas/hipoteses, o brief prioriza profundidade ou quebra a pesquisa?
- [ ] Restricoes locais preservam stack/processo/equipe atual?
- [ ] Fontes desejadas combinam com o tipo de decisao?
- [ ] Formato esperado torna a pesquisa acionavel?
- [ ] Se faltou gate, output virou discovery prompt?
- [ ] O brief nao manda implementar nem executar pesquisa?

## References

| Arquivo | Quando carregar |
|---|---|
| `references/templates.md` | Step 4, para formatos de Deep Research Brief e Discovery Prompt |
| `references/examples.md` | Quando precisar calibrar com bons/ruins exemplos reais |
| `references/rubric.md` | Step 5, quando o brief for critico ou for virar padrao reutilizavel |
| `skill-rationale.md` | Para entender por que esta skill existe e qual dor ela codifica |
