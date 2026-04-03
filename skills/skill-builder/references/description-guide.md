# Description Guide — Keyword Bombing e GEO

Consulte este arquivo no **Step 4** do workflow. A description é o mecanismo de triggering — se ela é fraca, a skill nunca aciona.

---

## Por que a description importa

A `description` no frontmatter é a ÚNICA coisa que o Claude lê antes de decidir acionar a skill. O body do SKILL.md carrega DEPOIS do triggering — tarde demais. Toda informação de "quando usar" deve estar na description.

Duas funções:
1. **Triggering automático** — o Claude decide acionar quando lê a description
2. **Busca** — usuários encontram a skill por search (npx skills find)

## Técnica: Keyword Bombing (GEO)

GEO = Generative Engine Optimization. Otimizar pra agentes acharem a skill, não humanos.

Liste TODAS as possibilidades de trigger — ações, objetos, sinônimos, frases naturais.

### As 4 dimensões de uma boa description

1. **Core capability** — primeira frase, o que faz
2. **Action verbs** — 5+ verbos que o usuário usaria (criar, melhorar, analisar, revisar, gerar...)
3. **Object nouns** — 5+ substantivos do domínio (skill, component, API, workflow...)
4. **Natural phrases** — o que o usuário LITERALMENTE digitaria

### Exemplos excelentes

**ui-ux-pro-max (222K installs):**
```yaml
description: "UI/UX design intelligence. 50 styles, 21 palettes,
50 font pairings, 20 charts, 8 stacks (React, Next.js, Vue, Svelte,
SwiftUI, React Native, Flutter, Tailwind). Actions: plan, build,
create, design, implement, review, fix, improve, optimize, enhance,
refactor, check UI/UX code."
```
→ "Rede de keywords" — não importa o que o usuário diga sobre UI, vai acertar.

**Padrão com diferenciação (quando há overlap):**
```yaml
description: "Skill para [O QUE FAZ]. Use SEMPRE que [triggers].
Se houver dúvida entre esta skill e [skill X], pergunte:
'[pergunta que diferencia]'"
```

### Exemplos ruins vs bons

```yaml
# Ruim — vago demais, não triggera
description: "Ajuda a criar apresentações"

# Bom — rico em keywords
description: "Generate professional slide decks from content. Creates
outlines with style instructions, then generates individual slide images.
Use when user asks to 'create slides', 'make a presentation', 'generate
deck', 'slide deck', 'PPT', 'turn this into a presentation'."
```

### Dica avançada: use o Claude como GEO

Pergunte ao próprio Claude: "Se você precisasse encontrar uma skill que faz [X], que termos de busca você usaria?" Use essas keywords na description.

---

## Checklist

- [ ] Primeira frase declara a capability principal
- [ ] 5+ action verbs listados
- [ ] 5+ object nouns / tipos de projeto listados
- [ ] Frases naturais de trigger incluídas
- [ ] Abaixo de 1024 caracteres
- [ ] Sem angle brackets (`<` ou `>`)
- [ ] Toda info de "quando usar" está AQUI, não no body do SKILL.md
- [ ] Se há overlap com outra skill, inclui instrução de diferenciação

---

## Padrões de description por tipo de skill

### Skill de processo
```
"Skill para [processo]. Use SEMPRE que o usuário mencionar: [triggers].
Também use quando [triggers implícitos]. Se [ambiguidade], USE esta skill."
```

### Skill técnica
```
"[Ação] [artefatos]. Suporta [formatos/tecnologias]. Use quando [triggers
de ação]. Projetos: [tipos]. Keywords: [termos técnicos do domínio]."
```

### Skill de auditoria
```
"Analyze and review [domínio]. Use when user asks to: review, audit,
check, inspect, evaluate [objetos]. Frameworks: [quais usa].
Output: [tipo de relatório]."
```

## Regra final

NUNCA coloque "Quando usar esta skill" no body do SKILL.md. O body só ajuda DEPOIS do triggering — é tarde demais. Toda informação de ativação pertence ao campo `description`.
