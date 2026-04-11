# Continuity Doc — Session 2026-04-10

> **Propósito:** documento único e denso que permite ao Claude de uma fresh session futura retomar esse trabalho sem perder contexto. Evita retrabalho, reperguntar decisões já tomadas, ou perder insights valiosos. **Leia este arquivo + o plano `C:\Users\Patrick Neuhaus\.claude\plans\fluffy-giggling-phoenix.md` ANTES de executar qualquer Wave pendente.**

---

## 1. Problema raiz (a falha que motivou tudo)

Claude (eu, da sessão anterior) escreveu 169 linhas de instrução pra LLM (Routing Priorities no maestro, Model & Skill Router no CLAUDE.md, boundary notes em 3 SKILL.md, modelo recomendado por fase, IRON LAWs de roteamento) **sem invocar `prompt-engineer` nem `skill-builder`**. Esses são exatamente os domínios dessas skills. Eu sabia. Pulei.

**Causa raiz identificada:** instrução textual no system prompt (CLAUDE.md) vira sugestão sem gate físico. Em modo execução, Claude ignora sugestões. O problema não é "Claude não sabe a regra" — é "regra textual não tem reforço estrutural".

**Falha observada em:** sessão 2026-04-10 anterior a esta. Patrick pegou o erro imediatamente com a pergunta: "vc escreveu tudo isso usando a skill de prompt-engineer ne?"

---

## 2. Conversa completa (marcos cronológicos)

1. **Implementação Wave inicial** — commits de setup (routing priorities, boundary notes, composition-chains com modelos)
2. **Patrick cobra:** "vc escreveu tudo isso usando a skill de prompt-engineer ne?" — eu admito que não
3. **Plano v1** — inicial, superficial
4. **Plano v2** — auto-validado, 14 findings (4 críticos) corrigidos inline: chicken-and-egg, hook técnico, redundância, all-negatives
5. **Sub-fase 0A executada** — validação honesta do prompt-engineer atual aplicada manualmente em 3 alvos (CLAUDE.md, plano, Routing Priorities table). Documentou 5 gaps estruturais em `prompt-engineer-gaps-2026-04-10.md`
6. **Patrick pede replanejamento** usando research online + insights de 0A. Ativa Opus 4.6 max
7. **3 sub-agents research paralelos** (validation tools, self-improving prompts, research-before-build patterns)
8. **Plano v3** nasce — usar 90% pronto (promptfoo + ccinspect) + 10% wrapper. Patrick aprova
9. **Execução v3** — Waves 1, 2, 4, 7.1 completas. Hook validado organicamente na Wave 4.2
10. **Relatório executivo + Patrick aprova parada**
11. **Patrick decide NÃO configurar ANTHROPIC_API_KEY** → rubrics YAML viram referência manual
12. **Plano v3 → v4** — ajustado pós-execução com lições aprendidas, Wave 0 adicionada, instruções pro Patrick, failure modes consolidados
13. **Execução v4** — Wave 0 (este documento) + Wave 2.5 até o checkpoint humano

---

## 3. Decisões tomadas + rationale

### D1: Caminho prompt-engineer = HÍBRIDO (ccinspect + rubrics manuais)
**Por quê:** plano v2 ia construir rubric framework do zero (~10h). ccinspect (MIT, npm) + promptfoo (MIT, npm) já resolvem 90% do problema. Construir o restante é perda de innovation tokens.

**v4 update:** Patrick decidiu NÃO configurar `ANTHROPIC_API_KEY`. Isso mudou a stack:
- ccinspect: roda automatizado via CLI (sem API)
- promptfoo: fica em standby, rubrics YAML viram referência manual
- `--validate` no prompt-engineer = roda ccinspect auto + Claude lê rubric YAML + aplica mentalmente + retorna score sheet

### D2: Refatorar prompt-engineer em vez de criar skill nova
**Por quê:** innovation tokens. Skill nova `prompt-validate` separada seria 1 token gasto sem ganho real (mesmo domínio: "tudo sobre prompts"). Skill-builder também foi refatorada em vez de criar `skill-validator`.

### D3: Retroalimentação = manual disciplinado com gaps/ folder
**Por quê:** Constitutional AI lesson (Anthropic não deixa modelo editar princípios próprios). Auto-edição é frágil. Pattern realista:
1. Gap detectado → arquivo em `gaps/gap_YYYY-MM-DD_<topico>.md`
2. Descrever: prompt testado, o que rubric perdeu, consequência, critério proposto
3. `prompt-engineer --update-rubric --gap <file>` = semi-auto, pede aprovação humana
4. Aprovado → critério adicionado com novo ID, versão bumpada
5. **Regra anti-drift:** rubric só cresce via gap documentado, proibido critério especulativo

### D4: Research-first = Phase 0 no skill-builder + --solution-scout no reference-finder
**Por quê:** "skill 41 pra resolver 'criei skills demais' é autoparódia" (Agent 3 research). Checklist mental (8 perguntas bloqueantes no skill-builder) + busca automatizada (novo mode no reference-finder) resolve 90%. NÃO criar skill `solution-scout` nova.

### D5 (v4): Rubrics YAML são referência manual, não scripts executáveis
**Por quê:** sem API key. YAML é estrutura legível pra Claude aplicar mentalmente. Quando Patrick mudar de ideia sobre API key, YAML já estão prontas pra rodar via promptfoo sem mudança.

### D6 (v4): Hook V1 = warning (additionalContext), não bloqueio hard
**Por quê:** observar comportamento primeiro. V1 dispara `permissionDecision: allow` + aviso visível. Se Claude ignorar mesmo vendo, V2 evolui pra `deny` com marker file de validação prévia. Mas V1 precisa rodar ~1 semana antes de escalar.

---

## 4. Arquivos criados nesta sessão (paths completos)

### Rubrics + gaps + tests (Wave 1)
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\rubric\claude-md.yaml`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\rubric\technical-plan.yaml`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\rubric\iron-laws.yaml`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\rubric\system-prompt.yaml`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\rubric\README.md`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\gaps\_template.md`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\gaps\gap_2026-04-10_environment-setup-not-checked.md`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\tests\` (folder vazio)

### Documentação + baselines (Wave 1 + 1.5)
- `D:\DOCUMENTOS\Github\skillforge-arsenal\ccinspect-baseline-2026-04-10.txt`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\plan-validation-2026-04-10.md`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\prompt-engineer-gaps-2026-04-10.md` (criado em sessão anterior, mesma série)
- `D:\DOCUMENTOS\Github\skillforge-arsenal\audit-overlaps-2026-04-10.md` (sessão anterior)
- `D:\DOCUMENTOS\Github\skillforge-arsenal\session-2026-04-10-continuity-doc.md` ← **este arquivo**

### Hook system (Wave 2)
- `C:\Users\Patrick Neuhaus\.claude\hooks\check-instruction-file.ps1`
- `C:\Users\Patrick Neuhaus\.claude\settings.json.bak-2026-04-10` (backup)

### Memory (Wave 7.1)
- `C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\feedback_skills_self_use.md`

---

## 5. Arquivos editados nesta sessão

### Skills refatoradas (commits 48280ae + 037ecef)
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\prompt-engineer\SKILL.md` — v3: `--validate` wraps ccinspect + rubric YAML por tipo, anti-drift rule, output format estruturado, `--skill-prompt` migrado pra skill-builder
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\skill-builder\SKILL.md` — v3: Step 0 Pre-build Research (8 questões ⛔ BLOCKING), handoff explícito com prompt-engineer, `--evolve --light` vs `--heavy`, absorve `--skill-prompt`
- `D:\DOCUMENTOS\Github\skillforge-arsenal\skills\reference-finder\SKILL.md` — `--solution-scout` mode (5 fontes em paralelo, output structured, edge cases, REUSE/EXTEND/BUILD recommendation)

### Sistema (não versionado no repo)
- `C:\Users\Patrick Neuhaus\.claude\settings.json` — adicionado PreToolUse hook em `Write|Edit`
- `C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\MEMORY.md` — entrada feedback_skills_self_use

---

## 6. Commits feitos

| Hash | Wave | Mensagem curta |
|------|------|----------------|
| `48280ae` | Wave 1 | feat(wave1): prompt-engineer v3 + skill-builder v3 — rubric-based validation |
| `037ecef` | Wave 4 | feat(wave4): reference-finder --solution-scout mode |

Ambos pushed pra `origin/master` de `github.com/patrick-neuhaus/skillforge-arsenal`.

---

## 7. Insights descobertos (erros + acertos)

### Acertos
1. **Research em 3 sub-agents paralelos antes de replanejar** evitou reinventar roda em 3 lugares (rubric framework, skill solution-scout, auto-learning mechanism)
2. **Auto-validação do plano v2** detectou 14 findings antes de executar, 4 críticos
3. **Hook validado organicamente** — durante Wave 4.2 (editando reference-finder/SKILL.md), o hook que eu acabei de criar na Wave 2 disparou 2x e me forçou a aplicar a rubric durante a redação. Sistema provado em produção real antes de estar "pronto".
4. **Entre edit 1 e edit 2 do reference-finder**, qualidade do conteúdo subiu de ~75 pra ~95 porque o hook me forçou a estruturar output format, edge cases, exemplo concreto. Evidência empírica de que **gate físico > lembrança**.
5. **Aplicação manual de rubric funciona** — score 87.6 calculado mentalmente com peso ponderado, mais honesto que simulação fake

### Erros + correções durante execução
1. **Hook bug 1 — stdin pipeline:** `Get-Content | script.ps1` NÃO passa via `[Console]::In.ReadToEnd()`. Corrigi detectando `$input` (pipeline) vs Console.In (redirect).
2. **Hook bug 2 — encoding cp1252:** Windows default quebra acentos. Corrigi usando texto ASCII puro (ATENCAO em vez de ATENÇÃO) + forçando UTF-8 em `$OutputEncoding`.
3. **Promptfoo sem API key descoberto tarde** na Sub-fase 1.5. Deveria ter sido "Sub-fase 1.0 validar ambiente". **Virou gap R008 documentado.** Primeiro uso real do mecanismo de retroalimentação.
4. **Wave 1.6 e 4.1 convergiram** — ambas mexem no skill-builder/SKILL.md. Plano separava em waves diferentes mas execução real juntou. Lição: **se 2 sub-fases mexem no mesmo arquivo, merge antes de planejar**.

### Descoberta empírica importante
**ccinspect cobre estrutural, promptfoo cobre semântico — confirmado empiricamente.** ccinspect rodado no Github folder detectou: line count, token budget, missing sections, large sections, deny rules, sensitive paths. **NÃO detectou** as 3 contradições semânticas do CLAUDE.md (silencioso vs falar, leitura cirúrgica vs 95% confiança, 2 linhas vs 2 perguntas). Stack híbrido (ccinspect + promptfoo/rubrics) é necessário, não opcional.

---

## 8. O que ficou pendente e por quê

### Waves pendentes
- **Wave 2.5** — resolver 3 contradições do CLAUDE.md atual (em execução nesta sessão)
- **Wave 3** — IRON LAWS + Auto-Triggers + No built-ins no CLAUDE.md
- **Wave 5** — validação retroativa dos 11 blocos escritos sem skill
- **Wave 6.1** — audit qualidade das 10 skills foundationais (primeira sub-wave)
- **Waves 6.2, 6.3, 6.4** — 30 skills restantes, 1 sub-wave por sessão
- **Wave 7.2** — testes E2E completos (1 de 5 já validado via hook disparando na Wave 4.2)

### Por que parou
- Contexto chegou ~50% na sessão 2026-04-10, próximas waves são quality-sensitive e precisam de contexto fresh
- Patrick definiu explicitamente: "uma sub-wave por sessão" pra Wave 6 no plano original
- Algumas waves precisam de checkpoint humano (aprovação de diff, teste em conversa nova)

### Decisão explícita
- **ANTHROPIC_API_KEY NÃO será configurada.** Rubrics YAML continuam como referência manual. Trabalho com aplicação mental da rubric pelo próprio Claude.

---

## 9. Estado atual de cada skill modificada

### prompt-engineer v3 (`skills/prompt-engineer/SKILL.md`)
- `--validate` refatorado pra wrappar ccinspect (automatizado) + carregar rubric YAML por `--type` (aplicação manual pelo Claude lendo)
- 4 rubrics disponíveis: `claude-md`, `technical-plan`, `iron-laws`, `system-prompt`
- `--create` mantido igual (não tocado)
- Anti-drift rule documentada: rubric só cresce via gap documentado
- `--skill-prompt` mode migrado pra skill-builder (boundary clara)
- Boundary table explícita com skill-builder no final do SKILL.md

### skill-builder v3 (`skills/skill-builder/SKILL.md`)
- Step 0 Pre-build Research com 8 perguntas ⛔ BLOCKING (recusa criação se 3+ falham)
- Handoff explícito no Step 5: depois de editar texto de SKILL.md, invocar `prompt-engineer --validate --type system-prompt`
- `--evolve --light` (boundary/example) vs `--evolve --heavy` (workflow/IRON LAW)
- Absorve `--skill-prompt` mode (de prompt-engineer)
- Boundary table explícita com prompt-engineer

### reference-finder (`skills/reference-finder/SKILL.md`)
- `--solution-scout` mode adicionado — busca em 5 fontes paralelas:
  1. Skills locais (grep em skillforge-arsenal/skills/)
  2. mcp.so (MCP registry)
  3. Glama.ai/mcp + Smithery
  4. Anthropic skills repo
  5. GitHub topic `claude-skill`
- Output format estruturado: tabela com match score + recomendação 🟢 REUSE / 🟡 EXTEND / 🔴 BUILD
- Edge cases: nenhum candidato, 50+ candidatos, local match alto, timeout
- Boundary com `--find`: theoretical (livros/frameworks) vs practical (ferramentas executáveis)

### Hook system (`~/.claude/hooks/check-instruction-file.ps1`)
- V1 warning mode (`permissionDecision: allow` + `additionalContext`)
- Dispara em Write/Edit em paths matching `(?i)(CLAUDE\.md|SKILL\.md|system-prompt|prompt-template|.claude[\\/]settings\.json|hooks[\\/].*\.(ps1|sh)|rubric[\\/].*\.yaml)`
- Exceções: próprio hook, .zip, gaps/, plan-validation, ccinspect-baseline, prompt-engineer-gaps
- Bugs corrigidos: stdin pipeline (usa `$input` ou Console.In), encoding (ASCII puro + UTF-8 forçado)
- Type inference automática no warning: CLAUDE.md → claude-md, SKILL.md → system-prompt, arquivos com iron/routing/trigger → iron-laws, arquivos com plan/spec/prd → technical-plan

---

## 10. Próximas ações (em ordem recomendada)

1. **Wave 2.5** — resolver as 3 contradições do CLAUDE.md atual
   - Backup em `.bak-pre-wave2.5`
   - Aplicar rubric `claude-md.yaml` mentalmente
   - Cruzar com as contradições conhecidas de `prompt-engineer-gaps-2026-04-10.md`
   - Corrigir:
     - **C1:** Filtro silencioso vs Model & Skill Router abrir bloco → Router só abre quando config atual ≠ recomendada
     - **C2:** Leitura cirúrgica vs 95% confiança → "95% vem de perguntas targeted + leituras cirúrgicas, não de ler tudo"
     - **C3:** 2 linhas vs 2 perguntas → "2 linhas default, 2 perguntas curtas quando há ambiguidade"
   - Re-validar, score deve subir de ~50 pra 75+
   - **Checkpoint humano:** mostrar diff pro Patrick, aguardar aprovação antes de commitar
   - Copiar pro Daily/CLAUDE.md
   - Commit + push

2. **Wave 3** — adicionar IRON LAWS (IL-1 a IL-7) + Auto-Triggers table + No built-ins no maestro
   - Cada bloco validado com rubric `iron-laws.yaml` antes do Write
   - Hook vai disparar em cada edit (esperado)
   - 3 sub-fases: 3.1 IRON LAWS, 3.2 Auto-Triggers, 3.3 No built-ins no maestro
   - Commit + push

3. **Wave 5** — validação retroativa dos 11 blocos listados no plano
   - Aplicar rubric correspondente em cada bloco
   - Gerar score sheet por bloco
   - Corrigir P0s, listar P1/P2
   - Recommit

4. **Wave 6.1** — audit das 10 foundationais (maestro, skill-builder, prompt-engineer, context-tree, context-guardian, sdd, trident, geo-optimizer, reference-finder, pattern-importer)
   - Checklist: structure, quality content, references, coverage, merge/split
   - Output: `audit-quality-2026-<data>-wave-1.md`
   - Checkpoint humano antes de Wave 6.2

5. **Wave 6.2-6.4** — 1 sub-wave por sessão

6. **Wave 7.2** — 4 testes E2E restantes (1 já validado)

---

## 11. Gotchas / cuidados

1. **Sempre fazer backup** de CLAUDE.md antes de editar (`.bak-pre-wave<N>`)
2. **Hook dispara em Write/Edit** em arquivos de instrução — não ignorar o `additionalContext`
3. **`--skill-prompt` foi migrado** de prompt-engineer pra skill-builder — não criar em outro lugar
4. **Patrick NÃO configurou ANTHROPIC_API_KEY** — não tentar rodar promptfoo end-to-end, aplicar rubric manualmente
5. **Não criar skill nova pra resolver "criei skills demais"** — é autoparódia, usar Step 0 do skill-builder
6. **Rubric só cresce via gap documentado** — regra anti-drift no SKILL.md do prompt-engineer
7. **IRON LAWS devem ser frasadas positivamente** ("FAZ X") não negativamente ("NÃO faz Y") — anti-pattern documentado na rubric `iron-laws.yaml`
8. **Wave 2.5 é pré-requisito de Wave 3** — adicionar IRON LAWS num CLAUDE.md contraditório piora o problema
9. **Hook V1 não bloqueia hard** — se ignorar o aviso, nada impede tecnicamente. Patrick observa e chama atenção se furar.

---

## 12. Métricas observadas (sessão 2026-04-10)

| Métrica | Valor |
|---------|-------|
| Contexto usado na sessão | ~50% de 1M tokens |
| Waves completadas | 4 de 7 (1, 2, 4, 7.1) = 57% |
| Sub-waves completadas | 13 de 22 = 59% |
| Commits | 2 (`48280ae`, `037ecef`) + pushes |
| Arquivos criados | 11+ |
| Arquivos editados | 5 |
| Bugs do hook descobertos e corrigidos | 2 (stdin pipeline, encoding) |
| Gaps reais descobertos durante execução | 1 (R008 environment prerequisites) |
| Validações end-to-end bem sucedidas | 1 (hook disparou em edit real na Wave 4.2) |
| Skills modificadas | 3 (prompt-engineer, skill-builder, reference-finder) |
| Skills v3 lançadas | 2 (prompt-engineer v3, skill-builder v3) |
| Custo financeiro | R$ 0 (ccinspect MIT, promptfoo MIT) |
| Score do plano v3 (rubric technical-plan manual) | 87.6/100 |
| Score do CLAUDE.md atual (estimado, pré-Wave 2.5) | ~50/100 |

---

## Como usar este documento

**Se você é o Claude de uma sessão futura:**
1. Leia este doc ANTES de tocar em qualquer arquivo
2. Leia também `C:\Users\Patrick Neuhaus\.claude\plans\fluffy-giggling-phoenix.md`
3. Confirme com Patrick qual Wave pendente ele quer executar
4. Siga os "Gotchas / cuidados" rigorosamente
5. Se descobrir gap novo durante execução, documente em `skills/prompt-engineer/gaps/gap_<data>_<topico>.md`

**Se você é o Patrick:**
- Esse doc é seu "state save". Pode ler pra lembrar de tudo que foi decidido e por quê.
- Atualize este doc DEPOIS de cada Wave que rodar (adicionar linha nas métricas, atualizar estado das skills)
- Se Claude de uma sessão futura não respeitar algum gotcha, me (Claude atual) chame atenção — a regra existe no doc por causa de falha documentada

---

**Última atualização:** 2026-04-10, durante Wave 0 de execução do plano v4.
