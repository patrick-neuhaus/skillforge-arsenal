# PRD Template — AI-First

Use este template ao gerar o PRD na Step 3 (Gerar PRD).

---

## Template Principal

```markdown
# [Nome do Projeto]

## Resumo
[1 frase: o que é, pra quem, qual problema resolve]

## Declaração do problema
Nós observamos que [estado atual] faz com que [pessoas] sofram com [problema], o que causa [consequência].

## Hipótese
Nós acreditamos que [fazendo X] para [pessoa Y] vamos [resultado Z]. Saberemos que é verdade quando [métrica/evidência].

## North Star Metric
[Métrica única que define sucesso. Ex: "Documentos SST processados sem erro por semana"]

## Stack técnica
- Frontend: [ex: Lovable (React + Tailwind + shadcn/ui)]
- Backend: [ex: Supabase (PostgreSQL + Auth + Edge Functions)]
- Integrações: [ex: Evolution API, n8n, Kommo]

## Usuários
[Quem usa, roles, volume esperado]
[Personas se houver: nome + papel + problema + o que faz]

## Fluxos principais

### Fluxo 1: [Nome] [Wave N]

**Trigger:** [O que inicia este fluxo]
**Resultado:** [O que acontece no final]

1. [Passo 1] → Estado: [loading/success/error]
2. [Passo 2] → Estado: [...]
3. [Passo 3] → Estado: [...]

**Comportamentos explícitos:**
- Quando [condição X]: faça [ação Y]
- Quando [erro Z]: mostre [mensagem W]
- Quando [lista vazia]: mostre [empty state com texto e CTA]

**Input/Output de exemplo:**
\```json
{
  "input": { "campo1": "valor", "campo2": 123 },
  "output": { "status": "success", "resultado": "..." }
}
\```

### Fluxo 2: [Nome] [Wave N]
...

## User Stories / Job Stories
[Apenas pros fluxos principais do MVP]

User Story: "Como [persona], eu quero [ação] para que [benefício]"
Job Story: "Quando [situação], eu quero [motivação] para que [resultado]"

Critérios INVEST por story.

## Regras de negócio
- [Regra 1]: [descrição clara e sem ambiguidade]
- [Regra 2]: ...

## Modelo de dados (se aplicável)
[Tabelas, campos essenciais, relacionamentos. Incluir tipos.]

## Telas / Páginas (se app web) [Wave N]

### [Nome da tela]
- **Objetivo:** [o que o usuário faz aqui]
- **Estados:** empty | loading | filled | error | success
- **Elementos:** [componentes, campos, botões]
- **Ações:** [o que o usuário pode fazer + resultado de cada ação]
- **Regras:** [comportamentos condicionais]

## Integrações externas
- [Sistema]: [o que entra, o que sai, quando dispara, formato]

## NÃO construa (fora do escopo MVP)
[Lista explícita e específica do que NÃO entra]
- NÃO: [feature X] — motivo
- NÃO: [feature Y] — motivo
- NÃO: [otimização Z] — motivo

## Notas para implementação
[Decisões técnicas, padrões, preferências, ordem sugerida de build]
- Sequência recomendada: schema → auth → fluxo principal → UI → error handling
- [Decisão de webhook: direto vs Edge Function + Fila]
- [Libs específicas, padrões de naming, etc]
```

---

## Regras do Output AI-First

1. **Descrição em 1 frase.** O resumo do projeto deve caber em 1 frase. Se precisa de mais, o escopo tá grande demais.
2. **User flows numerados.** Cada passo do fluxo com número, estado, e resultado esperado.
3. **Comportamentos explícitos.** "Quando X, faça Y" pra CADA interação não-trivial. AI coding tools executam literalmente — se não especificou, vai chutar.
4. **Estados obrigatórios.** Toda tela/componente deve definir: empty, loading, filled, error, success. AI que não sabe o empty state inventa algo feio.
5. **Input/Output de exemplo.** Pra fluxos com dados complexos (OCR, integrações, formulários), inclua JSON de exemplo. Modelos performam dramaticamente melhor com exemplos concretos.
6. **Lista de exclusões.** "NÃO construa" é TÃO importante quanto "construa". Sem isso, AI tools adicionam features não solicitadas.
7. **Modelo de dados com tipos.** Se incluir, use tipos explícitos (`UUID`, `TIMESTAMPTZ`, `TEXT`, `JSONB`), não descrições vagas.
8. **Português brasileiro** exceto termos técnicos universais.
9. **Dois arquivos sempre.** PRD MVP e Roadmap pós-MVP são SEPARADOS.
10. **Sequência de build.** Na seção "Notas para implementação", sugira a ordem: schema → auth → fluxo principal → UI → error handling. AI tools constroem melhor com phasing explícito.

---

## Variações por Tipo de Projeto

### Para apps web (Lovable)
- Foco em telas, fluxos visuais, componentes com estados
- "Telas / Páginas" detalhada com empty/loading/error states
- Responsividade explícita
- Referência visual quando houver

### Para automações (n8n)
- Foco em triggers, condições, outputs
- "Workflows" no lugar de "Telas"
- Job Stories > User Stories
- Decisão de webhook obrigatória: direto vs Edge Function + Fila

### Para projetos mistos
- Separe frontend, backend, automação
- Especifique QUEM chama QUEM
- Onde cada parte vive (Lovable, Supabase, n8n)
