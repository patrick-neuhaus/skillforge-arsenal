# ByteRover Context Tree — Análise Técnica

**Fonte:** https://docs.byterover.dev/
**Objetivo:** Entender como o ByteRover mantém contexto persistente por meses e como replicar.

## O que é

ByteRover é um CLI local-first que dá memória persistente a agentes de IA. O sistema central é o **Context Tree**: uma base de conhecimento hierárquica em markdown, armazenada em `.brv/context-tree/`.

## Arquitetura

### Hierarquia (3 níveis)
```
.brv/context-tree/
├── authentication/          # Domínio
│   ├── context.md           # Escopo do domínio
│   ├── _index.md            # Resumo condensado (auto-gerado)
│   ├── jwt-implementation/  # Tópico
│   │   ├── context.md
│   │   ├── _index.md
│   │   ├── jwt_token_generation.md    # Arquivo de conhecimento
│   │   └── refresh-tokens/            # Subtópico (max 1 nível)
│   │       ├── context.md
│   │       └── refresh_token_rotation.md
│   └── session-management/  # Tópico
│       └── ...
├── api-design/              # Domínio
│   └── ...
└── _manifest.json           # Registro global com token budgeting
```

### Arquivos do Sistema

| Arquivo | Propósito | Localização |
|---------|-----------|-------------|
| `context.md` | Escopo, propósito e limites de cada nível | Todo domínio/tópico/subtópico |
| `_index.md` | Resumo condensado auto-gerado (YAML frontmatter) | Todo diretório com updates |
| `_manifest.json` | Registro global com 3 lanes (summaries, contexts, stubs) | Raiz do context tree |

## Formato dos Arquivos de Conhecimento

```yaml
---
title: JWT Token Generation
tags: [auth, jwt, security]
keywords: [token, generation, signing]
related: ["authentication/session-management"]
importance: 72
recency: 0.85
maturity: validated
accessCount: 15
updateCount: 3
createdAt: 2025-01-15
updatedAt: 2025-03-20
---

## Raw Concept
- task, files, flow, patterns

## Narrative
- structure, rules, examples, diagrams

## Facts
- structured statements with categories
```

## Sistema de Scoring

### Importance (0-100)
- Começa em 50
- +3 por resultado de busca (alguém achou útil)
- +5 por atualização curada

### Recency (0-1)
- Reset pra 1.0 em cada update
- Halves a cada ~21 dias (decay exponencial)

### Maturity Tiers
| Tier | Threshold | Efeito |
|------|-----------|--------|
| `draft` | <35 | Elegível pra archiving |
| `validated` | 65-85 | +8% boost em buscas |
| `core` | ≥85 | +15% boost em buscas |

## Sistema de Archive

Critério: maturity=`draft` AND importance<35

Arquivos archivados viram:
- `.stub.md` — "Ghost cue" compacto (~220 tokens), permanece buscável via BM25
- `.full.md` — Backup lossless, não buscável

Ambos em `_archived/` espelhando paths originais.

## Resumos Hierárquicos (_index.md)

| Nível | Ordem | Cobertura |
|-------|-------|-----------|
| Root | d3 | Todos os domínios |
| Domínio | d2 | Todos os tópicos |
| Tópico | d1 | Todo conhecimento |
| Subtópico | d0 | Foco único |

Mudanças propagam pra cima automaticamente. Excluídos de BM25 mas injetados como contexto estrutural em queries.

## Manifest (_manifest.json)

3 lanes:
- `summaries` — ordenado por condensação (mais amplo primeiro)
- `contexts` — ordenado por importance score
- `stubs` — ordem de inserção

## Relações

Campo `related` usa paths explícitos: `"authentication/session-management"`. Permite navegação graph-like além de similaridade textual.

---

## Como Replicar no Skillforge Arsenal

### Versão Simplificada Proposta

```
context-tree/
├── frontend/
│   ├── _index.md          # Resumo do domínio
│   ├── design-systems.md  # Tópico
│   ├── react-patterns.md
│   └── accessibility.md
├── backend/
│   ├── _index.md
│   ├── supabase.md
│   └── auth.md
├── devops/
│   └── ...
└── _manifest.json         # Índice global
```

### Simplificações vs ByteRover
- Sem scoring automático (import/recency manual)
- Sem archive automático (review periódico)
- Sem daemon (tudo via skills que leem/escrevem refs)
- `_manifest.json` simples: lista de arquivos + descrições
- Cross-pollination via campo `related` nos frontmatter

### Integração com Skills
- Cada skill pode referenciar refs do context-tree
- Ao encontrar algo útil, skill escreve no context-tree
- Reference Finder v3 seria o "curador" principal
