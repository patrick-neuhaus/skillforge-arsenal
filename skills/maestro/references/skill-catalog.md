# Skill Catalog — Mapa Completo do Arsenal

Consulte este arquivo no **Phase 2** quando for rotear o intent do usuário para skills.

---

## Routing Priorities (regras hard)

Quando o intent do usuário pode acionar 2+ skills, use estas regras antes de propor. Elas existem porque overlaps reais já causaram routing errado em sessões anteriores.

| Intent | Skill correta | NÃO usar |
|--------|---------------|----------|
| Code review (bugs, qualidade, DRY/KISS, security, SOLID) | **trident** | ❌ `simplify` (built-in Anthropic) — cobertura inferior, sem 3-agent verification |
| Design review code-level (CSS, layout, perf, a11y no código) | **trident --design** | ❌ ux-audit (essa é experiência, não código) |
| Auditoria de UX/experiência (fluxos, heurísticas, dark patterns, WCAG) | **ux-audit** | ❌ trident --design (essa é code-level) |
| Review de skill como produto (estrutura, GEO, distribuição) | **trident --skill** | ❌ geo-optimizer (esse é só description cirúrgico) |
| Otimização cirúrgica de description pra GEO | **geo-optimizer** | ❌ trident --skill (review holístico, não cirúrgico) |
| Mensagem operacional 1:1 pra cliente (cobrança, update, aprovação) | **comunicacao-clientes** | ❌ copy --mode whatsapp (essa é persuasão/conversão) |
| Copy persuasiva pra audiência (WhatsApp marketing, broadcast, vendas) | **copy --mode whatsapp** | ❌ comunicacao-clientes (essa é relacionamento operacional) |
| Importar padrão de outro repo (clone, extrai, limpa .tmp) | **pattern-importer** | ❌ reference-finder (essa é livros/frameworks teóricos) |
| Encontrar livros/frameworks/metodologias consagradas | **reference-finder** | ❌ pattern-importer (esse é código/repo concreto) |
| SEO tradicional (technical, on-page, programático) | **seo** | — |
| Aparecer em respostas de IA (AEO/GEO/LLMO) | **ai-seo** | — |
| Conteúdo que precisa Google + LLMs | **chain seo --content → ai-seo** | — |

### IRON LAW de roteamento (do maestro)

**Antes de propor uma skill ou chain, leia o SKILL.md das skills candidatas.** Não confie só no nome ou na sua memória — descriptions evoluem, modes mudam, boundaries se redefinem. Esta lei existe porque falhas de routing já aconteceram (ex: propor `simplify` quando `trident` era a skill certa). Custo: ~1k tokens. Economia: evitar refazer trabalho com skill errada.

### Tiebreaker quando 2+ regras matcham o mesmo intent

1. **Regra mais específica ganha** (ex: "review de skill" mais específico que "code review genérico")
2. **Skill com maior cobertura do domínio ganha** (ex: trident cobre mais que simplify)
3. **Em empate real, listar ambas** e perguntar ao Patrick

### Quando usar maestro vs chamar skill direto

- **Chama direto** se: tu sabe a skill, intent é claro, é 1 skill só
- **Roda maestro** se: 2+ skills candidatas, intent ambíguo, vai compor chain de 2+ skills, ou nunca usou essa skill antes

**Exemplo de aplicação:**
> Patrick: "revisa esse PR pra ver se tem bugs e se o design tá OK"
> Intent detectado: "review PR" + "design OK"
> 2 regras matcham: trident (code review) + trident --design (design code-level)
> Aplicação: roda trident `--mode pr` primeiro, depois trident `--design` no mesmo escopo. Mesma skill, 2 modos.

### Manutenção desta tabela

- Atualizar quando skill nova entra no arsenal — responsabilidade do `skill-builder --full` (Step 5 deve adicionar entry aqui)
- Revisar quando Patrick reportar routing errado em sessão — virar gap documentado
- Revisão completa trimestral

### Skills built-in vs locais (v3 — 2026-04-10)

**Regra hard:** sempre usar a versão local do skillforge-arsenal quando existir equivalente. Built-ins Anthropic (`anthropic-skills:*`) podem estar desatualizadas, ter cobertura inferior, ou conflitar com versões locais.

| Built-in (NÃO usar) | Local (USAR) | Motivo |
|---------------------|--------------|--------|
| `simplify` | `trident` | trident tem 3-agent verification, P0-P3, multi-lens scan |
| `anthropic-skills:trident` | `trident` (local) | local pode estar à frente no versionamento |
| `anthropic-skills:copy` | `copy` (local) | mesma razão |
| `anthropic-skills:skill-builder` | `skill-builder` (local) | v3 tem Step 0 Pre-build Research + handoff com prompt-engineer |
| `anthropic-skills:prompt-engineer` | `prompt-engineer` (local) | v3 tem 4 rubrics YAML + `--validate` refatorado |
| `anthropic-skills:reference-finder` | `reference-finder` (local) | tem `--solution-scout` mode |
| qualquer `anthropic-skills:X` onde X existe em `skillforge-arsenal/skills/` | local | versionamento, evolução |

**Exceções:** built-ins SEM equivalente local seguem normais (ex: pdf, docx, pptx, xlsx — enquanto não existir versão local no repo).

**Como verificar:** olhar `skillforge-arsenal/skills/<nome>/SKILL.md`. Se existe, usar local.

---

## Code Review

### trident
- **O que faz:** Pipeline de 3 agentes (Scanner→Verifier→Arbiter) para detecção profunda de bugs, vulnerabilidades, violações SOLID, e dead code
- **Triggers PT-BR:** "revisa esse código", "tem bug nisso?", "faz um audit", "analisa esse código", "code review"
- **Triggers EN:** review code, audit code, find bugs, security review, check for vulnerabilities
- **Modes:** unstaged, staged, all-local, pr, range, dir
- **Input:** Diff, PR, diretório, ou commit range
- **Output:** Tabela de findings com bug_id, severity (P0-P3), verdict (REAL_BUG/NOT_A_BUG/NEEDS_HUMAN_CHECK)
- **Quando NÃO usar:** Review de estilo, mudanças triviais, UX review

### react-patterns
- **O que faz:** Audita e implementa padrões modernos React/Next.js (Server Components, App Router, Server Actions)
- **Triggers PT-BR:** "tá certo esse padrão?", "onde coloco essa lógica?", "posso usar use client aqui?"
- **Triggers EN:** audit React code, fix React anti-patterns, server vs client component
- **Modes:** --audit (padrão), --scaffold, --migrate
- **Input:** Codebase React/Next.js
- **Output:** Tabela de anti-patterns com before/after examples
- **Iron Law:** Thin Client, Fat Server — zero business logic em 'use client'

### security-audit
- **O que faz:** Pipeline de 3 agentes para auditoria de segurança com domínios OWASP
- **Triggers PT-BR:** "auditoria de segurança", "tem vulnerabilidade?", "tá seguro?"
- **Triggers EN:** security audit, vulnerability scan, OWASP check
- **Input:** Codebase ou aplicação
- **Output:** Findings com severity e recomendações OWASP

---

## Implementation

### sdd (Spec Driven Development)
- **O que faz:** Pipeline anti-vibecoding: Research → Spec → Implement → Review
- **Triggers PT-BR:** "quero adicionar funcionalidade", "como implemento isso?", "faz um plano antes"
- **Triggers EN:** implement a feature, plan implementation, spec driven
- **Phases:** --phase research, --phase spec, --phase implement, --phase review
- **Input:** Descrição de feature ou escopo
- **Output:** prd.md → spec.md → código implementado → review via trident
- **Iron Law:** Nunca pular uma fase. Research → Spec → Implement → Review.

### component-architect
- **O que faz:** Planeja e constrói arquitetura de componentes (atomic design, shadcn, composição)
- **Triggers PT-BR:** "como organizo meus componentes", "componente tá muito grande", "quantos props é demais"
- **Triggers EN:** plan components, component tree, decompose monolithic component
- **Modes:** --plan, --create, --refactor, --audit
- **Input:** Feature ou componente existente
- **Output:** Component tree + interfaces + reuse map
- **Iron Law:** Check existing before creating.

### supabase-db-architect
- **O que faz:** Arquitetura de banco Supabase/PostgreSQL para apps PME
- **Triggers PT-BR:** "montar schema", "RLS", "migração", "índices"
- **Triggers EN:** database schema, Supabase architecture, RLS policies
- **Input:** Requisitos de dados ou schema existente
- **Output:** Schema, migrations, RLS policies, indexes

### n8n-architect
- **O que faz:** Desenha, arquiteta, constrói em waves, modulariza e revisa automações n8n
- **Triggers PT-BR:** "automação n8n", "workflow n8n", "integração", "pensar no fluxo", "construir em waves", "modularizar", "loop", "subworkflow"
- **Triggers EN:** n8n automation, workflow architecture, flow design, wave building, modularize
- **Modes:** --flow (design thinking), --waves (construção incremental), --build, --debug, --optimize, --review, --delegate, --doc, --template
- **Input:** Requisito de automação ou workflow existente
- **Output:** Diagrama textual (--flow), workflow em waves (--waves), node configuration, error handling patterns
- **Iron Law:** NUNCA construa workflow sem error handling em CADA node HTTP Request

---

## Design

### ui-design-system
- **O que faz:** Gera design tokens e design.json a partir de inputs de marca
- **Triggers PT-BR:** "cria um design.json", "monta identidade visual", "preciso de tokens de design"
- **Triggers EN:** create design system, generate design tokens, brand to code
- **Modes:** --generate, --audit, --apply
- **Input:** Cores hex, fontes, keywords de conceito, tipo de projeto
- **Output:** design.json completo + Tailwind config ou CSS variables
- **Iron Law:** Concrete brand inputs required (hex/fonts, not adjectives).

### ux-audit
- **O que faz:** Auditoria de UX/UI em aplicações web e mobile
- **Triggers PT-BR:** "auditoria de UX", "a interface tá ruim", "usabilidade"
- **Triggers EN:** UX audit, UI review, usability check
- **Input:** Screenshots, URLs, ou código de frontend
- **Output:** Heuristic evaluation com findings priorizados

### product-discovery-prd
- **O que faz:** Discovery de produto e geração de PRDs otimizados para Lovable
- **Triggers PT-BR:** "discovery de produto", "montar PRD", "validar ideia"
- **Triggers EN:** product discovery, PRD, validate idea
- **Input:** Ideia ou problema de produto
- **Output:** PRD estruturado com personas, user stories, requisitos

### seo
- **O que faz:** Audita, planeja, implementa e otimiza estratégias de SEO completas (technical, on-page, off-page, semântico, programático)
- **Triggers PT-BR:** "melhorar meu SEO", "keyword research", "auditar SEO", "programático ou manual?", "categorias ou flat?", "meu site não rankeia"
- **Triggers EN:** SEO audit, keyword research, content optimization, technical SEO, programmatic SEO, semantic SEO, topical authority
- **Modes:** --audit, --keyword, --content, --technical, --architecture, --programmatic, --semantic, --offpage
- **Input:** Site/projeto + nicho + objetivo
- **Output:** Auditoria, keyword research, plano de conteúdo, decisões de arquitetura, automação
- **Iron Law:** NUNCA otimize conteúdo sem keyword research fundamentado
- **Quando NÃO usar:** Automação n8n pura (n8n-architect), frontend/design (ui-design-system)

---

## Knowledge

### reference-finder
- **O que faz:** Encontra referências fundamentais (livros, frameworks, metodologias, pessoas) para qualquer tema
- **Triggers PT-BR:** "busca referências", "que livro fala sobre", "quem é referência em"
- **Triggers EN:** find references, who wrote about, best book for
- **Modes:** --find, --save, --connect, --moc
- **Input:** Tema + contexto do usuário
- **Output:** Referências curadas com obras seminais, frameworks práticos, pessoas, conexões
- **Iron Law:** Nunca citar referência que não tem certeza que existe.

### prompt-engineer
- **O que faz:** Cria, valida e otimiza prompts para qualquer LLM
- **Triggers PT-BR:** "cria um prompt", "melhora esse prompt", "o prompt tá ruim"
- **Triggers EN:** create prompt, optimize prompt, validate prompt, system prompt
- **Modes:** --create, --validate, --type (system/extraction/agents-md/json-schema)
- **Input:** Objetivo do prompt + contexto
- **Output:** Prompt estruturado com role, context, instructions, constraints, output format
- **Iron Law:** Nunca output prompt sem explicar WHY cada seção existe.

### lovable-knowledge
- **O que faz:** Gera Workspace Knowledge e Project Knowledge otimizados para Lovable
- **Triggers PT-BR:** "configurar Lovable", "knowledge pro Lovable"
- **Input:** Projeto existente ou novo
- **Output:** Arquivos de knowledge formatados para Lovable

### lovable-router
- **O que faz:** Classifica mudanças em projetos Lovable e roteia: editar direto (código) ou gerar prompt pro Lovable (banco)
- **Triggers PT-BR:** "editar projeto lovable", "mexer no banco do lovable", "posso editar direto?", "gerar prompt pro lovable"
- **Triggers EN:** route lovable change, classify lovable edit, generate lovable prompt, edit lovable project
- **Modes:** --route (default), --prompt, --direct
- **Input:** Descrição da mudança desejada
- **Output:** Classificação (código/banco/zona cinza) + ação (edição direta ou prompt otimizado pro Lovable)
- **Iron Law:** NUNCA editar schema/RLS/edge functions/storage policies diretamente num repo Lovable
- **Quando NÃO usar:** Gerar Knowledge (lovable-knowledge), design de schema sem Lovable (supabase-db-architect)

---

## Meta

### skill-builder
- **O que faz:** Cria, melhora e otimiza skills Claude Code com 12 técnicas battle-tested
- **Triggers PT-BR:** "criar skill", "melhorar skill", "a skill tá ruim", "transforma isso numa skill"
- **Triggers EN:** create skill, build skill, improve skill, validate skill
- **Modes:** --quick (scaffold), --full (guiado), --evolve (melhorar), --validate (checar)
- **Input:** Ideia de skill ou skill existente
- **Output:** SKILL.md + references/ + scripts/ (opcionais)
- **Iron Law:** Nunca gerar skill sem ler 2+ skills de referência.

### context-tree
- **O que faz:** Gestão hierárquica de conhecimento com scoring, decay, e archival
- **Triggers PT-BR:** "quero catalogar isso", "o que já sei sobre X?", "organizar conhecimento"
- **Triggers EN:** organize knowledge, score references, manage context tree, prune stale
- **Modes:** --add, --query, --prune, --status, --connect
- **Input:** Conhecimento a adicionar ou query de busca
- **Output:** Entry scored com importance/maturity/connections

---

## Content

### pdf
- **O que faz:** Criar, ler, editar, manipular PDFs
- **Triggers:** PDF, .pdf, "gerar relatório", "exportar como PDF"

### docx
- **O que faz:** Criar, ler, editar documentos Word
- **Triggers:** Word, .docx, "documento Word", "relatório em Word"

### pptx
- **O que faz:** Criar e manipular apresentações PowerPoint
- **Triggers:** PowerPoint, .pptx, "apresentação", "slides"

### xlsx
- **O que faz:** Criar e manipular planilhas Excel
- **Triggers:** Excel, .xlsx, "planilha", "spreadsheet"

---

## Guard

### architecture-guard
- **O que faz:** Valida implementações contra regras de arquitetura (thin client/fat server, layer separation, behavior organization)
- **Triggers PT-BR:** "tá seguindo a arquitetura?", "tem lógica no frontend?", "valida a estrutura", "antes de mergear valida"
- **Triggers EN:** validate architecture, check architecture rules, layer violation, guard architecture
- **Modes:** --scan, --init, --check, --rules
- **Input:** Codebase + architecture.md (opcional)
- **Output:** Violações com severity (P0-P2), file:line, evidence, fix suggestion
- **Iron Law:** NEVER approve business logic in client components
- **Quando NÃO usar:** Bugs funcionais (trident), segurança (security-audit), UX (ux-audit)

### code-dedup-scanner
- **O que faz:** Escaneia codebase pra encontrar componentes/funções reutilizáveis antes de criar código novo
- **Triggers PT-BR:** "já tem isso no projeto?", "tem componente parecido?", "antes de criar verifica se existe"
- **Triggers EN:** find duplicates, scan for reusables, check existing code, duplicate scan
- **Modes:** --scan, --check, --report
- **Input:** Descrição do que vai criar
- **Output:** Matches com recomendação (REUSE/EXTEND/CREATE) + localização exata
- **Iron Law:** NEVER report duplicate without exact location + usage context
- **Quando NÃO usar:** Code review (trident), planejamento de componentes (component-architect)

### context-guardian
- **O que faz:** Monitora context window, alerta quando perto de 40-50%, gera handoff pra /clear
- **Triggers PT-BR:** "quanto de contexto usei?", "tá pesado?", "hora do /clear?", "gera um handoff"
- **Triggers EN:** check context, context window, handoff document, context budget
- **Modes:** --check, --handoff, --budget
- **Input:** Estado atual da conversa
- **Output:** Status (🟢/🟡/🔴) + handoff document se necessário
- **Iron Law:** NEVER let context exceed 50% without alerting
- **Quando NÃO usar:** Conversa curta (<5 exchanges), fim da tarefa

---

## Optimization

### geo-optimizer
- **O que faz:** Otimiza descriptions de skills/pacotes pra GEO (descoberta por agentes)
- **Triggers PT-BR:** "a description tá fraca", "ninguém acha minha skill", "otimizar pra agentes"
- **Triggers EN:** optimize description, GEO, keyword bombing, improve triggering
- **Modes:** --analyze, --optimize, --benchmark, --keywords
- **Input:** Description existente ou nova skill
- **Output:** Description otimizada com score /15 + before/after comparison
- **Iron Law:** NEVER optimize without generating keywords from agent's perspective first
- **Quando NÃO usar:** Prompts (prompt-engineer --geo), criar skill do zero (skill-builder)

### cli-skill-wrapper
- **O que faz:** Transforma API em CLI tool otimizado pra agentes + gera SKILL.md companion
- **Triggers PT-BR:** "quero wrapar essa API", "o MCP tá pesado", "fazer um CLI pra isso"
- **Triggers EN:** wrap API, create CLI tool, API to CLI, agent tooling
- **Modes:** --analyze, --wrap, --compare
- **Input:** API (REST, SDK, binary, MCP)
- **Output:** Script CLI + SKILL.md
- **Iron Law:** NEVER wrap without verifying CLI output is shorter than raw API JSON
- **Quando NÃO usar:** API usada 1x, MCP funciona bem, criar skill sem API (skill-builder)

---

## Infra

### vps-infra-audit
- **O que faz:** Pipeline de 3 agentes para auditoria profunda de infraestrutura VPS
- **Triggers PT-BR:** "auditoria de VPS", "meu servidor tá seguro?", "infra audit"
- **Triggers EN:** VPS audit, infrastructure review, server security
- **Input:** Acesso SSH ou descrição de infra
- **Output:** Findings com severity e recomendações

---

## People

### tech-lead-pm
- **O que faz:** Gestão de projetos e liderança técnica para líder de primeira viagem
- **Triggers PT-BR:** "como gerenciar equipe", "liderança", "gestão de projeto", "1:1"
- **Triggers EN:** team management, tech lead, project management

### comunicacao-clientes
- **O que faz:** Comunicação com clientes via WhatsApp/Telegram
- **Triggers PT-BR:** "responder cliente", "mensagem pro cliente", "WhatsApp"
- **Input:** Contexto da conversa com cliente
- **Output:** Mensagem formatada para o canal

---

## Workflow

### schedule
- **O que faz:** Criar tarefas agendadas que rodam on demand ou automaticamente
- **Triggers:** "agendar tarefa", "scheduled task", "rodar a cada X horas"

### pattern-importer
- **O que faz:** Automatiza técnica .tmp: clone repo referência → analisa padrão → extrai → limpa
- **Triggers PT-BR:** "importa um padrão", "como isso é feito em outros projetos?", "clona pra eu ver"
- **Triggers EN:** import pattern, clone reference, .tmp technique, extract pattern from repo
- **Modes:** --import, --analyze, --clean, --list
- **Input:** Padrão desejado + stack do projeto
- **Output:** Pattern document com insights aplicáveis
- **Iron Law:** NEVER leave .tmp directories behind
- **Quando NÃO usar:** Referências teóricas (reference-finder), copiar código (clone normal)

---

## Marketing

### copy
- **O que faz:** Escreve, revisa e otimiza copy para qualquer canal com 8 modos (landing, social, email, cold-email, whatsapp, blog-seo, ux, ads). Usa frameworks AIDA, PAS, SB7, Value Equation e os 5 níveis de consciência de Schwartz
- **Triggers PT-BR:** "escreve copy", "melhora esse texto", "headline pra landing", "email sequence", "copy de anúncio", "texto pra landing page", "escreve um post", "cria um email"
- **Triggers EN:** write copy, improve this copy, landing page copy, email sequence, ad copy, social post copy, headline
- **Modes:** --mode landing/social/email/cold-email/whatsapp/blog-seo/ux/ads, --edit, --brief, --framework
- **Input:** Objetivo + canal + audiência + produto (ou copy existente para edição)
- **Output:** Copy estruturado com anotações explicando as escolhas + alternativas de headline
- **Iron Law:** NUNCA escreva copy sem classificar o nível de consciência da audiência (Schwartz) antes de escolher o framework
- **Quando NÃO usar:** Estratégia de posicionamento (product-marketing-context), auditoria SEO técnica (seo), fluxo UX completo (ux-audit), mensagens com clientes (comunicacao-clientes)

### product-marketing-context
- **O que faz:** Cria e mantém o documento `.agents/product-marketing-context.md` com posicionamento, ICP, proposta de valor e messaging — contexto base que todas as outras skills de marketing referenciam para evitar repetição
- **Triggers PT-BR:** "contexto de produto", "contexto de marketing", "posicionamento", "quem é meu público-alvo", "descreve meu produto", "ICP", "perfil de cliente ideal", "configurar contexto"
- **Triggers EN:** product context, marketing context, set up context, positioning, who is my target audience, describe my product, ICP, ideal customer profile
- **Input:** Projeto existente (pode auto-draftar lendo o repo) ou informações fornecidas em conversa
- **Output:** `.agents/product-marketing-context.md` com posicionamento, ICP, diferenciais, pricing, messaging e personas
- **Quando NÃO usar:** Escrever copy diretamente (copy), discovery de produto/PRD (product-discovery-prd)

### ai-seo
- **O que faz:** Otimiza conteúdo para ser citado por sistemas de IA (Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, Copilot). Cobre GEO, AEO, LLMO — estratégias para aparecer em respostas geradas por IA
- **Triggers PT-BR:** "AI SEO", "GEO", "AEO", "LLMO", "otimizar para IA", "aparecer no ChatGPT", "aparecer no Perplexity", "AI Overviews", "citações de IA", "visibilidade em IA", "zero-click search"
- **Triggers EN:** AI SEO, AEO, GEO, LLMO, answer engine optimization, generative engine optimization, LLM optimization, AI Overviews, optimize for ChatGPT, optimize for Perplexity, AI citations, AI visibility, LLM mentions
- **Input:** Site/conteúdo + queries-alvo + objetivo de visibilidade em IA
- **Output:** Estratégia de otimização para IA com recomendações de conteúdo, estrutura e autoridade
- **Quando NÃO usar:** SEO técnico tradicional (seo), dados estruturados/schema (seo --technical), auditoria on-page clássica (seo --audit)

### site-architecture
- **O que faz:** Planeja hierarquia de páginas, navegação, estrutura de URLs, breadcrumbs e internal linking de sites. Foco em IA de informação (information architecture) para UX e SEO
- **Triggers PT-BR:** "sitemap", "estrutura do site", "hierarquia de páginas", "arquitetura de site", "IA do site", "navegação", "estrutura de URLs", "o que páginas preciso", "como organizar meu site"
- **Triggers EN:** sitemap, site map, visual sitemap, site structure, page hierarchy, information architecture, IA, navigation design, URL structure, breadcrumbs, internal linking strategy, website planning
- **Input:** Tipo de site + objetivos + audiências + estado atual (novo ou reestruturação)
- **Output:** Hierarquia de páginas, estrutura de navegação, padrões de URL, estratégia de internal linking
- **Quando NÃO usar:** Sitemap XML técnico (seo --technical), auditoria SEO (seo --audit), dados estruturados (seo --technical)

### competitor-alternatives
- **O que faz:** Cria páginas de comparação e alternativas para SEO e sales enablement. Cobre 4 formatos: alternativa singular, alternativas plural, você vs concorrente, concorrente vs concorrente
- **Triggers PT-BR:** "página de alternativa", "página vs", "comparação com concorrente", "página de comparação", "como nos comparamos com X", "battle card", "teardown de concorrente", "alternativas ao [produto]"
- **Triggers EN:** alternative page, vs page, competitor comparison, comparison page, [Product] vs [Product], [Product] alternative, competitive landing pages, battle card, competitor teardown
- **Input:** Produto + concorrentes a cobrir + diferenciais + ICP
- **Output:** Páginas de comparação/alternativa com estrutura SEO, tabelas de comparação, posicionamento e CTAs
- **Quando NÃO usar:** Materiais internos de vendas (sales-enablement), auditoria SEO geral (seo)

### sales-enablement
- **O que faz:** Cria materiais de vendas B2B que reps realmente usam: pitch decks, one-pagers, docs de objeções, demo scripts, playbooks e propostas
- **Triggers PT-BR:** "deck de vendas", "pitch deck", "one-pager", "leave-behind", "objeções", "análise de ROI", "script de demo", "talk track", "playbook de vendas", "template de proposta", "materiais de vendas", "o que dar pra minha equipe de vendas"
- **Triggers EN:** sales deck, pitch deck, one-pager, leave-behind, objection handling, deal-specific ROI analysis, demo script, talk track, sales playbook, proposal template, buyer persona card, sales materials
- **Input:** Produto + motion de vendas + personas + ativos específicos necessários
- **Output:** Materiais de vendas estruturados (decks, docs, scripts) prontos para uso pelos reps
- **Quando NÃO usar:** Páginas de comparação para SEO (competitor-alternatives), copy para site de marketing (copy), cold outreach (copy --mode cold-email)

### free-tool-strategy
- **O que faz:** Planeja, avalia e define estratégia para ferramentas gratuitas de marketing (engineering as marketing) — calculadoras, geradores, graders, audit tools — para geração de leads, SEO e brand awareness
- **Triggers PT-BR:** "engineering as marketing", "ferramenta gratuita", "ferramenta de marketing", "calculadora", "gerador", "ferramenta interativa", "ferramenta de lead gen", "recurso gratuito", "calculadora de ROI", "grader tool", "audit tool", "devo construir uma ferramenta gratuita"
- **Triggers EN:** engineering as marketing, free tool, marketing tool, calculator, generator, interactive tool, lead gen tool, free resource, ROI calculator, grader tool, audit tool, should I build a free tool, tools for lead gen
- **Input:** Produto + público-alvo + objetivo (leads/SEO/awareness) + recursos disponíveis para construir
- **Output:** Estratégia de ferramenta: conceito validado, tipo de ferramenta, stack sugerida, plano de promoção e métricas
- **Quando NÃO usar:** Lead magnets estáticos (ebooks, checklists — use copy), ferramentas internas sem objetivo de marketing

### launch-strategy
- **O que faz:** Planeja lançamentos de produto, anúncios de feature e estratégias GTM. Cobre Product Hunt, beta launch, early access, waitlists e releases contínuos
- **Triggers PT-BR:** "lançamento", "Product Hunt", "feature release", "anúncio", "go-to-market", "beta launch", "early access", "waitlist", "atualização de produto", "como lanço isso", "checklist de lançamento", "plano GTM", "vamos shipar"
- **Triggers EN:** launch, Product Hunt, feature release, announcement, go-to-market, beta launch, early access, waitlist, product update, how do I launch this, launch checklist, GTM plan, we're about to ship
- **Input:** Produto/feature a lançar + audiência + canais disponíveis + timeline
- **Output:** Plano de lançamento com checklist, cronograma, mensagens por canal e estratégia de momentum
- **Quando NÃO usar:** Marketing contínuo pós-lançamento (use copy + seo), materiais de vendas (sales-enablement)

---

## Maestro (esta skill)
- **O que faz:** Orquestra e roteia entre todas as skills
- **Triggers:** "qual skill usar?", "o que posso fazer?", "me ajuda a decidir"
- **Modes:** --suggest, --chain, --catalog, --health, --loose
