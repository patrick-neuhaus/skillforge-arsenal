# Keyword Generation — Templates por Dominio

Consulte este arquivo no **Step 2** para gerar keywords organizadas por categoria.

---

## Framework de Keywords: 4 Dimensoes

Toda description precisa cobrir 4 dimensoes. Use este framework como checklist.

### Dimensao 1: Verbos de Acao

O que o usuario PEDE pra fazer. Sempre incluir tanto PT-BR quanto EN.

| Categoria | Verbos PT-BR | Verbos EN |
|-----------|-------------|-----------|
| Criacao | criar, montar, gerar, construir, iniciar | create, build, generate, scaffold, init |
| Melhoria | melhorar, otimizar, refatorar, evoluir | improve, optimize, refactor, enhance |
| Analise | analisar, revisar, auditar, inspecionar | analyze, review, audit, inspect, check |
| Correcao | corrigir, consertar, resolver, debugar | fix, repair, resolve, debug, patch |
| Validacao | validar, verificar, testar, checar | validate, verify, test, check, lint |
| Transformacao | converter, migrar, transformar, extrair | convert, migrate, transform, extract |
| Organizacao | organizar, estruturar, catalogar, documentar | organize, structure, catalog, document |

### Dimensao 2: Substantivos de Dominio

O que o usuario MENCIONA. Especifico ao dominio da skill.

**Exemplos por dominio:**

| Dominio | Substantivos |
|---------|-------------|
| Frontend | componente, pagina, layout, design system, estilo, CSS, tema |
| Backend | API, endpoint, rota, middleware, schema, migration |
| Database | tabela, coluna, index, RLS, policy, query, foreign key |
| DevOps | server, container, deploy, pipeline, CI/CD, VPS |
| Automacao | workflow, webhook, trigger, node, integracao |
| Design | tokens, paleta, tipografia, espacamento, grid, animacao |
| Seguranca | vulnerabilidade, OWASP, injection, XSS, autenticacao |

### Dimensao 3: Frases Naturais

O que o usuario LITERALMENTE digitaria. Mais importante que keywords isoladas.

**Templates de frases naturais:**

PT-BR:
- "[verbo] [substantivo]" — "criar componente", "revisar codigo"
- "como [verbo] [substantivo]" — "como organizar meus componentes"
- "[substantivo] ta [adjetivo-problema]" — "o codigo ta baguncado"
- "preciso de [substantivo]" — "preciso de um design system"
- "quero [verbo]" — "quero melhorar a performance"

EN:
- "[verb] [noun]" — "review code", "create component"
- "how to [verb]" — "how to optimize queries"
- "[noun] is [problem]" — "build is slow"
- "I need to [verb]" — "I need to audit security"

### Dimensao 4: Diferenciacao

O que a skill NAO faz. Evita acionamento falso.

**Template:**
```
NÃO use pra [X] — use [skill-Y].
Se é [cenario-confuso], use [skill-Z] em vez desta.
```

## Processo de Geracao

### Passo 1: Brainstorm Bruto
Use o prompt do Step 2.1 do SKILL.md pra gerar 30+ keywords brutas.

### Passo 2: Classificar
Organize nas 4 dimensoes. Identifique gaps:
- Faltam verbos? Adicione acao.
- Faltam substantivos? Adicione dominio.
- Faltam frases naturais? Adicione linguagem real.
- Falta diferenciacao? Identifique skills similares.

### Passo 3: Priorizar
- **Must-have:** Keywords que definem a skill. Sem elas, nao aciona.
- **Should-have:** Keywords que ampliam cobertura. Melhoram recall.
- **Nice-to-have:** Keywords de edge case. Bonus.

### Passo 4: Comprimir
Caber em 1024 caracteres. Prioridade: must-have > should-have > nice-to-have.
Tecnica: combinar keywords em frases ("criar, melhorar e auditar componentes React").

## Exemplo Completo

**Skill: trident (code review)**

Verbos: revisar, auditar, analisar, detectar, verificar, review, audit, scan, check, find
Substantivos: codigo, bugs, vulnerabilidades, SOLID, dead code, security, quality
Frases PT-BR: "revisa esse codigo", "tem bug nisso?", "faz um audit", "code review"
Frases EN: "review code", "find bugs", "audit code", "check for vulnerabilities"
Diferenciacao: "NAO use pra UX (use ux-audit) ou mudancas triviais"
