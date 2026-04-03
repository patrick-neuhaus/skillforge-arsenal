# Consolidado: Analise Profunda dos 5 Videos (Deborah Folloni / DevGPT)

> Sintese exaustiva dos 5 videos analisados, cruzando processos, skills propostas, referencias e conexoes com o arsenal existente.

---

## 1. Processos por Categoria

### Criacao de Skills (Videos 1, 3)

Processo unificado para criar, estruturar, distribuir e manter skills de alta qualidade:

**Fase A -- Concepcao e Estrutura**

1. **Definir o objetivo da skill** -- Descreva em 1-2 frases o que a skill resolve. Foque em um problema especifico que agentes ou usuarios buscariam resolver (Video 1: "problemas especificos que as pessoas buscariam resolver").
2. **Escolher a arquitetura da skill** -- Decida entre tres modelos:
   - **System-prompt-only:** Apenas instrucoes em linguagem natural no `skill.md`. Bom para skills de raciocinio/criacao (Video 3: skill de YouTube, propostas comerciais).
   - **CLI-first:** Um CLI real que o agente executa via bash, com a skill servindo como "manual de instrucoes". Superior para ferramentas que retornam dados, pois preserva a context window (Video 1: Agent Tools, `inference app run -p video`).
   - **Hibrida:** `skill.md` com instrucoes nao-deterministicas + scripts deterministicos na pasta `scripts/` (Video 3: skill de branding com `apply-branding.py`).
3. **Montar a anatomia da pasta:**
   ```
   minha-skill/
     skill.md              # Playbook principal: objetivo, triggers, roteiro de perguntas, estrutura de output, tom de voz
     references/           # Dados de referencia (planilhas, metricas, benchmarks)
     assets/               # Imagens, templates, logos
     scripts/              # Scripts deterministicos (Python, shell) chamados sob demanda
   ```
4. **Escrever o `skill.md` com roteiro de perguntas** -- Nao coloque apenas instrucoes. Inclua perguntas que a skill deve fazer ao usuario quando falta contexto (Video 3: "O roteiro de perguntas dentro da skill e o verdadeiro diferencial").
5. **Combinar determinismo com nao-determinismo** -- Use o `skill.md` para raciocinio criativo da IA e scripts para execucao precisa e reproduzivel (Video 3: "IA decide O QUE fazer, codigo faz COMO").

**Fase B -- Otimizacao para Descoberta (GEO)**

6. **Gerar keywords com o proprio agente** -- Peca ao Claude Code: "Se voce fosse buscar uma skill que faz [X], quais termos usaria?" O agente e o cliente da skill, nao o humano (Video 1: "let my agent come up with the right keywords because the agents are the customers for skills").
7. **Inspecionar o algoritmo da Find Skills** -- O codigo-fonte da skill Find Skills da Vercel e open source no GitHub. Analise como ela ranqueia resultados e otimize a descricao da sua skill para casar com esses criterios (Video 1: engenharia reversa do algoritmo de busca).
8. **Escrever descricao otimizada para agentes** -- Foque em verbos de acao e problemas resolvidos, nao em jargao de marketing. Agentes buscam por funcionalidade, nao por branding.

**Fase C -- Distribuicao**

9. **Publicar no skills.sh** -- O diretorio da Vercel e o principal canal de descoberta. Ser early adopter da vantagem desproporcional (Video 1: Omer foi first-mover no skills.sh).
10. **Garantir onboarding autoguiado** -- O processo de instalacao deve ser um unico comando. O installer pergunta: qual agente usa? Onde instalar? A skill inclui exemplos prontos para uso imediato (Video 1: instalacao e onboarding guiado).
11. **Iniciar conversa nova apos instalacao** -- O carregamento de skills acontece no inicio da sessao, nao dinamicamente (Video 5: "conversa nova obrigatoria").

**Fase D -- Manutencao e Evolucao**

12. **Implementar progressive disclosure** -- No system prompt do agente, liste apenas nome + descricao de 1 linha de cada skill. O conteudo so e carregado quando relevante (Video 3: "quanto mais usar da janela de contexto, menos efetiva vai ser sua IA").
13. **Retroalimentar a skill** -- Ao fim de cada uso, diga: "Registra isso na skill pra proxima vez eu nao precisar te falar de novo." O agente edita o `skill.md` ou cria novo arquivo em `references/` (Video 3: retroalimentacao substitui deploy).
14. **Versionar com Git** -- Skills sao pastas, portanto naturalmente versionaveis. Use PRs e code review para evolucao controlada (Video 3: "Git, PRs e code review se aplicam diretamente").

---

### Workflow de Desenvolvimento (Videos 2, 4)

Processo unificado anti-vibe coding, combinando os workflows dos Videos 2 (Spec/Break/Plan/Execute de 4 etapas) e 4 (Research/Spec/Implement de 3 etapas com foco em context window):

**Principio Central: Compressao Progressiva da Context Window**

Cada fase comprime o conhecimento da anterior num artefato. E um pipeline de destilacao onde cada etapa filtra ruido e concentra sinal. Regra de ouro: nunca ultrapassar 40-50% da context window. Usar `/clear` entre fases.

**Fase 0 -- Entendimento do Problema**

1. Defina em 1-2 frases o que quer implementar.
2. Identifique o tipo: nova feature, bug fix, refatoracao.

**Fase 1 -- Pesquisa (Research)**

3. **Pesquisa interna na base de codigo:**
   - Identifique todos os arquivos que serao afetados.
   - Encontre padroes de implementacao de coisas similares ja feitas (evitar duplicacao).
   - Encontre componentes/funcoes reutilizaveis (Video 4: "cria outro botao e agora voce tem manutencao dobrada").
4. **Pesquisa externa:**
   - Leia documentacoes relevantes (nao a inteira) das bibliotecas/servicos usados.
   - Busque padroes de implementacao em Stack Overflow, GitHub repos, docs oficiais.
   - **Tecnica .tmp:** Clone um repo de referencia numa pasta `.tmp`, peca ao Claude analisar o padrao, depois delete (Video 4: "few-shot learning manual").
5. **Gerar o PRD.md:**
   - Todos os arquivos da codebase relevantes (filtrando os inuteis).
   - Trechos das docs externas importantes.
   - Code snippets e padroes encontrados.
   - Descricao do que implementar.
   - O PRD e o "funil" que filtra informacao util de lixo.
6. **Executar `/clear`** para limpar a context window.

**Fase 2 -- Especificacao (Spec)**

7. **Gerar a spec a partir do PRD:**
   - Para projetos novos: estruturar como paginas > componentes > comportamentos (Video 2).
   - Para features: listar cada arquivo com path completo, acao (criar/modificar), o que fazer, e snippets/pseudocodigo (Video 4).
8. **Decomposicao em issues atomicas (para projetos maiores):**
   - Cada pagina da spec vira uma issue de prototipo (so frontend, nao funcional).
   - Cada comportamento vira uma issue separada.
   - Ordem: primeiro prototipos, depois funcionalidades (Video 2: "design first" adaptado para IA).
9. **Planejamento detalhado de cada issue:**
   - Pesquisa interna (codebase) + externa (docs/internet).
   - Cenarios: happy path, edge cases, cenarios de erro.
   - Lista explicita de arquivos a criar/modificar.
   - Tabelas do banco de dados necessarias.
   - Dependencias externas.
   - Checklist final.
   - "Se nao tiver la, ela nao vai mexer" (Video 2).
10. **Executar `/clear`** novamente.

**Fase 3 -- Implementacao (Execute)**

11. **Implementar com janela limpa:**
    - Anexar a spec como prompt: "Implementa essa spec."
    - A janela de contexto fica quase toda livre para a implementacao real.
12. **Usar agentes especializados por camada:**
    - Model Writer: tudo de banco de dados, schemas, migrations.
    - Component Writer: componentes frontend seguindo design system.
    - Outros agentes por camada do projeto (Video 2).
13. **Seguir documentos de referencia:**
    - `architecture.md`: regras de arquitetura (thin client/fat server, isolamento por comportamento).
    - Design system docs: padroes visuais.
    - A pasta `references/` funciona como "memoria persistente" do projeto (Video 2).

**Regras Arquiteturais Fundamentais**

- **Thin Client, Fat Server:** Frontend NAO controla nada. Apenas captura intencoes e renderiza respostas. Backend contem TODA logica de negocio. Tudo no frontend e acessivel "com dois cliques no navegador" (Video 2).
- **Organizacao por Comportamento:** Estrutura de pastas por pagina > comportamento (nao por tipo de arquivo). Garante isolamento e evita "efeito cobertor de pobre" (Video 2).

**Os 5 Problemas Sistematicos do Vibe Coding (taxonomia do Video 2)**

| Problema | Causa raiz | Antidoto no workflow |
|----------|-----------|---------------------|
| IA engasga | Tarefas grandes lotam context window | Decomposicao em issues atomicas (Fase 2) |
| Codigo baguncado | IA duplica/reinventa o que ja existe | Pesquisa na codebase antes de implementar (Fase 1) |
| IA desobediente | Usuario nao especifica arquivos | Spec com paths explicitos (Fase 2) |
| Cobertor de pobre | Falta isolamento/modularizacao | `architecture.md` + organizacao por comportamento (Fase 3) |
| Gafes de seguranca | Logica no frontend, chaves expostas | Thin client/fat server + security rules (Fase 3) |

---

### Frontend / Design (Video 5)

Processo para gerar interfaces com identidade visual distinta usando skills de design:

1. **Preparar o conteudo (copy):** Criar um arquivo Markdown com toda a copy da pagina, organizada por secoes (Hero, Social Proof, Comparacao, Features, Como Funciona, Depoimentos, CTA, FAQ).
2. **Gerar baseline sem skill (controle):** Pedir ao Claude Code para criar a pagina usando apenas o Markdown. Resultado: funcional mas generico, "com cara de AI."
3. **Criar mini identidade visual (licao de casa):**
   - Logo em versao dark e light/white.
   - Paleta de cores com codigos hex.
   - Duas fontes: uma display/marcante para titulos, uma body para textos.
   - Conceito visual (tema, ex: montanhas).
   - Imagem de fundo alinhada ao conceito.
4. **Instalar a Frontend Design Skill** da Anthropic (73.000+ instalacoes, 5a mais instalada no diretorio Vercel). Iniciar conversa nova apos instalacao.
5. **Preparar assets no projeto:** Colocar logos, imagem de fundo numa pasta (ex: `public/brands/`). Tirar screenshot da paleta e tipografia para anexar ao prompt.
6. **Rodar prompt com skill + assets:** Instrucao para melhorar o design + referencia a skill + screenshots da tipografia/paleta + referencia a pasta de assets.
7. **Iterar:** 2 prompts ja produzem diferenca dramatica. Mais iteracoes refinam ainda mais. A skill automaticamente adiciona micro-interactions (hover animations) sem que o usuario peca.

**Insight-chave:** A skill sozinha melhora a qualidade visual, mas sem assets de marca proprios, o resultado ainda sera "bonito generico." O diferencial real e skill + identidade visual, por menor que seja.

---

### Distribuicao e Marketing (Video 1)

Processo completo para maximizar a visibilidade e adocao de skills:

1. **Publicar no skills.sh** como canal principal de distribuicao. O skills.sh e mantido pela Vercel e e o diretorio padrao de skills do Claude Code.
2. **Aplicar GEO (Generative Engine Optimization):**
   - Otimizar descricoes/metadados para serem encontrados por agentes de IA (nao humanos).
   - Inspecionar o codigo open source da skill Find Skills da Vercel para entender o algoritmo de ranking.
   - Usar o proprio Claude para gerar keywords ("os agentes sao os clientes").
   - Focar em problemas especificos e verbos de acao.
3. **Preferir arquitetura CLI-first sobre MCP:**
   - CLIs retornam outputs curtos e diretos, preservando a context window.
   - MCPs retornam JSONs pesados que degradam a performance progressivamente.
   - O agente pode descobrir novos comandos dinamicamente (`inference apps list`).
   - A skill serve como "manual de instrucoes" para o CLI.
4. **Garantir onboarding autoguiado:** Comando de instalacao unico, deteccao automatica do agente, exemplos prontos para uso imediato.
5. **Modelo de monetizacao pay-per-use:** Agregar APIs caras (ex: Twitter) e oferecer acesso com custo por uso, criando arbitragem de demanda.
6. **Construir plataforma aberta:** Permitir que outros devs criem apps/ferramentas que se integram ao ecossistema, aumentando o valor da rede.

---

## 2. Todas as Skills que Podem Ser Geradas

| Nome | O que faria | Video | Prioridade |
|------|-------------|-------|------------|
| **geo-optimizer** | Otimiza descricoes de skills/pacotes para GEO -- gera keywords que agentes usariam para buscar, analisa como Find Skills ranqueia, sugere melhorias | 1 | Alta |
| **skill-publisher** | Automatiza publicacao no skills.sh -- valida formato, gera descricao GEO-otimizada, faz push | 1 | Media |
| **cli-skill-wrapper** | Transforma qualquer API em CLI tool otimizado para agentes, com skill de instrucao auto-gerada | 1 | Alta |
| **context-diet** | Analisa MCPs e ferramentas conectadas e sugere migracoes para CLI para reduzir context bloat | 1 | Media |
| **media-toolkit** | Ensina o agente a usar FFmpeg, ImageMagick e Remotion para manipulacao de midia local sem APIs externas | 1 | Baixa |
| **video-pipeline** | Orquestra pipeline de video: gerar imagens > animar > stitch > adicionar texto/transicoes via Remotion > exportar | 1 | Baixa |
| **social-media-agent** | Gera conteudo (imagem + texto) e posta automaticamente no X/Twitter com aprovacao humana | 1 | Baixa |
| **spec-writer** | Gera spec.md estruturado (paginas, componentes, comportamentos) a partir de descricao do projeto. Equivale ao `/spec` | 2 | Alta |
| **spec-breaker** | Decompoe spec em issues atomicas separando prototipos de UI e funcionalidades por behavior. Equivale ao `/break` | 2 | Alta |
| **issue-planner** | Para cada issue, roda pesquisa interna + externa, gera plano com cenarios, lista de arquivos, tabelas, dependencias, checklist. Equivale ao `/plan` | 2 | Alta |
| **layer-executor** | Orquestra execucao de issue chamando agentes especializados por camada (model-writer, component-writer). Equivale ao `/execute` | 2 | Alta |
| **architecture-guard** | Valida implementacoes contra regras de arquitetura (thin client/fat server, isolamento por comportamento). Lint de arquitetura | 2 | Alta |
| **code-dedup-scanner** | Escaneia codebase para encontrar componentes/funcoes reutilizaveis antes de criar codigo novo | 2, 4 | Alta |
| **vibe-code-auditor** | Detecta os 5 padroes problematicos do vibe coding (tarefas grandes, duplicacao, falta de isolamento, logica no frontend, chaves expostas) e sugere remediacoes | 2 | Media |
| **model-writer** | Agente especializado para camada de banco: cria schemas, migrations, tabelas seguindo padroes do projeto | 2 | Media |
| **component-writer** | Agente especializado para componentes frontend: cria componentes reutilizaveis seguindo design system | 2 | Media |
| **skill-composer** | Compoe multiplas skills em sequencia para tarefas complexas (gerar conteudo + branding + exportar PDF) | 3 | Media |
| **skill-retrofeeder** | Automatiza retroalimentacao: ao fim de cada conversa, sugere o que registrar na skill usada | 3 | Media |
| **progressive-loader** | Gera e otimiza o bloco de system prompt que lista skills com nome + descricao, otimizando progressive disclosure | 3 | Media |
| **skill-anatomy-validator** | Valida estrutura de pasta de skill (tem skill.md? references/? scripts chamados corretamente?) | 3 | Alta |
| **proposal-generator** | Gera propostas comerciais com roteiro de perguntas, tipos de projeto, tom customizado, output em PDF/Word | 3 | Baixa |
| **yt-title-thumb-advisor** | Sugere titulos e thumbnails baseados em dados de performance e concepts visuais de referencia | 3 | Baixa |
| **branding-applier** | Aplica identidade visual em documentos (PPTX, PDF) combinando instrucoes da marca com script deterministico | 3 | Baixa |
| **skill-migrator** | Converte agentes n8n existentes em skills: extrai system prompt, tools e knowledge base e reorganiza como pasta de skill | 3 | Media |
| **sdd-research** | Conduz Fase 1 do SDD: busca na codebase, leitura de docs externas, coleta de padroes, gera `prd.md` filtrado | 4 | Alta |
| **sdd-spec-writer** | Recebe PRD e gera spec ultra-tatica com paths, acoes (criar/modificar), snippets para cada arquivo | 4 | Alta |
| **sdd-implementer** | Recebe spec e executa implementacao arquivo por arquivo, respeitando paths e snippets definidos | 4 | Alta |
| **context-guardian** | Monitora uso de context window, alerta quando perto de 40-50%, sugere /clear e resume estado para handoff | 4 | Alta |
| **pattern-importer** | Automatiza tecnica .tmp: clona repo/trecho do GitHub, coloca em pasta temporaria, extrai padrao, limpa | 4 | Media |
| **brand-identity-builder** | Guia passo a passo para criar mini identidade visual (logo, paleta, tipografia, conceito) do zero | 5 | Media |
| **design-before-after** | Workflow de 2 fases: gerar baseline sem skill, refinar com skill + assets, documentando o delta | 5 | Baixa |
| **asset-prep-for-ai** | Organiza e valida assets de marca num formato otimizado para consumo por coding assistants | 5 | Media |
| **landing-page-architect** | Gera estrutura de copy para landing pages com secoes padrao (hero, social proof, comparativo, features, CTA, FAQ) | 5 | Media |
| **ai-design-smell-detector** | Analisa UI e identifica padroes visuais "cara de AI" (genericos, sem identidade, gradientes cliche) e sugere correcoes | 5 | Baixa |

**Resumo de prioridades:**
- **Alta:** 14 skills (geo-optimizer, cli-skill-wrapper, spec-writer, spec-breaker, issue-planner, layer-executor, architecture-guard, code-dedup-scanner, skill-anatomy-validator, sdd-research, sdd-spec-writer, sdd-implementer, context-guardian)
- **Media:** 13 skills
- **Baixa:** 8 skills

---

## 3. Todas as Referencias

### Ferramentas e Plataformas

| Nome | O que e | Video |
|------|---------|-------|
| **skills.sh** | Diretorio de skills da Vercel para Claude Code | 1, 5 |
| **inference.sh** | Plataforma de Omer com 150+ ferramentas de IA via CLI | 1 |
| **Claude Code** | Coding assistant CLI da Anthropic | 1, 2, 3, 4, 5 |
| **epic.new** | Plataforma com skills, agentes e prompts para Claude Code (Epic Learn + Epic Builder) | 2 |
| **Lovable** | Ferramenta de vibe coding mencionada como contraponto | 2 |
| **Remotion** | Framework React para criar videos programaticamente | 1 |
| **FFmpeg** | Ferramenta de manipulacao de video/audio via CLI | 1 |
| **ImageMagick** | Manipulacao de imagens via CLI | 1 |
| **Tavily** | Web search especializada para agentes | 1 |
| **Exa** | Web search semantica para agentes | 1 |
| **ProseMirror** | Framework para editores rich-text | 4 |
| **TipTap** | Editor rich-text baseado no ProseMirror | 4 |
| **NextAuth / Next.js** | Framework de autenticacao | 4 |
| **Resend** | Servico de envio de e-mails | 4 |
| **n8n** | Plataforma de automacao de workflows | 3 |
| **VS Code** | Editor de codigo usado no workflow de design | 5 |
| **GitHub/Git** | Versionamento de skills e repos de referencia | 1, 3, 4 |
| **Stack Overflow** | Fonte de padroes de implementacao | 4 |
| **Google Fonts** | Fonte de tipografia para identidade visual | 5 |
| **Motion (WMion)** | Biblioteca de animacoes React, mencionada como skill | 5 |

### Pessoas

| Nome | Quem e | Video |
|------|--------|-------|
| **Omer** | Fundador solo do Agent Tools / Inference.sh, criador da skill mais baixada do skills.sh | 1 |
| **Deborah (DebGPT)** | Host do canal, entrevistadora, fundadora da consultoria Donus, newsletter DebGPT no Substack | 1, 3 |
| **Criador do epic.new** | Autor do workflow Spec/Break/Plan/Execute, construiu epic.new 100% com IA (300 usuarios no 1o dia) | 2 |
| **DevGPT (autora)** | Criadora do app Epic (3.000+ usuarios em 90 dias), newsletter DevGPT no Substack (maior de software com IA do Brasil) | 4, 5 |
| **Reed Hastings** | Fundador do Netflix, citado sobre devs bons serem 10-20x mais produtivos por escrever codigo mais simples | 4 |

### Conceitos e Frameworks

| Conceito | Descricao | Video |
|----------|-----------|-------|
| **GEO (Generative Engine Optimization)** | SEO para agentes de IA -- otimizar conteudo para ser encontrado e consumido por LLMs, nao humanos | 1 |
| **Spec-Driven Development (SDD)** | Metodologia: Research > Spec > Implement. Comecar com especificacao completa antes de codar | 2, 4 |
| **Progressive Disclosure** | Revelar informacao apenas quando necessaria para preservar context window | 3 |
| **Thin Client, Fat Server** | Frontend magro (so renderiza), backend gordo (toda logica de negocio e seguranca) | 2 |
| **Context Window Management** | Gestao ativa do uso da janela de contexto: regra dos 40-50%, /clear entre fases, compressao progressiva | 2, 3, 4 |
| **Determinismo vs Nao-determinismo** | Scripts sao deterministicos (reproduziveis), LLMs nao. Combinar ambos e o padrao de ouro | 3 |
| **Retroalimentacao de Skills** | Pedir ao agente para registrar aprendizados na propria skill, substituindo ciclos de deploy | 3 |
| **Composicao Emergente** | Quando o agente tem CLI com multiplos comandos, comeca a compor workflows sozinho sem pre-configuracao | 1 |
| **Organizacao por Comportamento** | Estrutura de pastas por pagina > comportamento (nao por tipo de arquivo), garantindo isolamento | 2 |
| **Arbitragem de API** | Agregar demanda de APIs caras e oferecer acesso pay-per-use com custo reduzido | 1 |
| **Vibe Coding** | Abordagem de "jogar prompt e torcer para dar certo" -- contrario do SDD | 2, 4 |
| **Slash Commands** | Comandos customizados no Claude Code (/spec, /break, /plan, /execute, /clear) | 2, 4 |
| **Agentes Especializados por Camada** | Sub-agentes com skills dedicadas: Model Writer, Component Writer, etc. | 2 |
| **Tecnica .tmp** | Importar repo de referencia em pasta temporaria para a IA analisar padroes, depois deletar | 4 |
| **Compressao Progressiva** | Cada fase do pipeline comprime conhecimento da anterior num artefato (PRD > spec > codigo) | 4 |

---

## 4. Conexoes com Skills Existentes

| Skill do Arsenal | Melhorias sugeridas (de qual video) |
|-----------------|-------------------------------------|
| **skill-builder** | Incorporar modulo GEO para gerar descricoes otimizadas para agentes (V1). Adicionar template para skills CLI-first alem de system-prompt-first (V1). Incluir "roteiro de perguntas" como feature obrigatoria em toda skill gerada (V3). Usar taxonomia do V2 como template para skills de workflow (/spec, /break, /plan, /execute). Criar template de "design skill personalizada" que incorpora identidade visual (V5). |
| **prompt-engineer** | Criar modo "GEO" para otimizar textos para consumo por agentes (V1). Incorporar tecnicas de: especificar arquivos explicitamente, incluir cenarios (happy path, edge case, error), listar dependencias como padroes de prompt (V2). Criar modo "skill-prompt" que otimiza prompts para formato de skill (V3). Criar templates de prompts otimizados para interacao com skills de design (V5). |
| **sdd** | Enriquecer com detalhes praticos: estrutura pagina/componente/comportamento da spec, decomposicao em issues por behavior, fluxo prototipo-primeiro (V2). Fundamentar com o pipeline Research > Spec > Implement e a regra dos 40-50% de context window (V4). Integrar a tecnica .tmp como sub-etapa da fase de pesquisa (V4). |
| **context-tree** | Adicionar awareness de que MCPs poluem mais que CLIs e recomendar migracoes quando detectar context bloat (V1). Gerar automaticamente `architecture.md` e outros docs de referencia (V2). Estender para mapear skills disponiveis e seus triggers, gerando bloco de progressive disclosure do system prompt (V3). Mapear onde estao assets de marca no projeto (V5). |
| **maestro** | Adicionar modo "loose orchestration" onde da ao sub-agente acesso a um CLI e deixa ele compor o workflow emergentemente (V1). Orquestrar pipeline SDD (research > spec > implement) fazendo /clear entre fases (V2, V4). Funcionar como "system prompt enxuto" que decide quais skills carregar por etapa, implementando progressive disclosure a nivel de orquestracao (V3). |
| **trident** | Adicionar template especifico para "skill como produto" incluindo etapas de GEO, distribuicao via skills.sh, decisao CLI vs MCP vs system-prompt (V1). Usar para analisar cada issue sob multiplas perspectivas antes do planejamento (V2). Aplicar validacao em 3 camadas ao output de design (visual, acessibilidade, performance) (V5). |
| **reference-finder** | Catalogar GEO, Remotion, Tavily, Exa e modelos de video/audio como referencias tecnicas (V1). Integrar como sub-etapa do /plan para buscar padroes de implementacao comprovados (V2). Alimentar pasta `references/` de qualquer skill com fontes fundamentadas (V3). Usar antes da etapa de identidade visual para frameworks de design consagrados (V5). |
| **component-architect** | Enriquecer com regra "pesquisar componentes existentes antes de criar novos" (V2). Adicionar templates/patterns para Remotion (videos programaticos em React) (V1). Mapear componentes gerados por skills de design e garantir atomic design (V5). |
| **ui-design-system** | Adicionar templates para criacao de videos programaticos com Remotion (V1). Gerar automaticamente o documento de design system que alimenta o workflow de agentes especializados (V2). Servir como base para mini identidade visual que alimenta a Frontend Design Skill (V5). |
| **react-patterns** | Adicionar patterns especificos para Remotion (V1). Fornecer padroes que o component-writer aplicaria na fase de execucao (V2). Combinar com Frontend Design Skill para output com boas praticas React + animacoes Motion (V5). |
| **product-discovery-prd** | Servir como etapa "zero" antes do /spec: fazer discovery do produto, validar hipoteses, alimentar o /spec com informacoes mais ricas (V2). |
| **supabase-db-architect** | Servir como skill por tras do model-writer quando o banco e Supabase/Postgres (V2). |
| **security-audit** | Executar como etapa de validacao apos o /execute para detectar gafes de seguranca (logica no frontend, chaves expostas) (V2). |
| **repo-review** | Usar periodicamente para detectar os 5 padroes problematicos do vibe coding (V2). |
| **ux-audit** | Aplicar na etapa de prototipo (issues iniciais so com UI) para validar antes de prosseguir para implementacao funcional (V2). |
| **comunicacao-clientes** | Sem conexao direta identificada nos videos. |
| **tech-lead-pm** | Sem conexao direta identificada nos videos. |
| **docx** | Pode ser usado como skill auxiliar na exportacao de propostas e documentos gerados por skills (V3). |
| **pdf** | Pode ser usado como skill auxiliar na exportacao final de documentos (V3). |
| **pptx** | Pode ser usado com branding-applier para aplicar identidade visual em apresentacoes (V3). |
| **xlsx** | Pode alimentar pasta `references/` de skills com dados de performance em planilhas (V3). |
| **lovable-knowledge** | Principios do SDD (spec-driven, isolamento, thin client) se aplicam igualmente ao Lovable (V2). |
| **n8n-architect** | O workflow de 4 etapas poderia ser automatizado como workflow n8n (V2). A comparacao agentes vs skills sugere migrar agentes n8n para formato de skills (V3). |
| **schedule** | Sem conexao direta identificada nos videos. |
| **vps-infra-audit** | Sem conexao direta identificada nos videos. |

---

## 5. Proximos Passos Recomendados

### 1. Implementar o Pipeline SDD como skills encadeadas (Impacto: maximo)

Criar as 4 skills do workflow anti-vibe coding (`spec-writer`, `spec-breaker`, `issue-planner`, `layer-executor`) como skills independentes que se encadeiam. Estas resolvem o problema mais critico: qualidade de codigo gerado por IA em projetos de producao. Os Videos 2 e 4 convergem exatamente nesse ponto. O `maestro` ja existente pode orquestrar o pipeline.

**Acoes concretas:**
- Criar `sdd-research` (Fase 1: pesquisa + geracao do PRD)
- Criar `sdd-spec-writer` (Fase 2: spec tatica com paths e acoes)
- Criar `architecture-guard` (validacao continua de regras arquiteturais)
- Criar `context-guardian` (monitor de context window com alerta de 40-50%)

### 2. Adicionar modulo GEO ao skill-builder (Impacto: alto)

O `skill-builder` e a skill mais estrategica do arsenal porque gera todas as outras. Adicionar um modulo de GEO que: (a) peca ao proprio Claude para gerar keywords de busca, (b) otimize a descricao para o algoritmo da Find Skills, (c) valide contra o formato esperado pelo skills.sh. Isso multiplica a visibilidade de toda skill criada a partir de agora.

**Acoes concretas:**
- Incorporar geracao automatica de keywords GEO no pipeline de criacao
- Adicionar template CLI-first no skill-builder (nao apenas system-prompt-first)
- Criar `skill-anatomy-validator` como pre-publicacao obrigatoria

### 3. Criar code-dedup-scanner e pattern-importer (Impacto: alto)

Estes dois resolvem o problema mais citado nos videos: a IA duplicando/reinventando codigo. O `code-dedup-scanner` roda antes de cada implementacao para encontrar reutilizaveis. O `pattern-importer` automatiza a tecnica .tmp para transferencia de conhecimento de repos externos. Juntos, eliminam os dois maiores desperdicios de tokens e qualidade.

**Acoes concretas:**
- Criar `code-dedup-scanner` que escaneia a codebase e retorna componentes/funcoes reutilizaveis
- Criar `pattern-importer` que clona repo > extrai padrao > limpa pasta temporaria
- Integrar ambos como sub-etapas da Fase 1 (Research) do SDD

### 4. Evoluir context-tree com awareness de progressive disclosure e CLI vs MCP (Impacto: medio-alto)

O `context-tree` ja mapeia estrutura do projeto. Expandir para: (a) detectar MCPs que poluem context window e recomendar alternativas CLI, (b) mapear skills disponiveis e gerar automaticamente o bloco de progressive disclosure do system prompt, (c) gerar `architecture.md` automaticamente. Isso torna o context-tree o "hub de inteligencia" sobre contexto do projeto.

### 5. Publicar skills existentes no skills.sh com GEO (Impacto: medio-alto)

O arsenal ja tem 25 skills. Nenhuma esta no skills.sh. Publicar as mais maduras (skill-builder, prompt-engineer, sdd, reference-finder, maestro) com descricoes GEO-otimizadas seria o caminho mais rapido para ganhar visibilidade e validar a abordagem com a comunidade. Usar a vantagem de first-mover antes que o diretorio fique saturado.

**Acoes concretas:**
- Selecionar as 5 skills mais maduras do arsenal
- Rodar geo-optimizer (a ser criado) em cada descricao
- Publicar no skills.sh seguindo formato esperado pelo diretorio
- Monitorar instalacoes e feedback para iterar
