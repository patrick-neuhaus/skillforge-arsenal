# Docker Security Hardening — Checklist por nível

Referência completa dos 3 níveis de hardening Docker. O Analyzer verifica e o Architect recomenda.

## Nível 1 — Essencial (toda VPS de produção)

- [ ] Containers NÃO rodam como root (USER no Dockerfile ou `user:` no compose)
- [ ] Resource limits definidos (memory + CPU) em TODOS os containers
- [ ] Docker socket NÃO exposto a containers (NUNCA `-v /var/run/docker.sock`)
- [ ] Imagens com tag específica, NUNCA `:latest`
- [ ] Health checks definidos em serviços críticos
- [ ] Restart policy: `unless-stopped` ou `always`
- [ ] Logging com `max-size` e `max-file` configurados

## Nível 2 — Recomendado (produção com dados sensíveis)

- [ ] `security_opt: [no-new-privileges:true]` em todos os containers
- [ ] Capabilities dropadas: `cap_drop: [ALL]` + `cap_add` só do necessário
- [ ] Read-only rootfs onde possível: `read_only: true` + tmpfs pra /tmp
- [ ] Vulnerability scanning com Trivy (>= v0.69.3) no CI/CD ou periódico
- [ ] Imagens base slim/distroless quando possível

## Nível 3 — Avançado (compliance, multi-tenant com dados regulados)

- [ ] Docker rootless mode (limitação: sem cgroup limits, sem bind <1024)
- [ ] Image signing com Sigstore/Cosign (DCT sendo descontinuado — deadline mai/2026 pra novos registries, remoção total mar/2028)
- [ ] SBOMs gerados com Syft em cada build
- [ ] Runtime intrusion detection com Falco (CNCF graduated, eBPF)
- [ ] User namespaces habilitados

## Compose de referência com hardening completo

```yaml
services:
  app:
    image: app:1.2.3  # tag específica, nunca :latest
    restart: unless-stopped
    user: "1000:1000"  # non-root
    read_only: true  # read-only rootfs
    tmpfs:
      - /tmp  # tmpfs pra diretórios que precisam de escrita
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE  # só se precisar bind <1024
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 2G
        reservations:
          cpus: '0.25'
          memory: 512M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      - app_net  # rede isolada, não a default bridge
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Limitações do rootless mode

Antes de recomendar Docker rootless, considere:

- **Sem cgroup limits**: `deploy.resources.limits` não funciona
- **Sem bind < 1024**: portas 80/443 requerem workaround (socat, iptables redirect)
- **Sem overlay networks**: Docker Swarm não funciona em rootless
- **Sem systemd integration nativa**: precisa de `loginctl enable-linger`
- **Performance de storage**: slirp4netns é mais lento que native networking

## Alertas de supply chain

- **Trivy**: supply chain incident em mar/2026. SEMPRE usar versão >= 0.69.3
- **DCT (Docker Content Trust)**: sendo descontinuado. Usar Sigstore/Cosign como substituto
- **Falco**: versão estável 0.42.0 (out/2025), usa eBPF. CNCF graduated project
