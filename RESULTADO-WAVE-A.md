# Wave A — Re-teste dos 3 P0s

> **Data:** 2026-04-15
> **Ambiente:** sessão Sonnet medium nova em `skillforge-arsenal/`
> **Cada input em sessão NOVA** (/clear ou novo terminal entre cada)

---

## Input 1 — geo-optimizer (Input 38 original)

**Texto:** quero melhorar a skill do copy, ela não tá acionando direito

**Skill esperada:** geo-optimizer

**Sinal de OK:** "Launching skill: geo-optimizer" ou "skill: geo-optimizer" no output
**Sinal de FALHA:** leu copy/SKILL.md direto ou respondeu sem skill

**Resultado:**
```
The user wants to improve the copy skill so it triggers better. According to skill-routing.md, "skill X não tá acionando" or "melhorar triggering" → **geo-optimizer**. Let me invoke that skill.
Usou Skill
skill: anthropic-skills:geo-optimizer
args: --target copy

Launching skill: anthropic-skills:geo-optimizer
The user wants to improve the copy skill's triggering. I need to read the copy skill's SKILL.md to analyze the current description. Let me find it first.
Ler
SKILL.md
C:\Users\Patrick Neuhaus\Documents\Github\skillforge-arsenal\.claude\worktrees\practical-kowalevski/C:\Users\Patrick Neuhaus\Documents\Github\skillforge-arsenal\.claude\worktrees\practical-kowalevski\skills\copy\SKILL.md
---
name: copy
description: "Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."
---

# Copy v2

**Role:** write, edit, and optimize marketing copy across 8 channels. Applies audience classification (Schwartz for conversion, pillars for social, buyer stage for content) before choosing framework. Teaches Voice of Customer (VoC) over inventado language.

**Iron Law:** Nunca escreva copy sem antes classificar o contexto da audiência. Para modos de conversão direta (landing, cold-email), isso é o nível Schwartz (1-5). Para outros modos, cada um tem seu próprio sistema de classificação — veja Phase 0.

## Boundary com comunicacao-clientes

- **copy** = persuasão, conversão, broadcast, marketing. Audiência ≠ pessoa específica. Saída pode ser usada em landing, anúncio, sequência de email, post social, ou WhatsApp marketing pra base.
- **comunicacao-clientes** = relacionamento operacional 1:1 com cliente específico (cobrança, update de status, mudança de escopo, aprovação, reclamação). Saída é uma mensagem única pra um cliente conhecido.

Se a tarefa é "responder o cliente X sobre Y" → use `comunicacao-clientes`, não `copy --mode whatsapp`.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | landing, social, email, cold-email, whatsapp, blog-seo, ux, ads | auto-detect |
| `--edit` | Revisar/editar copy existente (Seven Sweeps) | false |
| `--brief` | Gerar copy brief antes de escrever | false |
| `--framework <f>` | Forçar framework: aida, pas, bab, sb7, pastor, value-eq | auto por contexto |

## Workflow


Copy Progress:

- [ ] Phase 0: Triagem ⚠️ REQUIRED
  - [ ] ⛔ GATE 0.0: Isto é copy de marketing/vendas? (Se não → redirecionar)
  - [ ] 0.1 Identificar modo (tabela Mode Detection) — se ambíguo: ⛔ PARAR e perguntar
  - [ ] 0.2 Classificar contexto da audiência (Load references/audience-classification.md)
  - [ ] 0.3 Definir objetivo (converter? nutrir? educar? funcional?)
  - [ ] 0.4 Classificar: B2B ou B2C? (afeta tom, prova, CTA, template)
- [ ] Phase 1: Pesquisa ⚠️ REQUIRED
  - [ ] 1.1 Load references/foundations.md (sempre)
  - [ ] 1.2 Load reference do modo (tabela Reference Mapping)
  - [ ] 1.3 Load condicional: copy-psychology.md (ver triggers)
  - [ ] 1.4 VoC: Perguntar "Tem reviews, depoimentos, ou frases exatas de clientes?"
         Se sim → usar como BASE do copy. Se não → seguir com frameworks.
  - [ ] 1.5 Se --brief: gerar copy brief → ⛔ GATE: aprovação antes de Phase 2
- [ ] Phase 2: Escrever ⚠️ REQUIRED
  - [ ] 2.1 Load references/framework-selection.md — escolher framework por modo + contexto
  - [ ] 2.2 Se --framework conflita com contexto: avisar mismatch, perguntar se prossegue
  - [ ] 2.3 Escrever primeiro rascunho seguindo estrutura do framework/sistema
  - [ ] 2.4 Load references/headlines.md → gerar 2-3 alternativas de headline/hook
Now I have the current description. Let me analyze it.

Current description:
"Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."


Let me evaluate the character count and score the core capabilities to see if this description is hitting the right balance.

Looking at the scoring breakdown: it's strong on action verbs and domain coverage, with good bilingual trigger phrases in both Portuguese and English. The main gap is that it doesn't specify what this isn't meant for—there's no clear boundary around when not to use it. The length is solid at under 1024 characters, and it's hitting all the major frameworks and modes clearly.

The total comes to 15 out of 17 possible points, which suggests the description is well-structured but could benefit from adding a "don't use for" statement to improve differentiation. The real issue is that the description isn't matching how users actually phrase their requests. I need to systematically identify what keywords and phrases are missing — both the action verbs people use and the specific deliverables they ask for. Let me map out the common PT-BR and EN terms people use when they want copywriting work, then figure out where the gaps are between this description and what would actually trigger it versus the comunicacao-clientes skill. I'm mapping out the domain vocabulary for copywriting tasks across both Portuguese and English. Looking at what's already covered, I have the main nouns and some natural user phrases, but I need to flesh out the social media variations and add a key distinction about when this applies versus when to use customer communication instead.

The current description is running about 430 characters with room for roughly 590 more. I should expand the social media examples—things like captions for Instagram, LinkedIn, and TikTok posts, plus variations like "reescreve" and "redige" for rewriting tasks. I also need to clarify that this is for marketing copy and public-facing content, not one-on-one customer communication, which would fall under a different category. I'm scoring how well this description captures the tool's capabilities—checking for core functionality, action verbs, domain-specific terminology, and language coverage across both Portuguese and English trigger phrases.

The original missed a key differentiator: clarifying that this tool handles marketing copy across channels, not one-on-one client communication. Adding that distinction and expanding the Portuguese and English phrase examples brings the score from 13 to 15 out of 15.

Now I'm verifying the skill name matches what's in the system and checking how this description integrates with the broader workflow.

Since this is a YAML frontmatter edit, I need to run validation first before making changes. Let me show the user the before/after comparison to get approval, then proceed with the marker and write steps.

## Step 1 — Análise da descrição atual

**Descrição atual:**
> "Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."

**Score:**

| Dimensão | Score | Nota |
|----------|:-----:|------|
| Core capability | 2/2 | Primeira frase clara |
| Action verbs | 3/3 | Write, review, improve, optimize, editing |
| Domain nouns | 3/3 | 10+ substantivos de domínio |
| Frases PT-BR | 2/2 | 4 frases presentes |
| Frases EN | 2/2 | 3 frases presentes |
| Diferenciação | **0/2** | **Nenhum "NÃO use pra X"** |
| Length | 1/1 | ~430 chars |

**Total: 13/15** — gaps identificados:

---

## Step 2 — Keywords geradas (perspectiva do agente)

Frases comuns que um agente buscaria e **não estão** na descrição atual:

**PT-BR ausentes:**
- `legenda pro Instagram`, `caption`, `cria post`, `copy pra Meta Ads`, `página de vendas`, `texto de anúncio`, `reescreve`

**EN ausentes:**
- `ad copy`, `sales page`, `product description`, `Facebook ad`, `Instagram caption`

**Diferenciação ausente:** não há nada dizendo "não use pra mensagem 1:1 → use comunicacao-clientes". Isso provavelmente é o maior motivo de falha de trigger — o agente não sabe separar os dois escopos.

---

## Step 3 — ⛔ GATE: Antes/Depois

**ANTES** (430 chars, 13/15):

Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'.


**DEPOIS** (580 chars, 15/15):

Write, review, improve, and optimize marketing copy across 8 channels. Modes: Landing Page, Sales Page, Social (Instagram/LinkedIn/TikTok), Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads (Meta/Google). Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing.
Use when: 'escreve copy', 'cria post', 'legenda pro Instagram', 'caption', 'texto de anúncio', 'copy pra Meta Ads', 'página de vendas', 'headline pra landing', 'email de vendas', 'melhora esse texto', 'reescreve', 'write copy', 'ad copy', 'sales page', 'product description', 'email sequence'.
NÃO use pra mensagem 1:1 com cliente específico → use comunicacao-clientes.


**Delta:** 13→15 (+2). Principais ganhos:
- Diferenciação explícita com `comunicacao-clientes` (maior gap)
- Frases social media: `legenda`, `caption`, `cria post`, `copy pra Meta Ads`
- EN ampliado: `ad copy`, `sales page`, `product description`
- Channels específicos: Instagram/LinkedIn/TikTok, Meta/Google

Aprova aplicar?
```

**Verdict:** OK / NENHUMA / ERRADA

---

## Input 2 — sdd (Input 31 original)

**Texto:** quero adicionar um sistema de favoritos no app, planeja antes de sair codando

**Skill esperada:** sdd

**Sinal de OK:** "Launching skill: sdd" ou entrou no pipeline Research/Spec
**Sinal de FALHA:** entrou em EnterPlanMode nativo ou só perguntou "qual app?"

**Resultado:**
```
The user wants to add a favorites system to an app. They want me to plan before coding. Let me first understand what app they're talking about. I'm in the skillforge-arsenal worktree, but this seems to be a different project. Let me look at the context.

The user said "plan before coding" - this triggers the SDD skill based on the skill-routing rules: "planeja antes de codar", "spec antes de implementar", "anti-vibecoding" → **sdd**

Let me invoke the SDD skill.
Usou Skill
skill: sdd
args: sistema de favoritos no app

Launching skill: sdd
Qual app? Preciso saber o repo/projeto antes de mergulhar no research.

The user wants to plan a favorites system for an app. I need to run Phase 1 of SDD - Research. But first, I need to understand which app they're talking about. I'm in the skillforge-arsenal worktree, but the user likely has a different app in mind.

Let me ask them which app they're referring to, since I don't know the context. Actually, wait - let me check if there's more context. The working directory is the skillforge-arsenal worktree, but the user might be referring to a different project.

Actually, I should ask which app before diving into research. But the SDD workflow says to start with research. Let me first ask for clarification about which app they're talking about.


I need to clarify which app they're building the favorites system for before I can proceed with research.
```

**Verdict:** OK / NENHUMA / ERRADA

---

## Input 3 — pdf (Input 5 original, via skill-routing.md)

**Texto:** junta esses 3 PDFs num só pra eu mandar pro cliente

**Skill esperada:** pdf

**Sinal de OK:** "Launching skill: pdf" ou "skill: pdf"
**Sinal de FALHA:** fez Glob direto ou pediu paths sem skill

**Resultado:**
```
The user wants to merge 3 PDFs into one. They haven't specified which PDFs. I need to ask which PDFs they want to merge, or they might attach them. Let me check if there's any file attachment or path mentioned.

No files were mentioned. I should ask which PDFs they want to merge. But wait - the skill-routing rules say "junta/merge/combina PDFs" → **pdf** skill. Let me invoke the pdf skill first.
Usou Skill
skill: pdf
args: juntar 3 PDFs em um único arquivo para envio ao cliente

Launching skill: pdf
The user wants to merge 3 PDFs into one. The skill has been loaded. Now I need to ask which 3 PDFs they want to merge, since they haven't specified the files.
Quais são os 3 PDFs? Me passa os caminhos ou arrasta os arquivos aqui.
```

**Verdict:** OK / NENHUMA / ERRADA

---

## Resultado Wave A

**Passaram:** _/3
**Decisão:** se 3/3 OK → Wave B. Se falhar → diagnóstico antes de avançar.
