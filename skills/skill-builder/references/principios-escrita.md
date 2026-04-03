# Princípios de Escrita de Skills — Guia Detalhado

Última atualização: 2026-03-26

Consulte este arquivo quando estiver na **Fase 3 (Escrita)** do fluxo de criação de skill. Ele detalha os princípios de como escrever instruções que funcionam bem com LLMs.

---

## 1. Context Engineering — O conceito central

Skill não é prompt. Skill é **curadoria de contexto**: decidir o que o modelo precisa ver, quando, e em qual formato. O conceito vem da evolução natural do prompt engineering — enquanto prompting otimiza as palavras, context engineering otimiza o conjunto COMPLETO de tokens que o modelo recebe (instruções, exemplos, referências, histórico, tools).

**Princípio do orçamento de atenção:** O modelo tem atenção finita. Cada token na skill compete com todos os outros tokens no contexto. Informação irrelevante não é neutra — ela DILUI a atenção disponível pra informação relevante.

**Implicações práticas:**
- Corte frases que não adicionam informação nova
- Se uma instrução pode ser inferida do contexto, não escreva
- Prefira 3 linhas precisas a 10 linhas vagas
- Se algo é importante, coloque no início da seção (recency bias + primacy bias)

## 2. Hierarquia de eficácia (Anthropic)

A Anthropic documentou uma hierarquia de técnicas por impacto. Respeite a ordem:

**Nível 1 — Clareza e direção (maior impacto)**
Instruções claras, específicas, sem ambiguidade. Se um humano lesse a instrução e não entendesse na primeira leitura, o modelo também vai ter dificuldade.

Teste: **Teste do colega** — Se você passasse essa instrução pra um colega inteligente que nunca fez essa tarefa, ele saberia exatamente o que fazer? Se não, reescreva.

**Nível 2 — Exemplos (few-shot)**
Mostrar é mais eficaz que descrever. Um exemplo de input → output vale mais que 10 linhas explicando o formato.

Padrão:
```markdown
**Exemplo:**
Input: [input real]
Output: [output ideal]
```

Regras:
- Mínimo 2 exemplos por formato de output importante
- Exemplos devem ser realistas (dados reais ou verossímeis)
- Inclua pelo menos 1 edge case nos exemplos
- Se o output varia conforme o input, mostre a variação

**Nível 3 — Chain of thought (raciocínio explícito)**
Pra tarefas que exigem análise ou decisão, instrua o modelo a pensar antes de responder. Não use "pense passo a passo" genérico — descreva OS passos.

Bom: "Antes de dar a recomendação, analise: 1) Qual o problema real? 2) Quais as opções? 3) Qual o tradeoff de cada?"
Ruim: "Pense cuidadosamente antes de responder."

**Nível 4 — Estrutura (XML tags, seções)**
Organize o contexto em blocos claros. O Claude responde especialmente bem a XML tags e headers Markdown.

Use XML tags pra separar:
- `<context>` — informações de background
- `<instructions>` — o que fazer
- `<examples>` — exemplos de input/output
- `<constraints>` — o que NÃO fazer

Ou use Markdown headers quando XML seria overkill.

**Nível 5 — Papel/persona**
Atribuir um papel ("Você é um senior UX designer...") ajuda, mas MENOS do que clareza e exemplos. Não comece por aqui.

## 3. Regras de escrita específicas pra skills

### Imperativo, não sugestivo
- ✅ "Pergunte o contexto técnico antes de sugerir solução"
- ❌ "Seria bom se você perguntasse sobre o contexto técnico"

### Explique o porquê
- ✅ "Sempre inclua seção 'Fora do escopo' — sem ela, o LLM pode inventar features que não foram pedidas, desperdiçando tokens e confundindo o usuário"
- ❌ "Sempre inclua seção 'Fora do escopo'"

### Específico com escape
- ✅ "Use shadcn/ui pra componentes de UI. Se o projeto já usa outra lib, mantenha a existente."
- ❌ "Use uma biblioteca de componentes moderna"
- ❌ "SEMPRE use shadcn/ui sem exceção" (rígido demais)

### Evite caps lock como muleta
Se você precisa gritar (SEMPRE, NUNCA, OBRIGATÓRIO), é sinal de que não explicou bem o porquê. Use caps lock com moderação — reserve pra restrições de segurança reais, não pra preferências.

- ✅ "Nunca invente referências — se não tem certeza que um livro existe, pesquise antes. Referência inventada destrói a credibilidade do output inteiro."
- ❌ "NUNCA INVENTE REFERÊNCIAS. ISSO É ABSOLUTAMENTE PROIBIDO."

### Não repita o sistema
O Claude já sabe: ser educado, pensar antes de responder, admitir quando não sabe. Não gaste tokens da skill repetindo isso. Adicione conhecimento NOVO.

### Seções opcionais, nunca vazias
Se um template tem seção "Integrações externas" e o projeto não tem, REMOVA a seção. `[placeholder]` é ruim — o modelo pode inventar conteúdo pra preencher.

## 4. Organização por progressive disclosure

O sistema de skills tem 3 níveis de carregamento. Use isso estrategicamente:

### Nível 1: Description (~100 palavras)
- Sempre no contexto do modelo
- Único mecanismo de triggering
- Deve ser pushy (melhor acionar demais que nunca acionar)
- Inclua triggers explícitos E implícitos

### Nível 2: SKILL.md body (~500 linhas)
- Carregado quando a skill aciona
- Deve conter o fluxo completo de trabalho
- Se passar de 500 linhas, mova detalhes pra references/

### Nível 3: References (sem limite)
- Carregados sob demanda
- Cada arquivo deve ter ponteiro claro no SKILL.md: "Consulte `references/X.md` quando [situação]"
- Pra arquivos grandes (>300 linhas), inclua table of contents

### Quando mover pro nível 3
- Detalhes técnicos de um sub-domínio (ex: patterns por framework)
- Templates extensos
- Checklists detalhados
- Exemplos longos
- Referências bibliográficas completas

## 5. Padrões de organização

### Skill com múltiplos domínios
Organize por variante — o modelo lê só o relevante:
```
skill-name/
├── SKILL.md (fluxo + seleção de variante)
└── references/
    ├── variante-a.md
    ├── variante-b.md
    └── variante-c.md
```

### Skill com processo em fases
Organize o SKILL.md por fase cronológica. Cada fase deve ser auto-contida o suficiente pra ser executada mesmo se o modelo perdeu contexto das fases anteriores.

### Skill com templates de output
Coloque o template no SKILL.md se cabe em ~30 linhas. Se for maior, mova pra `references/template-X.md`.

## 6. Armadilhas comuns

1. **Skill que tenta fazer tudo** → Quebre em 2+ skills com escopos claros e integração entre elas
2. **Instruções contraditórias** → Se a seção A diz "seja breve" e a seção B diz "detalhe tudo", o modelo fica confuso. Revise por consistência.
3. **Excesso de MUST/NEVER** → Cada restrição forte reduz a flexibilidade. Use poucas e justificadas.
4. **Sem exemplos** → O modelo inventa o formato. Sempre dê exemplos do output esperado.
5. **Description fraca** → Skill excelente que nunca aciona é skill inútil. Invista na description.
6. **Copy-paste de docs externas** → Não copie documentação inteira pra dentro da skill. Extraia os princípios e transforme em instruções.
7. **Skill que repete o que o Claude já sabe** → Não ensine o modelo a pesquisar, resumir, ou ser educado. Ensine o conhecimento de DOMÍNIO que ele não tem.

## 7. Fontes incorporadas neste guia

- Anthropic Prompt Engineering Guide (docs.anthropic.com) — Hierarquia de 5 níveis
- Anthropic Context Engineering for AI Agents — Curadoria de contexto como disciplina
- Manus Blog "Context Engineering for AI Agents" — KV-cache, progressive loading
- Paper "Agentic Context Engineering" (ACE) — Contextos como playbooks evolutivos
- Martin Fowler / Thoughtworks "Context Engineering for Coding Agents" — Skills como context interfaces
- Skill-creator original (Anthropic/examples) — Anatomia, progressive disclosure, testing
