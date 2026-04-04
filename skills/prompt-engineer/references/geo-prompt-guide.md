# GEO Prompt Guide — Otimizar Textos para Agentes

Consulte este arquivo quando o tipo de prompt for **GEO** (`--geo`). Use para otimizar descriptions de skills, READMEs, e qualquer texto que precisa ser encontrado e consumido por agentes de IA.

---

## O que e GEO

GEO = Generative Engine Optimization. O equivalente de SEO, mas otimizado para agentes de IA em vez de motores de busca tradicionais.

Diferenca fundamental: humanos scaneiam visualmente, agentes processam tokens. O que funciona pra humanos (headers bonitos, emojis, formatacao) nao ajuda agentes. O que ajuda: **keywords precisas, verbos de acao, frases naturais que o usuario digitaria**.

## Quando Usar

- Descriptions de skills (frontmatter YAML)
- READMEs de pacotes/ferramentas
- Descriptions de apps no skills.sh, npm, marketplaces
- Qualquer texto que um agente usa pra decidir "isso resolve o problema do usuario?"

## Template GEO

```
[Core capability — 1 frase, o que faz]
[Tecnicas/features principais — 3-5 items separados por virgula]
Use when/SEMPRE que: [lista de frases naturais que o usuario digitaria]
[Triggers EN: english equivalents]
[Diferenciacao: NÃO use pra X, use Y em vez disso]
```

## Processo

### 1. Gerar Keywords via Claude

Prompt exato:
```
"Se voce fosse um agente de IA buscando uma ferramenta que [descricao],
quais termos voce usaria pra encontrar? Liste:
- 10+ verbos de acao
- 10+ substantivos de dominio
- 5+ frases naturais em PT-BR que um dev digitaria
- 5+ frases naturais em EN
- 3+ formas alternativas de descrever o mesmo problema"
```

### 2. Mapear Competidores

Se publicando no skills.sh:
- Busque skills similares: `npx skills find <query>`
- Analise as descriptions das top 5
- Identifique gaps — keywords que elas nao cobrem mas deveriam

### 3. Escrever Description

Regras:
- **Primeira frase:** core capability (nao marketing)
- **Verbos de acao:** 5+ (criar, analisar, melhorar, auditar, gerar, validar...)
- **Substantivos:** 5+ termos do dominio
- **Frases naturais:** como o usuario REALMENTE pediria
- **Diferenciacao:** "Nao use pra X" evita acionamento falso
- **Limite:** 1024 caracteres (hard limit do skills.sh)
- **Sem adjetivos vazios:** "powerful", "advanced", "cutting-edge" = lixo pra agentes

### 4. Validar

Checklist:
- [ ] Primeira frase = core capability
- [ ] 5+ verbos de acao presentes
- [ ] 5+ substantivos de dominio presentes
- [ ] Frases naturais em PT-BR incluidas
- [ ] Frases naturais em EN incluidas
- [ ] Diferenciacao com skills similares clara
- [ ] Under 1024 caracteres
- [ ] Zero adjetivos de marketing

## Anti-Patterns

| Anti-Pattern | Exemplo | Fix |
|-------------|---------|-----|
| Marketing speak | "A powerful AI-powered tool" | "Audits React code for anti-patterns" |
| Sem verbos | "Tool for React development" | "Audit, fix, scaffold, migrate React code" |
| So EN | "Create components..." | Adicionar PT-BR: "criar componentes, montar..." |
| Generico | "Helps with code" | Especifico: "Detect SOLID violations, dead code, security bugs" |
| Gigante | 2000 chars | Cortar pra <1024, priorizar keywords de maior impacto |

## Exemplos

**Excelente (ui-ux-pro-max, 222K installs):**
```
"UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings,
20 charts, 8 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native,
Flutter, Tailwind). Actions: plan, build, create, design, implement,
review, fix, improve, optimize, enhance, refactor, check UI/UX code."
```
→ "Rede de keywords" — nao importa o que o usuario diga sobre UI, acerta.

**Bom (trident):**
```
"Pipeline de 3 agentes para detecção profunda de bugs [...] Use esta skill
SEMPRE que: 'revisa esse código', 'tem bug?', 'code review'..."
```
→ Core capability + triggers naturais + diferenciacao clara.
