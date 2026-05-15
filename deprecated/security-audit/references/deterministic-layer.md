# Camada determinística — Verificações automáticas

Rode ANTES dos agentes IA. Regras estáticas pegam o óbvio (secrets hardcoded, npm audit) sem custo de falso positivo dos agentes. Passe os resultados como contexto pro Scanner.

## Verificações automáticas — Modo Code

### 1. Secrets hardcoded

```bash
# Service role keys e API secrets
grep -rn "sk_live\|sk_test\|service_role\|SUPABASE_SERVICE_ROLE\|sb_secret_" src/ \
  --include="*.ts" --include="*.tsx" --include="*.js"

# Bearer tokens e API keys genéricos
grep -rn "Bearer [A-Za-z0-9]\{20,\}\|api_key.*=.*['\"][A-Za-z0-9]\{20,\}" src/ \
  --include="*.ts" --include="*.tsx" --include="*.js"

# AWS keys
grep -rn "AKIA[A-Z0-9]\{16\}" src/ --include="*.ts" --include="*.tsx" --include="*.js"
```

### 2. npm audit

```bash
npm audit --json 2>/dev/null | head -100
```

### 3. XSS patterns

```bash
# dangerouslySetInnerHTML sem DOMPurify
grep -rn "dangerouslySetInnerHTML" src/ --include="*.tsx" --include="*.jsx"

# href com protocolo dinâmico
grep -rn 'href={' src/ --include="*.tsx" --include="*.jsx" \
  | grep -v "https\|http\|mailto\|tel\|/"

# innerHTML direto
grep -rn "\.innerHTML\s*=" src/ --include="*.ts" --include="*.tsx" --include="*.js"
```

### 4. .env no git

```bash
git ls-files | grep -E "\.env$|\.env\."
```

### 5. RLS verification

```bash
# Tabelas sem RLS (se migrations existem)
grep -rL "ENABLE ROW LEVEL SECURITY" supabase/migrations/ 2>/dev/null

# Listar todas as tabelas criadas
grep -rn "CREATE TABLE" supabase/migrations/ 2>/dev/null
```

### 6. Supabase client sem RLS

```bash
# Queries diretas sem filtro de user
grep -rn "supabase\.from(" src/ --include="*.ts" --include="*.tsx" \
  | grep -v "user_id\|auth\|\.rpc("
```

## SAST tools (se disponíveis)

### Semgrep (preferido)

50-250x mais rápido que SonarQube. Regras YAML intuitivas pra React/TS.

```bash
# Scan básico com regras auto-detectadas
semgrep --config=auto src/

# Regras específicas pra segurança
semgrep --config=p/security-audit src/

# Regras pra React
semgrep --config=p/react src/
```

### CodeQL (se repo no GitHub)

Nativo, excelente precisão (~5% false positives). Configurar via GitHub Actions:

```yaml
# .github/workflows/codeql.yml
- uses: github/codeql-action/init@v3
  with:
    languages: javascript-typescript
- uses: github/codeql-action/analyze@v3
```

## O que fazer com os resultados (Modo Code)

1. **Documente tudo** que a camada determinística encontrou
2. **Passe como contexto** pro Scanner no Passo 1 — isso foca o agente nos problemas que grep/SAST não pegam (lógica, design, fluxo)
3. **Achados confirmados por SAST** têm barra mais alta pra rejeição pelo Verifier — precisa de evidência concreta de que não é exploitável
4. **Se nenhuma ferramenta estava disponível**, documente como gap de cobertura

---

## Verificações automáticas — Modo Web

Rode ANTES dos agentes. Substitui grep/npm audit pra targets sem acesso ao código. Usa apenas: curl, openssl, WebFetch, Chrome MCP, curl https://dns.google/resolve.

### 1. HTTP Headers

```bash
TARGET="https://TARGET_URL"
curl -sI "$TARGET/"
```

Documentar cada header: presente/ausente/valor. Foco: Content-Security-Policy, Strict-Transport-Security, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy.

### 2. SSL/TLS

```bash
curl -sv "$TARGET/" 2>&1 | grep -E "SSL|TLS|cipher|expire|subject|issuer"
```

### 3. Path enumeration — Information Disclosure

```bash
for path in /.git/HEAD /.git/config /.env /wp-login.php /wp-config.php /phpmyadmin/ \
  /admin/ /api/ /api/v1/ /.gitignore /package.json /sitemap.xml /crossdomain.xml \
  /README.md /composer.json /xmlrpc.php /server-status /server-info; do
  status=$(curl -so /dev/null -w "%{http_code}" --max-time 8 "$TARGET$path")
  echo "$status $path"
done
```

Atenção: 200 = existe, 301/302 = redirect (verificar destino), 403 = existe mas bloqueado (pode ter bypass), 404 = não existe.

### 4. DNS e email security (via DNS-over-HTTPS)

```bash
DOMAIN="dominio-raiz.com"
BASE="https://dns.google/resolve"
echo "=== SPF ===" && curl -s "$BASE?name=$DOMAIN&type=TXT"
echo "=== DMARC ===" && curl -s "$BASE?name=_dmarc.$DOMAIN&type=TXT"
echo "=== MX ===" && curl -s "$BASE?name=$DOMAIN&type=MX"
echo "=== CAA ===" && curl -s "$BASE?name=$DOMAIN&type=CAA"
```

### 5. CORS check

```bash
curl -sI -X OPTIONS "$TARGET/" \
  -H "Origin: https://evil-test.com" \
  -H "Access-Control-Request-Method: GET" \
  | grep -i "access-control"
```

### 6. robots.txt e sitemap

```bash
curl -s "$TARGET/robots.txt"
curl -s "$TARGET/sitemap.xml" | head -30
```

### 7. Cookies de aplicação

```bash
curl -sI "$TARGET/" | grep -i "set-cookie"
```

Verificar: HttpOnly, Secure, SameSite em cookies da app (ignorar __cf_bm do Cloudflare).

### 8. Bundle JS (SPAs Lovable/Vite)

```
WebFetch TARGET/assets/index-[hash].js
→ Buscar: service_role, sb_secret_, API keys, endpoints hardcoded
→ SUPABASE_ANON_KEY / sb_publishable_ são públicas — NÃO reportar como critical
```

### 9. Browser inspection (Chrome MCP)

```
navigate → TARGET
javascript_tool → "JSON.stringify({ls: Object.keys(localStorage), ss: Object.keys(sessionStorage)})"
read_network_requests → capturar chamadas de API reais do SPA
read_page → mapear forms, inputs, links, superfície de ataque
```

## O que fazer com os resultados (Modo Web)

1. **Documente todos os HTTP status codes** dos paths enumerados
2. **Liste headers presentes/ausentes** com valores exatos
3. **Documente cookies** encontrados com flags
4. **Passe tudo como contexto pro Scanner** — Scanner foca no que ferramentas não verificam (lógica, conteúdo JS, injeção, CORS semântico)
5. **Paths com 200 que deveriam ser 404** são achados CONFIRMED imediatos
6. **Se Cloudflare detectado:** separar o que é do CDN vs da aplicação
