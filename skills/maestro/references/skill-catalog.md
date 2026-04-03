# Skill Catalog — Mapa Completo do Arsenal

Consulte este arquivo no **Phase 2** quando for rotear o intent do usuário para skills.

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

### repo-review ⚠️ DEPRECATED
- **Status:** Substituído por trident. Mantido apenas como referência histórica.
- **Ação:** Sempre redirecionar para trident.

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
- **O que faz:** Arquitetura e padrões para automações n8n
- **Triggers PT-BR:** "automação n8n", "workflow n8n", "integração"
- **Triggers EN:** n8n automation, workflow architecture
- **Input:** Requisito de automação
- **Output:** Workflow design, node configuration, error handling patterns

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

---

## Maestro (esta skill)
- **O que faz:** Orquestra e roteia entre todas as skills
- **Triggers:** "qual skill usar?", "o que posso fazer?", "me ajuda a decidir"
- **Modes:** --suggest, --chain, --catalog, --health
