---
name: supabase-db-architect
description: "Supabase/PostgreSQL database architecture for SMB apps. Create schemas, design data models, review AI-generated databases (Lovable/Bolt/Cursor), optimize RLS policies, audit security gaps, plan migrations (DynamoDB→PostgreSQL), validate indexes, build multi-tenant structures, fix performance bottlenecks. Triggers PT-BR: 'schema', 'tabela', 'banco', 'supabase', 'RLS', 'migration', 'index', 'esse schema tá bom?', 'como estruturo isso?', 'avalia meu banco'. Triggers EN: 'database design', 'schema review', 'row level security', 'migration plan', 'index strategy'. Diferencial: combina pragmatismo PME (MVP vs produção) com segurança nativa Supabase (RLS, auth.uid, Supavisor, pgmq). NÃO use pra workflow n8n sem banco → n8n-architect. NÃO use pra frontend sem dados. Mesmo com MCP Supabase disponível, auditorias e revisões de policies passam por esta skill. Triggers: 'como tá meu banco', 'policies certas', 'auditar supabase'."
---

# Supabase Database Architect v4

IRON LAW: NUNCA crie uma tabela sem RLS policies. Uma tabela desprotegida é um vazamento de dados esperando acontecer. Se a tabela é server-only, habilite RLS sem policies (deny-all por padrão).

## Filosofia

O usuário constrói produtos com Supabase + n8n + Lovable pra PMEs. Agilidade > perfeição teórica.

- **Pragmático sobre acadêmico** — 3FN é ótimo em livro, mas desnormalizar pra economizar 3 JOINs pode ser certo pra MVP. Explique o tradeoff.
- **Ensine o porquê** — nunca diga "adiciona um index" sem explicar o impacto.
- **Contexto importa** — MVP pra 50 usuários != produção com 10k simultâneos. Pergunte.
- **Nativo do Supabase** — RLS, Edge Functions, Realtime, pg_cron, pgmq, Supavisor, Branching. Não sugira genérico quando tem nativo.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | Modo: evaluate, design, simplify, quick | auto-detect |
| `--context <c>` | Contexto: mvp, production | mvp |
| `--source <s>` | Origem do schema: lovable, bolt, cursor, manual, dynamo | - |

## Modos de operação

| Modo | Trigger | O que faz |
|------|---------|-----------|
| `evaluate` | "isso tá bom?", dump SQL, schema de IA | Avaliação 5 camadas |
| `design` | "monta isso pra mim", problema de negócio | Design completo |
| `simplify` | "faz portável", handoff pra cliente | Versão enxuta n8n+Supabase |
| `quick` | "devo indexar?", "essa RLS tá certa?" | Resposta direta |

## Workflow

```
Supabase DB Architect Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Identificar modo (evaluate/design/simplify/quick)
  - [ ] 1.2 Definir contexto (MVP vs produção)
  - [ ] 1.3 Identificar origem do schema (se evaluate)
- [ ] Step 2: Análise
  - [ ] 2.1 [evaluate] Rodar framework 5 camadas
    Load references/schema-evaluation.md
  - [ ] 2.2 [design] Mapear entidades e relacionamentos
  - [ ] 2.3 [simplify] Identificar entidades core vs artefatos de UI
  - [ ] 2.4 [quick] Responder direto com raciocínio
- [ ] Step 3: RLS ⚠️ REQUIRED (todos os modos)
  - [ ] 3.1 Toda tabela tem RLS habilitado?
  - [ ] 3.2 Policies usam (select auth.uid()) com parênteses?
  - [ ] 3.3 Indexes nas colunas filtradas por RLS?
  Load references/rls-patterns.md
- [ ] Step 4: Output
  - [ ] 4.1 SQL completo com comentários
  - [ ] 4.2 Notas de evolução (MVP → produção)
  - [ ] ⛔ GATE: Confirmar antes de rodar migrations em produção
- [ ] Step 5: Migração (se aplicável)
  - [ ] ⛔ GATE: "Isso vai rodar em produção? Confirme antes de prosseguir."
  - [ ] 5.1 Ordem: ADD → backfill → constrain → DROP
  - [ ] 5.2 Testar em branch antes de produção
  Load references/migration-patterns.md
```

## Framework de avaliação (5 camadas)

Quando avaliar schemas (especialmente de IA), passe pelas 5 camadas. Detalhes completos em `references/schema-evaluation.md`.

| Camada | Foco | Red flags comuns |
|--------|------|------------------|
| 1. Integridade estrutural | PKs, FKs, tipos, naming | `text` pra tudo, serial integers, sem FKs |
| 2. Relacionamentos | 1:N, N:M, polimórficos | Arrays JSONB pra N:M, sem ON DELETE |
| 3. Supabase-specific | RLS, timestamps, soft deletes | RLS desabilitado, USING(true), sem updated_at |
| 4. Performance | Indexes, RLS perf, JSONB, particionamento | Sem index em FK, auth.uid() sem select wrapper |
| 5. Red flags de IA | Tabelas faz-tudo, over/under-engineering | 30+ colunas, tudo em JSONB, nomes genéricos |

### Regra de ouro de RLS performance

```sql
-- RUIM: auth.uid() chamado pra CADA linha
CREATE POLICY "x" ON t USING (auth.uid() = user_id);

-- BOM: (select auth.uid()) cacheado como initPlan, 1x por query — até 100x+ melhoria
CREATE POLICY "x" ON t USING ((select auth.uid()) = user_id);
```

SEMPRE combine com index btree na coluna filtrada.

## Diretrizes por contexto

### MVP (velocidade > perfeição)

- Mínimo de tabelas, `text` pra campos incertos
- RLS simples: `(select auth.uid()) = user_id`
- JSONB `metadata` pra dados ad-hoc
- Sem particionamento, sem materialized views
- MAS: FKs e NOT NULL constraints sempre — pegam bugs cedo, custam nada

### Produção (confiabilidade > velocidade)

- Apertar tipos com CHECK constraints
- Indexes baseados em `pg_stat_user_indexes`
- RLS abrangentes com pattern `(select ...)`
- Trilhas de auditoria, pg_cron, read replicas
- Log Drains + Branching pra testar migrations

## Realtime: quando usar e quando não

| Usar | Não usar |
|------|----------|
| Dashboards com updates instantâneos | Tabelas de alto volume (logs, filas) |
| Listas colaborativas | Dados sensíveis sem RLS adequado |
| Status updates de processamento | Quando polling 30s resolve |

3 features: Broadcast (mensagens), Presence (quem tá online), Postgres Changes (notifica mudanças no banco).

## JSONB: quando usar vs normalizar

| JSONB | Normalizar |
|-------|-----------|
| Estrutura varia entre linhas | Consulta por campos específicos |
| Dados lidos como blob inteiro | Precisa de FK/constraints |
| Respostas de API de terceiros | Precisa agregar/ordenar por valores |
| Metadata/settings de MVP | Múltiplas linhas referenciam mesmos dados |

**Padrão de graduação:** comece JSONB no MVP, promova pra colunas quando padrões emergirem.

## Escalabilidade (em ordem)

1. **Otimize queries** — `EXPLAIN ANALYZE` antes de mudar infra
2. **Indexes parciais + particionamento** — `pg_partman` pra milhões de linhas
3. **Upstash Redis** — buffer pra filas de alta velocidade
4. **Read replicas** — dashboards read-heavy

90% dos casos PME resolve dentro do Supabase com melhor schema + indexes + cache.

## Anti-patterns

- **RLS ausente ou USING(true)** — a red flag mais grave. Expõe dados de todos os usuários via anon key.
- **auth.uid() sem (select ...)** — performance até 100x pior em tabelas grandes. É a otimização mais impactante que existe.
- **Single-table design (padrão DynamoDB)** — anti-pattern no PostgreSQL. Quebre em tabelas dedicadas com FKs.
- **Tudo em JSONB** — "é flexível" não é justificativa. Se consulta por campo, normalize.
- **Tabela faz-tudo com 30+ colunas** — sinal de que entidades distintas foram misturadas.
- **Migração sem branch** — rodar ALTER TABLE direto em produção sem testar antes.
- **Index em tudo** — todo index desacelera INSERT/UPDATE. Indexe baseado em queries reais.
- **varchar(255)** — hábito de MySQL. No Postgres, use `text`.
- **Serial integers como PK** — vazam contagem e ordem. Use `gen_random_uuid()`.
- **Ignorar ON DELETE** — FKs sem CASCADE/SET NULL/RESTRICT = orfãos no banco.

## Pre-delivery checklist

- [ ] Toda tabela tem RLS habilitado (mesmo server-only)
- [ ] Policies usam `(select auth.uid())` com parênteses
- [ ] FKs com ON DELETE explícito em todo relacionamento
- [ ] `created_at` (default now()) e `updated_at` (com trigger) em toda tabela
- [ ] NOT NULL em campos obrigatórios
- [ ] Indexes nas colunas filtradas por RLS policies
- [ ] Naming: snake_case, tabelas no plural, sem abreviações obscuras
- [ ] SQL gera tudo do zero (tabelas, indexes, RLS, functions, triggers)
- [ ] Notas de evolução MVP → produção documentadas

## Quando NÃO usar

- **Workflow n8n sem banco** — use `n8n-architect`
- **Frontend sem dados** — não envolve banco
- **Infraestrutura/VPS** — use `vps-infra-audit`
- **Escritas >10k/seg com <10ms latência** — precisa de DynamoDB
- **Grafos** — precisa de Neo4j
- **Full-text search em escala** — Typesense ou Meilisearch
- **Confuso sobre qual skill usar** — invoque `maestro`

## Integration

| Skill | Quando/como |
|-------|-------------|
| **sdd** | SDD Phase 1 (Research) pode identificar necessidade de schema. Esta skill define o banco. |
| **n8n-architect** | Workflows CRUD devem respeitar o schema. Pra filas, veja `references/filas-e-edge-functions.md`. |
| **security-audit** | RLS e auth são os primeiros alvos. Se encontrar gaps de RLS, sugira security-audit completo. |
| **lovable-knowledge** | "Key database tables" do Project Knowledge é alimentado pelo output desta skill. |
| **maestro** | Maestro roteia pra esta skill quando detecta contexto de banco/schema. |

## Referências carregáveis

| Arquivo | Conteúdo |
|---------|----------|
| `references/schema-evaluation.md` | Framework completo de avaliação 5 camadas |
| `references/rls-patterns.md` | Padrões RLS: user data, multi-tenant, server-only, JWT claims, MFA |
| `references/migration-patterns.md` | ALTER TABLE, upserts, DynamoDB→PostgreSQL, branching |
| `references/pgvector-rag.md` | pgvector, embeddings, RAG com RLS, integração n8n |
| `references/supabase-updates-2025-2026.md` | RS256, new API keys, PKCE, Supavisor, PostgREST v14, Branching, MCP |
| `references/filas-e-edge-functions.md` | pgmq, Edge Functions como webhook receiver, padrão completo |

## Formato de resposta

- **Avaliações:** análise geral → cada camada com achados → ações priorizadas
- **Designs:** entidades + relacionamentos → SQL completo com comentários → notas de evolução
- **Simplificação:** mantém vs remove e por quê → SQL limpo → notas de integração n8n
- **Quick:** resposta direta com raciocínio. Conciso mas educacional.

SEMPRE explique o porquê. Seja opinativo mas justifique. Adapte detalhamento ao contexto (MVP vs produção). Na dúvida, pergunte.
