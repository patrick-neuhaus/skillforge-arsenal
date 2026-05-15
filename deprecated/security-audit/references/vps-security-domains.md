# Domínios de segurança — Modo VPS

Checklist completo para auditoria de segurança de servidor via SSH. Complementa o vps-infra-audit com foco exclusivo em segurança.

## 1. Hardening do SO

- Patches de segurança aplicados (`apt list --upgradable`, `yum check-update`)
- Serviços desnecessários desativados
- Kernel params de segurança (sysctl):
  - `net.ipv4.conf.all.rp_filter = 1`
  - `net.ipv4.conf.all.accept_redirects = 0`
  - `net.ipv4.conf.all.send_redirects = 0`
  - `net.ipv4.icmp_echo_ignore_broadcasts = 1`
  - `kernel.randomize_va_space = 2`
- SELinux/AppArmor ativo

### Comandos de verificação

```bash
# SELinux/AppArmor
getenforce 2>/dev/null || aa-status 2>/dev/null

# Kernel params
sysctl net.ipv4.conf.all.rp_filter net.ipv4.conf.all.accept_redirects \
  net.ipv4.conf.all.send_redirects net.ipv4.icmp_echo_ignore_broadcasts \
  kernel.randomize_va_space 2>/dev/null

# Serviços rodando (excluir essenciais)
systemctl list-units --type=service --state=running \
  | grep -vE "systemd|dbus|ssh|cron|docker|network"

# Patches pendentes
apt list --upgradable 2>/dev/null || yum check-update 2>/dev/null
```

## 2. Acesso e autenticação

- SSH: key-only, root desabilitado, porta não-padrão (opcional)
- Usuarios com privilégios mínimos
- Fail2ban ativo e configurado
- Sudo: quem tem e por quê

### Comandos de verificação

```bash
# SSH config
cat /etc/ssh/sshd_config | grep -E "PermitRootLogin|PasswordAuthentication|Port|AllowUsers|AllowGroups|PubkeyAuthentication"

# Usuarios com sudo
grep -E "sudo|wheel" /etc/group

# Chaves SSH
ls -la /root/.ssh/ /home/*/.ssh/ 2>/dev/null

# Fail2ban
fail2ban-client status 2>/dev/null
```

## 3. Rede e firewall

- Firewall ativo com whitelist
- Portas expostas = mínimo necessário
- SSL/TLS válido e atualizado
- Rate limiting no reverse proxy

### Comandos de verificação

```bash
# Portas abertas
ss -tlnp

# Firewall
ufw status verbose 2>/dev/null || iptables -L -n 2>/dev/null

# Certificado SSL
openssl s_client -connect localhost:443 </dev/null 2>/dev/null \
  | openssl x509 -noout -dates 2>/dev/null
```

## 4. Containers (Docker/Podman)

- Docker socket NÃO exposto a containers (= dar root pro container)
- Containers rodando como non-root
- Imagens de sources confiáveis (Docker Hub oficial, ghcr.io)
- Sem privileged mode
- Volumes não montam paths sensíveis (/etc, /root)

### Comandos de verificação

```bash
# Docker socket exposto
docker inspect $(docker ps -q) \
  --format '{{.Name}}: {{range .Mounts}}{{.Source}}→{{.Destination}} {{end}}' \
  2>/dev/null | grep docker.sock

# Containers privilegiados
docker inspect $(docker ps -q) \
  --format '{{.Name}}: Privileged={{.HostConfig.Privileged}} User={{.Config.User}}' \
  2>/dev/null

# Env vars com secrets em containers
for c in $(docker ps -q 2>/dev/null); do
  echo "=== $(docker inspect --format '{{.Name}}' $c) ==="
  docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' $c 2>/dev/null \
    | grep -iE "key|secret|password|token"
done
```

## 5. Secrets e credenciais

- Secrets em environment variables ou secret manager, não em arquivos
- .env fora do git (verificar .gitignore)
- Chaves de API com escopo mínimo
- Nenhum .env acessível publicamente (não no document root do web server)

### Comandos de verificação

```bash
# .env files no filesystem
find / -name ".env" -not -path "*/node_modules/*" 2>/dev/null | head -20

# Permissões de .env files
find / -name ".env" -not -path "*/node_modules/*" -exec ls -la {} \; 2>/dev/null

# Secrets em docker compose files
grep -rn -iE "password|secret|key|token" /opt/*/docker-compose* 2>/dev/null
```

## Severidades específicas VPS

| Achado | Severidade |
|--------|-----------|
| Docker socket exposto a container | critical |
| SSH com PasswordAuthentication yes | high |
| Root login habilitado via SSH | high |
| Container em privileged mode | critical |
| Firewall desativado | high |
| Secrets em arquivo sem permissão restrita | high |
| Sem fail2ban | medium |
| Certificado SSL expirado | high |
| Kernel params inseguros | medium |
| Serviço desnecessário rodando | low |
