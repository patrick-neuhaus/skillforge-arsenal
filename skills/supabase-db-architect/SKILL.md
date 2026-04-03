---
name: supabase-db-architect
description: "Skill de arquitetura de banco Supabase/PostgreSQL pra apps de pequeno e médio porte. Use quando o usuário precisar de: design de schemas, avaliação de banco (especialmente gerados por IA como Lovable/Bolt/Cursor), simplificação pra handoff de cliente, migração DynamoDB→PostgreSQL, SQL pra Supabase, RLS, Edge Functions, cron jobs, triggers. Também dispare pra: tabelas, colunas, indexes, foreign keys, normalização, 'esse schema tá bom?', 'como estruturo isso?', dumps de SQL/schema, ou menções como 'minhas tabelas no supabase'. Na dúvida, dispare — decisões de banco têm impacto desproporcional. NÃO use se é workflow n8n sem banco → use n8n-architect. Se é frontend sem dados, não envolve esta skill."
---

# Supabase Database Architect v3

Esta skill conduz o processo de projetar, avaliar e melhorar schemas de banco Supabase/PostgreSQL pra aplicações de pequeno e médio porte. Toda recomendação deve vir com o raciocínio por trás — o objetivo é ensinar enquanto faz.

## Mudanças recentes do Supabase (2025-2026)

Estas mudanças afetam recomendações desta skill. Internalize antes de aconselhar.

### Auth: Asymmetric JWT (RS256)

Supabase Auth agora usa RS256 (asymmetric) em vez de HS256. Implicações:
- Chaves públicas expostas via endpoint JWKS pra validação externa
- Rotação de chaves mais fácil — não precisa redeploiar apps client
- Suporta RS256 e ES256
- Impacto prático pra o usuário: se valida JWT fora do Supabase (n8n, middleware customizado), use o endpoint JWKS em vez de shared secret

### Auth: Novas API Keys

Formato novo: `sb_publishable_*` e `sb_secret_*` substituindo `anon` e `service_role`:
- Desacopla gerenciamento de API keys de JWT secrets
- Rotação de secret key sem impacto em clients
- Projetos novos após nov/2025 já usam novo formato
- Projetos existentes: migrar progressivamente (opt-in)

Impacto nas recomendações: quando mencionar `anon key` ou `service_role key`, referencie também o novo formato e recomende migração se o projeto é novo.

### Auth: OAuth 2.1 + PKCE + MFA

- PKCE habilitado por default em todos os flows OAuth
- Auth codes válidos por 5 minutos, uso único
- MFA com TOTP e SMS/email OTP
- AAL (Authenticator Assurance Level) no JWT: AAL1 (básico) e AAL2 (MFA verificado)
- Use `auth.jwt() -> 'aal'` em RLS policies quando precisar de MFA enforcement

### Supavisor (substituiu PgBouncer)

Supavisor é o novo connection pooler, já deployado em todos os projetos:
- **Transaction mode** (default): libera conexão após cada transação — ideal pra apps web
- **Session mode**: conexão direta pra prepared statements
- Dedicated Poolers disponíveis em Micro Compute+ com IPv4
- Sem mudança de código — apenas atualizar connection string

Impacto: quando recomendar connection pooling, referencie Supavisor (não PgBouncer). Porta pooled continua sendo 6543.

### PostgREST v14

- ~20% mais throughput em GET requests
- JWT cache (mais RPS, mais memória)
- Schema cache loading: 7 min → 2s em bancos complexos
- Sem breaking changes pra apps existentes

### Edge Functions: Limites atualizados

- **CPU time:** 2 segundos (execução real, não inclui I/O async)
- **Wall clock:** 400 segundos max (Free/Pro limitado a 150s pra resposta inicial)
- **Background:** após retornar resposta, requests em background podem rodar os 400s completos
- **Runtime:** Supabase Edge Runtime (compatível com Deno, não Deno CLI padrão)
- **TypeScript-first** com compatibilidade Node.js

### Branching

Branches criam instâncias PostgreSQL isoladas clonadas do banco principal:
- Merge requests com diffs de schema pra code review
- Integração GitHub: banco por pull request, cleanup automático
- Custo: cada branch cobra como instância separada

### Log Drains

Exporta logs de Postgres, Auth, Storage, Edge Functions, Realtime, API Gateway:
- Disponível no Pro como add-on (mar/2026)
- Destinos: Datadog, Grafana Loki, Sentry, AWS S3, Axiom, HTTP, OTLP
- Pricing: $60/drain/projeto + $0.20/milhão eventos

### MCP Server do Supabase

Server MCP pra AI tools (Cursor, Claude Code, Windsurf, VS Code Copilot):
- Cloud-hosted (sem setup local) desde out/2025
- Read/write de dados, gerenciar tabelas, design de schemas
- Autenticação via browser redirect (sem PAT necessário)

## Filosofia central

O usuário trabalha num ambiente ágil construindo produtos com Supabase, n8n e Lovable. Clientes são PMEs onde agilidade importa mais que perfeição teórica:

- **Pragmático sobre acadêmico** — 3FN é ótimo em livro-texto, mas um campo desnormalizado que economiza 3 JOINs pode ser a decisão certa pra um MVP. Explique o tradeoff.
- **Ensine o porquê** — Nunca diga apenas "adiciona um index aqui." Diga por que e qual o impacto.
- **Contexto importa** — MVP pra 50 usuários ≠ produção com 10k simultâneos. Pergunte ou infira o contexto.
- **Nativo do Supabase** — Pense em termos do ecossistema: RLS, Edge Functions, Realtime, pg_cron, Storage, auth.users, Supavisor, Branching. Não sugira soluções genéricas quando o Supabase tem um jeito nativo.

## Como detectar o contexto

**Modo 1: Avaliação de schema ("Isso tá bom?")**
O usuário compartilha SQL ou descreve tabelas e quer análise. Especialmente comum com schemas gerados por IA (Lovable, Bolt, Cursor).

**Modo 2: Design de schema ("Monta isso pra mim")**
O usuário descreve um problema de negócio e quer que você projete o banco.

**Modo 3: Simplificação pra cliente ("Faz isso portável")**
Versão enxuta que o cliente consiga rodar independente (tipicamente n8n + Supabase, sem Lovable).

**Modo 4: Correção rápida / Pergunta ("Só uma coisa")**
Perguntas específicas tipo "devo indexar isso?", "como modelo esse relacionamento?", "essa policy de RLS tá certa?"

## Framework de avaliação de schema

Quando avaliar um schema (especialmente gerados por IA), passe por essas camadas sistematicamente. Pra cada issue, explique: o que tá errado, por que importa, como corrigir, e o que ficar de olho.

### Camada 1: Integridade estrutural

- **Primary keys**: UUIDs (`gen_random_uuid()`) são o padrão. Sinalize serial integers em projetos novos — vazam contagem e ordem. Se encontrar padrões DynamoDB (PK/SK), é red flag.
- **Foreign keys**: Todo relacionamento deve ter FK constraints explícitas. FKs faltando = zero integridade referencial.
- **Tipos de dados**: Erros comuns de IA: `text` pra tudo (quando `timestamptz`, `jsonb`, `boolean`, `integer` são melhores), `varchar(255)` por hábito de MySQL (no Postgres, use `text`).
- **Naming**: `snake_case` consistente. Tabelas no plural. Sem abreviações que sacrificam clareza.

### Camada 2: Design de relacionamentos

- **1:N**: FK no lado "muitos". ON DELETE explícito (CASCADE, SET NULL, ou RESTRICT).
- **N:M**: Tabela de junção. IA às vezes tenta usar arrays JSONB — funciona pra datasets pequenos mas quebra em queries reversas.
- **Polimórficos**: Colunas FK separadas quando há poucos tipos pai.

### Camada 3: Preocupações específicas do Supabase

- **RLS**: Toda tabela exposta ao client DEVE ter RLS habilitado com policies. Cheque: tabelas com RLS desabilitado, policies excessivamente permissivas (`USING (true)`), policies faltando pra operações específicas, policies que não usam `auth.uid()`.
- **Timestamps**: `created_at` (default `now()`) e `updated_at` (com trigger) em toda tabela.
- **Soft deletes**: Pra dados importantes, `deleted_at` em vez de DELETE hard.
- **Realtime**: Tabelas com alta frequência de escrita podem precisar de Realtime desabilitado.

### Camada 4: Performance

- **Indexes**: Indexe colunas em WHERE clauses frequentes e FKs em JOINs. Todo index desacelera INSERT/UPDATE — é tradeoff. Pra MVP, index da PK geralmente basta.
- **RLS performance (CRÍTICO):** Wrap functions em SELECT pra habilitar initPlan caching:
  ```sql
  -- RUIM: auth.uid() é chamado pra CADA linha
  CREATE POLICY "own_data" ON leads
    USING (auth.uid() = user_id);

  -- BOM: (select auth.uid()) é cacheado como initPlan, chamado 1x por query
  CREATE POLICY "own_data" ON leads
    USING ((select auth.uid()) = user_id);
  ```
  Isso pode dar **100x+ de melhoria** em tabelas grandes. Funciona pra auth.uid(), auth.jwt(), e qualquer function security definer. Só é válido quando o resultado não depende dos dados da linha.
  Combine com index btree na coluna filtrada: `CREATE INDEX idx_leads_user ON leads(user_id);`
- **JSONB**: Excelente pra dados flexíveis/dinâmicos. Não use como substituto pra colunas próprias em dados consultados frequentemente.
- **Particionamento**: Só pra tabelas com milhões de linhas (logs, eventos, time-series). Não sugira pra apps pequenos/médios.
- **Schemas pra domínio**: Organizar domínios diferentes (`evolution`, `n8n_data`, `app`).
- **Filas nativas (pgmq)**: Supabase Queues pra buffering de webhooks, processamento assíncrono, filas de retry.

### Camada 5: Red flags de schema gerado por IA

- **Tabelas faz-tudo**: 30+ colunas tentando lidar com tudo. Quebre.
- **Constraints faltando**: Sem NOT NULL, sem CHECK, sem UNIQUE.
- **Dados redundantes**: Mesma informação em múltiplas tabelas sem razão.
- **Over-engineering**: Tabelas separadas pra coisas que poderiam ser enum ou boolean.
- **Under-engineering**: Tudo em JSONB porque "é flexível."
- **Copy-paste de tutorial**: Nomes genéricos (`items`, `data`, `records`).
- **RLS ausente ou USING(true)**: A red flag mais grave em apps com frontend.

## Padrões de RLS em profundidade

### Os dois caminhos de acesso

**Client-side (Lovable, apps frontend)** → Usa key `anon`/`sb_publishable_*` ou `authenticated` → RLS é APLICADO → Toda query é filtrada por policies.

**Server-side (n8n, Edge Functions, cron jobs)** → Usa key `service_role`/`sb_secret_*` → RLS é BYPASSADO → Acesso total.

### Padrão 1: Dados do usuário (mais comum)

```sql
CREATE TABLE public.leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT,
  status TEXT DEFAULT 'new',
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

ALTER TABLE public.leads ENABLE ROW LEVEL SECURITY;

-- SEMPRE use (select auth.uid()) com parênteses pra caching
CREATE POLICY "Users manage own leads" ON public.leads
  FOR ALL
  USING ((select auth.uid()) = user_id)
  WITH CHECK ((select auth.uid()) = user_id);

-- Index pra performance da RLS policy
CREATE INDEX idx_leads_user_id ON public.leads(user_id);
```

### Padrão 2: Multi-tenancy por organização

```sql
CREATE TABLE public.organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE public.organization_members (
  organization_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  role TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member', 'viewer')),
  PRIMARY KEY (organization_id, user_id)
);

-- Index crucial pra performance das subqueries RLS
CREATE INDEX idx_org_members_user ON public.organization_members(user_id);

CREATE TABLE public.campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  status TEXT DEFAULT 'draft',
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

ALTER TABLE public.campaigns ENABLE ROW LEVEL SECURITY;

-- Membros veem campanhas da sua org
CREATE POLICY "Org members see campaigns" ON public.campaigns
  FOR SELECT
  USING (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
    )
  );

-- Admins e owners podem modificar
CREATE POLICY "Org admins manage campaigns" ON public.campaigns
  FOR ALL
  USING (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
      AND role IN ('owner', 'admin')
    )
  )
  WITH CHECK (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
      AND role IN ('owner', 'admin')
    )
  );
```

### Padrão 3: Tabelas só-server (n8n)

```sql
CREATE TABLE public.follow_up_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_item_id UUID NOT NULL,
  status TEXT NOT NULL,
  error_message TEXT,
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Habilite RLS como rede de segurança, mesmo sem policies
-- Se alguém acidentalmente consultar com anon key, não vê nada
ALTER TABLE public.follow_up_logs ENABLE ROW LEVEL SECURITY;
```

### Padrão 4: JWT custom claims + MFA enforcement

```sql
-- Acesso baseado em role via app_metadata
CREATE POLICY "Admins have full access" ON public.settings
  FOR ALL
  USING (
    (select auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
  );

-- Exigir MFA (AAL2) pra operações sensíveis
CREATE POLICY "MFA required for billing" ON public.billing
  FOR ALL
  USING (
    (select auth.jwt() ->> 'aal') = 'aal2'
    AND (select auth.uid()) = user_id
  );
```

### Dicas de performance de RLS

1. **SEMPRE** use `(select auth.uid())` e `(select auth.jwt())` com parênteses — habilita initPlan caching
2. Indexe colunas usadas em subqueries de RLS (`user_id`, `organization_id`)
3. Evite JOINs complexos em policies — rodam em cada checagem de linha
4. Pra dados acessados frequentemente, considere `security_definer` function que cache membership
5. Teste policies: `SET ROLE authenticated; SET request.jwt.claims = '{"sub": "user-uuid"}';`

## pgvector e RAG

Supabase integra pgvector nativamente pra embeddings e busca por similaridade:

### Setup básico

```sql
-- Habilitar extensão
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela de documentos com embedding
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),  -- 1536 pra OpenAI ada-002
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Index pra busca por similaridade (IVFFlat pra datasets médios)
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);  -- ajustar lists = sqrt(num_rows)

-- Function de busca por similaridade
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding VECTOR(1536),
  match_threshold FLOAT DEFAULT 0.78,
  match_count INT DEFAULT 5
)
RETURNS TABLE (
  id UUID,
  content TEXT,
  metadata JSONB,
  similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  WHERE 1 - (d.embedding <=> query_embedding) > match_threshold
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
```

### RAG com RLS

RLS funciona com queries de vetor — filtragem de acesso em retrieval:

```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users see own documents" ON documents
  FOR SELECT
  USING ((select auth.uid()) = user_id);
```

### Integração com n8n

O n8n tem node Supabase Vector Store nativo. Pra inserir documentos via n8n:
1. Gere embeddings via node OpenAI/Gemini Embeddings
2. Use Supabase Vector Store node no modo Insert
3. Pra retrieval: use como Tool no AI Agent

Pra detalhes de implementação no n8n, veja a reference `ai-nodes.md` na skill n8n-architect.

## Diretrizes de design de schema

### Pra MVPs (Velocidade > Perfeição)

- Mínimo de tabelas que representam entidades core
- `text` pra campos incertos (apertar tipos depois)
- Pule indexação avançada — index da PK basta pra datasets pequenos
- RLS simples: `(select auth.uid()) = user_id`
- JSONB `metadata` nas tabelas principais pra dados ad-hoc
- Sem particionamento, sem materialized views, sem triggers complexos
- MAS use FKs e NOT NULL constraints — pegam bugs cedo e custam nada

### Pra Produção (Confiabilidade > Velocidade)

- Apertar tipos de dados (text → tipos próprios com constraints)
- Indexes baseados em padrões reais de query (use `pg_stat_user_indexes`)
- RLS abrangentes com `(select ...)` pattern
- Trilhas de auditoria
- pg_cron pra manutenção
- Read replicas se carga de queries for alta
- CHECK constraints pra regras de negócio
- Log Drains configurados pra monitoramento
- Branching pra testar migrações antes de produção

### Template: Starter de projeto Supabase

```sql
-- Habilitar extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Perfil core do usuário (estende auth.users do Supabase)
CREATE TABLE public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  full_name TEXT,
  avatar_url TEXT,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Auto-update de updated_at
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON public.profiles
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- RLS com pattern otimizado
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own profile"
  ON public.profiles FOR SELECT
  USING ((select auth.uid()) = id);

CREATE POLICY "Users can update own profile"
  ON public.profiles FOR UPDATE
  USING ((select auth.uid()) = id);

-- Index pra RLS performance (neste caso PK já cobre, mas em outras tabelas é essencial)
-- CREATE INDEX idx_profiles_user ON profiles(user_id);
```

## Workflow de simplificação pra cliente

1. **Identifique entidades core**: Quais tabelas mínimas o cliente precisa? Remova artefatos de UI/app.
2. **Remova artefatos do Lovable**: Tabelas de gerenciamento de estado do Lovable não são necessárias.
3. **Simplifique RLS**: Se o cliente roda tudo pelo n8n (server-side), RLS pode ser mais simples ou acesso via `sb_secret_*`.
4. **Gere SQL limpo**: Único arquivo SQL que cria tudo do zero — tabelas, indexes, RLS, functions, triggers.
5. **Documente pontos de integração**: Onde o n8n conecta? Webhooks necessários? O que o cron job faz?
6. **Inclua seed data se necessário**.

## Realtime: Quando usar e quando não

### 3 features principais

- **Broadcast**: Mensagens entre usuários em tempo real (low-latency, channel-based)
- **Presence**: Sincronização de estado de usuário (quem tá online, typing indicators)
- **Postgres Changes**: Notifica clients quando dados mudam no banco

### Quando usar Postgres Changes
- Dashboards que precisam refletir mudanças instantaneamente
- Listas colaborativas (múltiplos usuários editando)
- Status updates (progresso de processamento)

### Quando NÃO usar
- Tabelas de alto volume de escrita (logs, filas) — flood nos clients
- Dados sensíveis sem RLS adequado — Realtime respeita RLS, mas erros de policy expõem dados
- Quando polling a cada 30s resolve — Realtime adiciona complexidade

### Canais públicos vs privados
- **Públicos**: qualquer usuário pode se inscrever (desabilitável por projeto)
- **Privados**: requerem Realtime Authorization

## Notas de migração DynamoDB → PostgreSQL

Se encontrar padrões DynamoDB em PostgreSQL:

- **PK/SK**: Substitua por tabelas dedicadas com foreign keys
- **Single-table design**: Quebre em tabelas separadas — é anti-pattern no PostgreSQL
- **Keys sobrecarregadas**: Extraia pra colunas próprias com tipo e constraints
- **GSI equivalentes**: São apenas indexes
- **Prefixos de entidade**: O nome da tabela É o tipo de entidade

### Processo de conversão

1. Mapeie tipos de entidade pra tabelas
2. Extraia dados reais das keys
3. Substitua access patterns por indexes
4. Adicione FKs
5. Valide com queries

## Padrões de migração segura

### ALTER TABLE sobre recriar

```sql
-- 1. Adicione a nova coluna
ALTER TABLE campaigns ADD COLUMN new_column TEXT;
-- 2. Backfill
UPDATE campaigns SET new_column = old_column;
-- 3. Constraints
ALTER TABLE campaigns ALTER COLUMN new_column SET NOT NULL;
-- 4. Só depois de verificar, drope a antiga
ALTER TABLE campaigns DROP COLUMN old_column;
```

Ordem: ADD → backfill → constrain → DROP. Nunca drope primeiro.

Pra migrações em produção, use **Branching** pra testar o migration script num branch antes de aplicar no banco principal.

### Upserts (ON CONFLICT)

```sql
INSERT INTO documents (hash_sha256, content, source_url)
VALUES ($1, $2, $3)
ON CONFLICT (hash_sha256) DO UPDATE SET
  content = EXCLUDED.content,
  updated_at = now();
```

- **DO UPDATE**: Versão mais recente ganha (sync, webhooks)
- **DO NOTHING**: Primeira escrita permanente (logs, audit trails)

## JSONB: Quando usar vs normalizar

### Use JSONB quando:
- Estrutura varia entre linhas (ex: `crm_config`)
- Dados lidos como blob inteiro, raramente consultados por campos
- Respostas de API de terceiros
- Metadata/settings que ainda não merecem colunas próprias

### Normalize quando:
- Consulta por campos específicos frequentemente
- Precisa de type safety e constraints
- Precisa de integridade referencial (FK)
- Múltiplas linhas referenciam mesmos dados aninhados
- Precisa agregar ou ordenar por valores aninhados

### Padrão de graduação (MVP → Produção)

Comece com JSONB no MVP, promova pra colunas quando padrões emergirem:
```sql
-- MVP
ALTER TABLE leads ADD COLUMN metadata JSONB DEFAULT '{}';

-- Depois
ALTER TABLE leads ADD COLUMN company_name TEXT;
UPDATE leads SET company_name = metadata->>'company_name';
```

## Quando NÃO usar Supabase

### Estratégias de escalabilidade (em ordem)

1. **Otimize queries primeiro** — `EXPLAIN ANALYZE` antes de mudar infra
2. **Indexes parciais + particionamento** — `pg_partman` pra tabelas com milhões de linhas
3. **Upstash Redis** — Buffer na frente do Supabase pra filas de alta velocidade
4. **Read replicas** — Pra dashboards read-heavy

### Quando realmente sair do Supabase

- Escritas >10k/seg com <10ms latência → DynamoDB
- Relacionamentos de grafo → Neo4j
- Full-text search em escala → Typesense ou Meilisearch

90% dos casos PME: resolve dentro do Supabase com melhor schema, indexes, ou cache.

## Integração com outras skills

- **Product Discovery & PRD:** Se o PRD menciona modelo de dados, esta skill define o schema
- **n8n Architect:** Workflows que fazem CRUD devem respeitar o schema. Pra filas, veja pgmq na reference de filas
- **Lovable Knowledge:** "Key database tables" do Project Knowledge pode ser alimentado pelo output desta skill
- **Tech Lead & PM:** Tasks de banco podem ser delegadas com briefing gerado aqui
- **Security Audit:** RLS e auth são os primeiros alvos de auditoria de segurança

## Formato de resposta

**Pra avaliações**: Análise geral rápida → cada camada com achados → lista de ações priorizadas.
**Pra designs**: Entidades e relacionamentos (conceitual) → SQL completo com comentários → notas de evolução.
**Pra simplificação**: O que mantém vs remove e por quê → SQL limpo → notas de integração n8n.
**Pra perguntas rápidas**: Responda diretamente com raciocínio. Conciso mas educacional.

## Lembretes importantes

- Sempre explique o **porquê** de toda recomendação
- Seja opinativo mas explique suas opiniões
- Quando avaliar schemas de IA, aponte o que fez bem também
- Adapte detalhamento ao contexto (MVP vs produção)
- Na dúvida sobre contexto, pergunte antes de prescrever
- Supabase É PostgreSQL. Tudo que Postgres faz, Supabase faz. Aproveite features nativas.
- **SEMPRE** use `(select auth.uid())` com parênteses em RLS policies — é a otimização de maior impacto
