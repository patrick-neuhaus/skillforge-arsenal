# Video 1: Esse dev criou a skill mais baixada do Claude Code (Omer)

**Fonte:** https://www.youtube.com/watch?v=rQ61RGI3DFk
**Canal:** DebGPT (Deborah)
**Convidado:** Omer (criador do Agent Tools / Inference.sh)
**Duracao:** ~19min

---

## Resumo Executivo

Omer e o criador do Agent Tools, a skill mais baixada do skills.sh (diretorio de skills do Claude Code mantido pela Vercel). O diferencial da estrategia dele nao foi marketing tradicional, mas sim GEO (Generative Engine Optimization) -- otimizar a descricao da skill para ser encontrada por *outros agentes* que usam a skill "Find Skills" da Vercel. Ele construiu uma plataforma (inference.sh) que oferece 150+ ferramentas de IA via CLI, e a skill ensina o agente a usar esse CLI ao inves de MCPs, preservando a context window. A abordagem CLI vs MCP e um dos insights mais valiosos: respostas CLI sao mais curtas e nao poluem o contexto como JSONs de MCPs.

---

## Processo Completo (passo a passo reproduzivel)

### 1. Distribuicao via skills.sh (Canal Principal)

**O que fazer:** Publicar sua skill no skills.sh (diretorio da Vercel), nao depender apenas do GitHub.

**Como:**
- Acesse skills.sh e publique sua skill seguindo as instrucoes do diretorio
- O skills.sh e o principal canal de descoberta de skills do Claude Code
- Ser early adopter em plataformas de distribuicao da vantagem desproporcional

**Ferramentas:** skills.sh, GitHub (repositorio da skill)

**Exemplo do video:** Omer foi um dos primeiros a publicar no skills.sh, o que deu vantagem de first-mover.

---

### 2. GEO -- Generative Engine Optimization

**O que fazer:** Otimizar a descricao/metadados da sua skill para ser encontrada por agentes de IA, nao por humanos.

**Como:**
1. A Vercel tem uma skill chamada "Find Skills" que busca no diretorio de skills
2. O codigo-fonte dessa skill e open source no GitHub -- inspecione como ela faz a busca/ranking
3. Identifique quais campos e keywords a Find Skills usa para ranquear resultados
4. Otimize a descricao da sua skill para casar com esses criterios

**Truque-chave (direto do Omer):**
> "I let my agent come up with the right keywords because the agents are the customers for skills."

- Peca para o proprio Claude Code sugerir as keywords. O raciocinio: se um agente Claude vai buscar "generate video" ou "image generation", e o proprio Claude quem melhor sabe quais termos usaria para buscar isso.
- Foque em problemas especificos que as pessoas buscariam resolver

**Ferramentas:** Claude Code (para gerar keywords), GitHub (codigo da skill Find Skills), skills.sh

**Exemplo do video:** Omer otimizou as descricoes do Agent Tools para que quando outros Claude Codes buscassem "generate image", "generate video", "post to twitter", etc., encontrassem sua skill.

---

### 3. Arquitetura CLI-First (ao inves de MCP)

**O que fazer:** Construir ferramentas como CLI tools e usar skills como "manuais de instrucao" para o agente, ao inves de usar MCPs.

**Como:**
1. Crie um CLI que o agente possa chamar via bash (ex: `inference app run -p video`)
2. A skill descreve: como instalar o CLI, exemplos de uso, comandos disponiveis
3. O agente aprende a usar o CLI lendo a skill e executando comandos bash
4. Respostas do CLI sao curtas e diretas -- nao poluem a context window

**Por que e melhor que MCP:**
- MCPs carregam JSONs grandes na context window a cada chamada
- Isso degrada a performance do modelo progressivamente
- CLI retorna outputs curtos e objetivos
- O agente pode descobrir novos comandos dinamicamente (`inference apps list`)

**Ferramentas:** Node.js/Python (para construir o CLI), npm/pip (distribuicao)

**Exemplo do video:** O comando `inference app run -p video` gera um video. O agente consegue combinar multiplos comandos (gerar historia -> gerar imagens -> criar videos -> lip sync -> montar filme curto).

---

### 4. Plataforma Aberta para Desenvolvedores

**O que fazer:** Construir uma plataforma onde outros devs possam criar apps/ferramentas que se integram ao seu ecossistema.

**Como:**
- Permitir que usuarios criem "apps privados" na plataforma
- APIs de terceiros (Twitter, geracao de video, etc.) ficam acessiveis via um unico CLI
- Monetizacao pay-per-use (ex: API do Twitter via inference e mais barata que acesso direto)

**Exemplo do video:** Outros empreendedores ja usam a plataforma para criar apps de geracao de conteudo 3D e apps mobile.

---

### 5. Instalacao e Onboarding Guiado

**O que fazer:** O processo de instalacao da skill deve ser autoguiado -- o agente deve conseguir instalar e configurar tudo sozinho.

**Como:**
1. Comando de instalacao unico que o usuario cola no terminal
2. O installer pergunta: qual agente usa? Onde instalar (global/projeto)?
3. A skill inclui exemplos prontos para o agente comecar a usar imediatamente
4. Usuarios podem pedir ao agente: "find the inference.sh skills" e ele descobre sozinho

**Ferramentas:** Shell scripts, skills.sh install command

---

## Referencias Citadas

| Tipo | Nome | URL/Detalhes |
|------|------|--------------|
| Plataforma | skills.sh | Diretorio de skills da Vercel para Claude Code |
| Plataforma | inference.sh | Plataforma de Omer -- 150+ ferramentas de IA via CLI |
| Skill | Find Skills | Skill da Vercel que busca no diretorio skills.sh (codigo open source no GitHub) |
| Skill | Agent Tools | Skill do Omer -- a mais baixada do skills.sh |
| Conceito | GEO (Generative Engine Optimization) | SEO para agentes de IA -- otimizar conteudo para ser encontrado por LLMs |
| Ferramenta | Remotion | Framework para criar videos programaticamente (React-based) |
| Ferramenta | Nano Banana 2 / Gemini 3.1 | Modelo de geracao de imagem usado na demo |
| Ferramenta | FFmpeg | Mencionado indiretamente -- usado para stitch videos |
| API | X/Twitter API | Disponivel via inference -- posting, delete, get, create |
| Ferramenta | Tavily | Ferramenta de web search especializada disponivel no inference |
| Ferramenta | Exa | Ferramenta de web search semantica disponivel no inference |
| Modelos | 11 Labs, XAI | Modelos de audio/speech disponiveis no inference |
| Modelos | Google, ByteDance, Prunas, Kling | Modelos de geracao de video disponiveis no inference |
| Pessoa | Omer | Fundador solo do Agent Tools / Inference.sh |
| Pessoa | Deborah (DebGPT) | Host do canal, entrevistadora |

---

## Skills que Podem Ser Geradas

| Nome proposto | O que faria | Baseado em qual trecho |
|---------------|-------------|------------------------|
| **geo-optimizer** | Otimiza descricoes de skills/pacotes para GEO -- gera keywords que agentes usariam para buscar, analisa como Find Skills ranqueia, sugere melhorias | Trecho 1:25-3:55 -- toda a explicacao de GEO e o truque de pedir ao agente as keywords |
| **skill-publisher** | Automatiza o processo de publicar uma skill no skills.sh -- valida formato, gera descricao GEO-otimizada, faz o push | Trecho 6:22-6:53 -- instalacao e distribuicao |
| **social-media-agent** | Gera conteudo (imagem + texto) e posta automaticamente no X/Twitter, com aprovacao humana antes do post | Trecho 8:54-9:52 -- demo de postar no Twitter direto do agente |
| **video-pipeline** | Orquestra pipeline de video: gerar imagens -> animar -> stitch -> adicionar texto/transicoes via Remotion -> exportar | Trecho 10:00-10:52 -- explicacao do pipeline de video com Remotion |
| **cli-skill-wrapper** | Transforma qualquer API em um CLI tool otimizado para agentes, com skill de instrucao auto-gerada | Trecho 4:29-6:09 -- explicacao de como Agent Tools funciona (CLI + skill como manual) |
| **context-diet** | Analisa MCPs e ferramentas conectadas ao agente e sugere migracoes para CLI para reduzir context bloat | Trecho 15:08-17:01 -- discussao CLI vs MCP e impacto na context window |
| **media-toolkit** | Skill que ensina o agente a usar FFmpeg, ImageMagick e Remotion para manipulacao de midia local (sem depender de APIs externas) | Trecho 12:31-13:23 -- utilitarios de merge, extract, caption, loop de video |

---

## Insights Nao-Obvios

### 1. O cliente da skill nao e o humano -- e o agente
> "The agents are the customers for skills."

Omer deixa claro que quem "compra" e "consome" skills sao os agentes, nao os humanos. Isso muda completamente como voce escreve descricoes, escolhe nomes e estrutura a documentacao. Voce deve otimizar para como um LLM interpretaria sua skill, nao para como um humano leria.

### 2. Engenharia reversa da Find Skills e a nova forma de SEO
O fato de a skill Find Skills ser open source no GitHub significa que qualquer pessoa pode inspecionar o algoritmo de busca e otimizar para ele. Isso e literalmente o equivalente a ter acesso ao algoritmo do Google -- so que ninguem ta fazendo isso ainda de forma sistematica.

### 3. CLI outputs preservam a context window de forma dramatica
MCPs retornam JSONs pesados que entram inteiros na context window. CLIs retornam strings curtas. Num workflow longo (ex: gerar 10 imagens + 5 videos + montar filme), a diferenca acumulada na context window e enorme. Omer disse que "never been a fan of MCPs" e que "it felt like just a lot of bloat for the agent."

### 4. Composicao emergente de ferramentas
Quando voce da ao agente um CLI com multiplos comandos, ele comeca a *compor* workflows sozinho -- sem que voce preconfigure pipelines. O agente gera uma historia, cria imagens, anima, faz lip sync e monta um curta-metragem. Isso so acontece porque o CLI e facil de usar e o agente consegue encadear comandos.

### 5. Arbitragem de API via plataforma
Omer monetiza oferecendo acesso a APIs caras (como Twitter) com modelo pay-per-use. O custo para o dev individual acessar a Twitter API diretamente e alto; via inference.sh, paga-se apenas pelo uso. Isso cria um modelo de negocio baseado em agregar demanda.

### 6. O agente pode aprender novas capacidades em runtime
O CLI do inference permite que o agente descubra novos apps dinamicamente (`inference apps list`). Isso significa que conforme novos modelos sao adicionados a plataforma, o agente ja consegue usa-los sem precisar atualizar a skill. A skill e o "bootstrap"; o CLI e auto-descobrivel.

### 7. Skills como system prompts e limitado
Omer destaca que a maioria das skills do ecossistema sao "just system prompts ready-made for specific tasks describing how to use a certain API". O diferencial do Agent Tools e ter um CLI real que o agente pode executar. Skills puramente textuais dependem do agente interpretar e gerar codigo; skills com CLI dao ao agente uma ferramenta concreta.

---

## Conexoes com Skills Existentes do Arsenal

### skill-builder
**Conexao direta e forte.** O skill-builder deveria incorporar um modulo de GEO: ao criar uma nova skill, gerar automaticamente descricoes otimizadas para agentes (nao humanos), sugerir keywords usando o proprio Claude, e validar contra o formato esperado pelo Find Skills. Tambem deveria ter um template para skills CLI-first (nao apenas system-prompt-first).

### prompt-engineer
**Conexao forte.** A tecnica de pedir ao agente para gerar keywords de busca ("let my agent come up with the right keywords because the agents are the customers") e uma forma de prompt engineering meta -- voce usa o LLM para otimizar conteudo que sera consumido por outro LLM. O prompt-engineer deveria ter um modo "GEO" para otimizar textos para consumo por agentes.

### reference-finder
**Conexao moderada.** O conceito de GEO e novo e merece ser catalogado como referencia. Alem disso, Remotion, Tavily, Exa, e os modelos citados (Kling, Prunas, ByteDance video models) sao referencias tecnicas relevantes que o reference-finder poderia indexar.

### trident
**Conexao moderada.** O Trident (planejamento de projeto) poderia se beneficiar de um template especifico para "skill como produto" -- incluindo etapas de GEO, distribuicao via skills.sh, e decisao CLI vs MCP vs system-prompt.

### context-tree
**Conexao forte.** A discussao CLI vs MCP e diretamente relevante para o context-tree. O context-tree gerencia o que entra na context window; deveria ter awareness de que MCPs poluem mais que CLIs e recomendar migracoes quando detectar context bloat.

### maestro
**Conexao moderada.** O Maestro orquestra sub-agentes. A abordagem de Omer de composicao emergente (agente combinando ferramentas CLI sozinho) sugere que o Maestro poderia ter um modo "loose orchestration" onde, ao inves de planejar cada passo rigidamente, ele da ao sub-agente acesso a um CLI e deixa ele compor o workflow.

### ui-design-system / component-architect / react-patterns
**Conexao indireta.** Remotion e React-based, entao o react-patterns e component-architect poderiam ter templates/patterns especificos para criacao de videos programaticos com Remotion.

### sdd (Spec-Driven Development)
**Conexao indireta.** A ideia de que a skill e um "manual de instrucao" para o CLI se alinha com SDD -- a skill funciona como uma spec que o agente segue. O SDD poderia ter um template "skill spec" que define como documentar um CLI para consumo por agentes.
