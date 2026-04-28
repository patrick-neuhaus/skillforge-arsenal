---
name: vps-infra-audit
description: "Pipeline 3 agentes pra auditoria profunda de VPS. Audita, inspeciona, escaneia servidores. Revisa Docker, segurança de rede, resource limits, performance, escalabilidade. Use SEMPRE em: VPS, servidor, infra, infraestrutura, 'como tá meu servidor', 'audit de infra', Docker Swarm, escalabilidade, 'servidor lento', 'preciso escalar', 'tá tudo no mesmo servidor', isolamento, multi-tenant, containers, hardening, 'servidor tá seguro?', server audit, infrastructure review, scan infrastructure, optimize server, plan scaling. Diferente de security-audit: esta = INFRA (SO, Docker, rede, storage); security-audit = APLICAÇÃO (código, RLS, OWASP, auth)."
---

# VPS Infra Audit v2

IRON LAW: NUNCA execute comandos destrutivos (rm, drop, stop, format, systemctl stop, docker rm) sem confirmação explícita do usuário. Auditoria significa OBSERVAR, não modificar. O Collector é read-only. O Architect PROPOE — quem aplica é o usuário.

Pipeline sequencial de 3 agentes: **Collector -> Analyzer -> Architect**. Coletar dados reais via SSH, analisar contra CIS Benchmarks e boas práticas, propor soluções concretas em waves.

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `--ssh` | Servidor tem SSH acessível via Claude Code | auto-detect |
| `--manual` | Modo manual: apresenta comandos pro usuário colar outputs | false |
| `--domain <d>` | Focar em domínio específico (docker, rede, storage, etc.) | todos (8) |
| `--fast` | Coleta rápida: só domínios críticos (Docker, Rede, Recursos) | false |

## Workflow

```
VPS Infra Audit Progress:

- [ ] Phase 0: Preflight ⚠️ REQUIRED
  - [ ] 0.1 Verificar acesso SSH ou definir modo manual
  - [ ] 0.2 Identificar SO e adaptar comandos
  - [ ] ⛔ GATE: Sem acesso SSH E usuário não quer modo manual → PARAR
- [ ] Phase 1: Collector (Agent 1) ⚠️ REQUIRED
  - [ ] Dispatch com references/collector-prompt.md
  - [ ] Coletar dados dos 8 domínios
  - [ ] Organizar output por domínio
  - [ ] ⛔ GATE: Sem dados coletados → NÃO prosseguir pro Analyzer
- [ ] Phase 2: Analyzer (Agent 2) ⚠️ REQUIRED
  - [ ] Dispatch com references/analyzer-prompt.md
  - [ ] Analisar contra CIS Benchmarks Level 1
  - [ ] Aplicar checklist Docker security hardening (3 níveis)
  - [ ] Gerar max 25 achados com evidência + contra-argumento
- [ ] Phase 3: Architect (Agent 3)
  - [ ] Dispatch com references/architect-prompt.md
  - [ ] Agrupar achados por tema
  - [ ] Propor soluções em 3 waves (Crítico / Importante / Estratégico)
  - [ ] Incluir comandos/configs prontos pra aplicar
- [ ] Phase 4: Apresentar ⛔ BLOCKING
  - [ ] Formatar plano com waves e arquitetura-alvo
  - [ ] ⛔ GATE: Apresentar ao usuário — NENHUMA mudança sem confirmação
```

## Phase 0: Preflight

Verificar acesso SSH. Se Claude Code tem SSH configurado, seguir com pipeline automático. Se não:

1. Ajudar a configurar SSH, OU
2. Modo manual: apresentar lista de comandos pro usuário executar e colar outputs

⛔ **Sem acesso a dados reais, o pipeline não funciona.** Análise sem dados do servidor é achismo.

## Phase 1: Collector (Agent 1)

Load `references/collector-prompt.md` para prompt completo e comandos por domínio.

O Collector executa comandos read-only organizados em 8 domínios:

1. **SO e Kernel** — versão, patches, sysctl, usuários, cron, SELinux/AppArmor
2. **Docker e Containers** — versões, containers, limits, volumes, networks, security posture
3. **Rede** — portas, firewall, reverse proxy, SSL/TLS, fail2ban, VPN
4. **Storage** — disco, filesystem, backups, cleanup
5. **Recursos** — CPU, RAM, swap, OOM, I/O, limits
6. **Isolamento Multi-tenant** — separação rede/storage/recursos por cliente
7. **Escalabilidade** — orquestração, replicas, rolling updates
8. **Monitoring e Observabilidade** — Prometheus, Grafana, Uptime Kuma, Falco, Trivy

Output: documento estruturado com dados brutos por domínio. Sem interpretação.

## Phase 2: Analyzer (Agent 2)

Load `references/analyzer-prompt.md` para prompt completo e critérios por domínio.

O Analyzer recebe dados do Collector e:

1. Analisa cada domínio contra CIS Benchmarks Level 1 + boas práticas
2. Aplica checklist Docker security hardening (Load `references/docker-security-hardening.md`)
3. Verifica presença de monitoring/observabilidade
4. Gera max 25 achados com: domínio, título, severidade, evidência, impacto, contra-argumento
5. Inclui Docker Security Hardening Assessment (score por nível)

## Phase 3: Architect (Agent 3)

Load `references/architect-prompt.md` para prompt completo e padrões de arquitetura.

O Architect transforma achados em plano de ação:

1. Agrupa por tema e prioridade
2. Usa matriz de orquestração quando relevante (Load `references/orchestration-matrix.md`)
3. Propõe soluções concretas com comandos/configs prontos
4. Organiza em 3 waves: Crítico (agora) / Importante (esta semana) / Estratégico (este mês)
5. Desenha arquitetura-alvo vs arquitetura atual
6. Inclui monitoring stack quando ausente (Load `references/monitoring-stack.md`)
7. Referência n8n quando aplicável (Load `references/n8n-self-hosted.md`)

Cada ação tem: o que fazer, por que, comando/config, risco, rollback, tempo estimado.

## Phase 4: Apresentar

⛔ **GATE: Apresentar plano ao usuário. NUNCA aplicar mudanças sem confirmação explícita.**

Formato de saída: Load `references/severity-output-contract.md`

Opções pro usuário:
1. **Aplicar Wave 1** — ações críticas
2. **Aplicar tudo** — todas as waves em sequência
3. **Escolher ações específicas** — cherry-pick
4. **Só o relatório** — sem aplicar nada

## Princípios

1. **Dados antes de opinião.** Sem dados reais do servidor, o pipeline para.
2. **Separação de responsabilidades.** Collector coleta. Analyzer analisa. Architect propõe. Não misture.
3. **Contexto de produção.** VPS roda serviços reais. Toda recomendação considera impacto, janela de manutenção, risco de downtime.
4. **CIS Benchmarks como baseline.** Level 1 é o piso mínimo.
5. **Multi-tenant exige isolamento real.** Rede, storage, recursos — fronteira clara entre tenants.
6. **Defense in depth.** Camadas de segurança se compensam mutuamente.
7. **Observabilidade não é opcional.** Servidor sem monitoring é bomba-relógio.

## Domínios da auditoria

| # | Domínio | Foco |
|---|---------|------|
| 1 | SO e Kernel | Patches, sysctl, usuários, cron, MAC |
| 2 | Docker e Containers | Versões, limits, security posture, rootless |
| 3 | Rede | Portas, firewall, proxy, SSL, fail2ban, Zero Trust |
| 4 | Storage | Disco, backups, cleanup |
| 5 | Recursos | CPU, RAM, swap, OOM, I/O |
| 6 | Isolamento Multi-tenant | Rede/storage/recursos por cliente |
| 7 | Escalabilidade | Orquestração, replicas, rolling updates |
| 8 | Monitoring | Prometheus, Grafana, Uptime Kuma, Falco, Trivy |

## Anti-patterns

- **Pular o Collector.** Análise sem dados reais é achismo. NUNCA.
- **Misturar papéis.** Collector que interpreta, Analyzer que propõe solução, Architect que re-analisa.
- **Comandos destrutivos na coleta.** O Collector é 100% read-only. Sem exceção.
- **"Reinicia o Docker" como solução.** Pode derrubar 15 containers de clientes diferentes.
- **Recomendar rootless cegamente.** Tem limitações reais: sem cgroup limits, sem bind <1024, sem overlay networks.
- **Ignorar multi-tenant.** Se tem serviços de clientes diferentes, TODA ação precisa considerar isolamento.
- **Trivy desatualizado.** Supply chain incident mar/2026 — SEMPRE >= v0.69.3.
- **Recomendar DCT.** Sendo descontinuado. Usar Sigstore/Cosign.
- **Aplicar mudanças sem confirmação.** Viola a Iron Law. Sempre apresentar antes.

## Pre-delivery checklist

Antes de entregar o relatório ao usuário, verificar:

- [ ] Todos os 8 domínios foram cobertos (ou gaps documentados)?
- [ ] Cada achado tem evidência citando output real do servidor?
- [ ] Cada achado tem contra-argumento?
- [ ] Docker Security Hardening Assessment incluso com score por nível?
- [ ] Monitoring status avaliado (Presente/Parcial/Ausente)?
- [ ] Waves organizadas por urgência real (não por domínio)?
- [ ] Cada ação de Wave 1/2 tem comando/config pronto pra aplicar?
- [ ] Ações com risco de downtime marcadas com aviso + rollback?
- [ ] Arquitetura-alvo desenhada (não só fixes pontuais)?
- [ ] Plano é delegável pra dev junior executar com supervisão mínima?

## Quando NAO usar esta skill

- **Problema de código/aplicação** (bugs, lógica, UI) -> use trident ou ux-audit
- **Segurança de aplicação** (OWASP, RLS, secrets, autenticação) -> use security-audit
- **Schema de banco sem contexto de infra** -> use supabase-db-architect
- **Pergunta pontual sobre Docker/Linux** -> responda direto sem acionar o pipeline
- **Sem acesso SSH e sem possibilidade de colar outputs** -> skill não funciona sem dados
- **Servidor managed/PaaS** (Heroku, Render, Railway) -> não tem acesso a infra

## Integração

- **security-audit** — VPS Infra Audit cobre INFRA (SO, Docker, rede). Security Audit cobre APLICAÇÃO (código, RLS, OWASP). Se encontrar problemas de segurança de app, encaminhe pra security-audit.
- **trident** — Se durante o audit encontrar código problemático em configs ou scripts, trident faz review detalhado.
- **maestro** — Maestro pode rotear pedidos de "revisa meu servidor" pra esta skill. Parte de cadeias de composição.
- **context-tree** — Após o audit, context-tree pode documentar a arquitetura do servidor pra referência futura da equipe.
- **n8n-architect** — Se encontrar problemas na arquitetura n8n (single instance, sem workers), sugira n8n-architect pra redesenhar.
- **tech-lead-pm** — Findings high/critical podem virar tasks no ClickUp. Sugira criar tasks pra equipe executar as waves.

## References

| Arquivo | Conteúdo |
|---------|----------|
| `references/collector-prompt.md` | Agent 1: comandos de coleta por domínio |
| `references/analyzer-prompt.md` | Agent 2: critérios de análise e severidade |
| `references/architect-prompt.md` | Agent 3: padrões de arquitetura e waves |
| `references/docker-security-hardening.md` | Checklist 3 níveis + compose de referência |
| `references/monitoring-stack.md` | Uptime Kuma, Prometheus, Grafana, Falco, Trivy |
| `references/n8n-self-hosted.md` | n8n production-ready, Swarm, backup |
| `references/zero-trust-tailscale.md` | Tailscale setup e ACLs |
| `references/orchestration-matrix.md` | Compose vs Swarm vs K3s vs Nomad |
| `references/severity-output-contract.md` | Severidades e contratos entre agentes |
