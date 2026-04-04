# Delegação de Workflows

Última atualização: 2026-04-03

Quando o usuário quiser delegar um workflow pra Hygor ou Jonas, gere um briefing técnico que a pessoa consiga seguir.

---

## Template de Briefing Técnico

```markdown
# Briefing: [Nome do Workflow]

## O que esse workflow faz
[2-3 frases explicando o resultado final, não a implementação]

## Trigger
- Tipo: [webhook / cron / chat trigger / evento]
- Quando dispara: [descrição humana]

## Fluxo (passo a passo)
1. [Recebe X] → Node: [tipo de node]
2. [Valida Y] → Node: [tipo de node]
3. [Processa Z] → Node: [tipo de node]
...

## Configurações importantes
- [Node X]: usar HTTP Request, não Code node
- [Node Y]: endpoint = [URL], método = [GET/POST], headers = [quais]
- [Autenticação]: usar credential [nome] que já existe no n8n

## Variáveis / Secrets
- [VAR_1]: onde encontrar, o que é
- [VAR_2]: onde encontrar, o que é

## Error handling obrigatório
- Se [X] falhar: [o que fazer]
- Log em: [tabela/local]

## Critérios de aceitação
- [ ] Workflow funciona como Draft (teste manual)
- [ ] Workflow publicado e funcionando em produção
- [ ] Erros são logados em [tabela]
- [ ] Nodes estão renomeados com padrão [Ação] [Alvo]
- [ ] Sticky notes explicando branches complexos

## Dúvidas?
Pergunte ANTES de começar. Melhor perguntar do que refazer.
```

---

## Calibração por Pessoa

### Jonas (estagiário)
- Screenshots do n8n mostrando onde clicar
- Especifique CADA campo do HTTP Request
- Não assuma que ele sabe o que é bearer token
- Inclua links pra documentação das APIs
- Passo a passo com prints se possível

### Hygor (junior)
- Descreva o resultado e restrições
- Ele sabe montar HTTP Request
- Foque nas regras de negócio e edge cases
- Pode dar mais autonomia na implementação
