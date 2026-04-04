# Zero Trust com Tailscale — Referência

## Por que Tailscale

- Mesh VPN sobre WireGuard — conexões diretas entre nodes, não hub-and-spoke
- NAT traversal automático (funciona atrás de qualquer firewall)
- ACLs baseadas em identidade (quem pode acessar o quê)
- SSO com qualquer OIDC provider
- Key rotation automática
- Free tier: até 100 devices, 3 users

## Padrão recomendado

1. Instalar Tailscale em cada VPS
2. Fechar porta SSH pública no firewall (só acesso via Tailscale)
3. Definir ACLs: dev acessa containers, admin acessa tudo
4. Usar Tailscale como DNS privado entre servers

## Setup

```bash
# Instalação em cada VPS
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --ssh  # habilita SSH via Tailscale

# Fechar SSH público (após confirmar acesso via Tailscale!)
ufw deny 22/tcp  # ou porta SSH customizada
# Manter SSH acessível APENAS via Tailscale IP

# ACL exemplo (tailscale admin console)
# {
#   "acls": [
#     {"action": "accept", "src": ["group:admin"], "dst": ["*:*"]},
#     {"action": "accept", "src": ["group:dev"], "dst": ["tag:server:80,443,5678"]}
#   ]
# }
```

## Quando NAO usar

Se o servidor é público por natureza (CDN, API pública) e não precisa de acesso administrativo remoto frequente. Tailscale é pra acesso ADMIN, não pra tráfego de usuário final.
