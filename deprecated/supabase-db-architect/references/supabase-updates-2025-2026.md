# Mudanças recentes do Supabase (2025-2026)

Estas mudanças afetam recomendações da skill. Internalize antes de aconselhar.

---

## Auth: Asymmetric JWT (RS256)

Supabase Auth agora usa RS256 (asymmetric) em vez de HS256. Implicações:
- Chaves públicas expostas via endpoint JWKS pra validação externa
- Rotação de chaves mais fácil — não precisa redeploiar apps client
- Suporta RS256 e ES256
- **Impacto prático:** se valida JWT fora do Supabase (n8n, middleware customizado), use o endpoint JWKS em vez de shared secret

## Auth: Novas API Keys

Formato novo: `sb_publishable_*` e `sb_secret_*` substituindo `anon` e `service_role`:
- Desacopla gerenciamento de API keys de JWT secrets
- Rotação de secret key sem impacto em clients
- Projetos novos após nov/2025 já usam novo formato
- Projetos existentes: migrar progressivamente (opt-in)

**Impacto nas recomendações:** quando mencionar `anon key` ou `service_role key`, referencie também o novo formato e recomende migração se o projeto é novo.

## Auth: OAuth 2.1 + PKCE + MFA

- PKCE habilitado por default em todos os flows OAuth
- Auth codes válidos por 5 minutos, uso único
- MFA com TOTP e SMS/email OTP
- AAL (Authenticator Assurance Level) no JWT: AAL1 (básico) e AAL2 (MFA verificado)
- Use `auth.jwt() -> 'aal'` em RLS policies quando precisar de MFA enforcement

## Supavisor (substituiu PgBouncer)

Supavisor é o novo connection pooler, já deployado em todos os projetos:
- **Transaction mode** (default): libera conexão após cada transação — ideal pra apps web
- **Session mode**: conexão direta pra prepared statements
- Dedicated Poolers disponíveis em Micro Compute+ com IPv4
- Sem mudança de código — apenas atualizar connection string

**Impacto:** quando recomendar connection pooling, referencie Supavisor (não PgBouncer). Porta pooled continua sendo 6543.

## PostgREST v14

- ~20% mais throughput em GET requests
- JWT cache (mais RPS, mais memória)
- Schema cache loading: 7 min → 2s em bancos complexos
- Sem breaking changes pra apps existentes

## Edge Functions: Limites atualizados

- **CPU time:** 2 segundos (execução real, não inclui I/O async)
- **Wall clock:** 400 segundos max (Free/Pro limitado a 150s pra resposta inicial)
- **Background:** após retornar resposta, requests em background podem rodar os 400s completos
- **Runtime:** Supabase Edge Runtime (compatível com Deno, não Deno CLI padrão)
- **TypeScript-first** com compatibilidade Node.js

## Branching

Branches criam instâncias PostgreSQL isoladas clonadas do banco principal:
- Merge requests com diffs de schema pra code review
- Integração GitHub: banco por pull request, cleanup automático
- **Custo:** cada branch cobra como instância separada

## Log Drains

Exporta logs de Postgres, Auth, Storage, Edge Functions, Realtime, API Gateway:
- Disponível no Pro como add-on (mar/2026)
- Destinos: Datadog, Grafana Loki, Sentry, AWS S3, Axiom, HTTP, OTLP
- Pricing: $60/drain/projeto + $0.20/milhão eventos

## MCP Server do Supabase

Server MCP pra AI tools (Cursor, Claude Code, Windsurf, VS Code Copilot):
- Cloud-hosted (sem setup local) desde out/2025
- Read/write de dados, gerenciar tabelas, design de schemas
- Autenticação via browser redirect (sem PAT necessário)
