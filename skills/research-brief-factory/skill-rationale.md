# Rationale: research-brief-factory

## Decisao

Criar uma skill local do SkillForge para transformar contexto operacional baguncado em research brief decisorio para Deep Research.

Esta skill nao executa pesquisa. Ela prepara o prompt/brief certo antes da pesquisa.

## Tese central

Deep Research bom comeca com diagnostico local, decisao-alvo, anti-escopo, evidencias locais e hipoteses falsificaveis. Nao com curiosidade aberta.

## Step 0: Pre-build Research

| Pergunta | Resposta |
|---|---|
| Dor concreta | Prompts de pesquisa e instrucao ficaram genericos quando partiram de pedido amplo, trace bruto ou vontade de "melhorar prompt/skill" sem decisao-alvo. |
| Frequencia 30 dias | Evidencia suficiente: AO/Maestro Deep Research, MktOps fresh session, resume capsules e casos ruins de trace amplo/edicao documental. |
| Busca local | `rg` em `skillforge-arsenal/skills` achou skills com partes proximas (`product-discovery-prd`, `context-guardian`, `sdd`, `meeting-sync`, `n8n-architect`), mas nenhuma focada em brief decisorio para Deep Research. |
| Busca externa | Scout da main achou solucoes proximas: Anthropic skills/skill-creator, prompt improvers, deep-research-skill e research-prompt/generate-research-prompt. Nenhuma cobre o metodo do Patrick com decisao-alvo, anti-escopo, evidencias locais e hipoteses falsificaveis. Resultado: BUILD, nao REUSE. |
| Por que similares nao servem | `product-discovery-prd` gera PRD; `context-guardian` gera handoff; `sdd` gera spec de implementacao; `meeting-sync` extrai tasks; `n8n-architect --delegate` gera briefing tecnico. Nenhuma fabrica prompt de Deep Research com decisao/anti-escopo/evidencias/hipoteses. |
| Core ou commodity | Core: codifica o jeito do Patrick preparar pesquisa para decisao operacional no ecossistema SkillForge. |
| Custo de inovacao | Baixo/moderado: SKILL.md linear, sem scripts, references delegadas a outros workers. Risco principal e virar skill generica demais. |
| Spike vs skill | A dor ja tem exemplos bons/ruins e invariantes claros. Skill faz sentido para repetir antes de pesquisas caras. |
| Criterio de delecao | Remover se nao for invocada por 60 dias ou se Deep Research tooling nativo passar a exigir decisao, anti-escopo e evidencia local por default. |

## Exemplos incorporados

### Bons

- AO/Maestro Deep Research: pesquisa orientada por decisao e gaps claros.
- MktOps fresh session: checkpoint, estado atual, restricoes e proximo passo.
- Resume capsule: `ACTIVE_ROLE`, `DIRECT_WRITE_PERMISSION`, `NEXT_ALLOWED_ACTION`, `NEXT_FORBIDDEN_ACTION`, `OPEN_GATES`, `CURRENT_WAVE`, `RESIDUAL_RISKS`.

### Ruins

- Pedido generico de melhorar prompt/instrucoes que virou edicao documental.
- Trace amplo demais sem triagem.
- Criar skill antes da dor estabilizar.

## Invariantes do brief

- Objetivo
- Decisao
- Contexto atual
- Evidencias locais
- Gaps
- Hipoteses
- Restricoes
- Fora de escopo
- Fontes desejadas
- Formato esperado
- Criterios de qualidade

## Gate principal

Se faltar decisao-alvo, anti-escopo ou evidencia local, perguntar no maximo 3 coisas. Se ainda faltar, gerar prompt de discovery, nao prompt de Deep Research.

## Arquitetura escolhida

Padrao Linear:

1. Triagem dos gates.
2. Diagnostico local.
3. Hipoteses falsificaveis.
4. Brief ou discovery prompt.
5. Checklist/rubrica.

Nao precisa de multi-agent, scripts ou execucao externa nesta primeira versao.

## References criadas

As references ja existem e sustentam a skill:

- `references/examples.md` - exemplos bons/ruins para calibrar o brief.
- `references/rubric.md` - criterios de score e qualidade do output.
- `references/templates.md` - formatos reutilizaveis para brief e discovery prompt.
