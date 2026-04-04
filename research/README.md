# Research — Fontes e Processo de Pesquisa

Este diretório contém toda a pesquisa que fundamentou o skillforge-arsenal. Cada skill do arsenal foi construída com base nessas fontes, não inventada do zero.

---

## Fontes Primárias

### 5 Vídeos — Deborah Folloni / DevGPT (Canal YouTube)

Análises completas de 5 vídeos sobre skills, agentes e workflows para Claude Code. Total: ~6000 linhas de transcrição processadas.

| # | Vídeo | Tema Central | Arquivo de Análise |
|---|-------|-------------|-------------------|
| 1 | Omer — Skill mais baixada (1M+ installs) | GEO, CLI vs MCP, distribuição via skills.sh | `video-transcripts/01-skill-mais-baixada-omer.md` |
| 2 | Vibe Coding Não Funciona — Epic Builder | /spec→/break→/plan→/execute, agentes por camada | `video-transcripts/02-vibe-coding-nao-funciona.md` |
| 3 | Skills > Agentes | Progressive loading, retroalimentação, composição | `video-transcripts/03-skills-vs-agentes.md` |
| 4 | SDD — Workflow Anti-Vibe Coding | Research→Spec→Implement, regra 40-50%, técnica .tmp | `video-transcripts/04-workflow-anti-vibe-coding.md` |
| 5 | Frontend Design Skill | Skill de design + assets + micro-interactions | `video-transcripts/05-frontend-design-skill.md` |

**Deep Analysis (reprocessamento com 5 agentes em paralelo):**

| Arquivo | Foco |
|---------|------|
| `video-deep-analysis/01-omer-geo-skills.md` | GEO, CLI-first, autodiscovery, composição emergente |
| `video-deep-analysis/02-vibe-coding-workflow.md` | 5 problemas do vibe coding, workflow 4 etapas, thin client |
| `video-deep-analysis/03-skills-vs-agentes.md` | Progressive loading, retroalimentação, determinismo + IA |
| `video-deep-analysis/04-anti-vibe-coding.md` | SDD pipeline, regra 40-50%, técnica .tmp, compressão progressiva |
| `video-deep-analysis/05-design-skill.md` | Skill + identidade visual, mini identity, antes/depois |
| `video-deep-analysis/CONSOLIDADO.md` | **Síntese final: 4 processos, 35 skills propostas, referências, conexões** |

### Repos de Referência (community/)

| Repo | Autor | O que extraímos | Localização |
|------|-------|----------------|-------------|
| **Skill Forge** | sanyuan0704 | 12 técnicas battle-tested para criação de skills | `community/sanyuan-skills/` |
| **HumanLayer Commands** | HumanLayer | 29 commands anti-vibecoding (research, plan, implement) | `community/humanlayer-commands/` |

### Análises Individuais

| Arquivo | Fonte | O que contém |
|---------|-------|-------------|
| `byterover-context-tree.md` | ByteRover (GitHub) | Sistema de memória hierárquica: scoring, decay, archive, manifest |
| `patterns-catalog.md` | Todas as fontes | 23 padrões catalogados prontos pra uso |
| `pluma-prompts/claude-prompt-01.txt` | Pluma (app real) | Prompt de geração de design.json |
| `pluma-prompts/replit-prompt-02.txt` | Pluma (app real) | Prompt completo com design system + brief por seção |

---

## Ecossistema Pesquisado

| Plataforma | O que é | Insights extraídos |
|-----------|---------|-------------------|
| **skills.sh** (Vercel) | Diretório de 91K+ skills pra Claude Code | Formato YAML frontmatter, CLI `npx skills`, ranking Find Skills |
| **inference.sh** (Omer) | 150+ ferramentas de IA via CLI | Modelo CLI-first, composição emergente, autodiscovery |
| **epic.new** | Skills + agentes + prompts pra Claude Code | Workflow /spec→/break→/plan→/execute |

---

## Como a Pesquisa Virou Skills

### Fluxo de Pesquisa → Implementação

```
Vídeos (6000 linhas de transcrição)
    ↓ 5 agentes em paralelo
Deep Analysis (5 análises + CONSOLIDADO)
    ↓ cruzamento com repos de referência
Patterns Catalog (23 padrões)
    ↓ priorização (alta/média/baixa)
35 Skills Propostas
    ↓ decisão: criar / absorver / adiar
6 Criadas + 15 Absorvidas + 14 Adiadas
    ↓ skill-builder --full + validate.py
30 Skills Operacionais (v3)
```

### Mapeamento Fonte → Skill

| Fonte | Skills que fundamentou |
|-------|----------------------|
| Video 1 (Omer/GEO) | geo-optimizer, cli-skill-wrapper, skill-builder (GEO module) |
| Video 2 (Epic Builder) | sdd, architecture-guard, code-dedup-scanner |
| Video 3 (Skills vs Agentes) | context-tree, maestro, skill-builder (retroalimentação) |
| Video 4 (SDD/Anti-Vibe) | sdd, pattern-importer, context-guardian |
| Video 5 (Design Skill) | ui-design-system (--identity), component-architect, react-patterns |
| Skill Forge (12 técnicas) | skill-builder (todas as 12 técnicas incorporadas) |
| HumanLayer (29 commands) | sdd (research/plan/implement pattern) |
| ByteRover | context-tree (scoring, decay, hierarchy) |
| Pluma Prompts | ui-design-system (design.json schema) |

---

## Cronologia

| Data | O que aconteceu |
|------|----------------|
| 2026-04-03 Sessão 1 | Repo criado, 18 skills pessoais migradas, 5 vídeos processados |
| 2026-04-03 Sessão 2 | Fases 1-4: skill-builder v2, prompt-engineer v2, reference-finder v3, trident |
| 2026-04-03 Sessão 3 | Fases 5-7: 3 skills frontend, SDD, context-tree |
| 2026-04-03 Sessão 4 | Quality Audit + maestro criado |
| 2026-04-03 Sessão 5 | Deep Analysis dos 5 vídeos + CONSOLIDADO |
| 2026-04-03 Sessão 6 | Arsenal v2: 6 novas skills, 10 atualizadas, repo-review deletado |
| 2026-04-03 Sessão 7 | Arsenal v3: 14 skills legadas refatoradas, 30/30 PASS |
