---
name: vps-infra-audit
description: "Pipeline de 3 agentes pra auditoria profunda de infraestrutura VPS. Use esta skill SEMPRE que o usuário mencionar: VPS, servidor, infra, infraestrutura, 'como tá meu servidor', 'audit de infra', Docker Swarm, escalabilidade, 'meu servidor tá lento', 'preciso escalar', 'como configuro minha VPS', 'tá tudo no mesmo servidor', isolamento, multi-tenant, 'quero separar os serviços', containers, 'como organizo meus containers', hardening, 'meu servidor tá seguro?', ou qualquer variação que envolva avaliar, otimizar ou planejar infraestrutura de servidor. Também use quando o usuário reclamar de performance, downtime, ou problemas de deploy — podem ser sintomas de infra mal configurada. Se o contexto for segurança de APLICAÇÃO (código, RLS, autenticação), use security-audit em vez desta. Se for apenas banco de dados sem envolver infra, use supabase-db-architect."
---

# VPS Infra Audit v2 — Auditoria profunda de infraestrutura

## Visão geral

Pipeline sequencial de 3 agentes pra auditoria completa de infraestrutura VPS: **Collector** coleta dados do servidor via SSH, **Analyzer** identifica problemas e riscos, **Architect** propõe soluções e arquitetura de escala.

O principio central é: Coletar → Analisar → Propor. Cada estágio opera com independência — o Collector não interpreta, o Analyzer não propõe solução, o Architect não re-analisa do zero. Isso evita viés de confirmação e garante que cada agente foca no que faz melhor.

A skill cobre 8 domínios de infra: SO/Kernel, Docker/Containers, Rede, Storage, Recursos, Isolamento Multi-tenant, Escalabilidade, e **Monitoring/Observabilidade** (NOVO v2). Cada domínio tem comandos específicos de coleta, critérios de análise baseados em CIS Benchmarks e boas práticas de produção, e padrões de arquitetura recomendados.

### Novidades na v2

- **Matriz de decisão de orquestração** — Docker Compose vs Swarm vs K3s vs Nomad, com critérios objetivos pra cada cenário
- **Docker security hardening** — rootless mode, drop ALL + add específicas, read-only FS, Sigstore/Cosign (DCT descontinuado), SBOMs com Syft
- **Zero Trust networking** — Tailscale como ponto de partida (WireGuard mesh + ACLs + SSO)
- **Monitoring stack** — Prometheus + Grafana pra métricas, Uptime Kuma pra status externo, 3 alertas iniciais
- **Container security** — Falco (CNCF graduated, eBPF) pra intrusion detection, Trivy pra vulnerability scanning (ATENÇÃO: verificar versão ≥ 0.69.3 por supply chain incident mar/2026)
- **n8n self-hosted patterns** — Docker Compose + PG + Redis, queue mode, reverse proxy TLS, pg_dump noturno
- **Domínio 8: Monitoring/Observabilidade** adicionado ao pipeline

## Princípios

1. **Dados antes de opinião.** Nenhuma recomendação sem evidência coletada do servidor real. O Collector existe pra isso — sem dados, o pipeline para.

2. **Separação de responsabilidades.** Collector coleta e organiza. Analyzer identifica problemas. Architect propõe soluções. Misturar papéis gera outputs superficiais.

3. **Contexto de produção.** A VPS roda serviços reais de clientes. Toda recomendação deve considerar: impacto em serviços rodando, janela de manutenção necessária, risco de downtime, e ordem de execução segura.

4. **Escalabilidade como princípio, não como feature.** Não é "se precisar escalar". É "como a arquitetura atual suporta crescimento". Decisões de orquestração são arquiteturais e devem ser avaliadas mesmo que hoje não sejam necessárias.

5. **CIS Benchmarks como baseline.** Pra configuração de SO e rede, os CIS Benchmarks Level 1 são o piso mínimo. Não invente critérios — use os que a indústria já validou.

6. **Multi-tenant exige isolamento real.** Se tem serviços de clientes diferentes no mesmo servidor, isolamento não é opcional. Rede, storage, recursos — tudo precisa de fronteira clara entre tenants.

7. **Defense in depth.** (NOVO v2) Segurança de infra não é um checklist — são camadas. Rootless Docker + network isolation + resource limits + monitoring + vulnerability scanning. Cada camada compensa falhas das outras.

8. **Observabilidade não é opcional.** (NOVO v2) Servidor sem monitoring é servidor que vai te surpreender. Mínimo: métricas de recurso (CPU/RAM/disco), health checks, e alertas pra disco > 80%.

## Domínios da auditoria

### 1. SO e Kernel
- Versão do SO e kernel, patches pendentes
- Parâmetros sysctl (net, vm, fs)
- Usuários e grupos, permissões sudo
- Cron jobs e serviços systemd
- SELinux/AppArmor status
- Logs (journald, syslog, rotação)

### 2. Docker e Containers
- Versão do Docker Engine e Compose
- Containers rodando: imagens, tags, restart policy, health checks
- Resource limits (CPU, memory) por container
- Volumes: bind mounts vs named volumes, permissões
- Networks: bridge, overlay, isolamento entre stacks
- Imagens: tamanho, layers, base images desatualizadas
- Docker Swarm: status do cluster, managers, workers, serviços, replicas
- (NOVO v2) **Security posture**: rootless mode, capabilities, read-only rootfs, user namespaces
- (NOVO v2) **Image provenance**: assinaturas (Sigstore/Cosign), SBOMs

### 3. Rede
- Portas abertas (listening) vs portas necessárias
- Firewall (ufw/iptables/nftables): regras ativas
- Reverse proxy (nginx/traefik/caddy): configuração, SSL/TLS
- DNS: resolução, TTL, registros
- Fail2ban ou equivalente: status e jails ativos
- (NOVO v2) **Zero Trust**: Tailscale/WireGuard mesh, ACLs, acesso por identidade vs por IP

### 4. Storage
- Uso de disco por partição e por container/volume
- Tipo de filesystem e opções de mount
- Backups: existência, frequência, teste de restore
- Cleanup: imagens/volumes/containers órfãos

### 5. Recursos
- CPU: cores, load average, top processes
- RAM: total, usada, swap, OOM history
- I/O: disk throughput, iowait
- Limites do SO: open files, max processes

### 6. Isolamento Multi-tenant
- Separação de rede entre clientes (Docker networks, namespaces)
- Separação de storage (volumes por cliente, permissões)
- Resource limits por tenant (cgroups, Docker limits)
- Acesso: quem tem SSH, quem tem acesso a quais containers
- Logs: separação por tenant, acesso restrito

### 7. Escalabilidade
- Orquestração atual: Compose puro, Swarm, K3s, Nomad
- Service replicas e placement constraints
- Rolling updates e rollback policy
- Overlay networks pra comunicação entre nodes
- Padrão n8n escalável: 1 editor + 1 webhook + N workers
- Horizontal scaling: quando adicionar nodes vs vertical scaling
- Load balancing: estratégia atual e recomendada

### 8. Monitoring e Observabilidade (NOVO v2)
- Coleta de métricas: Prometheus/node_exporter, cAdvisor
- Dashboards: Grafana
- Uptime externo: Uptime Kuma ou equivalente
- Alertas configurados: quais, pra onde notificam
- Logs centralizados: stack atual (se existe)
- Container runtime security: Falco ou equivalente
- Vulnerability scanning: Trivy ou equivalente

## Matriz de decisão de orquestração (NOVO v2)

Quando o Architect recomendar orquestração, use esta matriz:

| Critério | Docker Compose | Docker Swarm | K3s | Nomad |
|---|---|---|---|---|
| Complexidade de setup | Mínima | Baixa | Média | Média-Alta |
| Curva de aprendizado | Nenhuma | Baixa | Média (é Kubernetes) | Média |
| RAM mínima (overhead) | ~0 | ~50-100MB | ~450-500MB | ~200-300MB |
| Single node | Sim | Sim | Sim | Sim |
| Multi-node HA | Não | Sim (3+ managers) | Sim (etcd/SQLite) | Sim |
| Auto-healing | Não (restart policy) | Sim | Sim | Sim |
| Rolling updates nativos | Não | Sim | Sim | Sim |
| Service discovery | Não (DNS manual) | Sim (DNS built-in) | Sim (CoreDNS) | Sim (Consul) |
| Ecossistema/tooling | Docker nativo | Docker nativo | Kubernetes (CNCF) | HashiCorp |
| Licença | Apache 2.0 | Apache 2.0 | Apache 2.0 | BSL 1.1 |
| Manutenção | Docker Inc | Mirantis (até 2030) | SUSE/Rancher (CNCF) | HashiCorp |
| Ideal pra | 1 server, <10 containers | 1-5 servers, time pequeno | Quem quer/precisa K8s | Workloads heterogêneos |

**Recomendação default pro contexto do Patrick (equipe 3-5, clientes PME):**
- **Até 1 server, <15 containers**: Docker Compose + restart policies. Não complique.
- **1 server estressado ou precisa de zero-downtime deploys**: Docker Swarm. Setup mínimo, time já conhece Docker.
- **Multi-server ou precisa de ecossistema K8s (Helm charts, operators)**: K3s. Overhead de ~500MB vale pelo ecossistema.
- **Nomad**: Só se já usa stack HashiCorp (Vault, Consul). Pra time pequeno sem histórico, o ganho não justifica a licença BSL.

## Docker security hardening (NOVO v2)

Checklist que o Analyzer verifica e o Architect recomenda:

### Nível 1 — Essencial (toda VPS de produção)
- [ ] Containers NÃO rodam como root (USER no Dockerfile ou `user:` no compose)
- [ ] Resource limits definidos (memory + CPU) em TODOS os containers
- [ ] Docker socket NÃO exposto a containers (NUNCA `-v /var/run/docker.sock`)
- [ ] Imagens com tag específica, NUNCA `:latest`
- [ ] Health checks definidos em serviços críticos
- [ ] Restart policy: `unless-stopped` ou `always`
- [ ] Logging com `max-size` e `max-file` configurados

### Nível 2 — Recomendado (produção com dados sensíveis)
- [ ] `security_opt: [no-new-privileges:true]` em todos os containers
- [ ] Capabilities dropadas: `cap_drop: [ALL]` + `cap_add` só do necessário
- [ ] Read-only rootfs onde possível: `read_only: true` + tmpfs pra /tmp
- [ ] Vulnerability scanning com Trivy (≥ v0.69.3) no CI/CD ou periódico
- [ ] Imagens base slim/distroless quando possível

### Nível 3 — Avançado (compliance, multi-tenant com dados regulados)
- [ ] Docker rootless mode (limitação: sem cgroup limits, sem bind <1024)
- [ ] Image signing com Sigstore/Cosign (DCT está sendo descontinuado — deadline mai/2026 pra novos registries, remoção total mar/2028)
- [ ] SBOMs gerados com Syft em cada build
- [ ] Runtime intrusion detection com Falco (CNCF graduated, eBPF)
- [ ] User namespaces habilitados

## Zero Trust com Tailscale (NOVO v2)

Quando o servidor precisa de acesso remoto seguro:

**Por que Tailscale:**
- Mesh VPN sobre WireGuard — conexões diretas entre nodes, não hub-and-spoke
- NAT traversal automático (funciona atrás de qualquer firewall)
- ACLs baseadas em identidade (quem pode acessar o quê)
- SSO com qualquer OIDC provider
- Key rotation automática
- Free tier: até 100 devices, 3 users

**Padrão recomendado:**
1. Instalar Tailscale em cada VPS
2. Fechar porta SSH pública no firewall (só acesso via Tailscale)
3. Definir ACLs: dev acessa containers, admin acessa tudo
4. Usar Tailscale como DNS privado entre servers

**Quando NÃO usar:** Se o servidor é público por natureza (CDN, API pública) e não precisa de acesso administrativo remoto frequente. Tailscale é pra acesso ADMIN, não pra tráfego de usuário final.

## Monitoring stack recomendado (NOVO v2)

### Mínimo viável (toda VPS de produção)

**Uptime Kuma** — monitoring externo
- Container leve, UI simples
- HTTP(S), TCP, ping, DNS, Docker containers
- 95+ canais de notificação (Telegram, Slack, Discord, email)
- Monitora certificados TLS
- Setup: 1 container, <100MB RAM

**3 alertas iniciais que toda VPS precisa:**
1. **Disco > 80%** — aviso. > 90% — crítico
2. **Container down** — health check falhou ou container parou
3. **Certificado TLS** — expira em < 14 dias

### Stack completo (quando justifica)

**Prometheus + node_exporter + cAdvisor + Grafana**
- node_exporter: métricas do SO (CPU, RAM, disco, rede)
- cAdvisor: métricas por container
- Prometheus: coleta e armazena time series
- Grafana: dashboards e alertas
- Footprint: ~2-4GB RAM pra stack completo
- Justifica quando: >10 containers, múltiplos servers, precisa de histórico de métricas

**Falco** — runtime security (CNCF graduated)
- Detecta comportamento anômalo em containers via eBPF
- Regras pra: shell em container, acesso a arquivos sensíveis, network suspicious
- Versão atual: 0.42.0 (out/2025)
- Justifica quando: multi-tenant, dados regulados, ou pós-incidente

**Trivy** — vulnerability scanning
- Scanneia: containers, filesystems, repos, IaC
- Output: SBOM (CycloneDX, SPDX), SARIF, JUnit
- ATENÇÃO: supply chain incident em mar/2026. Usar versão ≥ 0.69.3
- Rodar: no CI/CD e periodicamente nos containers em produção

## n8n self-hosted — padrão de referência (NOVO v2)

```yaml
# docker-compose.yml — n8n production-ready
services:
  n8n:
    image: n8nio/n8n:1.x.x  # pin version SEMPRE
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
        reservations:
          memory: 1G
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=n8n
      - DB_POSTGRESDB_PASSWORD=${N8N_DB_PASSWORD}
      - EXECUTIONS_MODE=queue  # obrigatório pra escalar
      - QUEUE_BULL_REDIS_HOST=redis
      - N8N_SECURE_COOKIE=true
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
    volumes:
      - n8n_data:/home/node/.n8n
    networks:
      - n8n_net
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:5678/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3
    security_opt:
      - no-new-privileges:true

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 1G
    environment:
      - POSTGRES_DB=n8n
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=${N8N_DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - n8n_net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U n8n"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 256M
    command: redis-server --maxmemory 200mb --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
    networks:
      - n8n_net
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

networks:
  n8n_net:
    driver: bridge
    # overlay se Swarm

volumes:
  n8n_data:
  postgres_data:
  redis_data:
```

**Backup mínimo — pg_dump noturno:**
```bash
#!/bin/bash
# /opt/scripts/backup-n8n.sh — rodar via cron 0 3 * * *
BACKUP_DIR="/backups/n8n"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

# Dump do PostgreSQL
docker exec n8n-postgres pg_dump -U n8n n8n | gzip > "$BACKUP_DIR/n8n_${TIMESTAMP}.sql.gz"

# Manter últimos 7 dias
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +7 -delete

# Verificar tamanho (alerta se backup vazio)
SIZE=$(stat -f%z "$BACKUP_DIR/n8n_${TIMESTAMP}.sql.gz" 2>/dev/null || stat -c%s "$BACKUP_DIR/n8n_${TIMESTAMP}.sql.gz")
if [ "$SIZE" -lt 1000 ]; then
  echo "ALERTA: backup suspeitamente pequeno ($SIZE bytes)"
  # Enviar notificação aqui
fi
```

## O pipeline

```
Collector (references/collector-prompt.md)
    ↓ output: dados organizados por domínio (8 domínios)
Analyzer (references/analyzer-prompt.md)
    ↓ output: achados com severidade e evidência
Architect (references/architect-prompt.md)
    ↓ output: plano de ação priorizado com arquitetura proposta
Apresentar plano ao usuário
```

## Como executar

### Pré-requisito

O usuário precisa ter acesso SSH ao servidor via Claude Code. O pipeline roda comandos reais no servidor — não é análise teórica.

Se o usuário não tem SSH configurado no Claude Code, ajude a configurar antes de iniciar o pipeline.

### Passo 1 — Collector

Consulte `references/collector-prompt.md` pra o prompt completo e a lista de comandos por domínio.

O Collector faz:
1. Identifica o SO e versão pra adaptar comandos
2. Executa bateria de comandos diagnósticos organizados por domínio (8 domínios)
3. Coleta output bruto sem interpretar
4. Organiza os dados em blocos rotulados por domínio
5. Sinaliza comandos que falharam (permissão, pacote não instalado)

O output do Collector é um documento estruturado com os dados brutos de cada domínio.

Se estiver no Claude Code com subagents, dispatch como task com acesso SSH ao servidor.

### Passo 2 — Analyzer

Consulte `references/analyzer-prompt.md` pra o prompt completo e critérios de análise por domínio.

O Analyzer faz:
1. Recebe os dados do Collector
2. Analisa cada domínio contra critérios baseados em CIS Benchmarks Level 1 e boas práticas de produção
3. Aplica checklist de Docker security hardening (Nível 1 + 2) (NOVO v2)
4. Verifica presença de monitoring/observabilidade (NOVO v2)
5. Gera achados com: domínio, título, severidade, evidência, impacto
6. Cap de 25 achados (era 20), priorizados por severidade
7. Inclui contra-argumento pra cada achado

### Passo 3 — Architect

Consulte `references/architect-prompt.md` pra o prompt completo e padrões de arquitetura.

O Architect faz:
1. Recebe achados do Analyzer
2. Agrupa por tema
3. Usa a matriz de decisão de orquestração quando relevante (NOVO v2)
4. Propõe soluções concretas com comandos/configs prontos
5. Inclui recomendação de monitoring stack (NOVO v2)
6. Desenha arquitetura-alvo
7. Cria plano de ação em waves (Crítico / Importante / Estratégico)
8. Cada ação tem: o que fazer, por que, comando/config, risco de execução, tempo estimado

### No Claude.ai (sem subagents)

Se não tem acesso SSH direto:

1. **Collector manual:** Apresente a lista de comandos por domínio pro usuário executar. Receba os outputs colados na conversa.
2. **Analyzer:** Analise os dados coletados seguindo os critérios de `references/analyzer-prompt.md`.
3. **Architect:** Proponha soluções seguindo `references/architect-prompt.md`.

Limitação: sem acesso direto, alguns comandos podem ser esquecidos ou executados parcialmente. Compense pedindo confirmação ao usuário.

## Contrato de output

### Collector → Analyzer

Documento estruturado com blocos por domínio:
```
## [DOMÍNIO] SO e Kernel
### Comando: uname -a
[output bruto]

### Comando: cat /etc/os-release
[output bruto]

... (demais comandos do domínio, incluindo Domínio 8 - Monitoring)
```

### Analyzer → Architect

Lista de achados:
```
finding_id: INFRA-001
domain: Docker
title: Containers sem resource limits — risco de um container consumir toda a RAM
severity: high
evidence: "docker stats mostra container n8n-worker usando 3.2GB sem limit definido"
impact: "Se o worker processar batch grande, pode causar OOM e derrubar outros containers"
counter_argument: "Se o servidor tem RAM de sobra e pouco tráfego, risco é baixo no curto prazo"
security_hardening_level: 1  # (NOVO v2) Nível do checklist de hardening que falhou
```

### Architect → Usuário

Plano de ação em waves com arquitetura proposta:
```
## Wave 1 — Crítico (aplicar agora)

### INFRA-001: Definir resource limits em todos os containers
- Por que: sem limits, qualquer container pode causar OOM e derrubar o servidor inteiro
- Como: adicionar deploy.resources.limits no docker-compose.yml
- Config:
  services:
    n8n-worker:
      deploy:
        resources:
          limits:
            cpus: '1.0'
            memory: 2G
- Risco: se o limit for muito baixo, o container pode ser killed. Monitore por 24h após aplicar.
- Tempo: 15min por serviço

## Recomendação de orquestração (NOVO v2)
[Matriz preenchida com dados reais do servidor + recomendação contextual]

## Recomendação de monitoring (NOVO v2)
[Stack mínimo ou completo conforme contexto]
```

## Severidades

| Severidade | Critério | Exemplo |
|---|---|---|
| **critical** | Risco real e imediato de downtime, perda de dados, ou acesso não autorizado | Disco 95% cheio, SSH como root sem key |
| **high** | Problema que vai causar incidente se não corrigido em dias/semanas | Containers sem resource limits, sem backup |
| **medium** | Subótimo mas não urgente, impacta performance ou manutenibilidade | Imagens desatualizadas, logs sem rotação |
| **low** | Melhoria recomendada, boas práticas não seguidas | Swap desativado, parâmetros sysctl default |
| **info** | Observação sem risco direto, contexto pra decisões futuras | Versão do Docker, arquitetura atual |

## Red flags

- Nunca pule o Collector. Análise sem dados reais é achismo.
- Nunca execute comandos destrutivos (rm, format, drop) durante a coleta. O Collector é read-only.
- Nunca recomende mudanças sem avaliar impacto em serviços rodando. "Reinicia o Docker" pode derrubar 15 containers de clientes.
- Se o servidor roda serviços de múltiplos clientes, TODA recomendação deve considerar isolamento.
- (NOVO v2) Docker rootless mode tem limitações reais: sem cgroup limits, sem bind <1024, sem overlay networks. Não recomende cegamente.
- (NOVO v2) Trivy teve supply chain incident em mar/2026. SEMPRE verifique versão ≥ 0.69.3.
- (NOVO v2) DCT (Docker Content Trust) está sendo descontinuado. Recomende Sigstore/Cosign como substituto.

## Integração com outras skills

- **Security Audit:** VPS Infra Audit cobre infra (SO, Docker, rede, storage). Security Audit cobre aplicação (código, RLS, autenticação, OWASP). Se o audit de infra encontrar problemas de segurança de aplicação, sugira rodar Security Audit.
- **n8n Architect:** Se o audit encontrar problemas na arquitetura n8n (single instance, sem workers separados), sugira a skill n8n Architect pra redesenhar o setup.
- **Supabase DB Architect:** Se o servidor roda Supabase self-hosted, achados relacionados a banco devem ser passados pra essa skill.
- **Tech Lead & PM:** Findings de severidade high/critical podem virar tasks no ClickUp. Sugira criar tasks pra equipe executar as waves.

## Quando NÃO usar esta skill

- Se o problema é de código/aplicação (bugs, lógica, UI) → use repo-review ou ux-audit
- Se é sobre segurança de aplicação (OWASP, RLS, secrets) → use security-audit
- Se é sobre schema de banco sem contexto de infra → use supabase-db-architect
- Se é uma pergunta pontual sobre Docker/Linux → responda direto sem acionar o pipeline
- Se o usuário não tem acesso SSH e não pode colar outputs → não tem como coletar dados, a skill não funciona
