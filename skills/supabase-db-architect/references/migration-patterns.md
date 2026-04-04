# Padrões de migração — Referência completa

## Regra de ouro

**Ordem: ADD → backfill → constrain → DROP.** Nunca drope primeiro.

Pra migrações em produção, use **Branching** pra testar o migration script num branch antes de aplicar no banco principal.

---

## ALTER TABLE sobre recriar

```sql
-- 1. Adicione a nova coluna
ALTER TABLE campaigns ADD COLUMN new_column TEXT;

-- 2. Backfill dados existentes
UPDATE campaigns SET new_column = old_column;

-- 3. Adicionar constraints
ALTER TABLE campaigns ALTER COLUMN new_column SET NOT NULL;

-- 4. Só depois de verificar tudo, drope a antiga
ALTER TABLE campaigns DROP COLUMN old_column;
```

### Migrações com downtime zero

Pra tabelas grandes em produção:

1. Adicione coluna nullable
2. Deploy código que escreve em ambas colunas
3. Backfill em batches (`UPDATE ... WHERE id IN (SELECT id FROM ... LIMIT 1000)`)
4. Adicione constraint
5. Deploy código que lê da nova coluna
6. Drope coluna antiga

## Upserts (ON CONFLICT)

```sql
INSERT INTO documents (hash_sha256, content, source_url)
VALUES ($1, $2, $3)
ON CONFLICT (hash_sha256) DO UPDATE SET
  content = EXCLUDED.content,
  updated_at = now();
```

- **DO UPDATE**: Versão mais recente ganha (sync, webhooks)
- **DO NOTHING**: Primeira escrita permanente (logs, audit trails)

Requisito: precisa de UNIQUE constraint ou index na coluna de conflito.

---

## DynamoDB → PostgreSQL

Se encontrar padrões DynamoDB em PostgreSQL:

### Mapeamento de conceitos

| DynamoDB | PostgreSQL |
|----------|-----------|
| PK/SK (partition + sort key) | Tabelas dedicadas com FKs |
| Single-table design | Tabelas separadas por entidade |
| Keys sobrecarregadas (PK: `USER#123`) | Colunas próprias com tipo e constraints |
| GSI (Global Secondary Index) | Indexes (btree, GIN, etc.) |
| Prefixos de entidade | O nome da tabela É o tipo de entidade |
| Scan | SELECT com WHERE |
| Query por PK+SK | SELECT com JOIN |
| TTL | pg_cron + DELETE WHERE expired_at < now() |

### Processo de conversão

1. **Mapeie tipos de entidade pra tabelas** — cada prefixo de PK vira uma tabela
2. **Extraia dados reais das keys** — `USER#123#ORDER#456` vira `users.id` + `orders.user_id`
3. **Substitua access patterns por indexes** — cada GSI vira um index
4. **Adicione FKs** — o PostgreSQL garante integridade referencial
5. **Valide com queries** — recrie cada access pattern como SELECT/JOIN

### Red flags DynamoDB em PostgreSQL

- Coluna `PK` e `SK` do tipo `text` — padrão single-table
- Valores com prefixos (`USER#`, `ORDER#`) — entidades misturadas
- Tabela única com 50+ colunas nullable — todas as entidades numa tabela
- Sem FKs — o DynamoDB não tem, mas PostgreSQL precisa

---

## Workflow de simplificação pra cliente

Quando o objetivo é entregar schema portável (tipicamente n8n + Supabase, sem Lovable):

1. **Identifique entidades core**: Quais tabelas mínimas o cliente precisa? Remova artefatos de UI/app.
2. **Remova artefatos do Lovable**: Tabelas de gerenciamento de estado do Lovable não são necessárias.
3. **Simplifique RLS**: Se o cliente roda tudo pelo n8n (server-side), RLS pode ser mais simples ou acesso via `sb_secret_*`.
4. **Gere SQL limpo**: Único arquivo SQL que cria tudo do zero — tabelas, indexes, RLS, functions, triggers.
5. **Documente pontos de integração**: Onde o n8n conecta? Webhooks necessários? O que o cron job faz?
6. **Inclua seed data se necessário**.

---

## Branching pra testar migrações

Supabase Branching cria instâncias PostgreSQL isoladas clonadas do banco principal:

1. Crie um branch no dashboard ou via CLI
2. Aplique a migration no branch
3. Teste queries e RLS no branch
4. Se tudo ok, aplique no banco principal
5. Delete o branch

**Custo:** cada branch cobra como instância separada. Use pra migrações complexas, não pra cada ALTER TABLE.
