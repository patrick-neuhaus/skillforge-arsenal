# Discovery: Skillforge Arsenal

**Status:** Fases 0-7 completas + Quality Audit + Maestro — ecossistema operacional
**Última atualização:** 2026-04-03
**Plano detalhado:** `.claude/plans/swift-popping-zephyr.md`
**Catálogo de padrões:** `research/patterns-catalog.md`

---

## Objetivo

Transformar o `skillforge-arsenal` de uma coleção de 18 skills pessoais em um **ecossistema de skills de alta qualidade** com abordagem bootstrap: cada skill potencializa a próxima.

**Abordagem:** skill-builder v2 → prompt-engineer v2 → reference-finder v3 → skills de frontend → workflow commands → context tree.

---

## Estrutura do Repo

```
skillforge-arsenal/
├── skills/                    # 25 skills
│   ├── comunicacao-clientes/
│   ├── component-architect/   # NOVO Fase 5: atomic design, shadcn, composição
│   ├── context-tree/          # NOVO Fase 7: knowledge management com scoring
│   ├── docx/
│   ├── lovable-knowledge/
│   ├── n8n-architect/
│   ├── pdf/
│   ├── pptx/
│   ├── product-discovery-prd/
│   ├── prompt-engineer/       # v2 (Fase 2)
│   ├── react-patterns/        # NOVO Fase 5: App Router, SSR, Thin Client
│   ├── reference-finder/      # v3 (Fase 3)
│   ├── repo-review/           # DEPRECATED → use trident
│   ├── schedule/
│   ├── sdd/                   # NOVO Fase 6: Spec Driven Development pipeline
│   ├── security-audit/
│   ├── skill-builder/         # v2 (Fase 1)
│   ├── supabase-db-architect/
│   ├── tech-lead-pm/
│   ├── maestro/               # NOVO: Skill orquestradora — routing + chains
│   ├── trident/               # v2 (Fase 4): Scan→Verify→Judge
│   ├── ui-design-system/      # NOVO Fase 5: design tokens, design.json
│   ├── ux-audit/
│   ├── vps-infra-audit/
│   └── xlsx/
├── community/                 # Repos de referência clonados
│   ├── sanyuan-skills/        # Skill Forge + code-review-expert + sigma
│   └── humanlayer-commands/   # 29 commands anti-vibecoding
├── research/                  # Análises e documentação
│   ├── video-transcripts/     # 5 análises completas dos vídeos
│   ├── pluma-prompts/         # design.json + brief (base pra skill de design)
│   ├── patterns-catalog.md    # 23 padrões catalogados de 6+ fontes
│   └── byterover-context-tree.md  # Análise do sistema de memória
├── DISCOVERY.md               # Este arquivo — hub central
└── README.md
```

**Skills pessoais ficam em:** `C:\Users\Patrick Neuhaus\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\2e0d2a98-c8b7-4df2-967a-4b0f524507b0\8b27bf1e-bcdb-40be-86ac-68b8d19e9de9\skills\`

**GitHub:** https://github.com/patrick-neuhaus/skillforge-arsenal (privado)

---

## Ecossistema skills.sh (Vercel)

- Diretório aberto: 91K+ skills, 41+ agentes (Claude Code, Cursor, Copilot, etc.)
- Formato: `SKILL.md` com YAML frontmatter (`name`, `description`) + Markdown
- **CLI:** `npx skills add <repo>`, `npx skills find <query>`, `npx skills list`, `npx skills update`, `npx skills init <nome>`
- **Instalação:** `.claude/skills/` (projeto) ou `~/.claude/skills/` (global). Symlink recomendado.
- **Ranking:** find-skills da Vercel (open source) indexa e recomenda skills
- **Top skills frontend:** frontend-design (222K), vercel-react-best-practices (264K), web-design-guidelines (213K), shadcn (53K), ui-ux-pro-max (91K)

---

## Insights dos 5 Vídeos (Deborah Folloni / DevGPT)

### Video 1: Omer — Skill mais baixada (1M+ installs)
**Arquivo:** `research/video-transcripts/01-skill-mais-baixada-omer.md`

**GEO (Generative Engine Optimization)** — o conceito mais importante:
- "The agents are the customers for skills" — otimizar pra agentes, não humanos
- Ler código do find-skills (open source) pra entender ranking
- Usar o próprio Claude pra gerar keywords ("que termos você buscaria pra encontrar X?")
- Skills que resolvem problemas específicos = buscas previsíveis

**CLI-First > MCP:**
- MCPs bloatam context window com JSON enorme
- CLI tools retornam respostas curtas, preservam performance
- Padrão superior: SKILL.md + CLI tool executável (não apenas system prompt)

**Padrões replicáveis:**
- **Autodiscovery:** skill permite que agente descubra capacidades dinamicamente
- **Composable Tools:** ferramentas pequenas e modulares que o agente encadeia sozinho
- **Permission Gate:** aprovar antes de ações irreversíveis (ex: postar no Twitter)

### Video 2: Vibe Coding Não Funciona — Epic Builder
**Arquivo:** `research/video-transcripts/02-vibe-coding-nao-funciona.md`

**5 problemas do vibe coding:**
1. IA engasga com tarefas grandes (context window cheia)
2. Código bagunçado (over-engineering, duplicação)
3. IA "desobedece" (infere errado quando não tem instrução clara de QUAIS arquivos)
4. Arrumar uma coisa quebra outra (falta modularização)
5. Gafes de segurança (lógica no front, chaves expostas)

**Workflow 4 etapas:**
1. `/spec` — gera documento: páginas + componentes + behaviors
2. `/break` — quebra em issues atômicas (1 por behavior)
3. `/plan` — pesquisa codebase + docs externos, enriquece issue com paths + ações + pseudocódigo
4. `/execute` — implementa com agentes especializados por camada (Model Writer, Component Writer)

**Regras:**
- **Thin Client / Fat Server** — zero lógica de negócio no front
- **`/references` como guardrail** — `architecture.md` + `design-system.md` em todo projeto
- **Protótipo primeiro, lógica depois**
- **Especificar arquivos explicitamente:** `[path] → [o que fazer]`

### Video 3: Skills > Agentes
**Arquivo:** `research/video-transcripts/03-skills-vs-agentes.md`

**Progressive Loading (conceito mais importante):**
- System prompt lista APENAS nome + descrição de cada skill (1 linha)
- Conteúdo completo carrega SÓ quando a IA identifica que precisa
- Preserva context window para a tarefa real

**Retroalimentação:**
- "Registra isso na skill pra próxima vez" = melhoria contínua sem deploy
- Skill evolui com uso, acumulando conhecimento em `references/`

**Determinístico + Não-determinístico:**
- Scripts (consistência, exatidão) + IA (criatividade, decisão)
- Exemplo: IA decide layout → script Python aplica branding no PPTX

**Roteiro de perguntas no SKILL.md:**
- Sempre incluir coleta estruturada antes de executar
- Obrigatórias + opcionais, sequência lógica

**Estrutura demonstrada:**
```
skill/
├── SKILL.md          # System prompt + roteiro + regras
├── references/       # Dados, exemplos, planilhas
└── scripts/          # Operações determinísticas
```

### Video 4: SDD — Spec Driven Development
**Arquivo:** `research/video-transcripts/04-workflow-anti-vibe-coding.md`

**3 passos com `/clear` entre cada:**
1. **Research** — pesquisa codebase + docs + padrões → gera `prd.md`
2. **Spec** — lê prd.md → gera `spec.md` com paths exatos + ações + pseudocódigo
3. **Implement** — lê spec.md → executa com context window quase toda livre

**Regra dos 40-50%:** nunca usar mais que metade da context window. Quando passar, `/clear`.

**Técnica `.tmp`:** clonar repo de referência → importar em pasta `.tmp` → pedir ao Claude analisar padrão → deletar pasta.

**Handoff via arquivos .md:** prd.md e spec.md são a "memória" entre conversas. O `/clear` mata o contexto, os arquivos sobrevivem.

**Citação:** "Quem transforma água em vinho é Jesus, não a IA" — qualidade do input = qualidade do output.

### Video 5: Frontend Design Skill
**Arquivo:** `research/video-transcripts/05-frontend-design-skill.md`

**Skill + identidade visual = resultado profissional:**
- Skill sozinha = genérico. Skill + assets de marca = distinto e profissional.
- Pré-requisito: logo (dark/light), paleta hex, 2 fontes (display + body), conceito visual

**Workflow 2 fases:**
1. Gerar versão funcional básica
2. Refinar com skill + assets (prompt: "melhore o design usando a skill + essas cores/fontes/assets")

**Assets concretos > descrições:** prints de hex codes e nomes de fontes como imagens anexadas são mais eficazes que descrições textuais.

---

## Skill Forge — 12 Técnicas Battle-Tested

Repo: `community/sanyuan-skills/skills/skill-forge/`
**SKILL.md principal + 6 arquivos de referência + 3 scripts**

| # | Técnica | O que faz |
|---|---------|-----------|
| 1 | **Progressive Loading** | SKILL.md <250 linhas, refs carregadas sob demanda |
| 2 | **Keyword Bombing** | Description otimizada pra agentes (GEO) |
| 3 | **Workflow Checklist** | Passos numerados e trackáveis com warnings |
| 4 | **Script Encapsulation** | Operações determinísticas em scripts (menos tokens) |
| 5 | **Question-Style Instructions** | Perguntas concretas > comandos abstratos |
| 6 | **Confirmation Gates** | Aprovar antes de ações críticas |
| 7 | **Pre-Delivery Checklist** | QA antes do output final |
| 8 | **Parameter System** | Flags e variantes (`--quick`, `--full`) |
| 9 | **Reference Organization** | Refs por domínio, carregamento seletivo |
| 10 | **CLI + Skill Pattern** | CLI tools > MCP Servers |
| 11 | **Iron Law** | Uma regra inquebrável anti-atalhos |
| 12 | **Anti-Pattern Documentation** | Listar explicitamente o que NÃO fazer |

---

## HumanLayer — Workflow Anti-Vibecoding

Repo: `community/humanlayer-commands/.claude/commands/`
**29 commands**, os mais importantes:

- **`research_codebase.md`** — Documenta codebase as-is (nunca sugere melhorias). Sub-agents: codebase-locator (WHERE), codebase-analyzer (HOW), pattern-finder (PATTERNS). Output: documento com YAML frontmatter, GitHub permalinks.
- **`create_plan.md`** — Planning iterativo: context gathering → research/discovery → plan structure → detailed writing → sync/review. Plans em `thoughts/shared/plans/YYYY-MM-DD-description.md`. Separa success criteria em Automated (commands) e Manual (human testing).
- **`implement_plan.md`** — Execução por fases: revisa plano → cria tracking → implementa → verifica após cada fase (automated + manual). Pausa entre fases pra verificação humana. Adapta à realidade sem abandonar intent do plano.

---

## Trident — Repo Review v2

Skill: `skills/trident/`
**Pipeline 3 agentes: Scan → Verify → Judge**

- **Scanner** — Multi-lens: SOLID, security, quality, dead code. Forced counterarguments. Max 15 findings.
- **Verifier** — Re-lê código independente. CONFIRMED/REJECTED/INSUFFICIENT_EVIDENCE.
- **Arbiter** — Verdicts finais: REAL_BUG/NOT_A_BUG/NEEDS_HUMAN_CHECK.

**Severidade:** P0 (block merge) → P1 (fix before merge) → P2 (fix or follow-up) → P3 (optional)
**Shared Output Contract:** bug_id schema atravessa os 3 agentes.
**6 review modes:** unstaged, staged, all-local, PR, range, directory.
**Merge de:** code-review-expert + repo-review (skills que já temos)

---

## ByteRover — Context Tree

Análise: `research/byterover-context-tree.md`
**Sistema de memória persistente hierárquico em markdown.**

- **Hierarquia:** Domínios → Tópicos → Subtópicos (max 1 nível de sub)
- **Scoring:** importance (0-100, +3 busca, +5 curadoria), recency (0-1, decay 21d), maturity (draft→validated→core)
- **Archive:** maturity=draft AND importance<35 → stub searchable (~220 tokens) + full backup
- **`_index.md`:** Resumos condensados por nível, propagam pra cima
- **`_manifest.json`:** 3 lanes (summaries, contexts, stubs)
- **Relações:** paths explícitos no campo `related` = navegação graph-like

---

## Prompts Pluma (Base pra Skill de Design)

Arquivos: `research/pluma-prompts/`

**`claude-prompt-01.txt`:** Prompt inicial com seções da landing page (Hero, Why Pluma, Pluma Answers, Safety, CTA, Footer). Pede ao Claude gerar um `design.json` analisando screenshot de referência.

**`replit-prompt-02.txt`:** Prompt completo com:
- `design.json` detalhado: design principles, color palette (primary/accent/neutral), typography (serif headings + sans body), spacing philosophy, component specs (buttons/cards/icons/badges/inputs/nav/footer/chat UI), effects (shadows/gradients/transitions), patterns (hero layout, section rhythm, content hierarchy), responsive breakpoints, imagery guidelines
- Brief por seção com instruções específicas de layout, animação, micro-interações
- **Dois design systems:** um usando Playfair Display (serif) + Inter, outro todo Inter (sans-serif)

**Como usar:** Base pra criar skill `ui-design-system` que gera design.json a partir de identidade visual mínima.

---

## Decisões Tomadas

- [x] Estrutura: `skills/` (nossas) + `community/` (terceiros) + `research/` (análises)
- [x] Stack frontend: React/Next + Tailwind + shadcn
- [x] Trident substitui repo-review
- [x] Bootstrap: skill-builder v2 → prompt-engineer v2 → reference-finder v3
- [x] Prompts Pluma = base pra skill de UI design

## Decisões Pendentes

- [ ] Publicar skills no skills.sh? Quando?
- [x] Context Tree completo ou versão simplificada? → Versão simplificada (markdown-based, sem _manifest.json)
- [ ] Skills globais (~/.claude/skills/) vs. por projeto?

---

## Roadmap

```
Fase 0 (Setup)           ✅ Completa
Fase 1 (Skill Builder)   ✅ v2 — 211 linhas, 12 técnicas, init/validate scripts
Fase 2 (Prompt Eng.)     ✅ v2 — 183 linhas, claude-4x-guide.md extraído
Fase 3 (Ref. Finder)     ✅ v3 — 168 linhas, scoring ByteRover, organization-guide.md
Fase 4 (Trident)         ✅ 174 linhas, frontmatter GEO, repo-review deprecated
Fase 5 (Frontend)        ✅ 3 skills: ui-design-system (125L), component-architect (147L), react-patterns (133L)
Fase 6 (SDD)             ✅ sdd — 164 linhas, pipeline Research→Spec→Implement→Review
Fase 7 (Context Tree)    ✅ context-tree — 175 linhas, scoring ByteRover, prune/archive
Quality Audit             ✅ Avaliação 70%→85%: maestro, sdd refs, integrações bidirecionais
```

---

## Log de Conversa

### 2026-04-03 — Sessão 1
- Criado repo `skillforge-arsenal` com 18 skills pessoais
- Skills encontradas em: `AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/.../skills/`
- Pesquisado: skills.sh (Vercel), artigo Substack, 47+ skills frontend
- Processados 5 vídeos (6000 linhas) com 5 agentes em paralelo
- Pesquisados: Skill Forge, HumanLayer, Trident, ByteRover
- Lidos prompts Pluma (design.json + brief)
- Clonados: sanyuan-skills, humanlayer-commands
- Copiado: Trident (repo-review v2)
- Criados: patterns-catalog.md, byterover-context-tree.md, 5 análises
- Plano de 8 fases aprovado
- **Fase 0 completa** — próximo: Fase 1 (Skill Builder v2)

### 2026-04-03 — Sessão 2
- **Fase 1 completa:** Skill Builder v2 — 211 linhas (de 446), 12 técnicas incorporadas, scripts init_skill.py + validate.py, 3 novas references (discovery-guide, writing-guide, description-guide)
- **Fase 2 completa:** Prompt Engineer v2 — 183 linhas (de 307), Claude 4.x guide extraído pra reference, Iron Law + workflow checklist + parameter system
- **Fase 3 completa:** Reference Finder v3 — 168 linhas (de 265), scoring ByteRover (importance/maturity/recency), organization-guide.md com PARA+Zettelkasten+MOCs
- **Fase 4 completa:** Trident — 174 linhas (de 328), frontmatter GEO adicionado, review-modes.md extraído, repo-review deprecated

### 2026-04-03 — Sessão 3
- **Fase 5 completa:** 3 skills de frontend criadas
  - `ui-design-system` — 125 linhas, Iron Law: "concrete brand inputs required", design-json-schema.md com schema completo + Tailwind/CSS output examples
  - `component-architect` — 147 linhas, Iron Law: "check existing before creating", composition-patterns.md com atomic design detalhado + shadcn patterns + health metrics
  - `react-patterns` — 133 linhas, Iron Law: "Thin Client, Fat Server", pattern-guide.md com Server/Client decision tree + anti-pattern migration table
- **Fase 6 completa:** SDD (Spec Driven Development) — 164 linhas, pipeline 4 fases com /clear entre cada, prd.md → spec.md → implement → review via Trident
- **Fase 7 completa:** Context Tree — 175 linhas, scoring ByteRover (importance 0-100, maturity tiers, decay 21d), scoring-guide.md com critérios detalhados + index/manifest formats
- **Todas as 7 fases do roadmap completas.** 24 skills no repo (18 originais + 6 novas)
- Todas as 5 novas skills passam no validate.py (frontmatter, <250 linhas, Iron Law, checklist, gates, anti-patterns)

### 2026-04-03 — Sessão 4 (Quality Audit + Maestro)
- **Avaliação honesta:** Score inicial 70% — gaps: sdd/references vazio, integrações unidirecionais, ~15 insights de vídeos não incorporados
- **Maestro criada:** Skill orquestradora (168L) — routing de intent para skills, composition chains, context window budget. References: skill-catalog.md (mapa completo das 25 skills) + composition-chains.md (9 chains validadas)
- **SDD references preenchidas:** 3 arquivos criados — spec-writing-guide.md (formato path→action, técnica .tmp), prd-example.md (exemplo completo com anatomia), research-checklist.md (investigation checklist + layered agents + over-engineering check)
- **Integrações bidirecionais:** reference-finder ↔ context-tree, sdd ↔ context-tree, trident ↔ sdd. Cada skill agora menciona as outras explicitamente.
- **Feedback loop:** Adicionado na writing-guide.md do skill-builder — seção sobre retroalimentação (Video 3)
- **Micro-interactions playbook:** Adicionado no design-json-schema.md — hover states, animations, anti-generic-AI design (Video 5)
- **Trident:** Seção Integration adicionada (era o único skill v2 sem)
- **Todas 25 skills passam validate.py.** Repo: 25 skills (18 originais + 7 novas)

### 2026-04-03 — Sessão 5 (Deep Analysis + CLAUDE.md)
- **CLAUDE.md criado** em `D:/DOCUMENTOS/Github/CLAUDE.md` com system prompt completo do Patrick
- **Análise profunda dos 5 vídeos:** Reprocessamento completo das transcrições (5960 linhas), 5 agentes em paralelo
  - `research/video-deep-analysis/01-omer-geo-skills.md` — GEO, CLI vs MCP, distribuição via skills.sh
  - `research/video-deep-analysis/02-vibe-coding-workflow.md` — /spec→/break→/plan→/execute, agentes por camada
  - `research/video-deep-analysis/03-skills-vs-agentes.md` — progressive loading, retroalimentação, composição
  - `research/video-deep-analysis/04-anti-vibe-coding.md` — SDD (Research→Spec→Implement), regra 40-50%, técnica .tmp
  - `research/video-deep-analysis/05-design-skill.md` — skill de design, assets, micro-interactions, antes/depois
- **CONSOLIDADO.md criado** com: processos por categoria (4 categorias), 35 skills propostas sem duplicatas, referências unificadas, conexões com as 25 skills existentes, top 5 próximos passos
- **Memórias salvas:** perfil completo do Patrick, feedback "sempre PT-BR"
