# pgvector e RAG — Referência de implementação

Supabase integra pgvector nativamente pra embeddings e busca por similaridade.

---

## Setup básico

```sql
-- Habilitar extensão
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela de documentos com embedding
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),  -- 1536 pra OpenAI ada-002 / text-embedding-3-small
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

## Escolha de index

| Index type | Quando usar | Tradeoff |
|-----------|-------------|----------|
| **IVFFlat** | Datasets médios (<1M linhas), updates frequentes | Mais rápido de construir, menos preciso |
| **HNSW** | Datasets grandes, precisão importa | Mais lento de construir, mais preciso |
| **Nenhum** | <10k linhas | Scan sequencial é rápido o suficiente |

Ajuste `lists` (IVFFlat) ou `m`/`ef_construction` (HNSW) baseado no tamanho do dataset.

## Dimensões de embedding por modelo

| Modelo | Dimensão | Nota |
|--------|----------|------|
| OpenAI text-embedding-3-small | 1536 | Bom custo-benefício |
| OpenAI text-embedding-3-large | 3072 | Mais preciso, mais caro |
| OpenAI ada-002 | 1536 | Legacy, ainda funciona |
| Gemini text-embedding-004 | 768 | Grátis até certo limite |
| Cohere embed-v3 | 1024 | Multilingual nativo |

---

## RAG com RLS

RLS funciona com queries de vetor — filtragem de acesso em retrieval:

```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Cada usuário só busca nos seus documentos
CREATE POLICY "Users see own documents" ON documents
  FOR SELECT
  USING ((select auth.uid()) = user_id);

-- Index pra RLS performance
CREATE INDEX idx_documents_user ON documents(user_id);
```

Isso garante que busca por similaridade já retorna filtrada por tenant/usuário.

---

## Integração com n8n

O n8n tem node Supabase Vector Store nativo. Pra inserir documentos via n8n:

1. **Gere embeddings** via node OpenAI/Gemini Embeddings
2. **Use Supabase Vector Store node** no modo Insert
3. **Pra retrieval:** use como Tool no AI Agent node

### Workflow típico de RAG

```
[Trigger: novo documento] → [Text Splitter] → [Embeddings] → [Supabase Vector Store: Insert]

[AI Agent] → [Tool: Supabase Vector Store Retrieval] → [Resposta com contexto]
```

Pra detalhes de implementação no n8n, veja a reference `ai-nodes.md` na skill n8n-architect.

---

## Chunking strategies

| Estratégia | Quando usar |
|-----------|-------------|
| Fixed size (500-1000 tokens) | Documentos genéricos, início rápido |
| Paragraph/section split | Documentos estruturados (markdown, HTML) |
| Semantic chunking | Precisão importa, custo não é problema |
| Overlap (10-20%) | Evitar perda de contexto entre chunks |

## Dicas

- Comece com chunks de 500 tokens e overlap de 50 tokens
- Guarde o texto original + metadata (source, page, section) junto do embedding
- Use `match_threshold` conservador (0.78+) — melhor não retornar do que retornar lixo
- Monitore custos de embedding — cada insert gera chamada à API
