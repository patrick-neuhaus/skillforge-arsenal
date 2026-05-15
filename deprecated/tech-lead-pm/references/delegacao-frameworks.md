# Delegacao — Frameworks e Guias

Referencia detalhada para delegacao efetiva com equipe junior.

## Framework de 5 Componentes

| Componente | Descricao | Exemplo |
|------------|-----------|---------|
| **O QUE** | O que precisa ser feito | "Criar endpoint de webhook pra leads" |
| **POR QUE** | Contexto de negocio | "O cliente precisa receber leads em tempo real" |
| **COMO** | Nivel de detalhe por senioridade | Passo a passo (Jonas) / Resultado + restricoes (Hygor) |
| **QUANDO** | Prazo claro | "Ate quarta 18h" (nunca "quando puder") |
| **VERIFICACAO** | Como saber que ficou bom | Criterios de aceitacao especificos |

## Calibracao por Pessoa

| Aspecto | Jonas (estagiario) | Hygor (junior) | Senior (futuro) |
|---------|-------------------|----------------|-----------------|
| Detalhamento | Passo a passo | Resultado + restricoes | So o objetivo |
| Check-ins | Diario | A cada 2-3 dias | Semanal |
| Autonomia | Baixa — confirma antes | Media — decide coisas pequenas | Alta — so alinha estrategia |
| Feedback | Imediato e frequente | Regular | Quando necessario |

## Decision Zones — Green/Yellow/Red

Framework pra deixar claro QUAIS decisoes cada pessoa pode tomar sem consultar:

### Zonas

- **Green (decide sozinho):** Escolha de lib auxiliar, nome de variavel, ordem de implementacao, formatacao de codigo
- **Yellow (decide + avisa):** Mudar abordagem tecnica, adicionar dependencia, alterar schema de tabela existente
- **Red (escala pra voce):** Decisao de arquitetura, mudar stack, alterar fluxo de auth, qualquer coisa que impacta outros projetos

### Calibracao

- **Jonas:** mais coisas sao Red/Yellow. Conforme cresce, mova itens pra Green.
- **Hygor:** mais coisas sao Green/Yellow. Red so pra decisoes de arquitetura.

**Importante:** comunique as zonas PRO ATIVO no primeiro dia. Reduz ~70% das interrupcoes.

## Delegacao Async — WHO/WHAT/BY-WHEN

Pra delegacao rapida via ClickUp ou WhatsApp, formato minimo:

```
WHO: Hygor
WHAT: Implementar webhook de lead com error handling camada 2
BY-WHEN: Quarta 18h
```

Se precisa de mais contexto que isso, e task de ClickUp, nao mensagem.

## Decisoes de Arquitetura

Certas decisoes NAO ficam pro junior decidir. Voce define antes:
- Webhook direto no n8n vs Edge Function + Fila
- Error handling: qual camada usar
- Subworkflow sincrono vs assincrono
- Onde salvar dados (REST API vs Postgres direto)

## Armadilhas Comuns

| Armadilha | Realidade | O que fazer |
|-----------|-----------|-------------|
| "Mais rapido eu fazer" | Sim, HOJE. Mas toda vez que faz em vez de ensinar, compra velocidade agora e vende escala depois. | Delegar + investir 15min ensinando |
| "Ele nao vai fazer do jeito que eu faria" | Correto. 80% bem feito por outra pessoa libera 100% do seu tempo pra coisa mais importante. | Aceitar 80%, dar feedback no delta |
| "Nao quero microgerenciar" | Acompanhar NAO e microgerenciar. Microgerenciar = dizer COMO. Acompanhar = perguntar COMO ESTA. | Pergunte sobre resultado, nao processo |
| "Preciso revisar tudo" | Se revisa 100%, nao delegou — criou mais trabalho pra si. | Revise por amostragem, nao 100% |
