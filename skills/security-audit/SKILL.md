---
name: security-audit
description: "Pipeline de 3 agentes pra auditoria de segurança de aplicação. Dois modos: VPS (segurança do servidor via SSH) e Code (segurança do código via GitHub). Use esta skill SEMPRE que o usuário mencionar: segurança, security, OWASP, 'tá seguro?', 'tem vulnerabilidade?', RLS, 'dados expostos', 'token vazando', 'secrets', XSS, injection, autenticação insegura, 'qualquer um acessa', 'audit de segurança', 'meu app é seguro?', 'revisa a segurança', 'antes de lançar quero garantir segurança', ou qualquer variação que envolva avaliar se um servidor, aplicação ou banco está protegido contra ataques e acessos indevidos. Também use quando o usuário lançar um projeto Lovable e quiser validar segurança antes de ir pra produção. Se o contexto for infra (Docker, disco, escalabilidade, performance) sem foco em segurança, use vps-infra-audit. Se for bugs de lógica ou UX, use repo-review ou ux-audit."
---

# Security Audit v2 — Auditoria de segurança de aplicação e servidor

## Visão geral

Pipeline sequencial de 3 agentes pra auditoria de segurança: **Scanner** identifica vulnerabilidades potenciais, **Verifier** confirma ou rejeita cada achado com re-inspeção independente, **Arbiter** emite veredictos finais baseados em evidência.

A skill opera em dois modos:

- **Modo VPS:** Auditoria de segurança do servidor via SSH — portas, serviços, permissões, configurações de rede, hardening do SO. Complementa o vps-infra-audit com foco exclusivo em segurança.
- **Modo Code:** Auditoria de segurança do código via GitHub — OWASP Top 10, Supabase RLS, autenticação, secrets expostos, XSS, injection, React security patterns. É o modo principal pra projetos Lovable.

O padrão é o mesmo do repo-review: Gerar → Verificar → Julgar. A diferença é o foco: repo-review busca bugs funcionais, security-audit busca vulnerabilidades de segurança.

### Novidades na v2

- **OWASP Top 10 for LLM Applications 2025** — módulo dedicado pra apps com features de IA
- **Supply chain security** — verificação de dependências, typosquatting, lockfiles
- **Dual-tool SAST** — Semgrep + CodeQL como camada determinística antes dos agentes
- **React-specific patterns** — dangerouslySetInnerHTML, href="javascript:", Server Components
- **Riscos de código gerado por IA** — checklist pra código vindo de Lovable/Cursor/Copilot

## Princípios

1. **OWASP como framework, não como checklist cego.** O OWASP Top 10 2025 é o ponto de partida, mas cada aplicação tem seu contexto. Um app interno sem dados sensíveis tem perfil de risco diferente de um app financeiro público.

2. **Falso positivo é custo.** Cada achado falso queima tempo do dev pra investigar. O pipeline de 3 agentes existe pra minimizar isso — Scanner gera hipóteses, Verifier tenta falsificar, Arbiter decide.

3. **Severidade baseada em impacto real.** "XSS possível" sem contexto de impacto é inútil. A severidade depende de: o que o atacante consegue fazer, quais dados ficam expostos, qual o blast radius.

4. **Secrets são emergência.** Qualquer secret exposto (API key, service_role key, JWT secret) é critical por definição. Não importa o contexto — secret vazado = comprometido.

5. **RLS é a última linha de defesa.** Em apps Supabase, o código frontend roda no browser do usuário. Sem RLS, qualquer pessoa com a anon key acessa dados de qualquer outro usuário. Isso não é "melhoria" — é brecha.

6. **Re-inspeção independente.** Mesmo padrão do repo-review: cada agente lê o código/config real. Nenhum agente confia apenas no texto do agente anterior.

7. **Camada determinística primeiro.** Antes dos agentes IA, rode linters e SAST tools quando disponíveis. Regras estáticas pegam o óbvio (secrets hardcoded, npm audit) sem custo de falso positivo dos agentes.

## Modos de operação

### Modo VPS (via SSH)

**Input:** Acesso SSH ao servidor via Claude Code.
**Foco:** Segurança do servidor — hardening, portas, serviços, permissões, configurações de rede.
**Quando usar:** Quando quer saber se o servidor está protegido contra ataques externos e internos.

### Modo Code (via GitHub)

**Input:** Repositório GitHub clonado ou acessível via Claude Code.
**Foco:** Segurança da aplicação — OWASP Top 10, Supabase, React, autenticação, secrets.
**Quando usar:** Quando quer saber se o código e a configuração do app estão seguros. Principal caso de uso: projetos Lovable antes de ir pra produção.

**Stack alvo principal:** React/TypeScript + Supabase (Lovable stack), mas adaptável pra qualquer stack web.

### Modo combinado

Se o usuário quer auditoria completa (servidor + código), rode os dois modos sequencialmente. Comece pelo Code (mais provável de ter achados actionáveis) e depois VPS.

## Domínios de segurança — Modo Code

### 1. Controle de acesso (OWASP A01:2025)
- RLS habilitado em TODAS as tabelas públicas
- Policies RLS corretas — usar padrão `(select auth.uid()) = user_id` pra performance
- Verificação de ownership em operações de escrita/delete
- Roles e permissões no nível da aplicação
- Acesso a recursos de outros usuários (IDOR)

### 2. Configuração de segurança (OWASP A02:2025)
- Variáveis de ambiente vs hardcoded secrets
- Headers de segurança (CSP, CORS, X-Frame-Options)
- Modo debug desativado em produção
- Permissões de API keys (anon key / `sb_publishable_*` vs service_role / `sb_secret_*`)
- Supabase: service_role key NUNCA no frontend

### 3. Supply chain (OWASP A03:2025)
- Dependências com vulnerabilidades conhecidas (`npm audit`, Snyk)
- Lock files presentes e versionados (`package-lock.json` ou `pnpm-lock.yaml`)
- Scripts de build confiáveis — lifecycle hooks podem executar código malicioso
- Typosquatting: pacotes com nomes 1-2 chars diferentes de libs populares
- Dependências com poucas downloads + muitas permissões = red flag
- `npm ci` no CI/CD em vez de `npm install`

### 4. Criptografia (OWASP A04:2025)
- HTTPS enforçado
- Dados sensíveis encriptados at rest
- Tokens e sessões com expiração adequada
- Supabase: JWT agora suporta RS256 (asymmetric) — verificar se está configurado

### 5. Injeção (OWASP A05:2025)
- SQL injection (queries raw sem sanitização)
- XSS via `dangerouslySetInnerHTML` — verificar se tem DOMPurify
- XSS via `href="javascript:"` — validar protocolos em URLs dinâmicas
- XSS via manipulação direta de DOM (refs, innerHTML)
- Template injection

### 6. Design inseguro (OWASP A06:2025)
- Lógica de negócio no frontend (pode ser bypassada)
- Validação apenas no cliente sem server-side
- Rate limiting ausente em endpoints sensíveis
- Cálculos de preço/permissão no frontend

### 7. Autenticação (OWASP A07:2025)
- Fluxo de auth completo (signup, login, reset, logout)
- Session management (expiração, revogação)
- MFA disponível pra operações sensíveis (Supabase suporta TOTP + AAL levels)
- Token storage (localStorage = XSS-vulnerable vs httpOnly cookies)
- Proteção em rotas: RLS no banco ou middleware no backend, não só `useAuth()` no frontend

### 8. Integridade (OWASP A08:2025)
- Supabase database webhooks e triggers validados
- Edge Functions com input validation
- Dependências verificadas (SRI hashes, lockfiles)

### 9. Logging e alertas (OWASP A09:2025)
- Eventos de segurança logados (login, falha de auth, mudança de permissão)
- Logs não expõem dados sensíveis (PII, tokens, senhas)

### 10. Tratamento de exceções (OWASP A10:2025)
- Erros não expõem stack traces ou dados internos ao usuário
- Fail-safe: sistema nega acesso quando algo dá erro, não permite

## Domínios de segurança — LLM/AI (OWASP Top 10 for LLM 2025)

Aplique APENAS se o app tem features de IA (chatbot, agente, RAG, geração de conteúdo).

### LLM01: Prompt Injection
- System prompt separado de user input? Ou concatenação direta?
- Input do usuário sanitizado antes de ir pro LLM?
- Existe validação de output do LLM antes de executar ações?

### LLM02: Sensitive Information Disclosure
- O system prompt contém secrets, API keys, ou dados de negócio?
- O modelo tem acesso a dados que o usuário não deveria ver?
- Logs de conversa armazenam dados sensíveis sem mascaramento?

### LLM06: Excessive Agency
- O LLM tem mais permissões do que precisa? (princípio do least privilege)
- Ações destrutivas (delete, update, enviar email) passam por aprovação humana?
- API tokens do LLM estão com escopo mínimo?

### LLM07: System Prompt Leakage (NOVO 2025)
- System prompt é extraível via "repita suas instruções"?
- Secrets no system prompt? (devem estar em environment variables/external secrets)
- Instruções sensíveis de negócio no prompt que não deveriam vazar?

### LLM08: Vector & Embedding Weaknesses (NOVO 2025)
- RAG: corpus de documentos validado ou qualquer fonte é indexada?
- Multi-tenant: embeddings de um tenant acessíveis por outro?
- Vector store com controle de acesso (RLS no Supabase pgvector)?

## Domínios de segurança — Modo VPS

### 1. Hardening do SO
- Patches de segurança aplicados
- Serviços desnecessários desativados
- Kernel params de segurança (sysctl)
- SELinux/AppArmor ativo

### 2. Acesso e autenticação
- SSH: key-only, root desabilitado, porta não-padrão (opcional)
- Usuarios com privilégios mínimos
- Fail2ban ativo e configurado
- Sudo: quem tem e por quê

### 3. Rede
- Firewall ativo com whitelist
- Portas expostas = mínimo necessário
- SSL/TLS válido e atualizado
- Rate limiting no reverse proxy

### 4. Containers
- Docker socket NÃO exposto a containers
- Containers rodando como non-root
- Imagens de sources confiáveis
- Sem privileged mode

### 5. Secrets e credenciais
- Secrets em environment variables ou secret manager, não em arquivos
- .env fora do git (verificar .gitignore)
- Chaves de API com escopo mínimo

## Camada determinística (NOVO v2)

Antes de acionar os agentes IA, rode verificações determinísticas quando possível:

### Verificações automáticas (Modo Code)
```bash
# 1. Secrets hardcoded (grep patterns)
grep -rn "sk_live\|sk_test\|service_role\|SUPABASE_SERVICE_ROLE\|Bearer [A-Za-z0-9]" src/ --include="*.ts" --include="*.tsx" --include="*.js"

# 2. npm audit
npm audit --json 2>/dev/null | head -100

# 3. dangerouslySetInnerHTML sem DOMPurify
grep -rn "dangerouslySetInnerHTML" src/ --include="*.tsx" --include="*.jsx"

# 4. href com protocolo dinâmico
grep -rn 'href={' src/ --include="*.tsx" --include="*.jsx" | grep -v "https\|http\|mailto\|tel\|/"

# 5. .env no git
git ls-files | grep -E "\.env$|\.env\."

# 6. RLS verification (se migrations existem)
grep -rL "ENABLE ROW LEVEL SECURITY" supabase/migrations/ 2>/dev/null
```

### SAST tools (se disponíveis)
- **Semgrep** (preferido — 50-250x mais rápido que SonarQube, regras YAML intuitivas pra React/TS)
  - `semgrep --config=auto src/` pra scan básico
  - Regras custom pra padrões Supabase/Lovable
- **CodeQL** (se repo no GitHub — nativo, excelente precisão, 5% false positives)
  - GitHub Actions: `github/codeql-action/analyze`

Documente o que a camada determinística encontrou. Passe os resultados como contexto pro Scanner — isso foca o agente nos problemas que o grep/SAST não pega (lógica, design, fluxo).

## Riscos de código gerado por IA (NOVO v2)

Apps Lovable, Cursor, e Copilot têm padrões de vulnerabilidade específicos. O Stanford Research Lab mostrou que desenvolvedores com AI assistants produzem código mais inseguro E se sentem mais confiantes sobre a segurança — falsa sensação de proteção.

### Checklist pra código AI-generated
- [ ] Input validation presente? (AI frequentemente omite bounds checks e type validation)
- [ ] Secrets hardcoded? (AI gera exemplos com API keys reais ou placeholder que ficam)
- [ ] SQL injection? (AI gera queries concatenadas em vez de parametrizadas)
- [ ] Auth checks em todos endpoints? (AI esquece middleware em rotas que deveriam ser protegidas)
- [ ] Error handling expõe informações? (AI gera catch blocks com stack trace no response)
- [ ] Race conditions? (AI não pensa em concorrência — inserts sem UNIQUE constraints)
- [ ] Dependências adicionadas pelo AI são legítimas? (verificar se não é pacote inexistente/typosquatting)

## O pipeline

```
[Camada determinística: grep, npm audit, SAST]
    ↓ contexto pra agentes
Scanner (references/scanner-prompt.md)
    ↓ output: lista de vulnerabilidades potenciais com evidência
Verifier (references/verifier-prompt.md)
    ↓ output: cada achado confirmado, rejeitado, ou evidência insuficiente
Arbiter (references/arbiter-prompt.md)
    ↓ output: veredictos finais com classificação OWASP e recomendação
Apresentar relatório ao usuário
```

## Como executar

### Pré-requisito

- **Modo Code:** Repositório clonado localmente ou acessível via GitHub. Se o usuário fornecer link do GitHub, clone primeiro.
- **Modo VPS:** Acesso SSH ao servidor via Claude Code.

Pergunte qual modo o usuário quer antes de iniciar. Se mencionou "código", "app", "Lovable", "repositório" → Modo Code. Se mencionou "servidor", "VPS", "SSH" → Modo VPS.

### Passo 0 — Camada determinística (Modo Code)

Rode as verificações automáticas da seção "Camada determinística". Documente achados. Passe como contexto pro Scanner no Passo 1.

### Passo 1 — Scanner

Consulte `references/scanner-prompt.md` pra o prompt completo.

O Scanner faz:
1. Identifica a stack e estrutura do projeto (ou do servidor)
2. Recebe achados da camada determinística como input
3. Varre sistematicamente cada domínio de segurança aplicável (incluindo LLM se app tem IA)
4. Gera lista de vulnerabilidades potenciais com:
   - vuln_id, título, localização exata
   - Categoria OWASP (se Modo Code) — incluindo OWASP LLM se aplicável
   - Severidade (critical/high/medium/low/info)
   - Tier: CONFIRMED (certeza alta) ou SUSPICIOUS (precisa verificar)
   - Evidência: código/config que sustenta o achado
   - Contra-argumento: razão mais forte pela qual pode NÃO ser vulnerabilidade
5. Cap: 15 achados, máximo 4 SUSPICIOUS

### Passo 2 — Verifier

Consulte `references/verifier-prompt.md` pra o prompt completo.

O Verifier faz:
1. Re-inspeciona o código/config de cada achado do Scanner
2. Tenta FALSIFICAR cada achado — procura evidência de que NÃO é vulnerabilidade
3. Verifica se existem mitigações que o Scanner pode ter perdido
4. Classifica: CONFIRMED / REJECTED / INSUFFICIENT_EVIDENCE
5. Se rejeitar, explica por quê com evidência

### Passo 3 — Arbiter

Consulte `references/arbiter-prompt.md` pra o prompt completo.

O Arbiter faz:
1. Avalia argumentos do Scanner e Verifier
2. Pra achados de severidade high/critical, re-inspeciona o código uma última vez
3. Emite veredicto: VULNERABLE / NOT_VULNERABLE / NEEDS_HUMAN_CHECK
4. Adiciona classificação OWASP final e recomendação de fix
5. Gera relatório priorizado

## Contrato de output

### Scanner → Verifier

```
vuln_id: SEC-001
title: Tabela 'profiles' sem RLS — qualquer usuário autenticado acessa todos os perfis
category: A01:2025 Broken Access Control
location: supabase/migrations/001_create_profiles.sql
severity: critical
tier: CONFIRMED
evidence: "CREATE TABLE profiles (...); — sem ALTER TABLE profiles ENABLE ROW LEVEL SECURITY"
counter_argument: "Se a tabela só é acessada via Edge Function com service_role, RLS não seria necessário no path normal"
```

### Verifier → Arbiter

```
vuln_id: SEC-001
scanner_severity: critical
verifier_status: CONFIRMED
verifier_evidence: "Confirmado. A tabela é acessada diretamente pelo frontend via supabase.from('profiles').select(). Sem RLS, qualquer usuário autenticado pode fazer SELECT * e ver todos os perfis. Não encontrei Edge Function intermediária."
```

### Arbiter → Usuário

```
vuln_id: SEC-001
title: Tabela 'profiles' sem RLS — acesso irrestrito a dados de todos os usuários
category: A01:2025 Broken Access Control
severity: critical
verdict: VULNERABLE
confidence: 0.95
evidence_summary: "Tabela acessada diretamente pelo frontend sem RLS. SELECT * retorna todos os registros."
fix: "ALTER TABLE profiles ENABLE ROW LEVEL SECURITY; CREATE POLICY select_own ON profiles FOR SELECT USING ((select auth.uid()) = user_id);"
priority: Corrigir imediatamente — dados de usuários expostos
```

## Severidades

| Severidade | Critério | Exemplo |
|---|---|---|
| **critical** | Acesso não autorizado a dados ou sistema, exploitável remotamente | RLS ausente em tabela com dados de usuários, service_role key no frontend, SQL injection |
| **high** | Vulnerabilidade exploitável com condições específicas | XSS via dangerouslySetInnerHTML com input de usuário, IDOR em endpoint de API |
| **medium** | Fraqueza que aumenta superfície de ataque | Sem CSP headers, tokens em localStorage, sem rate limiting |
| **low** | Desvio de best practice sem risco imediato | Dependência desatualizada sem CVE conhecido, logs verbose em produção |
| **info** | Observação de arquitetura sem risco direto | Lógica de validação só no frontend (duplicar no backend recomendado) |

## Red flags

- Nunca pule o Verifier. Taxa de falso positivo do Scanner sozinho é 30-60%.
- Nunca classifique secret exposto como menos que critical. Secret vazado = comprometido, sem exceção.
- Nunca assuma que RLS está configurado sem verificar. "O Lovable deve ter criado" não é evidência.
- Nunca faça security audit parcial sem avisar. Se não verificou autenticação por falta de acesso, documente como gap.
- Nunca confie que código AI-generated é seguro. Stanford provou o contrário — AI aumenta vulnerabilidades E confiança ao mesmo tempo.

## Integração com outras skills

- **VPS Infra Audit:** Se o Security Audit (Modo VPS) encontrar problemas de infra que não são segurança pura (disco cheio, sem monitoring), sugira rodar vps-infra-audit.
- **Supabase DB Architect:** Se encontrar problemas de schema que facilitam vulnerabilidades (colunas sem tipo correto, FKs ausentes), sugira a skill de Supabase.
- **Repo Review:** Se encontrar bugs funcionais durante o scan de segurança, documente mas sugira repo-review pra análise completa.
- **Tech Lead & PM:** Vulnerabilidades critical/high devem virar tasks no ClickUp com prazo imediato.

## Quando NÃO usar esta skill

- Se é bug funcional sem implicação de segurança → use repo-review
- Se é performance/infra sem foco em segurança → use vps-infra-audit
- Se é UX/UI → use ux-audit
- Se é pergunta pontual sobre segurança ("como configuro CSP?") → responda direto
- Se é schema de banco sem contexto de segurança → use supabase-db-architect
