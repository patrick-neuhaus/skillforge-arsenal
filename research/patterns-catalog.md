# Catálogo de Padrões para Skills

Padrões extraídos de todas as fontes pesquisadas. Use como referência ao criar/melhorar skills.

## Fontes
- 5 vídeos (Deborah Folloni / DevGPT)
- Skill Forge (sanyuan0704) — 12 técnicas
- HumanLayer — workflow commands
- Trident — pipeline multi-agent
- ByteRover — Context Tree
- skills.sh (Vercel) — ecossistema

---

## 1. Criação de Skills

### 1.1 Progressive Loading
SKILL.md deve ter <250 linhas. Conteúdo pesado vai pra `references/` e é carregado sob demanda.
**Fonte:** Skill Forge (técnica 1), Video 3

### 1.2 Keyword Bombing (GEO)
Otimizar `description` pra agentes acharem a skill, não humanos. Usar o próprio Claude pra gerar keywords.
**Fonte:** Video 1 (Omer), Skill Forge (técnica 2)

### 1.3 Workflow Checklist
Passos numerados e trackáveis com indicators de warning/failure.
**Fonte:** Skill Forge (técnica 3)

### 1.4 Script Encapsulation
Operações determinísticas em scripts Python/Bash (menos tokens, mais consistência).
**Fonte:** Skill Forge (técnica 4), Video 3

### 1.5 Question-Style Instructions
Perguntas concretas > comandos abstratos. "O arquivo tem mais de 500 linhas?" > "Verifique o tamanho".
**Fonte:** Skill Forge (técnica 5)

### 1.6 Confirmation Gates
Aprovar antes de ações irreversíveis/críticas.
**Fonte:** Skill Forge (técnica 6), Video 1 (Permission Gate Pattern)

### 1.7 Pre-Delivery Checklist
QA checklist antes de entregar output final.
**Fonte:** Skill Forge (técnica 7)

### 1.8 Parameter System
Flags e variantes: `--quick`, `--full`, `--evolve`.
**Fonte:** Skill Forge (técnica 8)

### 1.9 Reference Organization
Refs por domínio, carregamento seletivo. Nunca carregar tudo de uma vez.
**Fonte:** Skill Forge (técnica 9), ByteRover

### 1.10 CLI + Skill Pattern
CLI tools > MCP Servers. CLIs preservam context window, MCPs bloatam.
**Fonte:** Skill Forge (técnica 10), Video 1

### 1.11 Iron Law
Uma regra inquebrável que impede atalhos do modelo.
**Fonte:** Skill Forge (técnica 11)

### 1.12 Anti-Pattern Documentation
Listar explicitamente o que NÃO fazer, em vez de depender de restrições implícitas.
**Fonte:** Skill Forge (técnica 12)

---

## 2. Distribuição de Skills

### 2.1 GEO (Generative Engine Optimization)
- Otimizar pra find-skills da Vercel (ler código open source pra entender ranking)
- Agentes são os clientes, não humanos
- Usar Claude pra gerar keywords de busca
- Skills específicas > genéricas (buscas previsíveis)
**Fonte:** Video 1

### 2.2 Publicar no skills.sh
Early adopter advantage. CLI: `npx skills add`.
**Fonte:** Video 1, skills.sh docs

---

## 3. Workflows de Desenvolvimento

### 3.1 SDD (Spec Driven Development)
Research → Spec → Implement, com `/clear` entre cada.
- Research: pesquisa codebase + docs → gera prd.md
- Spec: lê prd.md → gera spec.md com paths + ações
- Implement: lê spec.md → executa
**Fonte:** Video 4

### 3.2 4 Etapas Epic
`/spec` → `/break` → `/plan` → `/execute`
- Spec: páginas + componentes + behaviors
- Break: issues atômicas (1 por behavior)
- Plan: research codebase + docs externos + enriquecer issue
- Execute: agentes especializados por camada
**Fonte:** Video 2

### 3.3 Anti-Vibecoding Rules
- Regra dos 40-50%: nunca usar mais que metade da context window
- Especificar arquivos explicitamente (path + ação)
- Pesquisar antes de implementar SEMPRE
- Técnica .tmp: clonar repo de referência, analisar, deletar
- Protótipo primeiro, lógica depois
- Thin Client / Fat Server
**Fonte:** Videos 2, 4

---

## 4. Arquitetura de Skills

### 4.1 Composable Tools
Ferramentas pequenas e modulares que o agente encadeia.
**Fonte:** Video 1

### 4.2 Autodiscovery
Skill permite que agente descubra capacidades dinamicamente.
**Fonte:** Video 1

### 4.3 Retroalimentação
"Registra isso na skill pra próxima vez" = melhoria contínua sem deploy.
**Fonte:** Video 3

### 4.4 Determinístico + Não-determinístico
Scripts (consistência) + IA (criatividade) = combinação poderosa.
**Fonte:** Video 3

### 4.5 Pipeline Multi-Agent
Scan → Verify → Judge com shared output contract e bounded recall.
**Fonte:** Trident, HumanLayer

### 4.6 Roteiro de Perguntas
Coleta estruturada de informações antes de executar qualquer ação.
**Fonte:** Video 3

---

## 5. Memória e Contexto

### 5.1 Context Tree (ByteRover)
Hierarquia: Domínios → Tópicos → Subtópicos em markdown.
Scoring: importance (0-100), recency (decay 21d), maturity tiers.
Archive: stubs searchable + full backups.
**Fonte:** ByteRover docs

### 5.2 Handoff via Arquivos .md
prd.md e spec.md como memória entre conversas após `/clear`.
**Fonte:** Video 4

### 5.3 Pasta /references como Guardrail
architecture.md + design-system.md em todo projeto.
**Fonte:** Videos 2, 4
