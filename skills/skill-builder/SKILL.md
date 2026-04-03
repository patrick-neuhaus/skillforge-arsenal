---
name: skill-builder
description: "Skill para criar, modificar e otimizar skills do Claude. Use esta skill SEMPRE que o usuário mencionar: criar skill, nova skill, melhorar skill, skill builder, 'transforma isso numa skill', 'quero automatizar esse processo', 'faz uma skill pra isso', editar skill, atualizar skill, 'a skill tá ruim', 'a skill não tá funcionando', ou qualquer variação que envolva criar ou melhorar instruções persistentes pro Claude. Também use quando o usuário pedir pra 'capturar esse workflow', 'salvar esse processo', ou quando um padrão de trabalho se repetir 3+ vezes na conversa e poderia virar skill. Se o usuário disser 'roda os evals', 'testa a skill', ou 'otimiza a description', USE esta skill. Na dúvida entre skill e prompt, pergunte: 'Você quer instruções persistentes pro Claude (skill) ou um prompt pra usar em outro lugar?'"
---

# Skill Builder

## Visão geral

Esta skill conduz o processo completo de criar, testar e otimizar skills pro Claude. Cobre desde o discovery inicial (entender O QUE a skill deve fazer) até a validação final (garantir que ela FUNCIONA).

Uma skill é um conjunto de instruções persistentes que o Claude consulta quando relevante. Diferente de um prompt avulso, a skill fica disponível pra sempre e é acionada automaticamente pela description. Isso significa que a qualidade da skill tem impacto multiplicador — uma skill boa usada 1000 vezes gera 1000x mais valor que um prompt usado uma vez.

## Princípios

1. **Discovery antes de escrita.** Nunca comece a escrever uma skill sem entender profundamente o domínio, o problema, e o output esperado. A tentação é pular direto pro código — resista.
2. **Referências antes de achismo.** Se o domínio da skill tem frameworks, metodologias ou práticas consagradas, pesquise ANTES de escrever. Uma skill de UX sem Nielsen é uma skill fraca.
3. **Context engineering > prompt engineering.** Skill não é prompt. É curadoria de contexto — decidir O QUE o modelo precisa ver, QUANDO, e em QUAL formato pra gerar o melhor output possível. Cada token compete por atenção; informação irrelevante dilui qualidade.
4. **Explique o porquê, não só o quê.** Claude 4.x segue instruções literalmente. Explicar POR QUE uma regra existe gera melhor generalização do que repetir "SEMPRE" e "NUNCA" em caps lock. Linguagem agressiva ("CRITICAL: You MUST") era necessária em modelos antigos — nos atuais, instrução clara e direta funciona melhor.
5. **Generalize, não overfitte.** A skill vai ser usada milhares de vezes com inputs diferentes. Se ela só funciona pros 3 exemplos de teste, é inútil. Prefira princípios a regras rígidas.
6. **Teste antes de confiar.** Skill que não foi testada é rascunho, não skill. Mínimo de 10 eval cases por skill.

## Fluxo de trabalho

O processo tem 7 fases. Nem toda skill precisa de todas — skills simples podem pular fases, skills complexas podem iterar várias vezes. Use bom senso.

```
Fase 1: Discovery → Fase 2: Pesquisa → Fase 3: Escrita → Fase 4: Teste
                                                              ↓
                    Fase 7: Empacotamento ← Fase 6: Description ← Fase 5: Validação
                                                              ↑
                                                    (iterar se necessário)
```

---

### Fase 1: Discovery — Entender o que a skill deve fazer

O objetivo é extrair da cabeça do usuário tudo que ele sabe sobre o domínio e o processo que quer capturar. NÃO comece a escrever sem completar esta fase.

**Detecção de input — o que o usuário já traz:**

Antes das perguntas, identifique o que já existe:
- **Conversa anterior** — Se o usuário disse "transforma isso numa skill" durante uma conversa, EXTRAIA do histórico: ferramentas usadas, sequência de passos, correções feitas, formato de input/output. Apresente o que extraiu e peça confirmação.
- **Skill existente** — Se é melhoria de skill existente, leia a skill INTEIRA primeiro. Identifique o que funciona e o que não funciona antes de perguntar.
- **Nada** — Se é skill do zero, siga o fluxo de perguntas abaixo.

**Bloco 1 — O problema (não a solução):**

O usuário vai chegar falando da SOLUÇÃO ("quero uma skill que faz X"). Cave até o PROBLEMA.

- O que essa skill deve fazer? (deixe falar livremente)
- Qual problema isso resolve? O que acontece HOJE sem essa skill?
- Com que frequência esse problema aparece? (diário, semanal, por projeto?)
- Quem vai acionar essa skill? (o próprio usuário, equipe, qualquer pessoa?)

**Bloco 2 — Input e output:**
- Qual o input típico? (texto, arquivo, código, pergunta aberta?)
- Qual o output esperado? (arquivo, texto estruturado, decisão, código?)
- Tem formato específico de output? (template, markdown, JSON, arquivo .docx/.md?)
- Me dá um exemplo real: "Eu digo X e espero que o Claude faça Y"

**Bloco 3 — Processo e decisões:**
- Quais são os PASSOS que você segue hoje pra fazer isso manualmente?
- Tem decisões no meio? (se X, faz A; se Y, faz B)
- Tem edge cases que já deram problema?
- Tem algo que o Claude faz errado quando você tenta sem skill?

**Bloco 4 — Escopo e limites:**
- O que essa skill NÃO deve fazer? (tão importante quanto o que deve)
- Tem skills existentes que se sobrepõem? Como diferencia?
- Quer que a skill ENSINE o processo ou só EXECUTE?

**Bloco 5 — Padrão arquitetural:**

Identifique qual padrão agentic a skill precisa. Consulte `references/agentic-patterns.md` pra decidir:
- **Processo linear** — a maioria das skills (discovery → análise → output)
- **Pipeline multi-agente** — quando precisa de agentes especializados (ex: Repo Review com 3 agentes)
- **Fan-Out/Gather** — quando tarefas podem rodar em paralelo e um sintetizador consolida
- **Reflection** — quando o output precisa de auto-avaliação antes de entregar

**Bloco 6 — Testes (já plante a semente):**
- Me dá 2-3 situações reais em que você usaria essa skill
- Como você saberia se o output tá bom ou ruim? (critérios de sucesso)

Se o usuário for vago, use a técnica da **Declaração da Skill**: "Me ajuda a preencher: Quando [situação], o Claude deve [ação] pra que [resultado], seguindo [restrições]."

---

### Fase 2: Pesquisa de domínio — Fundamentar antes de escrever

ANTES de escrever a skill, pesquise o domínio. Isso separa skills medíocres de skills excelentes.

**Quando pesquisar (sempre que o domínio tiver corpo de conhecimento):**
- UX/UI → Nielsen, Norman, Yablonski, HEART, WCAG 2.2
- Gestão de produto → Teresa Torres, Fitzpatrick, Shape Up
- Liderança → Fournier, Kim Scott, Radical Candor
- Segurança → OWASP Top 10 Web + OWASP Top 10 LLM
- Vendas → SPIN Selling, Challenger Sale
- Qualquer domínio → busque as obras seminais e frameworks consagrados

**Quando NÃO pesquisar:**
- Skills puramente operacionais (ex: "converte CSV pra XLSX")
- Skills de integração técnica onde a doc oficial é a única fonte
- Skills triviais de formatação/template

**Como pesquisar:**

Use web search em camadas (mesmo padrão da skill Reference Finder):
1. **Obras seminais:** "[domínio] best books framework seminal"
2. **Frameworks práticos:** "[domínio] methodology practical steps"
3. **Pessoas-chave:** "[domínio] expert thought leader"
4. **Evolução recente:** "[domínio] 2025 2026 latest"

**O que fazer com as referências:**
- Incorpore os frameworks e princípios NA skill (não como citação, como instrução)
- Se a referência é rica, crie um arquivo em `references/` com o resumo curado
- Registre as fontes na seção de metadata da skill

Exemplo: A skill de UX Audit incorporou as 10 heurísticas de Nielsen não como "consulte Nielsen" mas como checklist operacional que o Claude aplica. Isso é o correto — transformar referência em instrução.

---

### Fase 3: Escrita — Construir a skill

Agora sim, escreva. Consulte `references/principios-escrita.md` pra os princípios detalhados de como escrever boas skills. Aqui vai o resumo:

#### Anatomia de uma skill

```
skill-name/
├── SKILL.md (obrigatório)
│   ├── Frontmatter YAML (name, description)
│   └── Instruções em Markdown
└── Recursos opcionais
    ├── references/  — docs carregados sob demanda
    ├── scripts/     — código executável pra tarefas repetitivas
    └── assets/      — arquivos usados no output (templates, fontes)
```

#### Progressive disclosure (3 níveis)

1. **Metadata** (name + description) — Sempre no contexto (~100 palavras). É o que decide se a skill é acionada.
2. **SKILL.md body** — Carregado quando a skill aciona (~500 linhas ideal, máximo absoluto ~700).
3. **Recursos bundled** — Carregados sob demanda. Sem limite, mas cada arquivo deve ser referenciado claramente no SKILL.md com instrução de QUANDO ler.

Se o SKILL.md tá passando de 500 linhas, mova conteúdo pra references/ com ponteiros claros.

#### Formato de output: AGENTS.md

Quando a skill gera instruções pra ferramentas de código AI (Lovable, Cursor, Claude Code, Copilot, Codex), considere gerar o output no formato **AGENTS.md** — o padrão universal adotado por 60K+ repos no GitHub e mantido pela Linux Foundation. AGENTS.md é lido nativamente por Claude Code, Cursor, Copilot, Codex CLI, Jules (Google), e Gemini.

Regras pra AGENTS.md como output:
- Limite de ~300 linhas (cada instrução compete por atenção no system prompt da tool)
- Foque no que a AI **erraria SEM** o arquivo — não repita o que linters fazem
- Inclua: contexto (1 linha), comandos exatos de build/test, versões do stack, estrutura do projeto
- NÃO inclua: code style (linters), instruções excessivas, comportamento óbvio

#### Template do SKILL.md

```markdown
---
name: nome-da-skill
description: "[descrição pushy — veja seção de Description Optimization]"
---

# Nome da Skill

## Visão geral
[2-3 parágrafos: o que faz, pra que serve, qual problema resolve]

## Princípios
[3-6 princípios que guiam TODO o comportamento da skill. Explique o porquê de cada um.]

## Fluxo de trabalho
[O processo passo a passo. Organize em fases/blocos se for complexo.]

### Fase 1: [Nome]
[Instruções claras, imperativas]

### Fase 2: [Nome]
...

## Regras do output
[Formato, linguagem, tom, restrições do output final]

## Integração com outras skills
[Quando e como combina com outras skills existentes]

## Quando NÃO usar esta skill
[Lista clara de situações em que a skill NÃO se aplica]
```

#### Regras de escrita (resumo — detalhes em references/principios-escrita.md)

1. **Imperativo.** "Faça X" em vez de "Você deveria fazer X".
2. **Explique o porquê.** Cada regra importante deve ter o motivo. "Sempre inclua seção 'Fora do escopo' — sem ela, o LLM pode inventar features."
3. **Exemplos > instruções.** Um exemplo de input/output vale mais que 10 linhas de explicação.
4. **Específico > genérico.** "Use shadcn/ui" é melhor que "Use uma biblioteca moderna de componentes".
5. **Seções opcionais > seções vazias.** Inclua apenas seções que têm conteúdo real. Template com [placeholder] é inútil.
6. **Português brasileiro** pra toda a skill, exceto termos técnicos universais.
7. **Não repita o system prompt.** Instruções como "seja educado" ou "pense passo a passo" já existem no comportamento base do Claude. Skill deve adicionar conhecimento NOVO.
8. **Calibre a linguagem pro Claude 4.x.** Opus 4.5+ e 4.6 são mais responsivos ao system prompt — instruções que forçavam triggering em modelos antigos agora podem causar overtriggering. Onde antes era "CRITICAL: You MUST use this tool when...", agora basta "Use this tool when...".

#### Meta-prompting pra otimização

Quando otimizar uma skill existente, use meta-prompting: Opus pra analisar e otimizar prompts que rodam em Sonnet/Haiku. O modelo mais capaz é melhor em identificar ambiguidades e gaps no prompt do modelo-alvo. 2-3 ciclos de melhoria atingem o sweet spot — depois disso, retornos decrescentes.

Processo:
1. Rode a skill no modelo-alvo com 3-5 test cases
2. Analise os outputs (com Opus): "O que o modelo errou? Por que? Qual instrução é ambígua?"
3. Reescreva as instruções problemáticas
4. Rode de novo e compare

#### Sobre a description (frontmatter)

A description é o mecanismo de triggering. O Claude lê TODAS as descriptions e decide qual skill acionar. Uma description ruim = skill nunca acionada.

Padrão de description eficaz:
```
"Skill para [O QUE FAZ]. Use esta skill SEMPRE que o usuário mencionar: [lista de triggers].
Também use quando [triggers implícitos]. Se [situação ambígua], USE esta skill."
```

Seja **pushy** — o Claude tende a sub-acionar skills. Melhor acionar demais e descartar do que nunca acionar.

---

### Fase 4: Teste — Verificar se funciona

Depois de escrever, teste. Sem teste, é rascunho.

**Requisito mínimo: 10 eval cases por skill.** Skills complexas devem ter 15-20. A auditoria mostrou que skills sem eval cases degradam silenciosamente — não dá pra saber se uma mudança melhorou ou piorou sem baseline.

**Composição dos eval cases:**
- 4-5 cenários do caminho feliz (variações de input normal)
- 2-3 edge cases (input vago, incompleto, ou ambíguo)
- 2-3 cenários de fronteira (overlap com outras skills, inputs que NÃO devem acionar)
- 1-2 cenários de stress (input muito longo, múltiplos pedidos simultâneos)

**No Claude.ai (sem subagents):**

1. Crie os prompts de teste realistas
2. Pra cada prompt, leia o SKILL.md e execute o fluxo completo como se fosse a primeira vez
3. Salve o output de cada teste
4. Apresente os outputs pro usuário: "Como ficou? O que tá bom? O que tá ruim?"

**Bons prompts de teste:**
- São específicos e detalhados (como uma pessoa real fala)
- Cobrem o caminho feliz E pelo menos um edge case
- Incluem contexto pessoal e detalhes concretos
- Variam em tom: um formal, um casual, um vago

**Maus prompts de teste:**
- Genéricos: "Crie uma skill" (ninguém fala assim)
- Óbvios: testam só o caminho feliz
- Curtos demais: "Faz X" sem contexto

Salve os prompts em `evals/evals.json`:
```json
{
  "skill_name": "nome-da-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Prompt realista do teste",
      "expected_output": "Descrição do output esperado",
      "files": [],
      "expectations": [
        "O output inclui X",
        "A skill seguiu a Fase 2 antes de escrever"
      ]
    }
  ]
}
```

**Critérios de sucesso por tipo:**
- **exact-match** — o output contém string específica (bom pra formatos)
- **semantic** — o output cobre o conceito esperado (bom pra conteúdo)
- **absence** — o output NÃO contém algo indesejado (bom pra restrições)
- **structural** — o output segue a estrutura definida (bom pra templates)

**Iteração:**
- Se o output tá ruim, identifique a CAUSA na skill (não no prompt de teste)
- Faça a correção no SKILL.md
- Rode de novo
- Repita até o usuário estar satisfeito

---

### Fase 5: Validação — Checklist de qualidade

ANTES de considerar a skill pronta, passe pelo checklist completo em `references/checklist-qualidade.md`. Resumo:

**Estrutura:**
- [ ] Tem frontmatter com name e description?
- [ ] Description é pushy e cobre triggers explícitos E implícitos?
- [ ] Tem seção "Visão geral" que explica o que faz em 2-3 parágrafos?
- [ ] Tem seção "Princípios" com pelo menos 3 princípios com porquê?
- [ ] Tem seção "Quando NÃO usar"?
- [ ] SKILL.md está abaixo de 500 linhas? (se não, moveu excesso pra references?)

**Conteúdo:**
- [ ] Cada instrução importante explica POR QUE existe?
- [ ] Tem exemplos concretos (pelo menos 2)?
- [ ] Tem tratamento de edge cases?
- [ ] Não tem instruções redundantes com o comportamento base do Claude?
- [ ] Tom e linguagem consistentes (PT-BR, imperativo)?
- [ ] Linguagem calibrada pra Claude 4.x? (sem caps lock desnecessário, sem "CRITICAL: You MUST")

**Context engineering:**
- [ ] Progressive disclosure correto? (metadata → SKILL.md → references)
- [ ] Cada reference file tem ponteiro claro no SKILL.md dizendo QUANDO ler?
- [ ] Não tem informação irrelevante competindo por atenção?
- [ ] O fluxo de trabalho é claro o suficiente pra seguir sem interpretar?

**Avaliação:**
- [ ] Tem pelo menos 10 eval cases em evals/evals.json?
- [ ] Eval cases cobrem caminho feliz + edge cases + fronteiras?
- [ ] Cada eval tem expectations verificáveis?
- [ ] Testou pelo menos 3 cenários reais antes de entregar?

**Integração:**
- [ ] Não conflita com skills existentes?
- [ ] Tem integração explícita com skills complementares?

---

### Fase 6: Description Optimization

A description é o que determina se a skill é acionada. Otimizar a description é tão importante quanto escrever a skill.

**Processo manual (Claude.ai):**

1. Escreva a description inicial seguindo o padrão pushy
2. Liste 8-10 prompts que DEVEM acionar a skill (variados, realistas)
3. Liste 8-10 prompts que NÃO devem acionar (near-misses — parecidos mas diferentes)
4. Analise: a description cobre todos os should-trigger sem capturar os should-not?
5. Ajuste e repita

**Bons should-trigger:**
- Variações de phrasing (formal, casual, vago)
- Situações onde o usuário não menciona a skill explicitamente mas precisa dela
- Edge cases entre esta skill e skills vizinhas

**Bons should-not-trigger (mais valiosos que os should-trigger):**
- Near-misses que compartilham keywords mas pedem coisa diferente
- Domínios adjacentes
- Situações ambíguas onde OUTRA skill é mais apropriada

**No Claude Code (com CLI):**
Se disponível, use o script de otimização automática:
```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id> \
  --max-iterations 5 \
  --verbose
```

---

### Fase 7: Empacotamento

Quando a skill está pronta, validada e testada:

1. Revise a estrutura final de arquivos
2. Se tem `present_files` disponível, empacote:
```bash
python -m scripts.package_skill <path/to/skill-folder>
```
3. Apresente o arquivo `.skill` pro usuário

Se estiver no Claude.ai e a skill for pra uso no Project Knowledge, apresente os arquivos diretamente pra download.

---

## Modificando skills existentes

Quando o pedido é MELHORAR uma skill, não criar do zero:

1. **Leia a skill inteira** — SKILL.md + todos os references
2. **Identifique a versão e nome** — preserve o name exato do frontmatter
3. **Copie pra local editável** antes de modificar (skills instaladas podem ser read-only)
4. **Faça a Fase 1 (Discovery) focada no problema** — "O que não tá funcionando? O que deveria ser diferente?"
5. **Mantenha o que funciona** — não reescreva do zero se só precisa ajustar
6. **Rode os evals existentes** como baseline antes de mudar qualquer coisa
7. **Teste a versão nova** contra os mesmos cenários que a versão antiga falhava
8. **Compare métricas** — se a skill tem eval cases, o pass_rate da versão nova deve ser >= versão antiga

---

## Padrões agentic pra skills

Skills que orquestram processos complexos devem escolher um padrão arquitetural. Consulte `references/agentic-patterns.md` pra detalhes. Resumo:

| Padrão | Quando usar | Exemplo |
|---|---|---|
| **Linear** | Processo sequencial com fases claras | PRD, Comunicação com Clientes |
| **Pipeline multi-agente** | Quando cada fase precisa de expertise isolada e contra-argumentos | Repo Review (Finder → Verifier → Arbiter) |
| **Fan-Out/Gather** | Quando análises independentes podem rodar em paralelo | UX + Security + Infra Audit simultâneos |
| **Reflection** | Quando o output precisa de auto-avaliação | Skill Builder (escrever → validar → iterar) |
| **Plan-and-Execute** | Quando o plano precisa ser gerado antes da execução | Projetos complexos com escopo variável |

Regra prática: comece com Linear. Só suba de complexidade se o Linear tá falhando.

---

## Integração com outras skills

A skill-builder pode e DEVE usar outras skills durante o processo:

| Fase | Skill auxiliar | Quando usar |
|---|---|---|
| Fase 2 (Pesquisa) | **Reference Finder** | Pra fundamentar o domínio da skill com referências consagradas |
| Fase 3 (Escrita) | **Prompt Engineer** | Pra estruturar prompts internos, templates de output, e few-shot examples. Lembre que o paradigma agora é context engineering — curar o contexto, não craftar a frase perfeita |
| Fase 3 (Escrita) | **Lovable Knowledge** | Se a skill gera knowledge/instruções pra outro LLM (usar formato AGENTS.md) |
| Fase 1 (Discovery) | **Product Discovery & PRD** | Se a skill é complexa e o escopo precisa ser definido como um produto |
| Fase 3 (Escrita) | **Supabase DB Architect** | Se a skill envolve schema de banco ou queries |
| Fase 3 (Escrita) | **n8n Architect** | Se a skill envolve workflows de automação |

---

## Quando NÃO usar esta skill

- Se o usuário quer um **prompt avulso** pra usar em outro lugar → use a skill Prompt Engineer
- Se quer **knowledge pro Lovable** → use a skill Lovable Knowledge
- Se é uma **pergunta pontual** sobre como skills funcionam → responda direto
- Se quer **rodar uma skill existente** → leia e execute a skill, não precisa da skill-builder

## Adaptações por ambiente

### Claude.ai
- Sem subagents: teste um cenário por vez, inline
- Sem browser: apresente resultados na conversa, não em viewer
- Sem `claude -p`: pule description optimization automática, faça manual
- Sem baseline: não roda "sem skill" pra comparar, foque em feedback qualitativo

### Claude Code / Cowork
- Use subagents pra testes paralelos quando disponível
- Use o viewer (`eval-viewer/generate_review.py`) pra review visual
- Use `run_loop.py` pra otimização de description
- Veja detalhes nos scripts bundled
