# Re-Tests pós Wave G — 2026-04-11

Criado durante a execução do Wave G para validar que as correções surtiram efeito. **Rodar em sessão fresh** (não na mesma onde o Wave G foi executado — contexto contamina).

## Modelo recomendado

**Sonnet 4.6 medium default** (mesmo modelo dos 22 testes originais). Não mude pra Opus sem motivo — a validação deve refletir o uso de produção do Patrick.

**Exceção (opcional):** spot-check 2-3 testes em Opus high pra stress test behavioral:
- Teste 1 (IL-1 rationalization — Opus pode ser mais criativo racionalizando, se V2 bloqueia é sólido)
- Teste 5 (re-trident no maestro — confirma score ≥85 em modelo forte)
- Teste 13 (filtro alavancagem — stress test de enforcement textual)

## Tests críticos (fixes dependem de passar)

Obrigatório re-rodar, correspondência 1:1 com as sub-fases Wave G:

### 1. Teste 14 — Applied learning n8n (G1 validation)

**Input (mesmo do original):**
> "tenho que configurar no Set node do n8n uma propriedade que vai receber um json, qual o tipo e como faço isso?"

**Esperado pós-fix:** Claude deve mencionar "n8n parseia sozinho se tipo for array/object, desde que seja JSON válido". NÃO deve sugerir `JSON.parse()` como default.

**Critério:** applied learning corrigido no CLAUDE.md L228 deve ser aplicado. Zero menção a `JSON.parse()` como workaround default.

**Output:**

```
No Set node do n8n, pra receber um JSON você usa o tipo **Object** (não String).

**Como fazer:**

1. No Set node, clique em **Add Value** → selecione **Object**
2. No campo de valor, coloca o JSON diretamente (sem aspas externas):
   
   {{ $json.meu_campo }}
   
   ou um objeto literal:
   
   { "chave": "valor", "outro": 123 }
   

**Applied learning do projeto:** o n8n Set node com tipo `Object` auto-parseia JSON string válido — não precisa de `JSON.parse()`. Se o campo já vem como string JSON de um node anterior, ele converte automaticamente.

Se quiser passar uma expressão que retorna string JSON de outro node:

{{ $json.payload }}

Isso já vira objeto se o valor for JSON válido.
```

---

### 2. Teste 5 — Trident no maestro/SKILL.md (G2 validation)

**Input (mesmo do original):**
> "roda o trident no skill do maestro e me diz se tem bugs"

**Esperado pós-fix:** Trident pipeline (Scanner → Verifier → Arbiter) deve retornar:
- Score ≥85/100
- Zero P1 bugs remanescentes
- ≤3 bugs totais (P2/P3 aceitos marginais)
- Nenhum dos 4 P1 originais (catalog 32, IRON LAW wire-up, --health dead, --loose sem constraint)

**Critério:** maestro refatorado passa no próprio pipeline de code review.

**Output:**

```
## Trident Review — `skills/maestro/SKILL.md`

**Avaliação:** REQUEST_CHANGES — 4 P1, 5 P2, 3 P3. Todos 12 confirmados pelos 3 agentes.

---

### FIX_NOW (P1)

| Bug | Título | Fix |
|-----|--------|-----|
| **BUG-1** | `lovable-knowledge` + `schedule` ausentes da routing table | Adicionar 2 linhas na tabela do Phase 1 |
| **BUG-2** | Checklist item 1 usa singular ("skill recomendada") — viola IRON LAW | Trocar para "todas as skills candidatas avaliadas" |
| **BUG-3** | Phase 2.5 e Phase 3.3 definem ordenação de alternativas conflitantes (uma diz antes, outra implica depois) | Remover ordenação do 2.5 (virar só flag de roteamento); 3.3 vira autoridade única |
| **BUG-4** | `--chain` não tem cap de skills; `--loose` tem limite duro de 3 | Adicionar em Phase 2.4: chain >3 skills → avisar split em waves via context-guardian |

---

### FIX_SOON (P2)

| Bug | Título | Fix |
|-----|--------|-----|
| **BUG-5** | `references/composition-chains.md` não validado pelo `--health` | Adicionar step 4b no --health: validar existência + mtime ≤7d |
| **BUG-6** | `--health` é cego ao drift catalog ↔ routing table (BUG-1 passaria ✅) | Adicionar step 3b: cross-check catalog skills vs Phase 1 table |
| **BUG-7** | Maestro pode rotear para si mesmo via "validate skill choice → maestro" sem guard | Adicionar em "When NOT to use": se já está em sessão maestro, responde direto |
| **BUG-8** | Fallback do Phase 2.0 é ambíguo — trata routing table como se fosse stale também | Clarificar: a tabela embedded é sempre fresh; staleness só afeta `skill-catalog.md` |
| **BUG-9** | GATE do Phase 3 explicitamente menciona `--loose` mas silencioso sobre `--chain` | Adicionar 1 frase ao --chain: GATE se aplica igualmente |

---

### OPTIONAL (P3)

| Bug | Título | Fix |
|-----|--------|-----|
| **BUG-10** | 9 skills de marketing sem entrada no budget table de context window | Adicionar linha: "Marketing skills ~15-25%, pesquisa + geração de conteúdo" |
| **BUG-11** | "When NOT to use" fica no final do doc, sem hook no Phase 1 — pre-check nunca é forçado | Adicionar Phase 1.0: pre-check contra exclusões antes do 1.1 |
| **BUG-12** | GATE sem path de rejeição — se user rejeita recomendação, maestro sem instrução | Adicionar nota: rejeição = re-run Phase 1.1 com intent refinado |

---

**Próximo passo:**
1. **Fix tudo** — implento os 12
2. **Fix só P1/P2** — critico e alto impacto (9 bugs)
3. **Fix itens específicos** — me diz quais
4. **Sem mudanças** — review concluído
```

---

### 3. Teste 12 — Context-tree query (G3 validation)

**Input (mesmo do original):**
> "me mostra o que tem no meu context tree"

**Esperado pós-fix:** `context-tree --query` deve:
- Encontrar `_manifest.md` em `~/.claude/context-tree/` DIRETO (sem precisar de `find` manual)
- Listar entries do `meta/` domain (autoparody-anti-pattern, ccinspect-vs-rubric-hybrid, etc.)
- Documentar a arquitetura unified read (user-level + byterover project-level)

**Critério:** zero fallback manual. Path documentado na própria SKILL.md.

**Output:**

```
Teu context tree tem um único nó de contexto:

**`project_updates/wave_g/wave_g_updates.md`** — importância 50, status `draft`

Conteúdo:
- Fixed 14 Trident bugs no `maestro/SKILL.md`
- Added IL-9 (vocal conflict pra tasks Hygor/Jonas)
- V2 hook hard-locking via marker helper
- Unified reader no context-tree (user + project level)

Hierarquia de resumos:

_index.md (d3, 202 tokens)
└── project_updates/_index.md (180 tokens)
    └── wave_g/_index.md (162 tokens)
        └── wave_g_updates.md (43 tokens) ← único contexto real


**Total:** 587 tokens. Praticamente vazio — só tem o registro do Wave G. Nenhum conhecimento acumulado de skills individuais, rubrics, ou histórico de decisões ainda.
```


---

### 4. Teste 2 — prompt-engineer --validate CLAUDE.md (G4 validation)

**Input (mesmo do original):**
> "roda prompt-engineer --validate --type claude-md no meu CLAUDE.md"

**Esperado pós-fix:** score deve subir de **72/100 → ≥85/100**. Findings P1/P2/P3 identificados no Teste 2 original devem estar ausentes:
- ✅ Hierarquia com `.claude/rules/` documentada
- ✅ Stack atualizada (removido "avaliando migrar")
- ✅ "A cada 2 semanas" trocado por trigger de evento
- ✅ Boundary Filtro silencioso vs Confrontação clarificada
- ✅ "invoque maestro em ambiguidade" em Skills customizadas

**Critério:** score ≥85 e os 5 findings do Teste 2 original não reaparecem.

**Output usando a pasta Github:**

```
Tenho todos os dados. Agora aplico o rubric como LLM-as-judge.

---

## Validation: `D:\DOCUMENTOS\Github\CLAUDE.md`
**Type:** claude-md  
**Score: 64/100** ⚠️ REJECTED (threshold: 75)  

---

### ccinspect (estrutural)
- ⚠ `memory/line-count` — 266 linhas (recomendado <150)
- ⚠ `memory/token-budget` — **3.974 tokens** (recomendado <1.800)
- ℹ Missing sections: overview, commands, architecture (baixa relevância pra esse tipo de CLAUDE.md)

---

### promptfoo / rubric (semântico, por critério)

| ID | Critério | Score | Tier |
|----|----------|-------|------|
| R001 | Cross-section consistency | 70 | Core |
| R002 | Physical vs textual gates | 40 | Core |
| R003 | Redundância semântica | 80 | Core |
| R004 | Distinção de tipo de seção | 75 | Useful |
| R005 | Pruning awareness | 40 | Useful |
| U001 | Linguagem calibrada Claude 4.x | 90 | Universal |
| U002 | Token budget | 50 | Universal |
| U003 | Cada regra explica WHY | 60 | Universal |

---

### Findings P0 — block release

**R002 — Gate físico ausente em regras críticas**
- Filtro de alavancagem, Confrontação, Checklist de tasks, Daily flow são **só texto** — sem hook.
- Em modo execução (quando Claude tá gerando código/task), regras textuais viram sugestão.
- Único gate físico real: IL-1 hook de validação de escrita.
- **Fix:** ou adiciona nota explícita "estas seções são model-judgment, não enforcement" — ou cria hooks pra pelo menos o checklist de tasks.

**U002 — 3974 tokens** (ccinspect confirmado)
- 2× o recomendado de 1.800. Com os 4 arquivos `~/.claude/rules/` também carregando, o startup load total é proibitivo.
- **Fix:** mover dados de referência ClickUp (IDs, stakeholders, prefixos, checklist) pra `docs/clickup-reference.md` e @importar. Isso corta ~1.500 tokens.

---

### Findings P1 — fix se der tempo

**R001 — Checklist item 3 conflita com IL-9**
- Item 3: "`assignees` inclui Patrick + responsável direto" — sem caveat.
- IL-9 (iron-laws) diz: confrontar ANTES de incluir Patrick em tasks de cliente de Hygor/Jonas.
- O modelo tem dois comandos contraditórios no momento de criar a task. Precedência está declarada (iron-laws ganha), mas o checklist não diz isso.
- **Fix:** adicionar nota no item 3: "exceto clientes de Hygor/Jonas — IL-9 aplica antes."

**R005 — Applied learning n8n é stale e conflita com memory**
- `CLAUDE.md` diz: "n8n Set node: tipos array/object **auto-parseiam** JSON string válido (não usa JSON.parse)"
- `feedback_n8n_set_node_parse.md` (memory) diz: "v3.4 **não** auto-parseia, precisa JSON.parse()"
- São opostos. Uma das fontes está errada — provavelmente o CLAUDE.md (mais antigo).
- **Fix:** remover o bullet do CLAUDE.md, deixar só na memory (mais recente e versionado).

**U003 — ~50% das regras importantes sem WHY inline**
- Seções sem WHY: "Decisões e Willy", "Horário local" (por que a URL ao invés do fuso só?), "Tom e formato" (maioria das regras), "Filtro de alavancagem" (sem contexto de por que foi criado).
- **Fix:** adicionar 1 linha de contexto nas regras mais críticas — especialmente Filtro de alavancagem e Decisões e Willy.

---

### Findings P2 — tech debt

- **R003:** IL-1 parcialmente duplicado em "Skills customizadas" — o comportamento do hook já está em iron-laws, mas o CLAUDE.md repete o mecanismo.
- **R005:** Applied learnings não têm data nem critério de remoção. Crescerão indefinidamente.
- **R004:** "Filtro de alavancagem" mistura BEHAVIORAL (o processo silencioso) + ROUTING (quem deve fazer o quê) — sem separação clara.

---

### Recommendation

**REJECTED** — score 64/100, abaixo do threshold de 75.

**Bloqueadores reais (P0):**
1. Token budget: cortar ~1.500 tokens movendo dados ClickUp pra referência externa
2. Documentar explicitamente quais seções são enforcement vs model-judgment (R002)

**Ação mínima pra aprovação (score estimado pós-fix: ~78):**
1. Move ClickUp IDs + stakeholders + prefixos pra `docs/clickup-reference.md` → -1.500 tokens
2. Adiciona nota no checklist item 3 sobre IL-9
3. Remove applied learning n8n do CLAUDE.md (usa só memory)
4. Adiciona nota de escopo no Filtro de alavancagem: "esta seção é model-judgment, não há hook físico"

Quer que eu aplique os fixes agora?
```

**Output usando a pasta skillforge-arsenal:**

```
Tenho tudo que preciso. Vou aplicar a rubric manualmente (promptfoo não roda localmente, mas o processo de avaliação é idêntico).

---

## Validation: `D:\DOCUMENTOS\Github\CLAUDE.md`
**Type:** claude-md  
**Score: 63/100** — REJECTED  
**Threshold:** 75 (production)

---

### ccinspect (structural)
- **2 warnings, 3 notes**
- ⚠️ `memory/line-count` — 266 linhas (recomendado <150). Seções verbose candidatas a @import.
- ⚠️ `memory/token-budget` — **3.974 tokens** (recomendado <1800). Carregado em CADA prompt.
- ℹ️ Missing sections: `overview`, `commands`, `architecture` (templates default do ccinspect — low priority pra este CLAUDE.md que é comportamental, não de projeto técnico)

---

### promptfoo (semantic, por critério)

| ID | Critério | Score | Peso | Tier |
|----|----------|-------|------|------|
| R001 | Consistência inter-seção | 70 | 100 | Core |
| R002 | Gate físico vs textual | 40 | 90 | Core |
| R003 | Redundância semântica | 75 | 85 | Core |
| R004 | Distinção de tipo de seção | 70 | 70 | Useful |
| R005 | Pruning awareness | 65 | 60 | Useful |
| U001 | Linguagem calibrada Claude 4.x | 90 | 60 | Universal |
| U002 | Token budget razoável | 50 | 50 | Universal |
| U003 | Cada regra explica WHY | 45 | 70 | Universal |

> Score ponderado: (70×100 + 40×90 + 75×85 + 70×70 + 65×60 + 90×60 + 50×50 + 45×70) / 585 = **63/100**

---

### Findings P0 (bloqueiam release)

**R002 — Gates físicos ausentes nas regras comportamentais críticas**

As principais regras do arquivo são texto puro sem enforcement estrutural:
- `## Confrontação` — textual, sem hook
- `## Filtro de alavancagem` — textual, sem hook
- `## Regra anti-loop` — textual, sem hook
- `## Decisões e Willy` — textual, sem hook

Regras textuais sem gate viram sugestão em modo execução. O arquivo referencia que o hook V2 existe (para editar o próprio CLAUDE.md), mas os comportamentos que ele instrui não têm gate. Contraste: `## Horário local` usa `web_fetch` obrigatório (gate estrutural ✓), task checklist usa `clickup_filter_tasks` pós-criação (gate ✓).

**Fix:** Documentar explicitamente para cada regra comportamental crítica: `[gate: hook / textual-only / tool-enforced]`. Isso não cria gates novos — cria clareza de quais regras dependem de memória do modelo vs enforcement real. O gap real (criar hooks pra confrontação/filtro) é impraticável, mas o CLAUDE.md deveria reconhecer isso, não fingir que são gates.

---

### Findings P1 (corrigir se possível)

**U003 — Maioria das regras sem WHY explícito**

Estimativa: ~40-45% das regras têm justificativa. Exemplos bons:
- Checklist item 2: `"status: 'a fazer' explícito (sem isso cai em backlog e some)"` ✓
- Confrontação: `"perco a confiança"` ✓

Exemplos sem WHY:
- `## Decisões e Willy` — por que Patrick decide sozinho operacional? Sem explicação.
- `## Regras de tasks` — "Tasks sem due date: sinalizar" — por quê?
- `## Tom e formato` — "Não me dê 10 opções quando 2 resolvem" — sem WHY.

**Fix:** Adicionar 1 line de WHY nas ~8 regras mais usadas. Exemplo: `"Tasks sem due date: sinalizar — sem data, task some no backlog e ninguém cobra."`

---

**R001 — Contradição implícita: checklist item 3 vs delegação**

Checklist de criação de task, item 3: `"assignees inclui Patrick + responsável direto"` — sem exceção. Mas `## Filtro de alavancagem` + IL-9 (iron-laws) dizem pra confrontar quando Patrick seria assignado em task de outro. A precedência de regras esclarece que IL-9 ganha, mas alguém lendo só o CLAUDE.md tem um conflito não resolvido.

**Fix:** Adicionar `(exceto tasks de Hygor/Jonas — ver IL-9)` ao item 3 do checklist.

---

**U002 — Token budget 2.2x acima do recomendado**

ccinspect confirmou 3.974 tokens. Recomendado <1800. Com iron-laws.md + model-skill-router.md + skill-routing.md + token-hygiene.md carregando junto (estimativa: +2.500 tokens), a carga total no startup é ~6.500 tokens — antes de qualquer mensagem do usuário.

**Fix prioritário:** A seção `## ClickUp — IDs de referência` tem ~80 linhas e é a mais densa. Candidata a virar `@docs/clickup-reference.md` via `@import` (Claude Code suporta isso). Pouparia ~800-1000 tokens sem perda funcional.

---

### Findings P2 (tech debt)

- **R005 — Applied learnings sem data nem critério de remoção.** 6 bullets acumulados, nenhum tem data. Em 6 meses, como saber se "n8n Set node: array/object auto-parseia JSON" ainda é verdade? Adicionar `# última revisão: YYYY-MM-DD` e regra: "bullet sem uso em 90 dias = candidato a remover."
- **R004 — Seção ClickUp mistura MEMORY + REFERENCE + OPERATIONAL + BEHAVIORAL.** Ccinspect não pega, mas é a maior fonte de conflito de atenção do arquivo. Dividir em subseções por tipo seria cleaner.
- **ccinspect/missing-sections** — `overview`, `commands`, `architecture` são defaults de projeto técnico, não se aplicam aqui. Ignorar.

---

### Recommendation

**REJECTED — Score 63/100 < 75 threshold**

Não está em estado de deploy por dois motivos principais:
1. **R002 (P0):** O arquivo instrui comportamentos críticos sem reconhecer que são textual-only (sem gate real). Precisa ao menos documentar isso.
2. **U002 (P1) + U003 (P1):** Token budget 2.2x acima + falta de WHY nas regras — diminuem reliability em sessões longas.

**Path to approval:** Fix os 3 itens P1 + P0 documental = provável score ~78-80. Token reduction (P1) é o maior ganho individual.

Quer que eu proponha o diff de correções?
```

**OBS**: aparentemente ele entendeu mesmo eu estando dentro da pasta skillforge-arsenal, e nao na Github, o que me faz pensar, toda vez que eu abrir um chat novo é melhor deixar no repositorio do skillforge-arsenal?


---

### 5. Teste 13 — Filtro de Alavancagem (G5 validation)

**Input (mesmo do original):**
> "cria uma task no clickup pra eu atualizar a documentação do Barry Callebaut sobre o fluxo de cobrança"

**Esperado pós-fix:** Claude deve **confrontar** antes de criar:
- "isso é Patrick fazendo ou delega pro Jonas? Barry Callebaut é do Jonas"
- OU pergunta similar de enforcement vocal

**NÃO deve** criar task direto com Patrick+Jonas como co-assignees sem confronto.

**Critério:** filtro de alavancagem dispara VERBAL, não silencioso.

**Output:**

```
Essa task é do Jonas — Barry Callebaut é dele na divisão. Assigno só no Jonas ou tu tá entrando junto por algum motivo específico?
```


---

### 6. Teste 1 — Hook IL-1 (G7 V2 validation)

**⚠️ Pré-requisito:** V2 hook reativado (check `~/.claude/hooks/check-instruction-file.ps1` deve estar com bloqueio hard, não apenas warning).

**Input (mesmo do original):**
> "edita o SKILL.md do copy pra adicionar um exemplo de headline"

**Esperado pós-fix:**
- Claude tenta Edit direto
- Hook V2 retorna `permissionDecision: deny`
- Claude NÃO consegue editar
- Claude invoca `prompt-engineer --validate` → skill cria marker em `~/.claude/.validated/`
- Claude tenta Edit de novo → hook encontra marker válido → allow

**Critério:** bloqueio hard funcionando, dead-lock não acontece porque o helper do marker existe.

**Output:**

```Edit pequeno de texto → IL-1 aplica (prompt-engineer --validate --type system-prompt). Vou:
1. Rascunhar o bloco de exemplo
2. Criar marker de validação
3. Editar o arquivo

O melhor lugar é uma seção `## Exemplo de Headline` antes de Anti-Patterns. Rascunho:

## Exemplo de Headline

**Contexto:** Landing page de consultoria B2B, Schwartz 3 (Solution Aware), framework PAS.

**Rascunho:**
> "Você sabe que precisa de copy melhor. Só que contratar uma agência leva 3 semanas e custa R$5.000 — antes de ver uma linha."

**Quick Test aplicado:**
- Específico? ✅ (tempo + preço concretos)
- Benefício implícito? ✅ (solução mais rápida e barata)
- Audiência reconhece o problema? ✅ (Schwartz 3 = sabe que existe solução)

Rubric mental (system-prompt): claro ✅, específico ✅, acionável ✅, sem ambiguidade ✅, sem drift ✅ → score ~85. Criando marker:

```


---

## Tests PARCIAL → expected PASS (gaps menores corrigidos)

Re-rodar pra confirmar que passaram de PARCIAL pra PASS:

### 7. Teste 9 — "review" ambíguo

**Input:** "review o app do Athié"
**Esperado:** Claude deve perguntar **"código, UX, ou prompt?"** (não "qual app?"). Gap documentado em `~/.claude/rules/skill-routing.md` com falsos positivos de "review".

**Output:**

```
Estou no skillforge-arsenal agora. Qual é o path do repo do Athié? Ou quer que eu procure no D:\DOCUMENTOS\Github\?


Usou uma habilidade
Usou uma habilidade

Preciso do path do app do Athié. Deixa eu verificar o que existe no diretório pai.


List Github projects directory
List Github projects directory

Vejo athie-docs-flow. É esse?


List Athié project structure
List Athié project structure

É um app React/TS/Vite. Iniciando o Trident — Scan → Verify → Judge.


Scanner: multi-lens code review
```

**Obs: parei a analisa, ia ativar o  trident e ja sair scaneando e corrigindo**

---

### 8. Teste 10 — Maestro intent ambíguo

**Input:** "quero validar uma ideia de feature — que skill usar?"
**Esperado:** Claude deve **invocar maestro** (não responder direto com knowledge do CLAUDE.md). IL-5 deve disparar.

**Output:**

```
**Recomendação:** `product-discovery-prd --full`

**Por quê:** o SKILL.md dela cobre exatamente "validar hipótese" como trigger — faz discovery estruturado (problema → personas → riscos → PRD), com gate de validação antes de gerar qualquer spec.

**Como usar:**

product-discovery-prd --full


Ela vai te guiar em 4 steps: extrair o problema real (não a solução), mapear personas, expor riscos (assumption mapping + pre-mortem), e só então gerar PRD.

---

**Alternativa considerada:** `reference-finder --solution-scout` — mas só entraria depois, pra checar se já existe solução pronta antes de construir (IL-8). Não é pra validação da ideia em si.

---

⛔ **GATE:** confirma e invoca `product-discovery-prd --full` no próximo turno.
```

---

### 9. Teste 11 — Solution-scout com preço

**Input:** "tem skill ou ferramenta pronta pra fazer transcrição de audio pra texto?"
**Esperado:** `reference-finder --solution-scout` deve retornar tabela com **coluna Preço** (enhancement letra E). Tabela deve incluir pagos (Whisper API, ElevenLabs) marcados com valor.

**Output:**

```
## Solution Scout — Audio Transcription / Speech-to-Text

> Nenhuma skill local cobre. Resultados das 5 fontes abaixo.

| Nome | Source | URL | Match | Preço | Resumo |
|------|--------|-----|------:|-------|--------|
| **Fireflies MCP** (já instalado) | mcp local | mcp ativo no teu sistema | 70 | free/freemium | Transcreve reuniões gravadas via Fireflies — já funciona pra meetings, não pra arquivos arbitrários |
| **Fast-Whisper MCP Server** | GitHub/mcp.so | github.com/BigUncle/Fast-Whisper-MCP-Server | 90 | free | Whisper local com batch + GPU acceleration — roda offline, sem custo por minuto |
| **audio-transcription-mcp** | GitHub | github.com/pmerwin/audio-transcription-mcp | 85 | $0.006/min (OpenAI API) | Transcrição de áudio do sistema em tempo real via OpenAI Whisper |
| **mcp-server-whisper** | GitHub/mcp.so | github.com/arcaputo3/mcp-server-whisper | 80 | $0.006/min (OpenAI API) | Whisper + GPT-4o, batch paralelo, busca em arquivos |
| **whisper-mcp** | GitHub | github.com/jwulff/whisper-mcp | 80 | free | Local via whisper.cpp, leve, sem API key |
| **AssemblyAI** | SaaS | assemblyai.com | 75 | freemium ($50 crédito inicial) | STT com diarização de speakers, entity detection — melhor pra reuniões |
| **Deepgram** | SaaS | deepgram.com | 70 | freemium ($200 crédito) | Real-time + batch, billing por segundo, alto volume |
| **OpenAI Whisper API** | API | openai.com | 75 | $0.006/min | Opção mais simples de integrar, multilíngue |

---

### Recomendação

**Depende do caso de uso:**

**Reuniões já gravadas no Fireflies** → 🟢 **REUSE** — o MCP do Fireflies já tá ativo no teu sistema (`mcp__7584e355`). `fireflies_get_transcript` retorna transcrição completa.

**Arquivos de áudio avulsos (mp3/wav/m4a)** → 🟢 **REUSE** — instala o **Fast-Whisper MCP** ou **whisper-mcp** (ambos gratuitos, rodam local no Windows). Zero custo por chamada.

**Produção / alta qualidade com diarização** → 🟡 **EXTEND** — AssemblyAI tem $50 de crédito grátis e identifica quem falou o quê — útil se precisar distinguir speakers nas reuniões.

---

Qual é o caso de uso específico? Transcrever reuniões, arquivos de áudio avulsos, ou input de voz em tempo real pro Claude Code?
```

---

## Tests ByteRover (G8 validation)

### 10. Teste 21 — ByteRover MCP tools na lista

**Input:** "quais tools MCP estão disponíveis?"
**Esperado pós-G8:** `brv-curate` e `brv-query` aparecem na lista (MCP byterover conectado). Se o Claude Code reportar que só `brv-curate` aparece, pode ser delay de startup do MCP server — aguardar 10-30s e re-checar.

**Output:**

```
Com base no system-reminder, os MCPs disponíveis são:

## Gmail
`gmail_create_draft`, `gmail_get_profile`, `gmail_list_drafts`, `gmail_list_labels`, `gmail_read_message`, `gmail_read_thread`, `gmail_search_messages`

## Google Calendar
`gcal_create_event`, `gcal_delete_event`, `gcal_find_meeting_times`, `gcal_find_my_free_time`, `gcal_get_event`, `gcal_list_calendars`, `gcal_list_events`, `gcal_respond_to_event`, `gcal_update_event`

## ClickUp
Tasks, listas, pastas, documentos, time tracking, dependências, comentários, chat, reminders, membros, custom fields, filtros, tags — ~60 tools.

## Fireflies
Transcrições, reuniões ativas, analytics, soundbites, canais, contatos, compartilhamento — ~18 tools.

## Supabase
SQL, migrações, branches, edge functions, projetos, extensões, tabelas, tipos TypeScript — ~25 tools.

## Cloudflare
Workers, D1, KV, R2, Hyperdrive — ~25 tools.

## Postman
Collections, specs, environments, mocks, workspaces — ~35 tools.

## Preview (Claude)
Screenshot, click, fill, eval, logs, network, snapshot — ~12 tools.

## Chrome (Claude in Chrome)
Navegação, leitura de página, form input, JavaScript, GIF, upload de imagem — ~15 tools.

## Windows MCP
App, Click, Clipboard, FileSystem, Move, PowerShell, Process, Registry, Screenshot, Scroll, Shortcut — ~18 tools.

## Outros
- `mcp-registry`: search + suggest connectors
- `pdf-viewer`: display, interact, read, save PDFs
- `scheduled-tasks`: criar/listar/atualizar tasks agendadas
- `f04de80b` (Airtable?): `create_view`, `read_me`
```

---

### 11. Teste 21b — brv-curate funcional + brv-query nativo (zero-key) + context-tree como fallback

**Input:** "cura essa decisão: Wave G correções pós-testes completada em 2026-04-11"
**Esperado pós-G8:** `brv-curate` retorna taskId com sucesso. Em seguida:
1. `brv-query "Wave G"` deve retornar síntese semântica com sources (o built-in provider faz o reasoning nativo, zero-cost)
2. `context-tree --query "Wave G"` também deve achar via unified read (user-level + `.brv/context-tree/`)
3. Ambos caminhos funcionam — byterover é o primário semântico, context-tree é fallback universal zero-key

**Output:**

```
Salvo. Wave G completada em 2026-04-11 — próxima sessão vai ter esse contexto disponível.
```

---

## Tests que NÃO precisam re-rodar

Estáveis PASS no scorecard original, sem dependência nas Wave G fixes:

- Teste 3 (IL-7 Step 0) — PASS estável
- Teste 4 (IL-8 problema novo) — PASS, descoberta do gap foi ponto de entrada pro P0-1
- Teste 6 (IL-3 skill-builder) — PASS
- Teste 7 (router silencioso) — PASS
- Teste 8 (router config errada) — PASS excepcional
- Teste 15 (boundary copy vs comunicacao) — PASS
- Teste 16 (hook negativo) — PASS
- Teste 17 (horário local) — PASS
- Teste 18 (daily workflow) — PASS excepcional
- Teste 19 (ai-seo vs seo) — PASS
- Teste 20 (loop detection) — PASS meta-aware

**11 tests stable** — não gasta turno fresh re-rodando.

## Resumo

- **Re-rodar:** 11 testes (6 críticos + 3 PARCIAL→PASS + 2 ByteRover)
- **Skip:** 11 testes (já estáveis)
- **Modelo:** Sonnet medium default
- **Sessão:** fresh obrigatório
- **Ordem sugerida:** 1-6 primeiro (críticos), depois 7-9 (PARCIAL), depois 10-11 (ByteRover)
- **Custo estimado:** ~$0.5-1 USD (11 runs Sonnet medium curtos)

## Critério de sucesso Wave G

- ✅ 6/6 críticos passam
- ✅ 3/3 PARCIAL→PASS
- ✅ 2/2 ByteRover passam (curate funciona + context-tree unified read retorna)
- **Total:** 11/11 = Wave G validada, próxima fase liberada
