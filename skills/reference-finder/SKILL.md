---
name: reference-finder
description: "Skill para fundamentar qualquer tema com referências consagradas — livros, frameworks, metodologias, pessoas, artigos. Use SEMPRE que o usuário mencionar: 'tem framework pra isso?', 'quem é referência?', 'tem livro sobre?', 'melhor prática pra X?', 'me fundamenta isso', 'preciso de referências', ou quando quiser embasar uma decisão ou aplicar conhecimento consagrado. Também sugira quando o usuário tomar decisão importante sem referências. Se o tema já tem referências em references/, consulte primeiro. NÃO use pra perguntas técnicas diretas ('como configuro RLS') — responda direto. Se o usuário já tem referências e só quer aplicar, ajude sem buscar mais."
---

# Reference Finder v3

IRON LAW: NEVER cite a book, framework, or author you're not sure exists. When in doubt, web search FIRST. One invented reference destroys the credibility of the entire output.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--find` | Find references for a topic | true |
| `--save` | Save found references to references/ | auto (ask) |
| `--connect` | Find connections with existing references | auto |
| `--moc` | Generate a Map of Content for cross-domain topic | false |

## Workflow

```
Reference Finder Progress:

- [ ] Step 1: Understand ⚠️ REQUIRED
  - [ ] 1.1 Identify topic, context, purpose
  - [ ] 1.2 Specify if vague
- [ ] Step 2: Check Existing
  - [ ] 2.1 Search references/ for existing files
  - [ ] 2.2 Check MOCs for related panorama
- [ ] Step 3: Research ⚠️ REQUIRED
  - [ ] 3.1 Layer 1: Seminal works
  - [ ] 3.2 Layer 2: Practical frameworks
  - [ ] 3.3 Layer 3: Recent evolution (if applicable)
  - [ ] 3.4 Layer 4: Key people
- [ ] Step 4: Present
  - [ ] 4.1 Organize by layers
  - [ ] 4.2 Cross-reference with existing base
  - [ ] 4.3 Contextual recommendation
  - [ ] ⛔ GATE: Present to user before saving
- [ ] Step 5: Save & Connect (conditional)
  - [ ] 5.1 Save to domain file in references/
  - [ ] 5.2 Add connections with existing refs
  - [ ] 5.3 Create MOC if 3+ domains crossed
```

If `--moc`: Skip to MOC generation from existing references.

## Principles

1. **Referência boa > referência recente.** Livro de 1997 que é bíblia da área > post de blog de ontem. Priorize seminais. Complemente com recentes quando o campo evoluiu.
2. **Aplicável > teórico.** Frameworks que o usuário aplica HOJE > papers acadêmicos puros.
3. **Fonte primária > secundária.** Livro original > resumo > post que cita > tweet.
4. **Honestidade sobre limitações.** Se o conhecimento é superficial ou desatualizado, USE WEB SEARCH.
5. **Confronte com o contexto.** Harvard Business Review é ótima, mas se o usuário tem equipe de 5 em cidade pequena, filtre.
6. **Conecte, não acumule.** Referência conectada com outras é mais poderosa que referência isolada.
7. **3 excelentes > 15 genéricas.** Curadoria é o valor. Não padde a lista.

## Step 1: Understand ⚠️ REQUIRED

Perguntas-chave:
- **Qual o tema?** (ex: vendas B2B, liderança, copywriting)
- **Qual o contexto?** (equipe, tamanho, setor, Brasil?)
- **Pra que vai usar?** (tomar decisão, montar processo, aprender do zero, fundamentar proposta)

Se o tema for vago ("quero melhorar em gestão"), especifique: "Gestão de quê? Pessoas, projetos, tempo, produto?"

## Step 2: Check Existing

ANTES de pesquisar, verifique `references/`:
- Existe arquivo do domínio? → Leia, use como base, complemente se necessário
- Existe MOC relacionado? → Consulte pra entender panorama
- Nada encontrado? → Step 3

## Step 3: Research ⚠️ REQUIRED

Use web search em 4 camadas:

**Camada 1 — Obras seminais:** "[tema] best books all time", "[tema] seminal framework"
→ Livros unanimidade, frameworks que todo profissional conhece, autores sinônimos do tema.

**Camada 2 — Frameworks práticos:** "[tema] framework practical", "[tema] methodology"
→ Modelos aplicáveis imediatamente, com passos claros.

**Camada 3 — Evolução recente:** "[tema] 2025 2026 trends", "[tema] latest research"
→ O que mudou no campo. Nem todo tema precisa — se seminais ainda valem, diga isso.

**Camada 4 — Pessoas:** "[tema] expert thought leader", "[tema] who to follow"
→ Quem o usuário deveria conhecer/seguir.

## Step 4: Present

Organize o output:

```
## [Tema] — Referências Fundamentais

### Obras seminais
- **[Livro/Framework]** — [Autor], [Ano]
  - O que é: [1-2 frases]
  - Por que importa pro seu contexto: [aplicação concreta]
  - Conceito-chave: [o que o usuário pode aplicar já]

### Frameworks práticos
- **[Framework]** — [Autor/Origem]
  - Como funciona: [2-3 frases práticas]
  - Quando usar / Quando NÃO usar

### Referências recentes (se relevante)
### Pessoas pra seguir

### Conexões com referências existentes
- [Referências da base que se conectam com as novas]

### Recomendação pro seu contexto
[Dado o que sei do usuário, começar por X porque Y. Ignorar Z porque não se aplica.]
```

⛔ **Confirmation Gate:** Apresente as referências. Pergunte se quer salvar em `references/`.

## Step 5: Save & Connect

Load `references/organization-guide.md` for the complete organization system (PARA + Zettelkasten + MOCs + scoring).

### Scoring (ByteRover-inspired)

Ao salvar, classifique cada referência:
- **Importance** (0-100): 80+ = seminal/core, 50-79 = útil, <50 = complementar
- **Maturity**: `draft` (recém-encontrada) → `validated` (aplicada pelo usuário) → `core` (referência base do domínio)
- **Recency**: referências com maturity=draft e importance<35 são candidatas a archive após 21 dias sem uso

### Save format (resumo — detalhes no guide)

Salve em `references/[dominio]-references.md`. Se já existe, ATUALIZE.
Cada referência deve ter pelo menos uma **conexão** com outra existente.
Crie MOC em `references/moc-[tema].md` quando o tema cruza 3+ domínios.

## Anti-Patterns

- **Inventar referências** — citar livro que não tem certeza que existe. Web search primeiro.
- **Lista enciclopédica** — 15 referências genéricas em vez de 3 excelentes curadas.
- **Ignorar contexto** — recomendar Enterprise frameworks pra equipe de 3 pessoas.
- **Só seminais, sem práticos** — teoria sem aplicação. O usuário quer resolver problemas.
- **Referências sem conexão** — salvar sem identificar links com o que já existe na base.
- **Forçar organização** — o sistema PARA+Zettelkasten é recomendação, não obrigação. Se atrapalha, simplifique.

## Pre-Delivery Checklist

- [ ] Toda referência citada foi verificada (existe, autor correto, ano correto)
- [ ] Referências filtradas pro contexto do usuário
- [ ] Pelo menos 1 recomendação contextual ("comece por X porque Y")
- [ ] Conexões com referências existentes identificadas (se houver base)
- [ ] Output organizado por camadas (seminais → práticos → recentes → pessoas)

## Integration

Pode ser acionada POR DENTRO de outras skills:
- **Skill Builder** (Step 2): pesquisar domínio da skill sendo criada
- **Product Discovery & PRD**: fundamentar decisões de produto
- **Tech Lead & PM**: frameworks de priorização, gestão
- **Prompt Engineer** (Step 2): referências de domínio para prompts

Quando acionada por outra skill, seja breve — 1-2 referências inline, não o processo completo.

## When NOT to use

- Resposta rápida e direta → não force referências em tudo
- Pergunta técnica específica ("como configurar RLS") → responda direto
- Usuário já tem referências e quer aplicar → ajude a aplicar, não busque mais
