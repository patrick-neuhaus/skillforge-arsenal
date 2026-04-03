# Discovery Guide — Entender o Que a Skill Deve Fazer

Consulte este arquivo no **Step 1** do workflow. O objetivo é extrair do usuário tudo que ele sabe sobre o domínio e o processo que quer capturar.

---

## Antes de perguntar: detecte o que já existe

- **Conversa em andamento** — Se o usuário disse "transforma isso numa skill" durante uma conversa, EXTRAIA do histórico: ferramentas usadas, sequência de passos, correções feitas, formato de input/output. Apresente o que extraiu e peça confirmação.
- **Skill existente** — Se é melhoria (`--evolve`), leia a skill INTEIRA primeiro (SKILL.md + references + scripts). Identifique o que funciona e o que não funciona antes de perguntar.
- **Nada** — Se é skill do zero, siga o fluxo de perguntas abaixo.

---

## Bloco 1 — O problema (não a solução)

O usuário vai chegar falando da SOLUÇÃO ("quero uma skill que faz X"). Cave até o PROBLEMA.

- O que essa skill deve fazer? (deixe falar livremente)
- Qual problema isso resolve? O que acontece HOJE sem essa skill?
- Com que frequência esse problema aparece? (diário, semanal, por projeto?)
- Quem vai acionar essa skill? (o próprio usuário, equipe, qualquer pessoa?)

## Bloco 2 — Input e output

- Qual o input típico? (texto, arquivo, código, pergunta aberta?)
- Qual o output esperado? (arquivo, texto estruturado, decisão, código?)
- Tem formato específico de output? (template, markdown, JSON, .docx/.md?)
- Me dá um exemplo real: "Eu digo X e espero que o Claude faça Y"

## Bloco 3 — Processo e decisões

- Quais são os PASSOS que você segue hoje pra fazer isso manualmente?
- Tem decisões no meio? (se X, faz A; se Y, faz B)
- Tem edge cases que já deram problema?
- Tem algo que o Claude faz errado quando você tenta sem skill?

## Bloco 4 — Escopo e limites

- O que essa skill NÃO deve fazer? (tão importante quanto o que deve)
- Tem skills existentes que se sobrepõem? Como diferencia?
- Quer que a skill ENSINE o processo ou só EXECUTE?

## Bloco 5 — Padrão arquitetural

Identifique qual padrão a skill precisa (consulte `references/agentic-patterns.md`):
- **Linear** — a maioria (80%+). Processo sequencial com fases claras.
- **Pipeline multi-agente** — expertise isolada com contra-argumentos (ex: Trident).
- **Fan-Out/Gather** — análises independentes em paralelo.
- **Reflection** — output precisa de auto-avaliação antes de entregar.
- **Plan-and-Execute** — escopo variável, plano antes da execução.

## Bloco 6 — Testes (plante a semente cedo)

- Me dá 2-3 situações reais em que você usaria essa skill.
- Como você saberia se o output tá bom ou ruim? (critérios de sucesso)

---

## Técnica: Declaração da Skill

Se o usuário for vago, use este template pra alinhar:

> "Me ajuda a preencher: Quando **[situação]**, o Claude deve **[ação]** pra que **[resultado]**, seguindo **[restrições]**."

---

## Dicas

- Não faça todas as perguntas de uma vez — comece pelo Bloco 1, depois aprofunde conforme a complexidade.
- Se o usuário já deu 3+ exemplos concretos e o escopo está claro, pule os blocos restantes.
- Se é uma skill operacional simples (converter CSV, formatar arquivo), os Blocos 1-2 são suficientes.
- Perguntas do Bloco 3 são as mais valiosas — é onde você descobre o processo real que a skill deve capturar.
