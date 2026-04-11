# 20 testes E2E — Wave 7.2 validação sistema fluffy-giggling-phoenix

## Como usar este arquivo

- **Input** → copia e cola em sessão fresh (nova conversa, não `/clear`)
- **Esperado / Observar / Critério** → baseline pra tu marcar PASS/FAIL na hora, se quiser
- **Resposta real** → campo obrigatório, cola o que o Claude realmente respondeu
- **Análise** → opcional marcar na hora; se não marcar, eu analiso quando tu mandar de volta
- Pode rodar em lotes de 5-10 por dia. Fecha conversa entre testes (não `/clear`).

> **Instrução:** rodar cada teste em **sessão fresh** (nova conversa, não `/clear` dentro da mesma sessão — isso mantém alguma coisa em cache).
>
> **O que medir:** não importa se a resposta é 100% idêntica ao "Esperado". Importa se o **comportamento de roteamento e validação** tá correto.

---

## Teste 1 — Hook dispara em edit de SKILL.md

**Input:**
```
Edita o arquivo D:\DOCUMENTOS\Github\skillforge-arsenal\skills\maestro\SKILL.md e adiciona a linha "- Test comment" no final
```

**Esperado:**
- Claude vai tentar editar
- Hook PS1 dispara → mensagem `ATENCAO -- arquivo de instrucao: ...maestro/SKILL.md` aparece como `additionalContext`
- Claude deve PARAR, confirmar os 3 checks (prompt-engineer --validate, skill-builder --validate, ccinspect), e só então editar

**O que observar:** Claude mostra os 3 checks ou edita direto ignorando o aviso?

**Critério PASS:** Claude menciona os 3 checks antes de aplicar o edit.
**Critério FAIL:** Claude edita sem mencionar o aviso do hook.

**Resposta real:**
```
[cola aqui o que Claude respondeu]
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 2 — Validação de CLAUDE.md via prompt-engineer

**Input:**
```
Valida o arquivo D:\DOCUMENTOS\Github\CLAUDE.md usando prompt-engineer
```

**Esperado:**
- Claude invoca skill `prompt-engineer` com `--validate --type claude-md`
- Roda ccinspect primeiro (estrutural)
- Aplica rubric `claude-md.yaml` mentalmente (sem API key, aplicação manual)
- Retorna score sheet com findings P0/P1/P2 e recomendação (APPROVED/REJECTED)

**O que observar:** Score retornado deve ser ~68-72 (estado atual pós Wave 2.5-2.7). Deve mencionar tipos de findings por critério (R001, R002, etc).

**Critério PASS:** gera score sheet estruturado com pelo menos 3 critérios avaliados.
**Critério FAIL:** responde genericamente "o CLAUDE.md parece bom" sem aplicar rubric.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 3 — IL-7 Step 0 bloqueando skill nova

**Input:**
```
Cria uma skill pra gerar PDFs a partir de templates HTML
```

**Esperado:**
- Claude invoca `skill-builder`
- skill-builder Step 0 dispara as 8 perguntas bloqueantes
- Q3 "já procurou em skills locais?" obriga Claude a invocar `reference-finder --solution-scout "html to pdf"`
- Reference-finder retorna: skill `pdf` local + bibliotecas existentes (puppeteer, wkhtmltopdf, etc)
- skill-builder RECUSA criação, recomenda usar a skill `pdf` existente

**O que observar:** Claude verifica solução pronta ANTES de propor criar skill nova?

**Critério PASS:** Claude invoca reference-finder ou menciona explicitamente a skill `pdf` existente antes de propor criar nova.
**Critério FAIL:** Claude começa a construir skill nova direto sem verificar.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 4 — IL-8 (nova) — problema novo sem mencionar skill

**Input:**
```
Preciso automatizar um resumo diário de métricas do Supabase que chega no meu WhatsApp toda manhã às 9h
```

**Esperado (crítico pra validar IL-8):**
- Claude detecta problema novo sem skill mencionada
- **IL-8 dispara:** Claude deve invocar `reference-finder --solution-scout "supabase daily metrics whatsapp"` ANTES de propor solução
- Retorna matches: `schedule` (skill local, 85% match), `n8n-architect` (skill local, 90% match), supabase MCP, evolution-api MCP
- Propõe chain: `schedule` (cron 9h) + `n8n-architect` (workflow com supabase → whatsapp)
- NÃO sugere criar skill nova

**O que observar:** Claude pula direto pra "vou criar um workflow" ou passa por reference-finder primeiro?

**Critério PASS:** Claude menciona reference-finder ou faz solution-scout antes de propor implementação.
**Critério FAIL:** Claude propõe solução direto sem verificar soluções prontas.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 5 — IL-3 prioridade local vs Anthropic (trident)

**Input:**
```
Revisa o código desse arquivo: skills/maestro/SKILL.md — tem bugs ou anti-patterns?
```

**Esperado:**
- Intent bate com 3 skills: `simplify` (built-in), `anthropic-skills:trident` (Anthropic), `trident` (skillforge local)
- IL-2 elimina `simplify`
- IL-3 prioriza `trident` local sobre `anthropic-skills:trident`
- Claude chama **trident** (skillforge), não `anthropic-skills:trident`

**O que observar:** No log/output, Claude diz qual versão de trident ele chamou?

**Critério PASS:** Claude usa a skill local OU menciona que está priorizando a versão local.
**Critério FAIL:** Claude chama `anthropic-skills:trident` ou `simplify`.
**Critério OBSERVAÇÃO:** Se tu não conseguir distinguir qual versão ele chamou (às vezes não aparece no output), marca como OBSERVAÇÃO e descreve o comportamento.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL ⬜ OBSERVAÇÃO

---

## Teste 6 — IL-3 prioridade local (skill-builder vs anthropic-skills:skill-builder)

**Input:**
```
Quero criar uma skill nova pra gerenciar releases de produto. Qual skill eu uso?
```

**Esperado:**
- Claude recomenda `skill-builder` (local) com Step 0
- NÃO chama `anthropic-skills:skill-builder`
- Menciona que vai rodar as 8 perguntas bloqueantes primeiro

**O que observar:** qual skill-builder ele chamou? Mencionou Step 0 v3?

**Critério PASS:** Menciona skill-builder local com Step 0 (8 perguntas bloqueantes).
**Critério FAIL:** Usa anthropic-skills:skill-builder ou cria skill direto sem Step 0.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 7 — Model router silencioso (config correta)

**Input:**
```
Lê o arquivo package.json desse projeto e me diz qual o framework usado
```

**Esperado:**
- Task trivial (só leitura + resposta)
- Model router NÃO deve exibir bloco 🎯 (porque config atual cabe a task)
- Claude responde direto após ler o arquivo

**O que observar:** Claude abre bloco de "config sugerida" ou responde direto?

**Critério PASS:** Claude responde direto sem mencionar model/thinking.
**Critério FAIL:** Claude abre bloco 🎯 pra task trivial.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 8 — Model router dispara quando config errada

**Input (em Sonnet medium, configuração default):**
```
Arquiteta uma solução completa multi-tenant pra SaaS de gestão de contratos: Supabase com 15 tabelas, RLS por org, Edge Functions pra webhooks, automação n8n pra lembretes, frontend Lovable. Precisa considerar auth, billing, escalabilidade pra 10k usuários, e integração com Stripe, DocuSign e Google Calendar.
```

**Esperado:**
- Task arquitetural multi-sistema complexa
- Model router DEVE detectar que Sonnet medium não dá conta
- Deve sugerir `Opus high + ultrathink` OU sugerir plano antes (SDD completo)
- Claude deve interromper antes de executar: "tá em Sonnet, isso pede Opus high + ultrathink, troca antes"

**O que observar:** Claude interrompe pra sugerir troca de modelo/plano, ou tenta executar direto em Sonnet?

**Critério PASS:** Claude interrompe e sugere upgrade de modelo OU propõe planejar antes.
**Critério FAIL:** Claude começa a responder sem sugerir upgrade.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 9 — Skill routing: "review" ambíguo (code vs UX vs prompt)

**Input:**
```
Revisa o checkout do meu app
```

**Esperado:**
- Trigger "revisa" + "checkout" é ambíguo (code review? UX review? security review?)
- Claude deve PERGUNTAR qual tipo de review antes de invocar skill
- skill-routing.md rule: "review é ambíguo" → perguntar "código, prompt, ou UX?"

**O que observar:** Claude pergunta o tipo de review ou assume um deles?

**Critério PASS:** Claude pergunta "código, UX, ou segurança?" antes de invocar skill.
**Critério FAIL:** Claude assume um tipo e executa (ex: vai direto pra trident ou ux-audit).

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 10 — Maestro quando não sabe qual skill

**Input:**
```
Tenho uma ideia de projeto novo, quero validar antes de construir. O que eu faço?
```

**Esperado:**
- Intent ambíguo (product-discovery? reference-finder? tech-lead-pm?)
- Claude deve invocar `maestro` pra rotear
- Maestro Phase 1 (Intent) → Phase 2 (Route) → propõe chain:
  - `product-discovery-prd` (validação de ideia)
  - OU `reference-finder` (buscar frameworks de validação tipo Lean Startup)
- Apresenta com gate de confirmação

**O que observar:** Claude invoca maestro ou pula direto pra uma skill?

**Critério PASS:** Maestro é invocado, skills são comparadas, proposta apresentada com confirmação.
**Critério FAIL:** Claude assume skill sem rotear.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 11 — reference-finder --solution-scout com campo preço

**Input:**
```
Tem MCP pronto pra integrar Google Analytics no Claude Code?
```

**Esperado:**
- Claude invoca `reference-finder --solution-scout "google analytics mcp"`
- 5 fontes paralelas buscadas
- Retorna tabela com **coluna Preço** (enhancement da letra E):
  `| Nome | Source | URL | Update | Match | Preço | Resumo |`
- Pra cada MCP encontrado, tenta achar preço (free/freemium/$X/?)
- Recomendação REUSE/EXTEND/BUILD

**O que observar:** Tabela tem coluna preço? Valores são realistas (não inventados)?

**Critério PASS:** Tabela estruturada com coluna preço preenchida (mesmo que seja `?`).
**Critério FAIL:** Responde genericamente sem tabela estruturada.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 12 — Context-tree query funcional

**Input:**
```
O que eu sei sobre skills e qualidade de arsenal? Usa a skill context-tree pra me responder.
```

**Esperado:**
- Claude invoca `context-tree --query <topic>`
- Busca em `~/.claude/context-tree/meta/`
- Encontra 9 entries: hook-physical-gate-lesson, r005-few-shot-critical-criterion, autoparody-anti-pattern, pipelines-3-agent-pattern, etc
- Retorna ranked por importance + connections

**O que observar:** Claude encontra os entries que eu criei hoje? Retorna ranked?

**Critério PASS:** Retorna 3+ entries do domain meta/ com seus scores.
**Critério FAIL:** Diz que não há knowledge armazenado OU responde sem query.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 13 — Filtro de alavancagem em task delegável

**Input:**
```
Preciso criar uma task no ClickUp pra configurar o repositório novo do cliente Barry Callebaut: clonar template, configurar SSH, criar initial commit, deploy na VPS
```

**Esperado:**
- Task operacional delegável (Hygor ou Jonas podem fazer)
- Filtro de alavancagem (CLAUDE.md L184-193) deve disparar
- Claude deve confrontar: "Isso é Patrick fazendo ou delega pro Jonas?"
- Se Patrick insistir, procede; senão, cria task com assignee Jonas

**O que observar:** Claude confronta ou executa direto?

**Critério PASS:** Claude sugere delegação antes de criar task como Patrick-assignee.
**Critério FAIL:** Cria task direto com Patrick como assignee sem questionar.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 14 — CLAUDE.md applied learning disparando

**Input:**
```
Preciso usar um Set node no n8n pra transformar um campo JSON string em object
```

**Esperado:**
- CLAUDE.md tem applied learning: "n8n Set node v3.4: campo object não auto-parseia JSON string, precisa JSON.parse()"
- Claude deve **aplicar o learning** na resposta
- Deve mencionar JSON.parse() explicitamente

**O que observar:** Claude menciona o gotcha do Set node v3.4?

**Critério PASS:** Menciona JSON.parse() ou o gotcha do v3.4 explicitamente.
**Critério FAIL:** Responde genericamente sem mencionar o learning.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 15 — Boundary copy vs comunicacao-clientes

**Input:**
```
Escreve uma mensagem pra mandar pro cliente Athié avisando que o deploy atrasou 2 dias
```

**Esperado:**
- Trigger ambíguo: `copy --mode whatsapp` (broadcast) ou `comunicacao-clientes` (1:1 operacional)?
- CLAUDE.md + boundary table: "mensagem pro cliente + contexto de gestão (atraso)" → **comunicacao-clientes**
- Claude deve usar framework ACPR (Abertura/Conteúdo/Proposta/Reforço)
- Deve aplicar Filtro de bad news (gate de confirmação)

**O que observar:** Claude usa comunicacao-clientes ou copy --mode whatsapp?

**Critério PASS:** Usa comunicacao-clientes, menciona ACPR, pede contexto adicional (tem plano de resolução?).
**Critério FAIL:** Usa copy --mode whatsapp ou escreve mensagem direto sem framework.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 16 — Hook NÃO dispara em arquivo normal

**Input:**
```
Cria um arquivo test.txt no Desktop com o conteúdo "hello world"
```

**Esperado:**
- Arquivo `test.txt` não é arquivo de instrução (CLAUDE.md, SKILL.md, etc)
- Hook PS1 dispara mas retorna `permissionDecision: allow` sem `additionalContext`
- Claude cria o arquivo direto sem mensagem ATENCAO

**O que observar:** Hook aparece ou Claude edita limpo?

**Critério PASS:** Criação limpa, sem mensagem ATENCAO.
**Critério FAIL:** Hook disparou com warning em arquivo normal (falso positivo).

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 17 — Sequência de ações triviais sem interromper

**Input:**
```
Me diz as horas
```

**Esperado:**
- Task trivial
- Model router NÃO dispara bloco
- Claude deve usar o web_fetch de https://www.horariodebrasilia.org/ (regra do CLAUDE.md seção "Horário local")
- Retorna hora atual direto

**O que observar:** Claude consulta horariodebrasilia.org ou estima?

**Critério PASS:** Faz web_fetch pra horariodebrasilia.org e retorna hora.
**Critério FAIL:** Estima hora sem consultar ou abre bloco de config.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 18 — Daily workflow (trigger implícito)

**Input:**
```
bom dia
```

**Esperado:**
- CLAUDE.md trigger: "bom dia" dispara Daily de abertura
- Claude invoca `clickup_filter_tasks` com filtro padrão (Patrick/Hygor/Jonas, due date, status ativo, sem tag reunião)
- Organiza por prioridade (🟢 > 🟡 > 🔴)
- Gera plano separado por Patrick/Hygor/Jonas
- Confronta se Patrick tem tasks delegáveis

**O que observar:** Claude puxa tasks do ClickUp automaticamente?

**Critério PASS:** Invoca filter_tasks, gera plano estruturado, confronta delegação.
**Critério FAIL:** Responde "bom dia" sem puxar tasks.

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 19 — Skill de domínio específica (seo vs ai-seo)

**Input:**
```
Quero meu blog aparecer nas respostas do ChatGPT quando alguém perguntar sobre n8n
```

**Esperado:**
- Trigger claro: "aparecer no ChatGPT" → ai-seo (não seo tradicional)
- skill-routing.md: "AI SEO/GEO/AEO" → ai-seo
- Claude deve invocar `ai-seo`, não `seo`
- Retorna estratégia GEO com Three Pillars (Structure/Authority/Presence)

**O que observar:** Claude diferencia ai-seo de seo corretamente?

**Critério PASS:** Invoca ai-seo, menciona Three Pillars ou Princeton GEO research.
**Critério FAIL:** Usa seo tradicional (keyword research, backlinks).

**Resposta real:**
```
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Teste 20 — Loop detection (Sonnet falhou 2x na mesma coisa)

**Input (seguir passo a passo):**
```
Passo 1: "Debug esse erro: TypeError: Cannot read property 'map' of undefined em src/components/Dashboard.tsx linha 42"

[Claude vai tentar resolver. Provavelmente falha ou dá solução genérica.]

Passo 2: "Não resolveu, ainda dá o mesmo erro"

[Claude tenta de novo. Segunda falha.]

Passo 3: "Continua dando erro, mesma coisa"
```

**Esperado no Passo 3:**
- Model router detecta loop (falhou 2x na mesma coisa)
- Claude deve ESCALAR: "Loop detectado, escala pra Opus + ultrathink antes da 3ª tentativa"
- Não deve tentar debug cego uma 3ª vez

**O que observar:** Claude interrompe pra escalar ou tenta 3ª vez?

**Critério PASS:** Claude sugere trocar pra Opus + ultrathink no Passo 3.
**Critério FAIL:** Tenta debug genérico uma 3ª vez sem reconhecer o loop.

**Resposta real:**
```
Passo 1:

Passo 2:

Passo 3:
```

**Análise:** ⬜ PASS ⬜ FAIL ⬜ PARCIAL

---

## Resumo (preencher depois de rodar todos)

| # | Teste | Resultado |
|---|-------|-----------|
| 1 | Hook dispara em SKILL.md | ⬜ |
| 2 | prompt-engineer --validate CLAUDE.md | ⬜ |
| 3 | IL-7 Step 0 bloqueia skill nova | ⬜ |
| 4 | IL-8 problema novo | ⬜ |
| 5 | IL-3 trident local vs Anthropic | ⬜ |
| 6 | IL-3 skill-builder local | ⬜ |
| 7 | Router silencioso (task trivial) | ⬜ |
| 8 | Router dispara (config errada) | ⬜ |
| 9 | "review" ambíguo pergunta tipo | ⬜ |
| 10 | Maestro pra intent ambíguo | ⬜ |
| 11 | Solution-scout com preço | ⬜ |
| 12 | Context-tree query | ⬜ |
| 13 | Filtro alavancagem | ⬜ |
| 14 | Applied learning disparando | ⬜ |
| 15 | Boundary copy vs comunicacao | ⬜ |
| 16 | Hook NÃO dispara arquivo normal | ⬜ |
| 17 | Horário local via web_fetch | ⬜ |
| 18 | Daily workflow "bom dia" | ⬜ |
| 19 | ai-seo vs seo | ⬜ |
| 20 | Loop detection | ⬜ |

**Total:** __/20 PASS

---

## Como me mandar o resultado

Depois de rodar todos (ou os que conseguir), cola o arquivo completo numa conversa comigo e eu analiso:
- Taxa de acerto geral
- Padrões de falha (se houver)
- Se IL-8 tá funcionando
- Se IL-3 tá priorizando local
- Gaps descobertos que viram entries em `gaps/` pra evoluir o sistema

**Não precisa rodar os 20 de uma vez.** Pode fazer em lotes de 5-10 por dia se quiser.
