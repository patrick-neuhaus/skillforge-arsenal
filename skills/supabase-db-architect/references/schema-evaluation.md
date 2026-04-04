# Framework de avaliação de schema — Referência completa

Quando avaliar um schema (especialmente gerados por IA como Lovable/Bolt/Cursor), passe por essas 5 camadas sistematicamente. Pra cada issue: o que tá errado, por que importa, como corrigir, e o que ficar de olho.

---

## Camada 1: Integridade estrutural

- **Primary keys**: UUIDs (`gen_random_uuid()`) são o padrão. Sinalize serial integers em projetos novos — vazam contagem e ordem. Padrões DynamoDB (PK/SK) são red flag.
- **Foreign keys**: Todo relacionamento deve ter FK constraints explícitas. FKs faltando = zero integridade referencial.
- **Tipos de dados**: Erros comuns de IA:
  - `text` pra tudo (quando `timestamptz`, `jsonb`, `boolean`, `integer` são melhores)
  - `varchar(255)` por hábito de MySQL (no Postgres, use `text`)
  - `text` em vez de `boolean` pra flags
  - `text` em vez de `integer`/`numeric` pra valores numéricos
- **Naming**: `snake_case` consistente. Tabelas no plural. Sem abreviações que sacrificam clareza.
- **Constraints**: NOT NULL em campos obrigatórios. CHECK pra regras de negócio. UNIQUE onde faz sentido.

## Camada 2: Design de relacionamentos

- **1:N**: FK no lado "muitos". ON DELETE explícito (CASCADE, SET NULL, ou RESTRICT). Sempre explicar a escolha.
- **N:M**: Tabela de junção. IA às vezes tenta usar arrays JSONB — funciona pra datasets pequenos mas quebra em queries reversas e não tem integridade referencial.
- **Polimórficos**: Colunas FK separadas quando há poucos tipos pai. Evite generic `entity_type` + `entity_id` quando possível — perde FK constraint.
- **Self-referencing**: Hierarquias (categorias, comentários) com FK pra mesma tabela. Cuidado com queries recursivas (CTEs).

## Camada 3: Preocupações específicas do Supabase

- **RLS**: Toda tabela exposta ao client DEVE ter RLS habilitado com policies. Cheque:
  - Tabelas com RLS desabilitado
  - Policies excessivamente permissivas (`USING (true)`)
  - Policies faltando pra operações específicas (SELECT sem INSERT/UPDATE/DELETE)
  - Policies que não usam `auth.uid()` ou `auth.jwt()`
  - Tabelas server-only sem RLS (devem ter RLS habilitado sem policies = deny-all)
- **Timestamps**: `created_at` (default `now()`) e `updated_at` (com trigger) em toda tabela. Template do trigger:
  ```sql
  CREATE OR REPLACE FUNCTION update_updated_at()
  RETURNS TRIGGER AS $$
  BEGIN
    NEW.updated_at = now();
    RETURN NEW;
  END;
  $$ LANGUAGE plpgsql;

  CREATE TRIGGER set_updated_at
    BEFORE UPDATE ON public.nome_tabela
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();
  ```
- **Soft deletes**: Pra dados importantes, `deleted_at TIMESTAMPTZ` em vez de DELETE hard.
- **Realtime**: Tabelas com alta frequência de escrita podem precisar de Realtime desabilitado.
- **Schemas pra domínio**: Organizar domínios diferentes (`evolution`, `n8n_data`, `app`).

## Camada 4: Performance

- **Indexes**: Indexe colunas em WHERE clauses frequentes e FKs em JOINs. Todo index desacelera INSERT/UPDATE — é tradeoff. Pra MVP, index da PK geralmente basta.
- **RLS performance (CRITICO):** Wrap functions em SELECT pra habilitar initPlan caching:
  ```sql
  -- RUIM: auth.uid() é chamado pra CADA linha
  CREATE POLICY "own_data" ON leads
    USING (auth.uid() = user_id);

  -- BOM: (select auth.uid()) é cacheado como initPlan, chamado 1x por query
  CREATE POLICY "own_data" ON leads
    USING ((select auth.uid()) = user_id);
  ```
  Pode dar **100x+ de melhoria** em tabelas grandes. Funciona pra auth.uid(), auth.jwt(), e qualquer function security definer. Válido quando resultado não depende dos dados da linha.
  Combine com index btree: `CREATE INDEX idx_leads_user ON leads(user_id);`
- **JSONB**: Excelente pra dados flexíveis. Não use como substituto pra colunas próprias em dados consultados frequentemente. Considere GIN index pra queries em JSONB grandes.
- **Particionamento**: Só pra tabelas com milhões de linhas (logs, eventos, time-series). Não sugira pra apps pequenos/médios.
- **Filas nativas (pgmq)**: Supabase Queues pra buffering de webhooks, processamento assíncrono, filas de retry. Detalhes em `filas-e-edge-functions.md`.

## Camada 5: Red flags de schema gerado por IA

- **Tabelas faz-tudo**: 30+ colunas tentando lidar com tudo. Quebre em entidades distintas.
- **Constraints faltando**: Sem NOT NULL, sem CHECK, sem UNIQUE. IA gera "happy path" sem proteção.
- **Dados redundantes**: Mesma informação em múltiplas tabelas sem razão.
- **Over-engineering**: Tabelas separadas pra coisas que poderiam ser enum ou boolean. Hierarquias de herança onde um campo `type` resolveria.
- **Under-engineering**: Tudo em JSONB porque "é flexível." Sem FKs porque "o app controla."
- **Copy-paste de tutorial**: Nomes genéricos (`items`, `data`, `records`, `info`).
- **RLS ausente ou USING(true)**: A red flag mais grave em apps com frontend.
- **Tabelas de gerenciamento de estado do Lovable**: Artefatos de UI que não pertencem ao schema de negócio.

---

## Template: Starter de projeto Supabase

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
```
