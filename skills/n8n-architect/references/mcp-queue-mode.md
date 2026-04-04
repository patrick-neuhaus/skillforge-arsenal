# MCP e Queue Mode

Última atualização: 2026-04-03

Detalhes de MCP (Model Context Protocol) e Queue Mode para escalabilidade.

---

## MCP (Model Context Protocol)

O n8n suporta MCP em 3 dimensões:

### MCP Client Tool (n8n como consumidor)

Permite que AI Agents do n8n chamem tools de MCP servers externos:
- Conecta a qualquer servidor MCP-compliant
- Agent descobre e executa tools automaticamente
- Use quando: seu agente precisa acessar ferramentas de sistemas que expõem MCP (Supabase MCP Server, ferramentas customizadas)

### MCP Server Trigger (n8n como provedor)

Transforma workflows do n8n em tools MCP consumíveis por AI coding tools:
- Expõe URL pra clientes MCP se conectarem
- Suporta SSE e Streamable HTTP
- Use quando: quer que Lovable, Cursor, ou Claude Code chamem workflows do n8n

### Instance-level MCP (Beta)

Configuração centralizada em Settings > Instance-level MCP:
- Uma conexão por instância servindo todos os workflows habilitados
- Autenticação via OAuth redirect ou Personal MCP Access Token
- Habilitar MCP no nível da instância, depois por workflow individual
- Connectors nativos disponíveis: Lovable, Mistral AI (mais vindo)

**Atenção:** não tem scoping por client — todos os clientes MCP conectados veem todos os workflows habilitados. Controle qual workflow habilitar.

---

## Queue Mode e Escalabilidade

### Benchmarks de Performance

| Setup | RPS | Latência | Nota |
|-------|-----|----------|------|
| Single instance (baseline) | 23 | - | Baseline |
| Queue mode habilitado | 72 | <3s | 3x melhoria |
| Queue mode + hardware maior (16 vCPUs, 32GB) | 162 | <1.2s | 7x melhoria |

### Arquitetura de Scaling

```
[Main Instance] → [Redis Queue] → [Worker 1]
                                → [Worker 2]
                                → [Worker N]
        ↓
[Webhook Processor] (opcional, pra alto volume de requests)
```

- Main instance recebe triggers/webhooks e coloca na fila Redis
- Workers puxam execuções da fila e processam
- Webhook Processors adicionam paralelismo no recebimento

### Considerações

- Queue mode dobra uso de RAM mesmo idle — só é custo-efetivo em 100+ RPS
- Workers são processos Node.js separados com alto IOPS
- Escale horizontalmente adicionando workers
