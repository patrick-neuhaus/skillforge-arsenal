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

## O que fazer com os resultados

1. **Documente tudo** que a camada determinística encontrou
2. **Passe como contexto** pro Scanner no Passo 1 — isso foca o agente nos problemas que grep/SAST não pegam (lógica, design, fluxo)
3. **Achados confirmados por SAST** têm barra mais alta pra rejeição pelo Verifier — precisa de evidência concreta de que não é exploitável
4. **Se nenhuma ferramenta estava disponível**, documente como gap de cobertura
