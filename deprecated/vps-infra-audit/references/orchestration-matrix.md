# Matriz de Decisão de Orquestração

Quando o Architect recomendar orquestração, use esta matriz com dados reais do servidor.

## Comparativo

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

## Recomendação default pro contexto (equipe 3-5, clientes PME)

- **Até 1 server, <15 containers**: Docker Compose + restart policies. Não complique.
- **1 server estressado ou precisa de zero-downtime deploys**: Docker Swarm. Setup mínimo, time já conhece Docker.
- **Multi-server ou precisa de ecossistema K8s (Helm charts, operators)**: K3s. Overhead de ~500MB vale pelo ecossistema.
- **Nomad**: Só se já usa stack HashiCorp (Vault, Consul). Pra time pequeno sem histórico, o ganho não justifica a licença BSL.

## Docker Swarm mínimo pra HA

```
Topologia mínima:
- 3 managers (quorum Raft, tolera 1 falha)
- N workers (conforme carga)

Se só tem 1 servidor hoje:
- Manager + Worker no mesmo node (ok pra início)
- Segundo node: adicionar como manager
- Terceiro node: adicionar como manager
- Redistribuir serviços com placement constraints
```

## Isolamento multi-tenant com Docker networks

```yaml
# Cada cliente tem sua própria rede
networks:
  cliente_a_net:
    driver: overlay
    internal: true  # sem acesso externo direto
  cliente_b_net:
    driver: overlay
    internal: true
  proxy_net:
    driver: overlay  # o reverse proxy conecta nas redes dos clientes

# Reverse proxy (traefik/nginx) é o único que faz bridge entre redes
services:
  proxy:
    networks:
      - proxy_net
      - cliente_a_net
      - cliente_b_net

  cliente_a_app:
    networks:
      - cliente_a_net  # só vê containers na sua rede

  cliente_b_app:
    networks:
      - cliente_b_net  # isolado do cliente A
```

## Template de recomendação

Preencher com dados reais do servidor:

```
## Recomendação de orquestração

### Contexto do servidor
- Containers rodando: [N]
- RAM total: [X]GB
- RAM disponível: [Y]GB
- Necessidade de HA: [Sim/Não/Desejável]
- Múltiplos servers: [Sim/Não/Planejado]

### Recomendação
[Docker Compose / Swarm / K3s] — porque [justificativa baseada nos dados]

### Se migrar:
1. [Passo 1]
2. [Passo 2]
...
```
