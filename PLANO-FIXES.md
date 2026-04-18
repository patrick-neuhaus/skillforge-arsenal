# Plano — Fixes nas skills baseado no teste de triggering

**Base:** [ANALISE-RESULTADOS.md](ANALISE-RESULTADOS.md) — 39% de acerto, 20 NENHUMA + 4 ERRADA + 1 MAESTRO.
**Estratégia:** 3 waves com teste entre elas (approved). Re-teste só das que foram corrigidas (sem loop).
**Ambiente de edit:** skillforge-arsenal/ (onde os SKILL.md moram).
**Ambiente de teste:** decidido na Wave 0 abaixo.

---

## Wave 0 — Sanity check do ambiente (fazer PRIMEIRO)

**Por quê:** o teste das 41 foi rodado em skillforge-arsenal/ (CLAUDE.md enxuto). Uso real do Patrick é majoritariamente em Github/ (CLAUDE.md com equipe, ClickUp, agenda, filtro de alavancagem, confrontação — muito mais contexto competindo). **Antes de gastar esforço nos 20+ fixes, preciso confirmar se o problema é das descriptions ou se tem componente de ambiente.**

**Ação:**
1. Patrick abre sessão nova Sonnet medium na pasta `C:\Users\Patrick Neuhaus\Documents\Github\`
2. Cola 3 inputs seletos (que falharam em skillforge mas representam diferentes root causes):
   - Input 5: `"junta esses 3 PDFs num só pra eu mandar pro cliente"` (desc-keyword-miss simples — pdf)
   - Input 31: `"quero adicionar um sistema de favoritos no app, planeja antes de sair codando"` (context-hijack com plan mode — sdd)
   - Input 38: `"quero melhorar a skill do copy, ela não tá acionando direito"` (meta-bug — geo-optimizer)
3. Patrick cola os 3 resultados num arquivo `RESULTADO-WAVE0.md` (formato vertical igual ao RESULTADO-TESTES.md)

**Decisão da Wave 0:**

| Resultado em Github/ | Interpretação | Próximo passo |
|---|---|---|
| Igual ou pior que skillforge (3 falham) | Problema é description + possivelmente CLAUDE.md do Github | Wave A + considerar slim-down CLAUDE.md depois |
| Melhor (1-2 passam) | CLAUDE.md do Github ajuda o triggering | Wave A direto, CLAUDE.md tá OK |
| Todos passam | Problema era exclusivo de skillforge | Abortar plano, investigar CLAUDE.md do skillforge como causa |

**Esforço:** 15min do Patrick pra rodar.

---

## Wave A — Fix P0 (desbloqueia o resto)

**Escopo:** 3 mudanças que são pré-requisito pras outras 20. São as que têm maior alavanca.

### A1. Fix `geo-optimizer` (Input 38 — meta-bug)

**Por quê primeiro:** geo-optimizer é a ferramenta que você vai usar pra consertar as outras 19 skills da Wave B. Se ela mesma não dispara, cada fix vira manual.

**Mudança:** edit em [skills/geo-optimizer/SKILL.md](skills/geo-optimizer/SKILL.md) frontmatter `description`.

Adicionar triggers explícitos:
- "skill não tá acionando"
- "não ativa direito"
- "melhorar triggering da skill X"
- "skill não invoca"
- "quero melhorar a skill X"

Adicionar regra de priorização na description: "meta sobre skill (melhorar/debug) > skill em si (usar)".

**Tipo de edit:** description only → **IL-1** (prompt-engineer --validate --type system-prompt).

### A2. Fix `sdd` (Input 31 — plan mode conflict)

**Por quê:** "planeja antes de codar" é o trigger natural pra sdd, mas caía em EnterPlanMode nativo. Sem fix, sdd nunca vai disparar em uso real.

**Mudança:** edit em [skills/sdd/SKILL.md](skills/sdd/SKILL.md) description.

Adicionar:
- "planeja antes de codar"
- "antes de sair codando"
- "anti-vibecoding"
- "spec antes de implementar"

Anti-trigger: "NÃO confundir com `plan mode` nativo do Claude Code — este é Spec Driven Development".

**Tipo:** description only → **IL-1**.

### A3. Expandir `~/.claude/rules/skill-routing.md`

**Mudança:** adicionar 25 linhas na tabela de auto-triggers (palavra → skill obrigatória). Lista completa em P1 do [ANALISE-RESULTADOS.md](ANALISE-RESULTADOS.md).

**Tipo:** arquivo cai no pattern `iron|routing|trigger` do hook → **IL-1** com type `iron-laws`.

**Candidata a IL nova:** "Patrick reporta falha de skill X → force `geo-optimizer --debug <skill>`". Adicionar ao `iron-laws.md`. Destrava P0-3.

### Teste Wave A

Re-testar os 3 inputs em sessão Sonnet medium nova (mesmo ambiente definido na Wave 0):
- Input 38 (geo-optimizer)
- Input 31 (sdd)
- Input 5 (pdf — pra validar se expansão do skill-routing.md funciona sem precisar mexer na SKILL.md do pdf ainda)

**Critério de sucesso:** 3/3 passam (OK ou OK-PARCIAL).

**Se passar:** segue pra Wave B.
**Se falhar algum:** diagnosticar. Não avança pra Wave B até entender — pode ser bug em maior camada (hook, CLAUDE.md, indexação).

---

## Wave B — Fix por skill (em lote)

**Escopo:** 19 skills restantes com falha. Organizadas por tipo de edit.

### B1. Edits só de description (IL-1, system-prompt) — 15 skills

Rodar `geo-optimizer --debug <skill>` em sequência pra gerar patches de description. Cada um aplica IL-1 individualmente.

| Skill | Input | Triggers a adicionar (resumo) |
|---|---|---|
| pdf | 5 | "juntar/merge/combina PDFs" |
| n8n-architect | 6 | "workflow quebrando", "n8n bug" |
| docx | 8 | "faz doc Word", "proposta Word" |
| product-discovery-prd | 9 | "app novo + escopo", "discovery" |
| component-architect | 11 | "quebrar componente", "componente grande/gigante" |
| supabase-db-architect | 14 | "como tá meu banco", "policies certas" + nota "mesmo com MCP direto, passa pela skill" |
| tech-lead-pm | 16 | "travado N dias", "como lido com dev parado" |
| context-guardian | 19 | "antes de /clear", "salva estado sessão" |
| prompt-engineer | 20 | "instruções pro Claude", "CLAUDE.md do projeto X" |
| launch-strategy | 22 | "go-to-market", "lançamento de produto" |
| ui-design-system | 24 | "cores/fontes/espaçamento padronizados", "paleta" |
| sales-enablement | 28 | "material de vendas", "reunião com prospect" |
| architecture-guard | 29 | "lógica no front/backend", "separação de camadas" |
| product-marketing-context | 30 | triggers PT-BR: "o que é X, pra quem é, diferencial" |
| react-patterns | 32 | "useEffect", "renderizando demais", "re-render" |
| context-tree | 34 | "catalogar aprendizados", "organizar conhecimento" |
| lovable-router | 36 | "mudar direto ou mandar prompt Lovable" |
| maestro | 37 | "não sei por onde começar", "qual ferramenta usar" |
| meeting-sync | 41 | "transcrição daily→tasks", "cruza com ClickUp" |

**Método:** 1 sessão pega 3-5 skills em batch (ler description atual + rodar geo-optimizer + aplicar fix + marker IL-1 + Write). 4-5 sessões cobrem as 19.

### B2. Edits estruturais (IL-1 + IL-4) — 4 skills

Essas têm mudanças de workflow, não só description. Rodam IL-1 + IL-4 (skill-builder --validate).

| Skill | Input | Mudança estrutural |
|---|---|---|
| trident | 3 | Adicionar fallback Phase 1: "se arquivo não encontrado → pedir paste inline, não bloquear" |
| code-dedup-scanner | 25 | Adicionar scan proativo Phase 1 (glob `*.tsx`, `*.ts`) antes de pedir desambiguação |
| skill-builder | 39 | Step 0 deve disparar `AskUserQuestion` pelas 8 perguntas (ou batch) e aplicar gate baseado em respostas, não só listar |
| security-audit | 40 | Description + workflow: trigger pela intenção, não presença de código. Phase 1 coleta artefato. |

### B3. Edits cross-skill (boundaries + collisions) — 2 edits

| Edit | Skills afetadas | Input |
|---|---|---|
| Boundary note `reference-finder` ↔ `free-tool-strategy` | ambas | 21 (confusão semântica) |
| Anti-trigger em `reference-finder`: "NÃO usar quando intenção é CONSTRUIR ferramenta própria" | reference-finder | 21 |

### Teste Wave B

Re-testar SÓ as 24 inputs que foram endereçados nesta wave (5+6+8+9+11+14+16+19+20+22+24+28+29+30+32+34+36+37+41+3+25+39+40+21 = 24).

**Ambiente:** igual Wave 0 (skillforge ou Github, conforme decisão).

**Critério de sucesso:** 20+/24 passam. Abaixo disso, investigar antes de continuar.

**Se passar:** Wave C.
**Se falhar:** fix manual individual nas que falharam. Sem loop infinito — máximo 1 retry por skill (tu sugeriu "quqalquer uma que nao se encaixe nisso, a gente testa novamente somente mais uma vez, pq dai tbm nao precisa ficar em loop").

---

## Wave C — Consolidação final

### C1. Verificação

Rodar `python test-rubric-loading.py` (existe no repo) pra validar que as 4 rubrics do prompt-engineer carregam — sanidade básica.

### C2. Rezipar skills modificadas

Todas as skills editadas precisam de re-zip pra `dist/` (pra upload em anthropic-skills/Claude.ai):

```
python zip-skills.py geo-optimizer sdd pdf n8n-architect docx product-discovery-prd component-architect supabase-db-architect tech-lead-pm context-guardian prompt-engineer launch-strategy ui-design-system sales-enablement architecture-guard product-marketing-context react-patterns context-tree lovable-router maestro meeting-sync trident code-dedup-scanner skill-builder security-audit reference-finder free-tool-strategy
```

### C3. Documento de fechamento

Criar [FIXES-APLICADOS.md](skillforge-arsenal/FIXES-APLICADOS.md) com:
- Lista das skills editadas e que triggers foram adicionados
- Antes/depois de taxa de acerto (39% → ?)
- Skills que ainda falham após retry (se houver) — candidatas a redesign mais profundo
- Lições aprendidas pra próximo teste

### C4. Commit

Um commit por wave:
- `fix(skills): wave-A p0 fixes — geo-optimizer + sdd + skill-routing expansion`
- `fix(skills): wave-B batch fixes — 24 skills triggers + structural`
- `docs: wave-C test results and wrap-up`

**Não pushar** sem tu aprovar o diff.

---

## IL-compliance resumida

- **IL-1** (prompt-engineer --validate --type): aplica em **todas** as edits de description + `skill-routing.md` + `iron-laws.md`. ~28 markers de validação.
- **IL-4** (skill-builder --validate): aplica **só em B2** (4 skills com mudança estrutural).
- **IL-2** (trident, não simplify): não aplica — não tô fazendo code review, tô fazendo fixes direcionados.
- **IL-5** (maestro): não aplica — tu já aprovou a skill-chain aqui (geo-optimizer pra cada skill).
- **IL-7** (skill-builder Step 0 pra skill nova): não aplica — não tô criando skill nova.
- **IL-8** (reference-finder --solution-scout): não aplica — não tô propondo solução nova.

---

## Orçamento estimado

| Wave | Trabalho | Quem executa |
|---|---|---|
| 0 | 15min re-teste 3 inputs | Patrick (manual, sessão Sonnet em Github/) |
| A | 2 edits SKILL.md + 1 edit skill-routing.md + IL-1 markers | Claude Opus (1 sessão) |
| A teste | 15min 3 inputs | Patrick (manual) |
| B1 | 19 edits description (em batches de 3-5) | Claude Opus (4-5 sessões) |
| B2 | 4 edits estruturais | Claude Opus (1-2 sessões) |
| B3 | 2 boundary edits | Claude Opus (1 sessão) |
| B teste | ~1h 24 inputs | Patrick (manual) |
| C | Verify + rezip + docs | Claude Opus (1 sessão) |

**Total:** ~10 sessões Claude + ~1h30 de teste manual do Patrick.

---

## Perguntas ainda em aberto

1. **Ambiente de teste pós-Wave 0:** skillforge/ ou Github/? (decidido pelo resultado da Wave 0)
2. **CLAUDE.md do Github precisa slim-down?** (só vira agenda se Wave 0 mostrar que ambiente é o problema — aí vira Wave D ou volta pro escopo)
3. **Tu quer que eu rode tudo sozinho ou quer revisar cada wave antes de avançar?**
   - Default: reviso Wave A contigo antes de Wave B (Wave A é mais crítica, 3 fixes em áreas sensíveis).
4. **Skills `anthropic-skills:*` prefixadas tiveram taxa de acerto maior.** Vale testar se prefixar localmente ajuda? Fora do escopo atual, mas finding interessante.

---

## Resposta direta às tuas perguntas

**"sempre mexo em projeto usando a pasta skillforge?"**
Não. Skillforge/ só pra editar SKILL.md. Github/ é melhor pro dia a dia (acessa todas as pastas). Fix em skillforge vale pro uso em Github automaticamente.

**"melhorar o trigger seria só nas skills?"**
Principalmente nas SKILL.md. Secundariamente em `skill-routing.md`. Terceiro em CLAUDE.md.

**"meu claude.md do github parece que ta mt grande e ele ta perdendo informações, ou não?"**
~200 linhas, 8 seções. Não é absurdo, mas tem bastante competindo pela atenção (papel, equipe, ClickUp detalhado, agenda, filtro, confrontação, decisões, learnings). Wave 0 vai me dizer se isso interfere.

**"e o claude.md do skillforge ta melhor?"**
Sim, é minimal (30 linhas focadas no próprio repo). Mas **foi onde o teste rodou e deu 39%**, então a hipótese "CLAUDE.md grande = ruim pro triggering" não é isolável — só Wave 0 confirma.
