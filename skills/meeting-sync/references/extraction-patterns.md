# extraction-patterns

Regras de classificação de itens de transcrição + algoritmo de match com ClickUp.

## Classificação de itens

### NEW_TASK — ação nova que não existe no ClickUp

**Patterns de linguagem:**
- "precisa criar", "precisa ter", "faz isso", "monta isso", "implementa"
- "vou precisar de", "a gente precisa", "tem que criar"
- Verbo ação + dono + objeto concreto

**Exemplos reais (reunião 12/04):**
- "Hygor, tu ainda precisa resolver o campo do PGR né" → NEW_TASK (campo PGR não extraindo)
- "precisa ter uma validação cruzada do CTPS com o NR" → NEW_TASK

### UPDATE — mudança de status/progresso em task existente

**Patterns de linguagem:**
- "tá pronta", "já foi feito", "terminei", "concluímos"
- "tô fazendo", "tá em andamento", "semana que vem entrego"
- "travou em X", "depende do Y", "bloqueou porque"
- "atualizei", "mudei", "ajustei"

**Exemplos reais (reunião 12/04):**
- "Hygor já arrumou o campo do PGR" → UPDATE status para concluído (`86e0vya8b`)
- "o blog automático do Júlio tá parado, retomou" → UPDATE status
- "a fila SEO tá travada por credencial do Gemini" → UPDATE + BLOCKER

### DECISION — decisão tomada, registrar sem criar task

**Patterns de linguagem:**
- "decidimos que", "ficou definido que", "vai ser assim"
- "a gente vai usar X", "escolhemos Y", "mudamos pra Z"
- "não vai mais ser feito", "cancelamos"

**Exemplos reais (reunião 12/04):**
- "vamos usar PGR pra testar a extração de validade" → DECISION
- "assinatura digital vai ser Ponto.GOV" → DECISION

### DECISION também pode gerar uma task de acompanhamento

Se DECISION implica ação futura com dono e prazo identificável → criar também NEW_TASK.

### INFO — informação contextual, registrar sem criar task

**Patterns de linguagem:**
- Disponibilidade de pessoa: "Hygor vai ficar indisponível semana 16-22/04"
- Contexto de prazo: "reunião com Barry é amanhã"
- Status de cliente: "Rafael disse que o módulo X vai sair em maio"

**Exemplos reais (reunião 12/04):**
- "Hygor vai ficar indisponível de 16 a 22/04" → INFO (registrar, não criar task)
- "reunião com Barry é 14/04" → INFO

### BLOCKER — impedimento em task existente

**Patterns de linguagem:**
- "travou porque", "não consegue avançar sem", "depende de X"
- "bloqueou em", "tá esperando", "só dá quando"

**Exemplos reais (reunião 12/04):**
- "a fila SEO não roda porque a credencial do Gemini tá errada" → BLOCKER na task de fila SEO

### NOT_TASK — operacional puro, descartar com motivo

**O que é NOT_TASK:**
- Timesheet / controle de horas solto: "Hygor, tu botou 26h no timesheet?"
- Mensagem avulsa no WhatsApp: "manda pra ele no WhatsApp"
- Conversa de agenda sem ação concreta: "a gente se fala semana que vem"
- Comentário opinativo sem ação: "acho que ficou bom"
- Pergunta retórica: "entendeu o que eu quis dizer?"

**Exemplos reais (reunião 12/04):**
- "Supply Map tem relatório de 7h" → NOT_TASK (métrica de tempo, não ação)
- "migrar fila Gemini pra..." (contexto fragmentado, sem dono/prazo) → NOT_TASK até confirmar
- "timesheet 26h" → NOT_TASK (controle de horas)

---

## Algoritmo de match com ClickUp

### Tokenização

1. Lowercase nos dois lados (item da transcrição + nome+descrição da task)
2. Remove stop words PT-BR: `de, da, do, e, ou, para, pra, com, em, na, no, a, o, as, os, um, uma, que, se, por, já, mais, só, foi, vai, tá, está, ser, ter, fazer`
3. Stemming simples: remove plurais (`-s`, `-es`) e gerúndios (`-ndo`)
4. Quebra em palavras únicas

### Score de match

| Nível | Critério | Ação |
|-------|----------|------|
| HIGH (>80%) | 3+ keywords match + mesmo folder/list | Propor UPDATE |
| MEDIUM (50-80%) | 2 keywords match + tema próximo | Apresentar opções: UPDATE ou NEW |
| LOW (<50%) | <2 keywords ou folder errado | Propor NEW_TASK |

### Regra anti-false-match (Fix C)

Mesmo com score HIGH, rebaixar pra LOW quando:

- **Folder/list divergente do contexto:** task achada está em folder diferente do cliente em discussão (ex: transcrição fala de Artemis Comercial mas task candidate está em Artemis Marketing).
- **Stakeholder de domínio diferente:** task foi pedida por stakeholder diferente (ex: task `Lead Scoring` existente é demanda do Hélio/Marketing; na reunião o Enzo/Comercial pede `Lead Scoring` com escopo distinto). Nome igual + contexto diferente = NEW_TASK, não UPDATE.
- **Escopo técnico incompatível:** task achada tem descrição técnica oposta (ex: input site+email → relatório SEO ≠ scoring de conversa EVO no Kommo).

**Exemplo real (14/04 Enzo):** `86e0kwjga` "Leadscoring: Criar análise SEO automática — input site + email" apareceu como candidate pro lead scoring que o Enzo pediu. Aparentemente nome-match HIGH. MAS:
- Folder: ambos em Comercial — convergente
- Stakeholder: `86e0kwjga` foi aberta a pedido do Hélio/Marketing; pedido do Enzo/Comercial é distinto
- Escopo técnico: SEO automático (URL → relatório) ≠ scoring de conversa (EVO → tag+notas Kommo)

Conclusão correta: LOW match → NEW_TASK separada. NÃO atualizar `86e0kwjga`.

### Padrão "item já buildado fora do ClickUp" (Fix D)

Quando alguém menciona na reunião que algo "já foi feito" mas busca no ClickUp não acha task correspondente:

1. **Buscar com termos adjacentes:** se "contador de leads" não acha, tentar "contador", "lead count", "daily count", "monitor", nome do cliente + funcionalidade
2. **Buscar em lists vizinhas:** automação de um cliente pode estar em `Operação` ou `Comercial` — tentar ambas
3. **Se ainda não acha:** criar task de `[CONFIG]` ou `[REGISTRO]` pra ter rastreabilidade. Marcar no título: "já implementado — registrando pra histórico"
4. **Registrar decisões técnicas que a reunião capturou sobre o item:** horário de envio, grupo de destino, formato

**Exemplo real (14/04 Enzo):** Patrick falou "ele [Hygor] criou um contador de lead que foi inserido no Kommo por dia". Buscar "contador" em Artemis Comercial → 0 matches. Decisão da reunião: enviar às 7h com total do dia anterior, mandar pro Efesto. Ação correta: criar `[CONFIG] Configurar contador de leads Kommo → envio 7h` pra registrar a decisão, mesmo que o código já exista.

### Regra de ouro

**Sempre** `clickup_get_task` com `detail_level: detailed` antes de decidir match. Nome curto da task engana, descrição salva. Exemplos de nomes curtos que são enganosos:
- "Arrumar campo" → pode ser de qualquer cliente
- "Validação" → pode ser NR, CTPS, ou outra coisa
- "Blog automático" → pode ser Artemis SEO ou outro cliente

### Erro crítico a evitar

`dateUpdated` = quando a task foi modificada pela última vez. `date_created` = quando foi criada. **NUNCA** dizer que uma task "foi criada hoje" baseado em `dateUpdated`.

---

## Phase 2 — fallback strategy (Fix B)

O MCP `clickup_search` tem flakiness conhecido: pode retornar 0 resultados em lists que claramente têm matches, ou devolver erro de server intermitente. Fallback obrigatório:

### Ordem de tentativas

1. **Primeiro try:** `clickup_search` com `keywords: "<termo>"`, filtro `location.categories: [<folder_id>]`, `sort: [{field: updated_at, direction: desc}]`
2. **Se retornar 0 em folder que deveria ter matches OU erro de server** → NÃO desistir. Ir pro próximo passo.
3. **Fallback confiável:** `clickup_filter_tasks` com:
   - `list_ids: [<id_esperado_da_list>]`
   - `order_by: "updated"`
   - `reverse: true`
   - `include_closed: true`
4. Iterar nos resultados paginados se houver cursor.
5. **Segundo search** só se você precisa cross-list no space inteiro — mas aceite que search pode ser inútil e vá direto pros filter_tasks per-list.

### Quando usar cada um

- **`clickup_search`:** melhor pra buscas por palavra-chave cross-workspace sem escopo claro
- **`clickup_filter_tasks`:** melhor pra listagens escopadas a lists/folders específicos (uso padrão quando você sabe onde a task deveria estar)

### Anti-pattern

Assumir que task não existe porque search retornou 0. Isso causou o furo da execução Sonnet 14/04 — várias tasks em Artemis Comercial não apareceram no search mas estavam lá (apareceram no filter_tasks). Sempre confirmar com fallback antes de classificar como NEW_TASK.