# n8n Self-Hosted — Padrões de referência

## Docker Compose production-ready com queue mode

```yaml
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

## n8n escalável com Docker Swarm

```yaml
# Padrão: 1 editor + 1 webhook + N workers
services:
  n8n-editor:
    image: n8nio/n8n:1.x.x
    deploy:
      replicas: 1  # editor é stateful, 1 replica
      placement:
        constraints: [node.role == manager]
    environment:
      - EXECUTIONS_MODE=queue
      - QUEUE_BULL_REDIS_HOST=redis

  n8n-webhook:
    image: n8nio/n8n:1.x.x
    deploy:
      replicas: 2  # pode ter mais de 1 pra HA
    environment:
      - EXECUTIONS_MODE=queue
      - QUEUE_BULL_REDIS_HOST=redis
    command: webhook

  n8n-worker:
    image: n8nio/n8n:1.x.x
    deploy:
      replicas: 4  # escale conforme demanda
      resources:
        limits:
          cpus: '1.0'
          memory: 2G
    environment:
      - EXECUTIONS_MODE=queue
      - QUEUE_BULL_REDIS_HOST=redis
    command: worker

  redis:
    image: redis:7-alpine
    deploy:
      replicas: 1
    volumes:
      - redis_data:/data
```

## Backup mínimo — pg_dump noturno

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
