# HOW TO USE — sistema fluffy-giggling-phoenix

> **Propósito:** guia prático de como rodar no dia a dia o sistema construído na sessão 2026-04-10/11. Se é a primeira vez lendo, começa aqui — não precisa ler os audits ou o SESSION-NARRATIVE pra usar.
>
> **Pra quem é:** Patrick (usuário) e Claude de sessões futuras (que precisam entender como o sistema já construído funciona antes de modificar).

---

## O que tu tem agora (em 1 parágrafo)

40 skills auditadas e refatoradas no skillforge-arsenal. Hook PS1 que avisa quando vai editar arquivo de instrução (CLAUDE.md, SKILL.md, etc.). `.claude/rules/` user-level com iron-laws, skill-routing, token-hygiene e model-skill-router carregados em qualquer projeto. Prompt-engineer com rubrics YAML pra validar 4 tipos de arquivo (claude-md, technical-plan, iron-laws, system-prompt). Skill-builder com Step 0 (8 perguntas bloqueantes) pra evitar criar skill nova quando já existe solução pronta. Logging do hook alimentando decisão futura sobre bloqueio hard.

---

## Uso no dia a dia — 5 cenários

### 1. Criar uma skill nova

```
Patrick: "cria uma skill pra [X]"
```

**O que vai acontecer automaticamente:**
1. Claude carrega skill-builder
2. skill-builder roda Step 0 (8 perguntas bloqueantes):
   - Qual a dor concreta?
   - Quantas vezes em 30 dias?
   - Já procurou em skills locais / Anthropic repo / mcp.so / GitHub / awesome-claude-code?
   - Se existe algo parecido, por que não serve?
   - É core ou commodity?
   - Quantos innovation tokens custa?
   - Dá pra resolver com spike de 2h?
   - Qual o critério pra DELETAR depois?
3. Se 3+ perguntas falharem → skill-builder RECUSA criação e recomenda spike com `reference-finder --solution-scout <topic>` primeiro
4. Se passar → prossegue com Step 1 (Understand) até Step 7 (Validate)
5. Step 5 faz handoff explícito pra prompt-engineer validar o texto do SKILL.md
6. Step 7 valida estrutura (line count <250, frontmatter, references organizadas)

**Tu não precisa lembrar nada disso.** A skill-builder atualizada faz tudo automaticamente.

**Quando isso pode dar ruim:** se Step 0 recusar criação e tu achar que está errado. Nesse caso, rode `reference-finder --solution-scout <topic>` manualmente e **mostre o resultado** pro Claude antes de insistir. Se mesmo assim nada bater, tu tem contexto pra justificar por que Step 0 errou.

---

### 2. Editar um CLAUDE.md, SKILL.md, ou arquivo de instrução

**Ação tua:** só pede a edição normalmente.

```
Patrick: "atualiza o CLAUDE.md pra adicionar Y"
```

**O que vai acontecer:**
1. Claude vai começar a editar
2. **Hook dispara** — mensagem ATENCAO aparece no contexto do Claude:
   ```
   ATENCAO -- arquivo de instrucao: <path>
   Antes de prosseguir com Write/Edit, confirme:
   [ ] prompt-engineer --validate --type <tipo inferido> rodado no novo conteudo?
   [ ] Se SKILL.md core: skill-builder --validate rodado tambem?
   [ ] ccinspect lint rodado pra detectar contradicoes estruturais?
   ```
3. Claude deve parar, aplicar a rubric correspondente (`~/.claude/skills/prompt-engineer/rubric/<tipo>.yaml`), rodar ccinspect, e só então editar.
4. Se Claude ignorar o aviso e editar direto, tu pega e confronta.

**O hook loga cada dispatch em** `~/.claude/logs/hook-dispatches.jsonl`. Se ver que Claude tá ignorando sistematicamente, é sinal pra escalar V1→V2 (bloqueio hard). Em 7 dias dá pra rodar:

```powershell
$e = Get-Content ~/.claude/logs/hook-dispatches.jsonl | ForEach-Object { $_ | ConvertFrom-Json }
$e | Group-Object outcome | Select-Object Count, Name
$e | Where-Object { $_.outcome -eq "warned" } | Group-Object file | Sort-Object Count -Descending | Select-Object Count, Name
```

Detalhes em `C:\Users\Patrick Neuhaus\.claude\logs\README.md`.

---

### 3. Validar um prompt ou arquivo de instrução existente

```
Patrick: "valida esse CLAUDE.md" (ou plan, ou iron-laws, ou system-prompt)
```

**O que vai acontecer:**
1. Claude carrega prompt-engineer
2. `--validate` detecta o tipo automaticamente (ou tu passa `--type <claude-md|technical-plan|iron-laws|system-prompt>`)
3. Roda ccinspect (estrutural) + aplica rubric YAML (semântico) mentalmente
4. Output estruturado:
   ```
   ## Validation: <file>
   Type: <tipo>
   Score: X/100 [tier]
   Threshold: 75 (production)
   
   ### ccinspect (structural)
   - errors/warnings/notes
   
   ### promptfoo (semantic, by criterion)
   | R001 | ... | score | tier |
   
   ### Findings P0 / P1 / P2
   ### Recommendation: APPROVED | APPROVED WITH RESERVATIONS | REJECTED
   ```

**Nota:** sem ANTHROPIC_API_KEY, o rubric é aplicado manualmente pelo Claude (não automatizado via promptfoo). Ainda funciona — Claude lê o YAML, aplica mentalmente, gera score sheet. Mais lento mas mais honesto.

---

### 4. Encontrar uma ferramenta pronta antes de construir

```
Patrick: "tem skill pra [X]?"
Patrick: "já existe algo pronto pra Y?"
```

**O que vai acontecer:**
1. Claude carrega reference-finder
2. Invoca `--solution-scout` mode (5 fontes em paralelo):
   - Skills locais (grep em `skillforge-arsenal/skills/`)
   - mcp.so (MCP registry)
   - Glama.ai/mcp + Smithery
   - Anthropic skills repo
   - GitHub topic `claude-skill`
3. Retorna tabela estruturada:
   ```
   | Nome | Source | URL | Match score | Recomendação |
   |------|--------|-----|:-----------:|--------------|
   | ... | local | ... | 85 | 🟢 REUSE |
   | ... | mcp | ... | 60 | 🟡 EXTEND |
   | ... | github | ... | 30 | 🔴 BUILD |
   ```
4. Recomendação explícita: REUSE (usa pronto) / EXTEND (forka) / BUILD (constrói)

**Quando usar:** antes de qualquer ideia de "criar skill nova". Se reference-finder retornar solução >80% match, não faz sentido construir.

---

### 5. Maestro — quando não sabe qual skill usar

```
Patrick: "qual skill usar pra X?"
Patrick: "me ajuda a decidir"
Patrick: "quero fazer X mas não sei por onde começar"
```

**O que vai acontecer:**
1. Claude carrega maestro
2. maestro segue sua IRON LAW: NEVER recomendar skill sem ler o SKILL.md primeiro (descriptions ficam stale)
3. Phase 1 (Intent) → Phase 2 (Route) → Phase 3 (Present com gate de confirmação)
4. Se for chain multi-skill, calcula context budget e sugere `/clear` entre fases

---

## Uso periódico — 3 manutenções

### Uma vez por semana: revisar logs do hook

```powershell
# Total de dispatches
(Get-Content ~/.claude/logs/hook-dispatches.jsonl | Measure-Object -Line).Lines

# Top arquivos editados
$e = Get-Content ~/.claude/logs/hook-dispatches.jsonl | ForEach-Object { $_ | ConvertFrom-Json }
$e | Group-Object file | Sort-Object Count -Descending | Select-Object Count, Name -First 10

# Dispatches dos últimos 7 dias
$cutoff = (Get-Date).AddDays(-7)
$e | Where-Object { [datetime]$_.timestamp -gt $cutoff } | Measure-Object | Select-Object Count
```

**Se ver violações reais** (Claude editou sem rodar prompt-engineer), anota em `~/.claude/logs/violations.md` com formato:
```
2026-04-15 14:32 — CLAUDE.md — Claude editou sem validar. Eu chamei.
```

---

### Uma vez por mês: revisar tech debt conhecido

Arquivos a olhar:
1. `skills/prompt-engineer/gaps/` — gaps documentados aguardando virar rubric
2. `CLAUDE.md` applied learnings — remover os que não dispararam em 90 dias
3. `~/.claude/rules/` — manutenção, adicionar/remover regras conforme uso real

---

### A cada 3 meses: audit da tripulação

Rodar `trident --mode all-local` no skillforge-arsenal pra pegar tech debt de código novo.

Rodar `prompt-engineer --validate --type claude-md` no CLAUDE.md atual pra ver se score caiu.

Se tiver novas skills adicionadas desde o último audit, rodar Wave 6.5+ (audit incremental das novas).

---

## Troubleshooting — o que fazer quando der ruim

### "O hook disparou mas Claude ignorou e editou mesmo assim"

Isso é **violação real da IL-1**. Registra em `~/.claude/logs/violations.md`. Se acontecer 3+ vezes em 7 dias, escala pra **Wave 2.8 (V2 hard block)** — Claude cria marker file em `~/.claude/.validated/<hash>.marker` após rodar prompt-engineer, e o hook V2 verifica. Sem marker = `permissionDecision: deny`.

Plano de Wave 2.8 já tá documentado no `session-2026-04-10-continuity-doc.md`.

---

### "ccinspect reclama de CLAUDE.md tá com muitas linhas/tokens ainda"

CLAUDE.md atual (~238 linhas / 3250 tokens) tá em **warning, não error**. Soft targets (150/1800) são aspiracionais. Hard limits (300/4500) já saímos.

Se quiser encolher mais, extrair mais seções pra `.claude/rules/` seguindo o pattern de `token-hygiene.md` e `model-skill-router.md`. Cuidado com project-specific info — não mover pra user-level `.claude/rules/`, deixar no CLAUDE.md do projeto.

---

### "Skill X ficou com score baixo depois de editar"

Rode `prompt-engineer --validate --type system-prompt skills/X/SKILL.md` pra ver findings específicos. Corrige os P0 primeiro, depois P1. P2 pode virar tech debt.

**Se não melhorar:** o edit provavelmente introduziu redundância ou caps lock excessivo. Compara com o `.bak` pre-edit (se tiver) ou `git diff` pra ver o que mudou.

---

### "Quero desabilitar o hook temporariamente"

Edita `C:\Users\Patrick Neuhaus\.claude\settings.json` e comenta o bloco de PreToolUse. Lembra de reativar depois.

**Alternativa melhor:** adiciona o path do arquivo que tá editando na lista de exceções dentro do próprio hook (`check-instruction-file.ps1`, array `$exceptions`).

---

### "Perdi o acesso ao `~/.claude/rules/` (troca de máquina)"

Recria manualmente. Os 4 arquivos estão no git do skillforge-arsenal como referência via `SESSION-NARRATIVE-2026-04-10-11.md` seção 7. Copia-cola o conteúdo.

Alternativamente, cria um **dotfiles repo separado** pra versionar `.claude/` — tô deixando isso como melhoria opcional.

---

## Arquivos importantes (mapa mental)

### No repo `skillforge-arsenal`

```
skillforge-arsenal/
├── SESSION-NARRATIVE-2026-04-10-11.md    ← narrativa humana da sessão (ler pra entender o contexto)
├── HOW-TO-USE.md                          ← você está aqui (guia prático de uso)
├── session-2026-04-10-continuity-doc.md  ← state save técnico pro Claude retomar
├── audit-quality-2026-04-11-wave-6-1.md  ← audit das 10 foundationais
├── audit-quality-2026-04-11-wave-6-2.md  ← audit marketing/content
├── audit-quality-2026-04-11-wave-6-3.md  ← audit engenharia
├── audit-quality-2026-04-11-wave-6-4.md  ← audit utils/auditoria/docs
├── skills/
│   ├── prompt-engineer/
│   │   ├── SKILL.md                       ← v3, role + rubric-based validate
│   │   ├── rubric/                        ← 4 YAMLs por tipo de arquivo
│   │   │   ├── claude-md.yaml
│   │   │   ├── technical-plan.yaml
│   │   │   ├── iron-laws.yaml
│   │   │   └── system-prompt.yaml
│   │   ├── gaps/                          ← gaps reais documentados
│   │   │   └── gap_2026-04-10_environment-setup-not-checked.md
│   │   └── references/
│   │       └── create-criteria.md         ← universal checklist pra --create
│   ├── skill-builder/
│   │   ├── SKILL.md                       ← v3, com Step 0 pointer
│   │   └── references/
│   │       └── step-0-pre-build-research.md  ← 8 questões bloqueantes
│   └── [outras 38 skills]/
└── dist/                                  ← zips atualizados
```

### Em `C:\Users\Patrick Neuhaus\.claude\` (user-level)

```
.claude/
├── rules/                                 ← carrega em QUALQUER projeto
│   ├── iron-laws.md                       ← IL-1 a IL-7 (comportamentos duros)
│   ├── skill-routing.md                   ← tabela palavra → skill
│   ├── token-hygiene.md                   ← regras universais de contexto
│   └── model-skill-router.md              ← árvore de decisão modelo/skill
├── hooks/
│   └── check-instruction-file.ps1         ← hook V1 warning + logging
├── logs/
│   ├── README.md                          ← comandos de análise
│   ├── hook-dispatches.jsonl              ← telemetria do hook
│   └── violations.md                      ← (criar se precisar)
├── settings.json                          ← PreToolUse hook registrado
└── plans/
    └── fluffy-giggling-phoenix.md         ← plano completo v4 (ref histórica)
```

### No Daily (cópia de trabalho)

```
C:\Users\Patrick Neuhaus\Desktop\Daily\
└── CLAUDE.md                              ← espelho do D:\DOCUMENTOS\Github\CLAUDE.md
```

---

## Como a próxima sessão do Claude deve retomar

Se tu abrir uma sessão nova e quiser que o Claude entenda tudo que foi feito:

```
Patrick: "leia nessa ordem antes de qualquer coisa:
1. D:\DOCUMENTOS\Github\skillforge-arsenal\SESSION-NARRATIVE-2026-04-10-11.md
2. D:\DOCUMENTOS\Github\skillforge-arsenal\HOW-TO-USE.md (este arquivo)
3. D:\DOCUMENTOS\Github\skillforge-arsenal\session-2026-04-10-continuity-doc.md
4. C:\Users\Patrick Neuhaus\.claude\rules\iron-laws.md
5. C:\Users\Patrick Neuhaus\.claude\rules\skill-routing.md

Status: plano fluffy-giggling-phoenix completo. Pendentes: Wave 7.2 (testes E2E) e Wave 2.8 futura (V2 hook). Resto tá versionado.

Tarefa de hoje: [X]"
```

---

## TL;DR absoluto

**Pra usar no dia a dia:** não faz nada diferente. O sistema roda em background. Pede skill, skill roda, hook dispara se tu tocar em arquivo de instrução, prompt-engineer valida quando chamado.

**Pra manutenção:** olhar logs do hook 1x por semana. Audit do CLAUDE.md 1x por 3 meses. Revisar applied learnings 1x por mês.

**Se algo der ruim:** o troubleshooting acima cobre os cenários mais prováveis. Se for caso novo, documenta em `~/.claude/logs/violations.md` ou gap em `skills/prompt-engineer/gaps/`, e a rubric/hook evolui via retroalimentação documentada (regra anti-drift).

**Feche a sessão quando quiser.** Tudo versionado. Tudo recuperável. Tamo tranquilo.
