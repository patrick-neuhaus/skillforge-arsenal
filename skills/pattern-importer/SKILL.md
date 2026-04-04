---
name: pattern-importer
description: "Automate the .tmp technique: clone reference repositories, analyze implementation patterns, and generate pattern documents. Few-shot learning from real codebases to improve your implementations. Use when user asks: 'importa um padrão', import pattern, 'como isso é feito em outros projetos?', clone reference, .tmp technique, 'quero ver como X faz isso', 'pega um exemplo de implementação', review pattern from repo, 'busca referência de código', learn from repo, 'clona pra eu ver o padrão', check reference implementation, 'tem repo de exemplo?', pattern extraction, create pattern document, 'quero ver um exemplo real', analyze reference repo, study implementation, analisar código de referência, revisar padrão. Sub-step of SDD Phase 1 Research. NÃO use pra copiar código — use pra entender PADRÕES."
---

# Pattern Importer — Técnica .tmp Automatizada

IRON LAW: NEVER leave .tmp directories behind. Every import operation MUST end with cleanup confirmation. An orphaned .tmp/ is technical debt that confuses the codebase and can accidentally be committed.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--import` | Full pipeline: identify → clone → analyze → extract → clean | default |
| `--analyze` | Clone and analyze only (no extraction document) | - |
| `--clean` | Just clean up existing .tmp/ directories | - |
| `--list` | List curated reference repos by domain | - |

## Workflow

```
Pattern Importer Progress:

- [ ] Step 1: Identify Target ⚠️ REQUIRED
  - [ ] 1.1 What pattern do you need? (auth flow, editor, DnD, etc.)
  - [ ] 1.2 Find reference repo(s) (search or curated list)
  - [ ] 1.3 Identify specific files/folders to clone
- [ ] Step 2: Clone
  - [ ] 2.1 Clone to .tmp/ with depth 1
  - [ ] 2.2 Remove .git from clone
  - [ ] 2.3 Verify .tmp/ is in .gitignore
- [ ] Step 3: Analyze
  - [ ] 3.1 Read relevant files
  - [ ] 3.2 Document the pattern (structure, composition, edge cases)
  - [ ] 3.3 Note differences with your project's stack/conventions
- [ ] Step 4: Extract & Clean ⛔ BLOCKING
  - [ ] 4.1 Write pattern document (what to apply, how to adapt)
  - [ ] 4.2 Delete .tmp/ directory
  - [ ] 4.3 Verify .tmp/ is gone
  - [ ] ⛔ GATE: Confirm cleanup before finishing
```

If `--analyze`: Steps 1-3 only → present analysis without extraction document.
If `--clean`: Skip to 4.2-4.3 → clean up any .tmp/ directories.
If `--list`: Show curated repos from `references/import-workflow.md` → done.

## Step 1: Identify Target

Ask (if not clear from context):
- "Qual padrão você precisa?" — auth, rich text editor, DnD, payment, real-time, etc.
- "Qual sua stack?" — para encontrar repos compatíveis (Next.js, React, Supabase, etc.)
- "Precisa de algo específico?" — um componente, um flow, uma arquitetura completa

### Finding Reference Repos

Load `references/import-workflow.md` for curated repos by domain.

Search strategies:
```bash
# GitHub search
# "rich text editor" language:typescript stars:>100

# Ask Claude
# "Qual repo open source implementa bem [pattern] com [stack]?"

# Check awesome-* lists
# awesome-nextjs, awesome-react, awesome-supabase
```

**Regra:** Máximo 2 repos de referência. Mais que isso confunde em vez de ajudar.

## Step 2: Clone

### Clone Parcial (preferido)

```bash
# Opção A: Repo inteiro (shallow)
git clone --depth 1 <repo-url> .tmp/<name>
rm -rf .tmp/<name>/.git

# Opção B: Pasta específica (via degit)
npx degit user/repo/path/to/folder .tmp/<name>

# Opção C: Download direto de arquivos específicos
mkdir -p .tmp/<name>
curl -sL "https://raw.githubusercontent.com/user/repo/main/path/file.ts" > .tmp/<name>/file.ts
```

### Safety Checks

```bash
# Garantir .gitignore tem .tmp/
grep -q "^\.tmp/" .gitignore 2>/dev/null || echo ".tmp/" >> .gitignore

# Verificar que .tmp/ não está tracked
git status .tmp/ 2>/dev/null
```

Load `references/cleanup-rules.md` for safety protocols.

## Step 3: Analyze

Analisar com foco em PADRÕES, não em código específico.

### Prompt de Análise

```
"Analisa a implementação em .tmp/<name>/.
Foco em:
1. Estrutura de arquivos — como estão organizados
2. Padrões de composição — como componentes/módulos se conectam
3. Tratamento de edge cases — o que eles consideram
4. Decisões de design — por que fizeram assim (não apenas como)

NÃO sugira melhorias — apenas documente o padrão como ele é.
NÃO copie código — descreva o padrão em nível conceitual."
```

### O que Documentar

| Aspecto | Pergunta-chave |
|---------|---------------|
| **Estrutura** | Como os arquivos estão organizados? Há padrão de pastas? |
| **Composição** | Como componentes se conectam? Props drilling? Context? Store? |
| **Data flow** | De onde vêm os dados? Como fluem? Server → Client? |
| **Error handling** | Como erros são tratados? Boundaries? Fallbacks? |
| **Edge cases** | Quais cenários não-óbvios o código trata? |
| **Adaptação** | O que muda ao aplicar no nosso projeto? (stack, convenções) |

## Step 4: Extract & Clean

### Pattern Document

Salvar como `pattern-[nome].md` no projeto (ou incluir no prd.md do SDD):

```markdown
# Pattern: [Nome do Padrão]
**Source:** [repo-url]
**Analyzed:** [data]
**Files studied:** [lista]

## Pattern Summary
[2-3 frases descrevendo o padrão]

## Structure
[Como os arquivos estão organizados]

## Key Decisions
- [decisão 1 — por quê]
- [decisão 2 — por quê]

## Adaptation Notes
- [diferença 1: no repo usam X, no nosso usamos Y]
- [diferença 2: adaptar Z por causa de W]

## Applicable to Our Project
1. [insight aplicável — como implementar]
2. [insight aplicável — como implementar]
```

### Cleanup (OBRIGATÓRIO)

```bash
# Deletar .tmp/
rm -rf .tmp/

# Confirmar que sumiu
ls .tmp/ 2>/dev/null && echo "ERRO: .tmp ainda existe!" || echo "✓ Clean"
```

⛔ **GATE:** Confirmar que .tmp/ foi removido antes de finalizar.

## Anti-Patterns

- **Copiar código direto:** O objetivo é entender o PADRÃO, não fazer copy-paste
- **Clonar repo inteiro de 500MB:** Use clone parcial ou degit pra pasta específica
- **Analisar 5+ repos:** Máximo 2. Mais confunde — diminishing returns
- **Esquecer de limpar:** .tmp/ commitado acidentalmente é constrangedor
- **Não adaptar ao contexto:** Padrão de Next.js 13 pode não aplicar a Next.js 15
- **Ignorar licença:** Se vai usar código (não apenas padrão), verifique a licença

## Pre-Delivery Checklist

- [ ] Pattern document escrito com insights aplicáveis
- [ ] .tmp/ directory deletado e confirmado
- [ ] .gitignore contém `.tmp/`
- [ ] Nenhum código copiado literalmente (apenas padrões)
- [ ] Fonte (repo URL) documentada

## When NOT to use

- Padrão já conhecido e documentado → consulte docs oficiais direto
- Quer copiar código, não entender padrão → clone o repo normal, sem .tmp trick
- Pesquisa de frameworks/referências teóricas → use **reference-finder**
- Implementação do padrão → use **SDD** (este skill apenas EXTRAI o padrão)

## Integration

- **SDD** — Phase 1, Step 7: sub-etapa opcional da Research. Output alimenta prd.md
- **Reference Finder** — reference-finder busca TEORIA (livros, frameworks); pattern-importer busca PRÁTICA (código real)
- **Component Architect** — após extrair padrão de componentes, component-architect planeja a implementação
