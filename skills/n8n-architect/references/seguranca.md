# Segurança em Workflows n8n

Última atualização: 2026-04-03

Checklist e padrões de segurança pra workflows de produção.

---

## Checklist de Segurança

1. **Credentials:** nunca hardcode tokens/senhas nos nodes. Use Credentials do n8n ou External Secrets.
2. **Webhook auth:** webhooks públicos devem validar origem (header signature, token no query param, IP whitelist).
3. **Code nodes:** não acessam variáveis de ambiente por default no 2.0. Se precisar, configure explicitamente.
4. **service_role key:** se o workflow usa service_role do Supabase, NUNCA exponha em webhook responses ou logs.
5. **Execution Data:** não salve dados sensíveis — fica visível pra todos os usuários do n8n.
6. **Data Tables:** dados são acessíveis por qualquer workflow no projeto — não armazene secrets.
7. **MCP:** todos os clientes MCP conectados veem todos os workflows habilitados — controle quais workflows habilitar.

---

## Python em Code Nodes

n8n 2.0 suporta Python nativo nos Code nodes:
- Cloud: sem imports de bibliotecas (apenas built-ins)
- Self-hosted: imports via imagem customizada do runner
- Python tem overhead de compilação maior que JavaScript
- Variáveis: `_items` (all-items mode), `_item` (per-item mode)
- Use quando a lógica é significativamente mais simples em Python que JS
