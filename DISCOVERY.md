# Discovery: Construindo o Arsenal Definitivo de Skills

**Status:** Em andamento
**Última atualização:** 2026-04-03

---

## Objetivo

Transformar o `skillforge-arsenal` de uma coleção pessoal em um arsenal completo e organizado por domínio, onde cada tarefa tem uma skill focada (não generalista). Inspirado pelo ecossistema do skills.sh.

---

## Pesquisa: Como o Ecossistema de Skills Funciona

### skills.sh (Vercel)
- Diretório aberto de skills para agentes IA (Claude Code, Cursor, Copilot, etc.)
- CLI: `npx skills add <owner/repo>` para instalar
- +91K skills listadas, com leaderboard por installs
- Skills são SKILL.md com YAML frontmatter (name, description) + instruções em Markdown
- Instalação local: `.claude/skills/` (projeto) ou `~/.claude/skills/` (global)
- Suporta 41+ agentes diferentes

### Formato de uma Skill
```yaml
---
name: minha-skill
description: O que faz e quando usar
---

# Instruções em Markdown
```

### Onde ficam instaladas
- **Projeto:** `./.claude/skills/<nome>/SKILL.md`
- **Global:** `~/.claude/skills/<nome>/SKILL.md`
- Symlink é o método recomendado (single source of truth)

### CLI úteis
- `npx skills add <repo>` — instalar
- `npx skills add <repo> -s <nome>` — instalar skill específica
- `npx skills add <repo> -g` — instalar global
- `npx skills list` — listar instaladas
- `npx skills find <query>` — buscar no diretório
- `npx skills update` — atualizar todas
- `npx skills init <nome>` — criar template

---

## Artigo: Deborah Folloni (Substack)

### Insights principais
- "Taste is the new moat" — design diferenciado é vantagem competitiva quando IA nivela tudo
- Skill é um playbook carregado sob demanda (diferente de system prompt)
- Pré-requisito: ter identidade visual mínima (logo, paleta, tipografia, conceito)
- A skill `frontend-design` sozinha não basta — precisa de contexto de marca

### Workflow recomendado
1. Preparar assets (logos, cores, fontes)
2. Prompt específico mencionando a skill + assets
3. Iniciar conversa nova para a skill ser detectada

---

## Top Skills de Frontend no skills.sh

### Design & Visual
| Skill | Repo | Installs |
|-------|------|----------|
| frontend-design | anthropics/skills | 222K |
| web-design-guidelines | vercel-labs/agent-skills | 213K |
| ui-ux-pro-max | nextlevelbuilder/ui-ux-pro-max-skill | 91K |
| frontend-design | pbakaus/impeccable | 37K |
| tailwind-design-system | wshobson/agents | 26K |
| canvas-design | anthropics/skills | 28K |
| brand-guidelines | anthropics/skills | 20K |
| theme-factory | anthropics/skills | 21K |
| landing-page-design | inferen-sh/skills | 8K |

### Componentes & Patterns
| Skill | Repo | Installs |
|-------|------|----------|
| vercel-react-best-practices | vercel-labs/agent-skills | 264K |
| vercel-composition-patterns | vercel-labs/agent-skills | 107K |
| shadcn | shadcn/ui | 53K |
| react:components | google-labs-code/stitch-skills | 26K |
| ui-component-patterns | supercent-io/skills-template | 11K |
| web-artifacts-builder | anthropics/skills | 22K |

### Frameworks
| Skill | Repo | Installs |
|-------|------|----------|
| next-best-practices | vercel-labs/next-skills | 48K |
| vercel-react-native-skills | vercel-labs/agent-skills | 76K |
| vue-best-practices | hyf0/vue-skills | 14K |
| vue | antfu/skills | 13K |
| nuxt | antfu/skills | 9K |
| vite | antfu/skills | 12K |

### Acessibilidade & Responsividade
| Skill | Repo | Installs |
|-------|------|----------|
| web-accessibility | supercent-io/skills-template | 13K |
| responsive-design | supercent-io/skills-template | 11K |

### TypeScript & Estado
| Skill | Repo | Installs |
|-------|------|----------|
| typescript-advanced-types | wshobson/agents | 19K |
| state-management | supercent-io/skills-template | 11K |

---

## Visão: Organização por Domínio (Foco Frontend)

A ideia é ter skills **focadas e separadas**, não generalistas. Exemplo para frontend:

### Camada de Design
- **UI Design** — visual, cores, tipografia, hierarquia, espaçamento
- **UX Audit** — heurísticas, fluxos, usabilidade (JÁ TEMOS)
- **Brand/Identity** — guidelines de marca, consistência visual
- **Responsive Design** — breakpoints, mobile-first, adaptação

### Camada de Componentes
- **Component Architecture** — padrões de composição, atomic design, reusabilidade
- **shadcn/UI Library** — como usar shadcn corretamente, customizar temas
- **Form Patterns** — validação, UX de formulários, acessibilidade

### Camada de Implementação
- **React Best Practices** — hooks, performance, patterns
- **Next.js Patterns** — App Router, SSR, caching, ISR
- **Tailwind System** — utility-first, design tokens, custom plugins
- **State Management** — quando usar o quê (zustand, jotai, context)

### Camada de Qualidade
- **Accessibility (a11y)** — WCAG, aria, screen readers
- **Performance** — Core Web Vitals, lazy loading, bundle size
- **Testing** — component tests, visual regression, e2e

---

## Pesquisa: 5 Vídeos Processados

### Video 1: Skill mais baixada (Omer / Agent Tools)
- **GEO**: otimizar description pra agentes (não humanos). Usar Claude pra gerar keywords.
- **CLI-First > MCP**: CLIs preservam context window
- **Composable Tools**: ferramentas modulares que o agente encadeia
- Análise completa: `research/video-transcripts/01-skill-mais-baixada-omer.md`

### Video 2: Vibe Coding Não Funciona (Epic)
- **4 etapas**: `/spec` → `/break` → `/plan` → `/execute`
- **Agentes especializados**: Model Writer (banco), Component Writer (front)
- **Thin Client / Fat Server**: zero lógica no front
- Análise completa: `research/video-transcripts/02-vibe-coding-nao-funciona.md`

### Video 3: Skills > Agentes
- **Progressive Loading**: só carrega skill quando precisa
- **Retroalimentação**: "registra na skill pra próxima vez"
- **Determinístico + Não-determinístico**: scripts + IA
- Análise completa: `research/video-transcripts/03-skills-vs-agentes.md`

### Video 4: Workflow Anti-Vibe Coding (SDD)
- **3 passos**: Research → Spec → Implement com `/clear` entre cada
- **Regra dos 40-50%**: nunca estourar context window
- **Técnica .tmp**: clonar repo, analisar padrão, deletar
- Análise completa: `research/video-transcripts/04-workflow-anti-vibe-coding.md`

### Video 5: Frontend Design Skill
- **Skill + identidade visual = resultado profissional**
- **Workflow 2 fases**: gerar básico → refinar com skill + assets
- Análise completa: `research/video-transcripts/05-frontend-design-skill.md`

---

## Pesquisa: Ferramentas e Repos de Referência

### Skill Forge (sanyuan0704) — 12 técnicas battle-tested
Clonado em `community/sanyuan-skills/`. Meta-skill para criar skills de qualidade.
Técnicas: Progressive Loading, Keyword Bombing, Workflow Checklist, Script Encapsulation, Question-Style Instructions, Confirmation Gates, Pre-Delivery Checklist, Parameter System, Reference Organization, CLI+Skill, Iron Law, Anti-Patterns.

### HumanLayer — Workflow Commands
Clonado em `community/humanlayer-commands/`. 29 commands incluindo:
- `research_codebase.md` — documenta codebase as-is com sub-agents
- `create_plan.md` — planning iterativo com research paralelo
- `implement_plan.md` — execução por fases com verification gates

### Trident — Repo Review v2
Copiado em `skills/trident/`. Pipeline 3 agentes: Scan→Verify→Judge.
Merge do code-review-expert + repo-review. Multi-lens (SOLID, security, quality, dead code).

### ByteRover — Context Tree
Análise em `research/byterover-context-tree.md`. Sistema hierárquico de memória persistente.
Domínios → Tópicos → Subtópicos com scoring, archiving e manifestos.

---

## Decisões tomadas

- [x] Estrutura: `skills/` (nossas) + `community/` (terceiros) + `research/` (análises)
- [x] Stack frontend: React/Next + Tailwind + shadcn
- [x] Trident substitui repo-review
- [x] Abordagem bootstrap: skill-builder v2 → prompt-engineer v2 → reference-finder v3

## Decisões pendentes

- [ ] Publicar skills no skills.sh? Quando?
- [ ] Implementar Context Tree completo ou versão simplificada?
- [ ] Skills globais (~/.claude/skills/) vs. por projeto?

---

## Roadmap

```
Fase 0 (Setup)           ✅ Completa
Fase 1 (Skill Builder)   ← Próxima
Fase 2 (Prompt Eng.)
Fase 3 (Ref. Finder)
Fase 4 (Trident)         Paralelo com 1-3
Fase 5 (Frontend)
Fase 6 (Commands)
Fase 7 (Context Tree)
```

Ver plano completo: `.claude/plans/swift-popping-zephyr.md`
Catálogo de padrões: `research/patterns-catalog.md`

---

## Log de conversa

### 2026-04-03 — Sessão 1
- Criado repo `skillforge-arsenal` com 18 skills pessoais existentes
- Pesquisado skills.sh, artigo da Deborah Folloni, formato técnico de skills
- Mapeado 47+ skills de frontend disponíveis no ecossistema
- Definida visão de organização por camadas (Design → Componentes → Implementação → Qualidade)

### 2026-04-03 — Sessão 1 (continuação)
- Processados 5 vídeos (6000 linhas de transcrições) com agentes em paralelo
- Pesquisados: Skill Forge, HumanLayer, Trident, ByteRover, skills.sh
- Lidos prompts Pluma (design.json + brief) como base pra skill de design
- Clonados repos: sanyuan-skills, humanlayer-commands
- Copiado Trident (repo-review v2 do amigo)
- Criados: patterns-catalog.md, byterover-context-tree.md, 5 análises de vídeo
- Plano de 8 fases aprovado e documentado
- **Fase 0 completa** — próximo: Fase 1 (Skill Builder v2)
