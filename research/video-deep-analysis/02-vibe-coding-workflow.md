# Video 2: Vibe Coding nao funciona (Novo Workflow no Claude Code)

**Fonte:** https://www.youtube.com/watch?v=Ea5yaWGqoHQ
**Canal:** Epic (criador do epic.new)
**Duracao aproximada:** ~24 minutos

---

## Resumo Executivo

O video apresenta um workflow completo de 4 etapas (Spec, Break, Plan, Execute) para criar aplicacoes profissionais com Claude Code, em contraposicao direta ao Vibe Coding. O autor demonstra que Vibe Coding gera 5 problemas sistematicos (IA engasga, codigo bagunçado, IA desobediente, cobertor de pobre, gafes de seguranca) e que cada etapa do seu workflow foi desenhada como antidoto especifico para um ou mais desses problemas. O produto epic.new foi construido 100% com IA usando esse workflow e alcancou 300 usuarios no primeiro dia, servindo como prova de conceito de que o processo funciona para aplicacoes de producao. O diferencial central e que o workflow trata a IA como um executor que precisa de instrucoes extremamente precisas (quais arquivos criar/modificar, quais padroes seguir, quais componentes reutilizar) em vez de um "genio" que adivinha o que voce quer.

---

## Processo Completo (passo a passo reproduzivel)

### Visao Geral do Workflow

O workflow possui 4 etapas sequenciais, cada uma com um comando (slash command) dedicado no Claude Code:

```
/spec --> /break --> /plan --> /execute
```

A logica e: especificar o projeto inteiro --> quebrar em tarefas atomicas --> planejar cada tarefa individualmente --> executar cada tarefa com agentes especializados.

---

### Etapa 1: /spec - Escrever a Especificacao

**O que fazer:**
Criar um documento completo (spec.md) que descreve toda a aplicacao antes de escrever qualquer linha de codigo. E o "contrato" entre voce e a IA sobre o que sera construido.

**Como fazer:**
1. Abrir o Claude Code no projeto
2. Digitar `/spec` seguido de uma descricao do que voce quer construir
3. O Claude gera um documento spec.md estruturado

**Estrutura da Spec gerada:**
- **Descricao geral do projeto** - explicacao por alto do que e a aplicacao
- **Lista de todas as paginas** da aplicacao
- **Para cada pagina:**
  - Todos os **componentes** que existem nela
  - Todos os **comportamentos** (behaviors) que esses componentes tem

**Exemplo concreto do video:**
O autor mostrou a spec de um chat de IA multi-provider (estilo ChatGPT). A pagina de chat continha:
- Componentes: thread de mensagens, mensagem do usuario, mensagem da IA, botao de parar streaming
- Comportamentos: mandar mensagem, fazer streaming da resposta da IA, parar o streaming no meio do processo

**Ferramentas/comandos:**
- Comando: `/spec [descricao do que quero construir]`
- Output: arquivo `spec.md` na raiz do projeto

**Por que essa etapa existe (antidoto para qual problema):**
- Resolve o problema da IA "nao obedecer": ao ter uma spec clara, a IA sabe exatamente o que construir
- Resolve o problema de escopo descontrolado: tudo esta documentado antes de comecar

---

### Etapa 2: /break - Quebrar a Spec em Issues (Tarefinhas)

**O que fazer:**
Pegar o documento spec.md e automaticamente decompor em multiplas tarefas pequenas e atomicas (issues). Cada tarefa deve ser pequena o suficiente para nao lotar a janela de contexto da IA.

**Como fazer:**
1. Digitar `/break` e arrastar o arquivo spec.md
2. O Claude le a spec e gera multiplos arquivos de issue

**Regra de decomposicao:**
- Cada **pagina** da spec vira uma issue (prototipo de UI)
- Cada **comportamento** (behavior) da spec vira uma issue separada
- A ordem segue uma logica: **primeiro prototipos (apenas frontend/telas), depois funcionalidades**

**Estrutura da decomposicao:**
1. Issues iniciais = prototipos de cada pagina (so frontend, nao funcional, apenas a tela)
2. Issues seguintes = implementacao funcional de cada comportamento

**Exemplo concreto do video:**
O autor mostrou uma pasta com varias issues numeradas:
- Issues 1-3: prototipos das paginas (so tela, sem funcionalidade)
- Issue 4 em diante: implementacao funcional dos comportamentos
- Exemplo: "new chat" (comportamento da spec) virou uma issue especifica

**Ferramentas/comandos:**
- Comando: `/break [arrastar spec.md]`
- Output: pasta com multiplos arquivos de issue (tarefinhas), cada um com ~3 linhas de descricao simples

**Por que essa etapa existe (antidoto para qual problema):**
- Resolve o problema de "IA engasga com tarefas grandes": tarefas pequenas preservam a janela de contexto
- Garante a melhor performance do modelo: contexto limpo = melhor output

**Insight importante:** O autor enfatiza que "issue" e apenas o nome tecnico para "tarefinha". A decomposicao segue a granularidade de comportamento, nao de feature ou pagina inteira.

---

### Etapa 3: /plan - Pesquisa e Planejamento de cada Issue

**O que fazer:**
Para CADA issue individualmente (antes de implementar), rodar uma etapa de pesquisa e planejamento. Essa e a etapa mais critica do workflow, pois e o que diferencia codigo profissional de codigo vibe-coded.

**Como fazer:**
1. Digitar `/plan` e arrastar a issue especifica que quer planejar
2. O Claude roda duas pesquisas:
   - **Pesquisa interna** (na base de codigo): encontra trechos de codigo e arquivos que podem ser reutilizados/importados
   - **Pesquisa externa** (internet/documentacoes): encontra padroes de implementacao comprovados e documentacoes de dependencias externas

**O que o plano gerado contem:**
1. **Descricao detalhada da tarefa**
2. **Cenarios do comportamento:**
   - Caminho feliz (happy path)
   - Edge cases (cenarios pouco provaveis mas possiveis)
   - Cenarios de erro
3. **Tabelas do banco de dados** que precisam ser criadas, com colunas especificadas
4. **Lista explicita de arquivos** que precisam ser criados ou modificados, com descricao do que fazer em cada arquivo
5. **Dependencias externas** necessarias
6. **Checklist final** resumindo tudo que precisa ser feito

**Exemplo concreto do video:**
O autor mostrou que a issue que antes tinha ~3 linhas de descricao ficou com dezenas de linhas apos o planejamento, incluindo:
- Quais arquivos criar
- Quais arquivos modificar
- O que modificar em cada arquivo
- Quais tabelas do banco criar e quais colunas
- Quais dependencias externas usar

**Ferramentas/comandos:**
- Comando: `/plan [arrastar issue-XX.md]`
- Input: issue com ~3 linhas
- Output: issue expandida com planejamento completo e detalhado
- Usa pesquisa na codebase (grep/search) + pesquisa na web (documentacoes)

**Por que essa etapa existe (antidoto para qual problema):**
- Resolve "codigo bagunçado": ao pesquisar na codebase, evita duplicacao de componentes (ex: criar um segundo botao quando ja existe um)
- Resolve "reinventar a roda": ao pesquisar documentacoes externas, usa padroes comprovados
- Resolve "IA nao obedece": ao listar explicitamente quais arquivos mexer, a IA nao tem margem para mexer em arquivos errados
- Citacao direta: "Se nao tiver la, ela nao vai mexer"

**Insight critico:** O autor diz que quando voce especifica QUAIS arquivos a IA deve mexer, "nao tem como ela nao te obedecer". O problema de "IA desobediente" e na verdade o usuario nao especificando os arquivos, e a IA tendo que inferir/adivinhar -- e conforme o projeto cresce (mais arquivos), a probabilidade de acertar diminui estatisticamente.

---

### Etapa 4: /execute - Implementacao com Agentes Especializados

**O que fazer:**
Executar a issue planejada, usando agentes e skills especializados por camada do software.

**Como fazer:**
1. Digitar `/execute` e arrastar a issue ja planejada
2. O Claude implementa seguindo o planejamento feito na etapa anterior
3. Durante a implementacao, o Claude chama agentes especializados por tipo de arquivo/camada

**Agentes especializados mencionados:**
| Agente | Skill | Responsabilidade |
|--------|-------|------------------|
| Model Writer | (skill de banco de dados) | Tudo relacionado a banco de dados, schemas, migrations |
| Component Writer | write-components | Criacao de componentes frontend |
| (outros agentes) | (outras skills) | Cada camada do projeto tem seu agente |

**Cada agente tem:**
- Descricao do que faz
- Regras especificas para aquele tipo de arquivo
- Padroes de implementacao a seguir

**Documentos de apoio utilizados durante a execucao:**
O projeto mantem uma pasta `references/` com documentacoes que guiam os agentes:
- `architecture.md` - documentacao da arquitetura do projeto
- Design system documentation - padroes visuais
- Especificacao do workflow
- Outras referencias especificas do projeto

**Ferramentas/comandos:**
- Comando: `/execute [arrastar issue-XX.md planejada]`
- Usa: agentes especializados (sub-agentes com skills dedicadas)
- Referencia: pasta `references/` com documentacoes do projeto

**Por que essa etapa existe (antidoto para qual problema):**
- Resolve "cobertor de pobre" (arrumar uma coisa, quebrar outra): `architecture.md` garante isolamento de comportamentos por pasta
- Resolve "gafes de seguranca": `architecture.md` contem regra de "thin client, fat server" -- nenhuma logica de negocio no frontend
- Resolve "codigo bagunçado": agentes especializados por camada garantem padroes consistentes

---

### Arquitetura mencionada: Thin Client, Fat Server

O autor descreve uma regra arquitetural fundamental aplicada via `architecture.md`:

- **Frontend (client):** NAO controla nada. Apenas captura intencoes do usuario (cliques, interacoes), manda para o backend, e renderiza a resposta recebida.
- **Backend (server):** Contem TODA a logica de negocio, regras, validacoes.
- **Motivo:** Tudo no frontend e acessivel com "literalmente dois cliques no navegador". Chaves expostas = banco de dados comprometido. Regras de admin no frontend = qualquer usuario pode se promover a admin.

### Arquitetura mencionada: Organizacao por Comportamento

A estrutura de pastas do projeto segue um padrao especifico:

```
/pagina-login/
  /comportamento-fazer-login/
  /comportamento-recuperar-senha/
/pagina-chat/
  /comportamento-enviar-mensagem/
  /comportamento-streaming/
```

**Beneficio:** Quando ha um bug em "recuperar senha", o Claude so olha na pastinha de "recuperar senha" e nao toca na pastinha de "fazer login". Isso garante isolamento e evita o efeito "cobertor de pobre".

---

## Referencias Citadas

### Ferramentas e Produtos
- **Claude Code** - ferramenta CLI da Anthropic para desenvolvimento com IA
- **epic.new** - produto do autor (plataforma com skills, agentes e prompts para Claude Code). Dois pilares: Epic Learn (educacao) e Epic Builder (CLI + skills)
- **Lovable** - mencionado como exemplo de ferramenta de vibe coding

### Conceitos Tecnicos
- **Vibe Coding** - abordagem de "vida louca total" onde voce da instrucoes vagas para a IA
- **Spec-Driven Development** - abordagem do autor: comecar com especificacao completa antes de codar
- **Janela de Contexto** - limitacao dos LLMs; quanto mais limpa, melhor a performance
- **Thin Client, Fat Server** - padrao arquitetural: frontend magro (so renderiza), backend gordo (toda logica)
- **Issues / Tarefinhas** - unidades atomicas de trabalho
- **Behaviors / Comportamentos** - acoes do usuario que viram unidades de implementacao
- **Edge Cases** - cenarios pouco provaveis mas possiveis
- **Slash Commands** - comandos customizados no Claude Code (/spec, /break, /plan, /execute)
- **Skills** - conjuntos de regras e instrucoes que guiam agentes especializados
- **Agentes especializados por camada** - sub-agentes com skills dedicadas (Model Writer, Component Writer, etc.)

### Padroes Problematicos do Vibe Coding (taxonomia do autor)
1. **IA engasga** - tarefas grandes demais lotam a janela de contexto
2. **Codigo bagunçado** - IA complica o simples, repete codigo existente, reinventa a roda
3. **IA desobediente** - usuario nao especifica arquivos, IA infere errado (piora com projeto grande)
4. **Cobertor de pobre** - arrumar X quebra Y por falta de isolamento/modularizacao
5. **Gafes de seguranca** - logica de negocio no frontend, chaves expostas

### Pessoas
- Autor do canal/video (criador do epic.new) - nao mencionado por nome na transcricao

---

## Skills que Podem Ser Geradas

| Nome proposto | O que faria | Baseado em qual trecho |
|---------------|-------------|------------------------|
| **spec-writer** | Gera um documento spec.md estruturado (paginas, componentes, comportamentos) a partir de uma descricao do projeto. Equivale ao `/spec` do video. | Etapa 1 - "Eu tenho um comando salvo, que ele e basicamente barra spec... vai listar todas as paginas da aplicacao e para cada pagina todos os componentes e todos os comportamentos" |
| **spec-breaker** | Decompoem uma spec em issues atomicas, separando prototipos de UI e funcionalidades, respeitando a granularidade de comportamento. Equivale ao `/break`. | Etapa 2 - "Cada comportamento vai virar uma tarefinha... as primeiras tarefinhas sao prototipos. A gente implementa so o frontend, nao funcional, so a tela" |
| **issue-planner** | Para cada issue, roda pesquisa interna (codebase) e externa (docs/internet), gera plano com cenarios (happy path, edge cases, erros), lista de arquivos a criar/modificar, tabelas, dependencias e checklist. Equivale ao `/plan`. | Etapa 3 - "Vai rodar uma pesquisa tanto na base de codigo quanto fora... encontrar trechos de codigo que eu posso reutilizar... padroes de implementacao comprovados" |
| **layer-executor** | Orquestra execucao de uma issue planejada chamando agentes especializados por camada (model-writer, component-writer, etc). Equivale ao `/execute`. | Etapa 4 - "Cada agente tem a sua respectiva skill... tenho um agente para cada camada do projeto" |
| **architecture-guard** | Valida que implementacoes seguem regras de arquitetura (thin client/fat server, isolamento por comportamento, nenhuma logica no frontend). Funciona como lint de arquitetura. | "Architecture MD... quando ele le esse architecture MD, ele sabe exatamente como que e a nossa arquitetura e o que que ele pode e nao pode fazer" |
| **code-dedup-scanner** | Antes de criar novo codigo, escaneia a codebase para encontrar componentes/funcoes/trechos reutilizaveis que podem ser importados em vez de recriados. | "Faco ela rodar uma pesquisa no meu projeto para ela identificar trechos de codigo que eu posso importar ao inves de recriar" |
| **vibe-code-auditor** | Analisa um projeto existente para detectar os 5 padroes problematicos (tarefas grandes, codigo duplicado, falta de isolamento, logica no frontend, chaves expostas) e sugere remediacoes. | Secao "Os principais problemas do Vibe Coding" - taxonomia completa dos 5 padroes |
| **model-writer** | Agente especializado para camada de banco de dados: cria schemas, migrations, tabelas, seguindo padroes do projeto. | "Quando eu vou fazer algo do banco de dados, eu tenho um agente e uma skill que so faz banco de dados, que e esse model writer" |
| **component-writer** | Agente especializado para componentes frontend: cria componentes reutilizaveis seguindo design system do projeto. | "Quando eu vou fazer alguma coisa no front end, eu preciso criar componentes, eu vou usar esse agente de component writer e ele vai ter essa skill de write components" |

---

## Insights Nao-Obvios

### 1. A "desobediencia" da IA e um problema estatistico, nao de inteligencia
O autor explica que em um projeto com 20 arquivos, a IA tem boa chance de acertar qual arquivo mexer mesmo sem instrucao explicita. Mas conforme o projeto cresce para centenas de arquivos, a probabilidade de acertar cai drasticamente. Nao e que a IA ficou "mais burra" -- e que o espaco de busca aumentou. **Implicacao:** A necessidade de especificidade nos prompts escala com o tamanho do projeto.

### 2. Prototipos antes de funcionalidade -- e uma estrategia deliberada
O /break gera primeiro issues de prototipo (so UI, sem funcionalidade) e so depois issues funcionais. Isso permite validar visualmente antes de investir em logica. E uma adaptacao do conceito de "design first" para o workflow de IA.

### 3. A pesquisa no /plan serve dois propositos simultaneos
Nao e so "encontrar codigo para reutilizar". A pesquisa externa tambem garante que a IA use padroes de implementacao documentados e comprovados em vez de inventar solucoes proprias. Isso e sutil mas crucial: a IA nao e proibida de criar codigo novo, mas e direcionada a preferir padroes existentes.

### 4. O workflow e um antidoto para a proatividade indesejada da IA
O autor menciona que a IA "tende a ser proativa e tentar implementar algo que voce talvez nem precise". O workflow inteiro e desenhado para transformar a IA de "agente autonomo que decide o que fazer" para "executor preciso que faz exatamente o que foi especificado". Cada etapa adiciona mais restricoes.

### 5. A pasta references/ funciona como "memoria persistente" do projeto
Ao colocar architecture.md, design system, e outros docs na pasta references/, o autor criou uma "memoria de longo prazo" que sobrevive entre sessoes do Claude Code. A IA le esses documentos a cada execucao e opera dentro das restricoes ali definidas. E essencialmente context engineering aplicado a nivel de projeto.

### 6. Isolamento por comportamento > isolamento por tipo de arquivo
O padrao mais comum em projetos e organizar por tipo (components/, pages/, utils/). O autor organiza por comportamento dentro de cada pagina (pagina-login/recuperar-senha/, pagina-login/fazer-login/). Isso e menos convencional mas resolve diretamente o problema de acoplamento que causa o "efeito cobertor de pobre".

### 7. O custo aparente de burocracia e investimento em manutencao
O autor reconhece que o processo "parece burocratico" para quem vem do Vibe Coding, mas argumenta que e inevitavel para projetos que vao a producao. A frase-chave: "Nao e SE e QUANDO der pau, voce vai ter que resolver. Se o seu projeto tiver uma grande bagunca, voce nao vai conseguir resolver e a IA tambem nao vai conseguir resolver." Projetos vibe-coded frequentemente sao reescritos do zero.

### 8. Seguranca e trivialmente quebravel no frontend
"Literalmente dois cliques" no navegador para acessar tudo no frontend. O autor nao fala de hacking sofisticado, mas de F12 + Inspect. Isso inclui chaves de banco de dados e regras de permissao (trocar "user" para "admin").

---

## Conexoes com Skills Existentes no Arsenal

### skill-builder
**Conexao direta e forte.** O video descreve exatamente o tipo de skill que o skill-builder deveria ser capaz de gerar: skills especializadas por camada (model-writer, component-writer), skills de workflow (/spec, /break, /plan, /execute), e skills de governanca (architecture-guard). O skill-builder pode usar a taxonomia do video como template para gerar skills de workflow completas.

### prompt-engineer
**Conexao forte.** Todo o workflow e essencialmente context engineering -- cada etapa adiciona contexto mais preciso para a IA. O prompt-engineer pode incorporar as tecnicas de: (1) especificar arquivos explicitamente, (2) incluir cenarios (happy path, edge case, error), (3) listar dependencias, como padroes de prompt para qualquer projeto.

### sdd (Spec-Driven Development)
**Conexao diretissima.** O video descreve literalmente Spec-Driven Development. A skill sdd do arsenal e a implementacao desse conceito. O video valida a abordagem e adiciona detalhes praticos que podem enriquecer o sdd: a estrutura pagina/componente/comportamento da spec, a decomposicao em issues por behavior, o fluxo prototipo-primeiro.

### context-tree
**Conexao forte.** O architecture.md e a pasta references/ do video sao essencialmente o que o context-tree mapeia: a arvore de contexto do projeto que a IA precisa conhecer. O context-tree pode ser usado para gerar automaticamente o architecture.md e outros docs de referencia mencionados no video.

### maestro
**Conexao forte.** O /execute do video usa orquestracao de multiplos agentes especializados, que e exatamente o que o maestro faz. O padrao de "agente por camada" (model-writer, component-writer) e um caso de uso direto para o maestro orquestrar.

### component-architect
**Conexao forte.** O component-writer mencionado no video e essencialmente o que o component-architect faz: criar componentes frontend seguindo padroes. O component-architect pode ser enriquecido com a regra do video de "pesquisar componentes existentes antes de criar novos".

### ui-design-system
**Conexao moderada.** O video menciona uma documentacao de design system na pasta references/. O ui-design-system pode gerar esse documento automaticamente, servindo como input para o workflow.

### react-patterns
**Conexao moderada.** O component-writer do video segue padroes de componentes React. O react-patterns pode fornecer os padroes que o component-writer aplicaria.

### reference-finder
**Conexao forte.** A etapa /plan faz exatamente o que o reference-finder faz: buscar referencias externas (documentacoes, padroes comprovados) antes de implementar. O reference-finder pode ser integrado como sub-etapa do /plan.

### trident
**Conexao moderada.** O trident faz analise em 3 perspectivas. Pode ser usado na etapa de /plan para analisar cada issue sob multiplas perspectivas antes de planejar a implementacao.

### product-discovery-prd
**Conexao forte.** O /spec do video gera algo similar a um PRD tecnico. O product-discovery-prd pode servir como etapa "zero" antes do /spec: fazer discovery do produto, validar hipoteses, e entao alimentar o /spec com informacoes mais ricas.

### supabase-db-architect
**Conexao forte.** O model-writer do video e um agente de banco de dados. O supabase-db-architect pode servir como a skill por tras do model-writer quando o banco e Supabase/Postgres.

### security-audit
**Conexao moderada.** O video menciona gafes de seguranca (logica no frontend, chaves expostas) e agentes de teste de seguranca. O security-audit pode ser executado como etapa de validacao apos o /execute.

### repo-review
**Conexao moderada.** Pode ser usado periodicamente para detectar os 5 padroes problematicos que o video descreve (codigo duplicado, falta de isolamento, logica no frontend).
