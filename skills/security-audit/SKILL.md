---
name: security-audit
description: "Three-agent security audit pipeline (Scanner → Verifier → Arbiter). Three modes: Code (OWASP Top 10, RLS, secrets, XSS, injection, auth), VPS (hardening, ports, containers, firewall), Web (blackbox pentest — headers, SSL, CORS, DNS). Use when: 'audit security', 'tem vulnerabilidade?', 'tá seguro?', 'revisa a segurança'. Stack: React/Supabase, adaptável. Includes OWASP LLM Top 10 for AI features."
---

# Security Audit v2

IRON LAW: NEVER skip the Verifier agent. Single-agent scanning has 30-60% false positive rate — independent verification is non-negotiable. NEVER apply security fixes without explicit user confirmation.

Pipeline de 3 agentes: **Scanner → Verifier → Arbiter**. Três modos: Code (OWASP Top 10 2025 + Supabase RLS + secrets + XSS + auth), VPS (hardening + portas + containers + firewall), e Web (blackbox pentest externo — headers, SSL, paths, CORS, DNS, bundle JS, Chrome MCP). Camada determinística roda antes dos agentes.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | Modo: `code`, `vps`, `web`, `combined` | auto-detect |
| `--target <t>` | Repo path, SSH host, GitHub URL, ou HTTPS URL (web) | current dir |
| `--llm` | Inclui OWASP LLM Top 10 (apps com IA) | auto-detect |
| `--deterministic-only` | Só roda camada determinística, sem agentes | false |

## Workflow

```
Security Audit Progress:

- [ ] Phase 0: Detect Mode ⚠️ REQUIRED
  - [ ] 0.1 Identificar modo (Code/VPS/Web/Combined)
  - [ ] 0.2 Validar acesso (repo / SSH / URL HTTPS)
  - [ ] 0.3 Se Combined: separar pipelines independentes
- [ ] Phase 1: Deterministic Layer ⚠️ REQUIRED
  - [ ] Modo Code: secrets grep, npm audit, XSS patterns, RLS, .env no git, SAST
  - [ ] Modo Web: curl headers, path enumeration, SSL, DNS, CORS, cookies, bundle JS, Chrome MCP
  - [ ] Modo VPS: integrado ao Scanner
  - [ ] Load references/deterministic-layer.md
- [ ] Phase 2: Scanner (Agent 1) ⚠️ REQUIRED
  - [ ] Dispatch with references/scanner-prompt.md
  - [ ] Load references/owasp-web-checklist.md (Code)
  - [ ] Load references/vps-security-domains.md (VPS)
  - [ ] Load references/web-pentest-domains.md (Web)
  - [ ] Load references/owasp-llm-checklist.md (se app tem IA)
  - [ ] Load references/ai-generated-risks.md (se AI-generated)
  - [ ] Collect output (max 15 findings, max 4 SUSPICIOUS)
- [ ] Phase 3: Verifier (Agent 2) ⛔ BLOCKING — NÃO PULAR
  - [ ] Dispatch with references/verifier-prompt.md
  - [ ] Re-inspeção independente de cada achado
  - [ ] Classificar: CONFIRMED / REJECTED / INSUFFICIENT_EVIDENCE
- [ ] Phase 4: Arbiter (Agent 3)
  - [ ] Dispatch with references/arbiter-prompt.md
  - [ ] Re-inspecionar todos critical + disputados
  - [ ] Veredictos finais + fixes concretos
  - [ ] Load references/output-contracts.md pra formato
- [ ] Phase 5: Present ⛔ BLOCKING
  - [ ] Relatório priorizado por severidade
  - [ ] ⛔ GATE: Apresentar ao usuário — NENHUM fix sem confirmação
  - [ ] Se critical: destacar como ação imediata
```

## Phase 0: Detect Mode

Identifique o modo antes de qualquer coisa:

| Contexto do usuário | Modo |
|---------------------|------|
| "código", "app", "Lovable", "repositório", "GitHub" | Code |
| "servidor", "VPS", "SSH", "Docker" | VPS |
| "site", "URL", "https://", "pentest", "blackbox", "ao vivo" | Web |
| "auditoria completa", "tudo" | Combined (pipelines independentes) |

**Se ambíguo:** pergunte. Não assuma.

## Phase 1: Deterministic Layer

Load `references/deterministic-layer.md` pra comandos completos.

Rode verificações automáticas ANTES dos agentes. Documente resultados. Passe como contexto pro Scanner.

**Modo Code:** secrets hardcoded, npm audit, XSS patterns, .env no git, RLS em migrations, SAST tools.
**Modo Web:** curl headers, path enumeration (/.git, /.env, /admin, etc.), SSL check, DNS-over-HTTPS, CORS preflight, cookies, bundle JS, Chrome MCP (localStorage, network, DOM).
**Modo VPS:** checagem integrada ao Scanner — sem fase determinística separada.

## Phase 2: Scanner (Agent 1)

Load `references/scanner-prompt.md` pra prompt completo.

**Modo Code:** Load `references/owasp-web-checklist.md`. Se app tem IA: load `references/owasp-llm-checklist.md`. Se AI-generated: load `references/ai-generated-risks.md`.

**Modo VPS:** Load `references/vps-security-domains.md`.

**Modo Web:** Load `references/web-pentest-domains.md`. Se site é Lovable/AI-generated: load `references/ai-generated-risks.md`.

O Scanner:
1. Identifica stack/estrutura do projeto (ou do servidor)
2. Recebe achados da camada determinística como input
3. Varre sistematicamente cada domínio de segurança aplicável
4. Gera lista de vulnerabilidades com evidência, categoria OWASP, severidade, tier, contra-argumento
5. Cap: 15 achados, máximo 4 SUSPICIOUS

## Phase 3: Verifier (Agent 2)

Load `references/verifier-prompt.md` pra prompt completo.

O Verifier:
1. Re-inspeciona o código/config real de cada achado — NÃO confia no texto do Scanner
2. Tenta FALSIFICAR cada achado — procura mitigações que o Scanner perdeu
3. Classifica: CONFIRMED / REJECTED / INSUFFICIENT_EVIDENCE
4. Se rejeitar, explica por quê com evidência concreta

## Phase 4: Arbiter (Agent 3)

Load `references/arbiter-prompt.md` pra prompt completo. Load `references/output-contracts.md` pra formato.

O Arbiter:
1. Avalia argumentos do Scanner e Verifier
2. Re-inspeciona todos critical + achados onde Scanner ≠ Verifier
3. Emite veredicto: VULNERABLE / NOT_VULNERABLE / NEEDS_HUMAN_CHECK
4. Adiciona classificação OWASP final + fix concreto (código pronto)
5. Gera relatório priorizado

## Phase 5: Present ⛔ BLOCKING

Load `references/output-contracts.md` pra formato do relatório e escala de severidade.

### Output Format

```markdown
## Relatório de Segurança — [Modo] — [projeto] — [data]

### Resumo executivo
- Risco geral: [CRITICO/ALTO/MEDIO/BAIXO]
- Vulnerabilidades confirmadas: X (Y critical, Z high)
- Requer verificação humana: N

### Vulnerabilidades confirmadas (por severidade)
[SEC-001 a SEC-N com categoria OWASP, evidência, fix pronto]

### Achados rejeitados
[Lista breve com justificativa]

### Cobertura da auditoria
[Tabela de domínios verificados / não verificados]

### Recomendações de arquitetura
[Problemas sistêmicos, não só pontuais]
```

⛔ **Confirmation Gate:** NUNCA aplicar fixes sem escolha explícita do usuário. Opções:
1. **Fix all** — aplicar todos os fixes
2. **Fix critical/high only** — só os mais graves
3. **Fix specific** — usuário escolhe quais
4. **No changes** — relatório entregue, sem alterações

## Design Principles

1. **OWASP como framework, não checklist cego.** Cada app tem seu contexto de risco.
2. **Falso positivo é custo.** O pipeline de 3 agentes existe pra minimizar isso.
3. **Severidade baseada em impacto real.** "XSS possível" sem contexto é inútil.
4. **Secrets são emergência.** Secret exposto = critical, sem exceção.
5. **RLS é última linha de defesa.** Sem RLS, anon key = acesso total. Não é "melhoria".
6. **Re-inspeção independente.** Cada agente lê o código real, não confia no anterior.
7. **Camada determinística primeiro.** Regras estáticas antes dos agentes IA.

## Anti-Patterns

- **Pular o Verifier** — taxa de falso positivo do Scanner sozinho é 30-60%. O Verifier existe por um motivo.
- **Classificar secret como menos que critical** — secret vazado = comprometido, sem exceção, sem contra-argumento.
- **Assumir RLS configurado sem verificar** — "O Lovable deve ter criado" não é evidência. Verificar migration SQL.
- **Audit parcial sem avisar** — se não verificou autenticação por falta de acesso, documentar como gap.
- **Confiar que código AI-generated é seguro** — Stanford provou: AI aumenta vulnerabilidades E confiança ao mesmo tempo.
- **Aplicar fixes sem confirmar com usuário** — viola a Iron Law. Sempre apresentar primeiro.
- **Mesmo modelo pra 3 agentes em mesma thread** — risco de consensus collapse. Cada agente precisa ser independente.
- **Remover cap do Scanner** — achados ilimitados colapsam em ruído. 15 é o máximo.

## Pre-Delivery Checklist

Antes de entregar o relatório final ao usuário:

- [ ] Todos os domínios aplicáveis foram verificados ou gaps documentados?
- [ ] Camada determinística rodou (Modo Code/Web)?
- [ ] Verifier rodou em TODOS os achados do Scanner?
- [ ] Arbiter re-inspecionou TODOS os critical?
- [ ] Cada fix recomendado é código/config pronto pra copiar (não "considere implementar")?
- [ ] Padrões de RLS usam `(select auth.uid())` e não `auth.uid()` direto?
- [ ] Se projeto é AI-generated, padrões sistêmicos documentados?
- [ ] Severidades fazem sentido no contexto do app (não genéricas)?
- [ ] Relatório em PT-BR mesmo se código em inglês?

## When NOT to Use

| Situação | Use em vez |
|----------|-----------|
| Bug funcional sem implicação de segurança | **trident** |
| Performance, infra, disco, escalabilidade | **vps-infra-audit** |
| UX/UI review | **ux-audit** |
| Pergunta pontual sobre segurança ("como configuro CSP?") | Responda direto |
| Schema de banco sem contexto de segurança | **supabase-db-architect** |
| Code review geral (SOLID, code quality) | **trident** |
| Só quer rodar npm audit / Semgrep | Use `--deterministic-only` |

## Integration

- **Trident** — trident acha bugs funcionais, security-audit acha vulnerabilidades. Se trident encontrar achados de segurança, sugira security-audit pra análise OWASP profunda. Inverso: se security-audit encontrar bugs de lógica, documente mas sugira trident.
- **SDD** — SDD pode invocar security-audit como gate de qualidade antes de entregar feature. Input: diff da fase de implementação.
- **VPS Infra Audit** — se security-audit (Modo VPS) encontrar problemas de infra que não são segurança (disco cheio, sem monitoring), sugira vps-infra-audit. Inverso: vps-infra-audit pode sugerir security-audit se encontrar portas suspeitas ou configs inseguras.
- **Architecture Guard** — architecture-guard verifica estrutura e padrões. Se encontrar violações que abrem brechas de segurança (lógica no frontend, etc.), sugira security-audit.
- **Maestro** — maestro roteia pedidos de segurança pra security-audit. Parte de chains de composição.
- **Supabase DB Architect** — se encontrar problemas de schema que facilitam vulnerabilidades (colunas sem tipo correto, FKs ausentes), sugira a skill.
- **Tech Lead & PM** — vulnerabilidades critical/high devem virar tasks no ClickUp com prazo imediato.

## References

| File | Purpose |
|------|---------|
| `references/scanner-prompt.md` | Agent 1: varredura sistemática com contra-argumentos |
| `references/verifier-prompt.md` | Agent 2: verificação independente, tenta falsificar |
| `references/arbiter-prompt.md` | Agent 3: veredictos finais baseados em evidência |
| `references/owasp-web-checklist.md` | OWASP A01-A10:2025 + padrões Supabase RLS |
| `references/owasp-llm-checklist.md` | OWASP LLM01-LLM10:2025 pra apps com IA |
| `references/vps-security-domains.md` | Domínios de segurança VPS + comandos |
| `references/web-pentest-domains.md` | Domínios de pentest Web blackbox + comandos |
| `references/deterministic-layer.md` | Grep patterns, npm audit, SAST tools |
| `references/ai-generated-risks.md` | Padrões de vulnerabilidade em código AI |
| `references/output-contracts.md` | Contratos entre agentes + escala de severidade |
