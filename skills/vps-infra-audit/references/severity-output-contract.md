# Severidades e Contratos de Output

## Severidades

| Severidade | Critério | Exemplo |
|---|---|---|
| **critical** | Risco real e imediato de downtime, perda de dados, ou acesso não autorizado | Disco 95% cheio, SSH como root sem key |
| **high** | Problema que vai causar incidente se não corrigido em dias/semanas | Containers sem resource limits, sem backup |
| **medium** | Subótimo mas não urgente, impacta performance ou manutenibilidade | Imagens desatualizadas, logs sem rotação |
| **low** | Melhoria recomendada, boas práticas não seguidas | Swap desativado, parâmetros sysctl default |
| **info** | Observação sem risco direto, contexto pra decisões futuras | Versão do Docker, arquitetura atual |

## Contrato: Collector -> Analyzer

Documento estruturado com blocos por domínio:

```
## [DOMINIO] SO e Kernel
### Comando: uname -a
[output bruto]

### Comando: cat /etc/os-release
[output bruto]

... (demais comandos do domínio, incluindo Domínio 8 - Monitoring)
```

## Contrato: Analyzer -> Architect

Lista de achados:

```
finding_id: INFRA-001
domain: Docker
title: Containers sem resource limits — risco de um container consumir toda a RAM
severity: high
evidence: "docker stats mostra container n8n-worker usando 3.2GB sem limit definido"
impact: "Se o worker processar batch grande, pode causar OOM e derrubar outros containers"
counter_argument: "Se o servidor tem RAM de sobra e pouco tráfego, risco é baixo no curto prazo"
security_hardening_level: 1  # Nível do checklist de hardening que falhou
```

## Contrato: Architect -> Usuário

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

## Recomendação de orquestração
[Matriz preenchida com dados reais do servidor + recomendação contextual]

## Recomendação de monitoring
[Stack mínimo ou completo conforme contexto]
```
