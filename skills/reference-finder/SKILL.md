---
name: reference-finder
description: "Skill para fundamentar qualquer tema com referências consagradas — livros, frameworks, metodologias, pessoas, artigos. Use SEMPRE que o usuário mencionar: 'tem framework pra isso?', 'quem é referência?', 'tem livro sobre?', 'melhor prática pra X?', 'me fundamenta isso', 'preciso de referências', ou quando quiser embasar uma decisão ou aplicar conhecimento consagrado. Também sugira quando o usuário tomar decisão importante sem referências. Se o tema já tem referências em references/, consulte primeiro. NÃO use pra perguntas técnicas diretas ('como configuro RLS') — responda direto. Se o usuário já tem referências e só quer aplicar, ajude sem buscar mais."
---

# Reference Finder v2 — Fundamentação por Referências

## Visão geral

Esta skill encontra as melhores referências (livros, frameworks, metodologias, pessoas, artigos, estudos) pra qualquer tema que o usuário traga. O objetivo é transformar decisões baseadas em "achismo" em decisões fundamentadas por quem já resolveu esse problema antes.

A skill é genérica por design — cobre qualquer domínio. Mas ela aprende: toda vez que pesquisa um domínio novo, salva as referências encontradas em `references/` pra consulta futura. Com o tempo, os domínios mais usados ficam cada vez mais ricos.

### Novidades na v2

- **Sistema de organização de referências** — Zettelkasten + PARA pra manter a base de conhecimento útil e acionável, não só acumulativa
- **MOCs (Maps of Content)** — índices temáticos que conectam referências de domínios diferentes
- **Hub-and-Spoke** — PARA como hub de organização + Zettelkasten como spoke de conexões
- **Obsidian como ferramenta recomendada** pra quem quer manter a base fora do Claude
- **Conexões cruzadas** — ao encontrar referências, a skill agora identifica links com referências já salvas em outros domínios

## Princípios

1. **Referência boa > referência recente.** Um livro de 1997 que é considerado a bíblia de um assunto vale mais que um post de blog de ontem. Priorize obras seminais e atemporais. Complemente com referências recentes quando o campo evoluiu.
2. **Aplicável > teórico.** Não traga referências acadêmicas puras se o usuário quer resolver um problema prático. Priorize frameworks e metodologias que ele pode aplicar HOJE.
3. **Fonte primária > secundária.** O livro do autor original > resumo do livro > post que cita o livro > tweet sobre o post.
4. **Honestidade sobre limitações.** Se o conhecimento do Claude sobre um tema é superficial ou potencialmente desatualizado, USE WEB SEARCH. Não invente referências. Nunca cite um livro que você não tem certeza que existe.
5. **Confronte com o contexto do usuário.** Uma referência pode ser excelente em geral mas não se aplicar ao contexto dele (equipe pequena, SMB, Brasil). Sempre filtre.
6. **Conecte, não acumule.** (NOVO v2) Referência isolada é útil. Referência conectada com outras é poderosa. Ao salvar, sempre identifique links com o que já existe na base.

## Fluxo de trabalho

### Passo 1: Entender o que o usuário precisa

Quando o usuário pedir referências ou quando você identificar que referências agregariam:

1. **Qual o tema?** (ex: vendas B2B, liderança de primeira viagem, copywriting)
2. **Qual o contexto?** (ex: equipe de 5, cliente PME, produto digital)
3. **Pra que vai usar?** (ex: tomar uma decisão, montar um processo, aprender do zero, fundamentar uma proposta)

Se o tema for vago ("quero melhorar em gestão"), faça perguntas pra especificar: "Gestão de quê? Pessoas, projetos, tempo, produto?"

### Passo 2: Verificar referências existentes

ANTES de pesquisar, cheque se já existe arquivo em `references/`:
- Se existe → leia o arquivo, use como base, e complemente com pesquisa se necessário
- Se não existe → vá pro Passo 3
- (NOVO v2) Se existe um MOC (Map of Content) relacionado → consulte pra entender o panorama antes de mergulhar

### Passo 3: Pesquisar e curar referências

Use web search pra encontrar as melhores referências. Pesquise em camadas:

**Camada 1 — Obras seminais (atemporais):**
- Busque: "[tema] best books all time", "[tema] seminal framework", "[tema] bible book"
- O que procurar: livros que são unanimidade na área, frameworks que todo profissional conhece, autores que são sinônimo do tema
- Exemplos: SPIN Selling pra vendas complexas, Getting Things Done pra produtividade, Lean Startup pra validação de produto

**Camada 2 — Frameworks e metodologias práticas:**
- Busque: "[tema] framework practical", "[tema] methodology", "how to [tema] step by step"
- O que procurar: modelos que o usuário pode aplicar imediatamente, com passos claros
- Exemplos: OKRs pra definir metas, RICE pra priorização, Jobs To Be Done pra entender clientes

**Camada 3 — Referências recentes e evolução:**
- Busque: "[tema] 2025 2026 trends", "[tema] latest research", "[tema] modern approach"
- O que procurar: o que mudou recentemente no campo, novas abordagens, debates atuais
- Nem todo tema precisa dessa camada — se as referências seminais ainda são válidas e nada mudou, diga isso

**Camada 4 — Pessoas e autoridades:**
- Busque: "[tema] expert thought leader", "[tema] who to follow"
- O que procurar: quem são as pessoas que o usuário deveria conhecer/seguir nesse domínio

### Passo 4: Apresentar as referências

Organize o output assim:

```
## [Tema] — Referências Fundamentais

### Obras seminais (atemporais)
- **[Nome do livro/framework]** — [Autor], [Ano]
  - O que é: [1-2 frases]
  - Por que importa: [como se aplica ao contexto do usuário]
  - Conceito-chave: [o framework/ideia principal que o usuário pode aplicar já]

### Frameworks práticos
- **[Nome do framework]** — [Origem/Autor]
  - Como funciona: [descrição prática em 2-3 frases]
  - Quando usar: [situação ideal]
  - Quando NÃO usar: [limitações]

### Referências recentes (se relevante)
- **[Artigo/livro/estudo]** — [Autor], [Ano]
  - O que mudou: [como o campo evoluiu]

### Pessoas pra seguir
- **[Nome]** — [quem é, por que importa]

### Conexões com referências existentes (NOVO v2)
- [Se alguma referência encontrada se conecta com algo já salvo em references/, liste aqui]
- Exemplo: "Shape Up (já em lideranca-references.md) complementa o ciclo de desenvolvimento mencionado em [referência nova]"

### Minha recomendação pro seu contexto
[Dado o que sei sobre o usuário (equipe pequena, SMB, transição de operacional pra liderança), recomendo começar por X porque Y. Ignorar Z porque não se aplica.]
```

### Passo 5: Salvar e conectar (ATUALIZADO v2)

Depois de apresentar, salve as referências usando o sistema de organização abaixo.

## Sistema de organização de referências (NOVO v2)

### Modelo: Hub-and-Spoke (PARA + Zettelkasten)

A base de referências usa dois sistemas complementares:

**PARA (Tiago Forte) como Hub — organização por acionabilidade:**
- **Projects** — referências ativamente sendo usadas num projeto atual (ex: referências de NVC enquanto prepara feedback pra equipe)
- **Areas** — referências de responsabilidades contínuas (ex: liderança, arquitetura, vendas)
- **Resources** — referências de interesse futuro ou aprendizado (ex: IA generativa, economia)
- **Archives** — referências de projetos concluídos (movidas quando o projeto acaba)

Na prática dentro desta skill: os arquivos em `references/` são organizados por domínio (que correspondem a Areas no PARA). O próprio nome do arquivo indica a área: `lideranca-references.md`, `vendas-references.md`, `infra-references.md`.

**Zettelkasten como Spoke — conexões entre referências:**
- Cada referência salva deve ter pelo menos uma **conexão** com outra referência já existente
- Conexões são bidirecionais: "A complementa B" e "B é complementado por A"
- Com o tempo, as conexões revelam padrões e insights que referências isoladas não mostram

### MOCs — Maps of Content (NOVO v2)

MOCs são índices temáticos que conectam referências de múltiplos domínios. Crie um MOC quando:
- Um tema cruza 3+ domínios diferentes (ex: "escalar operação" cruza liderança + infra + produto)
- O usuário está tomando uma decisão estratégica que envolve múltiplas áreas
- Referências de domínios diferentes se complementam de forma não-óbvia

Formato de MOC:
```markdown
# MOC: [Tema transversal]

Última atualização: [data]

## Por que este MOC existe
[1-2 frases sobre por que essas referências precisam ser vistas juntas]

## Referências por domínio

### De lideranca-references.md
- [Referência] — relevância pro tema: [como se conecta]

### De infra-references.md
- [Referência] — relevância pro tema: [como se conecta]

### De produto-references.md
- [Referência] — relevância pro tema: [como se conecta]

## Insight da conexão
[O que emerge quando você olha essas referências juntas que não seria óbvio olhando cada uma isolada]
```

Salve MOCs em `references/moc-[tema].md`.

### Formato de arquivo de referências (ATUALIZADO v2)

```markdown
# [Domínio] — Base de Referências

Última atualização: [data]

## Obras seminais
- **[Livro]** — [Autor] ([Ano]): [1 frase do que é]
  - Conexões: → [outra referência no mesmo ou outro arquivo] (NOVO v2)

## Frameworks
- **[Framework]** — [Autor/Origem]: [1 frase de como funciona]
  - Conexões: → [framework complementar ou alternativo] (NOVO v2)

## Pessoas
- **[Nome]**: [quem é]

## Conexões cruzadas (NOVO v2)
- Este domínio se conecta com: [lista de outros arquivos de referências e por quê]

## Notas
- [Observações relevantes pro contexto do usuário]
```

Se o arquivo já existia, ATUALIZE em vez de recriar. Adicione novas referências e atualize conexões.

## Quando sugerir Obsidian (NOVO v2)

Se o usuário demonstrar interesse em manter referências de forma organizada FORA do Claude:

**Obsidian** é a ferramenta recomendada porque:
- Markdown puro (os arquivos de `references/` são compatíveis)
- Links bidirecionais nativos (`[[referência]]`) — perfeito pro Zettelkasten
- Graph view mostra conexões visualmente
- Plugins: Dataview (queries), Templates, Daily Notes
- Offline-first, dados locais
- Free pra uso pessoal

**Não force.** Só sugira se o usuário demonstrar que quer algo mais robusto que os arquivos de referência dentro do Claude. A maioria das vezes, `references/` dentro das skills é suficiente.

## Exemplo de output

**Input do usuário:** "Preciso fundamentar minha abordagem de priorização de backlog"

**Output da skill:**

```
### Priorização de Backlog — Referências Fundamentais

#### Obras seminais (atemporais)
- **Inspired** — Marty Cagan, 2008 (rev. 2018)
  - O que é: Referência em product management, cobre priorização como parte do processo de discovery
  - Por que importa: Framework de oportunidades de Cagan ajuda a filtrar o backlog pelo valor real
  - Conceito-chave: "Fall in love with the problem, not the solution" — priorize problemas, não features

#### Frameworks práticos
- **RICE** — Intercom
  - Como funciona: Reach × Impact × Confidence / Effort = score. Ordena do maior pro menor.
  - Quando usar: Backlog com 10+ itens onde precisa de critério objetivo
  - Quando NÃO usar: Itens urgentes do dia a dia — aí é Impacto × Esforço simples

- **Kano Model** — Noriaki Kano, 1984
  - Como funciona: Classifica features em Básico (must-have), Performance (mais é melhor), Encantamento (wow)
  - Quando usar: Pra entender o TIPO de cada feature antes de priorizar
  - Quando NÃO usar: Já sabe o que é must-have — pule direto pra RICE

#### Conexões com referências existentes
- **ICE Scoring** (já em lideranca-references.md) é alternativa ao RICE pra priorização rápida de experimentos
- **WSJF** (já em lideranca-references.md) complementa quando há urgência diferenciada entre itens
- **Shape Up** (já em lideranca-references.md) define como os itens priorizados entram em ciclos de execução

#### Minha recomendação pro seu contexto
Com equipe de 3-5 pessoas e projetos PME, use Kano pra classificar e depois RICE pra ordenar. Comece cobrindo 100% do Básico antes de qualquer Performance ou Encantamento.
```

## Integração com outras skills

Esta skill pode ser acionada POR DENTRO de outras skills:

- **Product Discovery & PRD:** "Antes de definir a solução, quer que eu busque como outros produtos resolvem esse problema?"
- **Tech Lead & PM:** "Pra priorização, o framework RICE é um dos mais usados, mas tem alternativas. Quer que eu busque?"
- **Comunicação com Clientes:** "Pra lidar com essa reclamação, a abordagem do livro X sugere..."
- **n8n Architect:** "Pra esse padrão de integração, a documentação oficial do n8n recomenda..."

Quando acionada por outra skill, seja breve — traga 1-2 referências relevantes inline, não faça o processo completo de 5 passos.

## Regras críticas

1. **NUNCA invente referências.** Se não tem certeza que um livro existe ou que um autor disse algo, pesquise antes. Referência inventada destrói credibilidade.
2. **SEMPRE use web search** quando o tema é fora do seu conhecimento profundo ou quando precisa de referências recentes. Não confie só no training data.
3. **Cite corretamente.** Nome do livro, autor, ano. Se não sabe o ano, pesquise.
4. **Filtre pra o contexto.** Harvard Business Review é ótima mas se o usuário é uma agência de 5 pessoas em Ilha Solteira, muita coisa não se aplica. Diga isso.
5. **Quantidade ≠ qualidade.** 3 referências excelentes > 15 referências genéricas. Curadoria é o valor.
6. **(NOVO v2) Conecte sempre.** Ao salvar referências, identifique pelo menos uma conexão com referências existentes. Referência isolada é nota perdida.
7. **(NOVO v2) Não force organização.** O sistema PARA + Zettelkasten + MOCs é a recomendação, mas a prioridade é que as referências sejam ÚTEIS. Se o sistema atrapalha mais do que ajuda, simplifique.

## Quando NÃO usar esta skill

- Se o usuário quer uma resposta rápida e direta — não force referências em tudo
- Se o tema é puramente técnico e específico (ex: "como configurar RLS no Supabase") — isso é skill técnica, não referência
- Se o usuário já tem referências e só quer aplicar — ajude a aplicar, não traga mais referências
