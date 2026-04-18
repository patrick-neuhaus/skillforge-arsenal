# Wave 0 — Sanity Check de Ambiente

> **Objetivo:** verificar se o triggering das skills degrada no ambiente real de trabalho (Github/) vs o ambiente mais limpo do teste original (skillforge-arsenal/).
>
> **Metodologia:** 3 inputs seletos representando diferentes root causes. Sessão Sonnet medium nova, em `C:\Users\Patrick Neuhaus\Documents\Github\` (NÃO abrir em skillforge-arsenal/).
>
> **Por que esses 3:** Input 5 = desc-keyword-miss simples (baseline). Input 31 = context-hijack com plan mode (pior caso). Input 38 = meta-bug (o fix mais crítico de todos).

---

## Como rodar

1. Fecha qualquer sessão Claude aberta
2. Abre sessão nova na pasta pai do Github:
   ```
   cd "C:\Users\Patrick Neuhaus\Documents\Github"
   claude
   ```
3. Confirma que está em Sonnet medium (`/model` deve mostrar Sonnet)
4. Cola o **Input 1** abaixo exato (sem aspas, sem add nada)
5. Copia a resposta inteira do Claude (incluindo tool calls) e cola no bloco `Resultado:` do Input 1
6. `/clear` ou abre sessão nova
7. Repete com Input 2 e Input 3

**Importante:** cada input em sessão NOVA. Se reutilizar a mesma sessão, contexto vaza entre testes.

---

## Input 1

**Texto:** "junta esses 3 PDFs num só pra eu mandar pro cliente"

**Skill esperada:** pdf

**Por que esse:** caso simples de desc-keyword-miss. Se dispara aqui e não disparava em skillforge, significa que o ambiente Github/ ajuda (CLAUDE.md com contexto de cliente/arquivo pode reforçar).

**Resultado:**
```
The user wants to merge 3 PDFs into one. They haven't specified which PDFs. Let me ask which PDFs they want to merge, or check if there's a skill for this.

Looking at the available skills, I see `anthropic-skills:pdf` which handles PDF tasks. Let me invoke that skill.

But wait - I don't know which 3 PDFs they're referring to. I should ask for the file paths.
Usou ToolSearch
query: AskUserQuestion
max_results: 1
The user wants to merge 3 PDFs but hasn't specified which files. I need to ask for the file paths. Let me use AskUserQuestion or just ask directly. Actually, I should just ask them to share the file paths since there are no options to choose from here - it's an open-ended question about which files.

Let me just ask directly in text.
Quais são os 3 PDFs? Me passa os caminhos dos arquivos.
```

**Verdict rápido (preenche depois de colar):** OK / NENHUMA / ERRADA / DESAMBIGUOU

---

## Input 2

**Texto:** "quero adicionar um sistema de favoritos no app, planeja antes de sair codando"

**Skill esperada:** sdd

**Por que esse:** pior caso — "planeja" conflita com `EnterPlanMode` nativo. Se mesmo em Github/ cair em plan mode nativo, confirma que fix da skill `sdd` é obrigatório.

**Resultado:**
```
The user wants to add a favorites system to an app. They're asking me to plan before coding. Let me first understand what app we're talking about - I need to explore the current working directory to understand the codebase.

Let me check what's in the current working directory first.
Executado
ls "C:\Users\Patrick Neuhaus\Documents\Github"
Qual app? Tem vários projetos aqui. Me diz o nome ou descreve o que é pra eu achar o certo.
```

**Verdict rápido:** OK / NENHUMA / ERRADA / DESAMBIGUOU

---

## Input 3

**Texto:** "quero melhorar a skill do copy, ela não tá acionando direito"

**Skill esperada:** geo-optimizer

**Por que esse:** meta-bug. Se dispara em Github/ e não disparava em skillforge, significa que algo no CLAUDE.md do Github favorece meta-frame. Se NÃO dispara em nenhum dos dois ambientes, confirma que fix da description de `geo-optimizer` é P0.

**Resultado:**
```
Patrick wants to improve the copy skill. Let me first read the current state of the skill to understand what's there, and check the memory about the copy skill project.

Let me look at the skillforge-arsenal repo and find the copy skill.
Pesquisado
**/copy*/**

Lembrado uma memória
Ler
SKILL.md
Patrick wants to improve the copy skill because it's not triggering correctly. Let me understand what "não tá acionando direito" means - the skill isn't being triggered/invoked when it should be.

The issue could be in:
1. The `description` in the YAML frontmatter - this is what Claude uses to decide whether to invoke the skill
2. The trigger patterns in the skill-routing.md rules

Let me think about what "not triggering correctly" means. In Claude Code, skills are invoked based on their description matching user intent. The description in the frontmatter is key.


Looking at the current description, it's quite comprehensive - it covers the 8 modes, frameworks, awareness levels, and includes both Portuguese and English trigger phrases. But I need to understand what specifically isn't working. Is the skill not triggering at all, or is it triggering in the wrong situations? The description seems well-structured, but maybe the trigger phrases aren't matching Patrick's actual usage patterns, or perhaps the description itself isn't clear enough for Claude to recognize when to invoke it.

Let me check the skill-routing documentation to see how copy-related requests are supposed to be routed - I'm noticing the table might not have explicit copy entries, which could be part of the issue.

Before I make any changes though, I need to understand what Patrick's actually experiencing: is the skill not being invoked at all when he asks for copy work, is it triggering but producing wrong output, or is something else going on? Given the context around improving existing skills, I should ask him for specifics on what behavior he's seeing rather than guessing at the fix.
Antes de entrar, preciso de 2 perguntas targeted:

1. "Não tá acionando direito" — o que exatamente acontece? Claude ignora a skill (não chama nenhuma) quando deveria chamar copy? Ou chama mas vai pro modo errado? Ou chama quando não deveria?
2. Em qual contexto falhou? Manda um exemplo de prompt que deveria ter acionado e não acionou (ou acionou errado).
Com isso consigo atacar o ponto certo — pode ser o description do frontmatter, pode ser a ausência na tabela do skill-routing.md, pode ser o workflow interno.
```

**Verdict rápido:** OK / NENHUMA / ERRADA / DESAMBIGUOU

---

## Decisão pós-Wave 0

Preenche só depois de rodar os 3:

| Resultado | Interpretação | Próximo passo |
|---|---|---|
| 3/3 NENHUMA/ERRADA (igual skillforge) | Ambiente não ajuda nem atrapalha. Fix é 100% nas descriptions. | Seguir Wave A direto em skillforge. |
| 1-2 passam | Ambiente Github/ ajuda parcialmente. | Seguir Wave A em skillforge. CLAUDE.md do Github tá OK. |
| 3/3 OK | CLAUDE.md do Github fix tudo sozinho (improvável) | Parar plano. Investigar o que tá diferente. |
| Pior que skillforge (3/3 NENHUMA mas antes tinha 1 passagem) | CLAUDE.md do Github atrapalha | Wave 0.5: slim-down do CLAUDE.md antes de seguir |

**Ambiente oficial pra rodar testes de Wave A e B:** decidido aqui. Default é skillforge (mais limpo), mas se Wave 0 mostrar que Github/ é equivalente, tu pode testar lá.

---

## Observações do Patrick

(Coisas que tu notou durante os testes — se o modelo demorou, se fez algo inesperado, se pediu pra fazer algo em vez de outro)
