# Output contracts — Contratos entre agentes

Formato padronizado de comunicação entre Scanner, Verifier e Arbiter. Cada agente preserva o `vuln_id` pra rastreabilidade.

## Scanner → Verifier

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

## Verifier → Arbiter

```
vuln_id: SEC-001
scanner_severity: critical
verifier_status: CONFIRMED
verifier_evidence: "Confirmado. A tabela é acessada diretamente pelo frontend via supabase.from('profiles').select(). Sem RLS, qualquer usuário autenticado pode fazer SELECT * e ver todos os perfis. Não encontrei Edge Function intermediária."
```

## Arbiter → Usuário (relatório final)

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

## Schema compartilhado

| Field | Scanner | Verifier | Arbiter |
|-------|---------|----------|---------|
| `vuln_id`, `title`, `location` | Cria | Preserva | Preserva |
| `category` (OWASP) | Cria | Preserva | Pode corrigir |
| `severity` | Inicial | Pode revisar | Final |
| `tier` (CONFIRMED/SUSPICIOUS) | Cria | — | — |
| `status` | — | CONFIRMED/REJECTED/INSUFFICIENT_EVIDENCE | — |
| `verdict` | — | — | VULNERABLE/NOT_VULNERABLE/NEEDS_HUMAN_CHECK |
| `confidence` | — | — | 0.0–1.0 |
| `fix` | — | — | Código/config pronto |
| `counter_argument` | Cria | Avalia | — |

## Escala de severidade

| Severidade | Critério | Exemplo |
|---|---|---|
| **critical** | Acesso não autorizado a dados ou sistema, exploitável remotamente | RLS ausente em tabela com dados de usuários, service_role key no frontend, SQL injection |
| **high** | Vulnerabilidade exploitável com condições específicas | XSS via dangerouslySetInnerHTML com input de usuário, IDOR em endpoint de API |
| **medium** | Fraqueza que aumenta superfície de ataque | Sem CSP headers, tokens em localStorage, sem rate limiting |
| **low** | Desvio de best practice sem risco imediato | Dependência desatualizada sem CVE conhecido, logs verbose em produção |
| **info** | Observação de arquitetura sem risco direto | Lógica de validação só no frontend (duplicar no backend recomendado) |

## Escala de risco geral (Arbiter)

| Risco | Critério |
|---|---|
| **CRITICO** | Pelo menos 1 vulnerabilidade critical confirmada. Dados expostos ou acesso não autorizado possível agora. |
| **ALTO** | Sem critical, mas 2+ high confirmados. Superfície de ataque significativa. |
| **MEDIO** | Sem critical/high, mas achados medium que, combinados, aumentam risco. |
| **BAIXO** | Apenas achados low/info. Boas práticas não seguidas mas sem risco imediato. |

## Caps e limites

- **Scanner:** máximo 15 achados, máximo 4 SUSPICIOUS (resto deve ser CONFIRMED)
- **Verifier:** verifica todos os achados do Scanner, foco de esforço em critical/high
- **Arbiter:** re-inspeciona todos critical + achados disputados (Scanner ≠ Verifier)
