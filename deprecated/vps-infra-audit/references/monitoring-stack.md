# Monitoring Stack — Referência de observabilidade

## Mínimo viável (toda VPS de produção)

### Uptime Kuma — monitoring externo

- Container leve, UI simples
- HTTP(S), TCP, ping, DNS, Docker containers
- 95+ canais de notificação (Telegram, Slack, Discord, email)
- Monitora certificados TLS
- Setup: 1 container, <100MB RAM

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 256M
    volumes:
      - uptime_data:/app/data
    ports:
      - "3001:3001"
    security_opt:
      - no-new-privileges:true
```

### 3 alertas iniciais que toda VPS precisa

1. **Disco > 80%** — aviso. > 90% — crítico
2. **Container down** — health check falhou ou container parou
3. **Certificado TLS** — expira em < 14 dias

## Stack completo (quando justifica)

### Prometheus + node_exporter + cAdvisor + Grafana

- **node_exporter**: métricas do SO (CPU, RAM, disco, rede)
- **cAdvisor**: métricas por container
- **Prometheus**: coleta e armazena time series
- **Grafana**: dashboards e alertas
- **Footprint**: ~2-4GB RAM pra stack completo
- **Justifica quando**: >10 containers, múltiplos servers, precisa de histórico de métricas

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 1G
    volumes:
      - prometheus_data:/prometheus
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alert.rules.yml:/etc/prometheus/alert.rules.yml
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 512M
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}

  node-exporter:
    image: prom/node-exporter:latest
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 128M
    pid: host
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
    networks:
      - monitoring

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 256M
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    networks:
      - monitoring

networks:
  monitoring:
    driver: bridge
```

## Ferramentas complementares

### Falco — runtime security (CNCF graduated)

- Detecta comportamento anômalo em containers via eBPF
- Regras pra: shell em container, acesso a arquivos sensíveis, network suspicious
- Versão atual: 0.42.0 (out/2025)
- Justifica quando: multi-tenant, dados regulados, ou pós-incidente

### Trivy — vulnerability scanning

- Scanneia: containers, filesystems, repos, IaC
- Output: SBOM (CycloneDX, SPDX), SARIF, JUnit
- ATENÇÃO: supply chain incident em mar/2026. Usar versão >= 0.69.3
- Rodar: no CI/CD e periodicamente nos containers em produção
