# OWASP Top 10 Web (2025) — Checklist de domínios

Referência completa dos domínios de segurança para Modo Code. Cada domínio mapeia para uma categoria OWASP A01-A10:2025.

## 1. Controle de acesso (A01:2025 — Broken Access Control)

- RLS habilitado em TODAS as tabelas públicas
- Policies RLS corretas — usar padrão `(select auth.uid()) = user_id` pra performance (initPlan caching)
- Verificação de ownership em operações de escrita/delete
- Roles e permissões no nível da aplicação
- Acesso a recursos de outros usuários (IDOR)
- DELETE/UPDATE sem `.eq('user_id', user.id)` = IDOR

### Padrões Supabase RLS

```sql
-- CORRETO: subquery pra performance (100x mais rápido)
CREATE POLICY select_own ON profiles
FOR SELECT USING ((select auth.uid()) = user_id);

-- INCORRETO: chamada direta (sem caching)
CREATE POLICY select_own ON profiles
FOR SELECT USING (auth.uid() = user_id);

-- CORRETO: verificação de ownership em UPDATE
CREATE POLICY update_own ON profiles
FOR UPDATE USING ((select auth.uid()) = user_id)
WITH CHECK ((select auth.uid()) = user_id);
```

### Red flags de acesso

- `supabase.from('table').select()` sem filtro de user_id — qualquer autenticado vê tudo
- `.delete().eq('id', id)` sem `.eq('user_id', user.id)` — IDOR
- Frontend fazendo query com ID vindo de URL params sem validação de ownership
- Tabela pública sem RLS = acesso irrestrito via anon key

## 2. Configuração de segurança (A02:2025 — Security Misconfiguration)

- Variáveis de ambiente vs hardcoded secrets
- Headers de segurança (CSP, CORS, X-Frame-Options, X-Content-Type-Options)
- Modo debug desativado em produção
- Permissões de API keys:
  - `SUPABASE_ANON_KEY` / `sb_publishable_*` → pública, OK no frontend
  - `SUPABASE_SERVICE_ROLE_KEY` / `sb_secret_*` → NUNCA no frontend
- CORS configurado com origins específicas, não `*`

## 3. Supply chain (A03:2025 — Vulnerable and Outdated Components)

- Dependências com vulnerabilidades conhecidas (`npm audit`, Snyk)
- Lock files presentes e versionados (`package-lock.json` ou `pnpm-lock.yaml`)
- Scripts de build confiáveis — lifecycle hooks podem executar código malicioso
  - Checar `preinstall`, `postinstall`, `prepare` em package.json
- Typosquatting: pacotes com nomes 1-2 chars diferentes de libs populares
- Dependências com poucas downloads + muitas permissões = red flag
- `npm ci` no CI/CD em vez de `npm install`

## 4. Criptografia (A04:2025 — Cryptographic Failures)

- HTTPS enforçado
- Dados sensíveis encriptados at rest
- Tokens e sessões com expiração adequada
- Supabase: JWT suporta RS256 (asymmetric) — verificar se está configurado
- Senhas nunca em plain text (Supabase Auth já faz bcrypt)

## 5. Injeção (A05:2025 — Injection)

- SQL injection (queries raw sem sanitização)
- XSS via `dangerouslySetInnerHTML` — verificar se tem DOMPurify
- XSS via `href="javascript:"` — validar protocolos em URLs dinâmicas
- XSS via manipulação direta de DOM (refs, innerHTML, document.write)
- Template injection
- `.rpc()`, `.sql()`, template literals em queries sem parametrização

### Padrões React de XSS

```tsx
// VULNERÁVEL: dangerouslySetInnerHTML sem sanitização
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// CORRETO: com DOMPurify
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />

// VULNERÁVEL: href dinâmico sem validação
<a href={userProvidedUrl}>Link</a>

// CORRETO: whitelist de protocolos
const safeUrl = /^https?:\/\//.test(url) ? url : '#';
<a href={safeUrl}>Link</a>
```

## 6. Design inseguro (A06:2025 — Insecure Design)

- Lógica de negócio no frontend (pode ser bypassada)
- Validação apenas no cliente sem server-side
- Rate limiting ausente em endpoints sensíveis
- Cálculos de preço/permissão no frontend
- Fluxos que dependem de ordem de operações sem transaction

## 7. Autenticação (A07:2025 — Identification and Authentication Failures)

- Fluxo de auth completo (signup, login, reset, logout)
- Session management (expiração, revogação)
- MFA disponível pra operações sensíveis (Supabase suporta TOTP + AAL levels)
- Token storage:
  - `localStorage` = XSS-vulnerable
  - `httpOnly cookies` = mais seguro
  - Supabase SDK gerencia isso automaticamente com `@supabase/ssr`
- Proteção em rotas: RLS no banco ou middleware no backend, NÃO só `useAuth()` no frontend
- Password reset com rate limiting e token expirável

## 8. Integridade (A08:2025 — Software and Data Integrity Failures)

- Supabase database webhooks e triggers validados
- Edge Functions com input validation
- Dependências verificadas (SRI hashes, lockfiles)
- CI/CD pipelines com verificação de integridade

## 9. Logging e alertas (A09:2025 — Security Logging and Monitoring Failures)

- Eventos de segurança logados (login, falha de auth, mudança de permissão)
- Logs NÃO expõem dados sensíveis (PII, tokens, senhas)
- Alertas pra padrões suspeitos (múltiplas falhas de login, acesso bulk a dados)

## 10. Tratamento de exceções (A10:2025 — Server-Side Request Forgery)

- Erros não expõem stack traces ou dados internos ao usuário
- Fail-safe: sistema nega acesso quando algo dá erro, não permite
- SSRF: validar URLs que o servidor acessa por input do usuário
- Catch blocks não retornam erro completo pro frontend
