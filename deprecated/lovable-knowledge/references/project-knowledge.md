# Project Knowledge — Coleta e Template

Referência para gerar Project Knowledge do Lovable.
Project Knowledge se aplica a UM projeto específico. Criado no início de cada projeto e atualizado conforme evolui.

**Limite:** 10.000 caracteres.
**Prioridade:** Project Knowledge tem prioridade sobre Workspace Knowledge quando conflitam.

---

## Detecção de Input

Antes de perguntar, verifique o que já existe:

1. **Tem PRD?** Leia e extraia: visão, stack, usuários, fluxos, regras, modelo de dados, fora do escopo. Pergunte APENAS o que o PRD não cobre.
2. **Tem codebase?** Analise: package.json, pastas, schema SQL, componentes, README. Pergunte o que o código não revela.
3. **Sem nada?** Fluxo completo de perguntas abaixo.

---

## Coleta — Perguntas em blocos de 2-3

### Bloco 1 — O projeto

- Em uma frase, o que esse app faz?
- Pra quem? Roles/permissões?

### Bloco 2 — Dados e arquitetura

- Tabelas/entidades principais?
- Integrações externas?
- Algo do schema que o Lovable PRECISA saber?

### Bloco 3 — Design e UX

- Referência visual?
- Paleta de cores? Tipografia?
- Layout: sidebar, tabs, dashboard?
- Mobile-first ou desktop-first?

### Bloco 4 — Domínio e terminologia

- Termos do negócio que o Lovable pode confundir? (ex: "Transaction = mudança de estoque, não pagamento")
- Regras de negócio não óbvias?

### Bloco 5 — Constraints

- O que o Lovable NÃO deve mexer?
- Componentes intocáveis?
- Decisões que parecem estranhas mas são intencionais?

---

## Template de Geração

```
Project overview
[1-3 frases: o que é, pra quem, qual problema resolve]

Users
[Roles, permissões, volume esperado]

Key database tables
[Tabelas com campos essenciais e tipos — só o que o Lovable precisa pra queries e types]

Design guidelines
[Paleta, tipografia, layout, componentes, referências]

Architecture rules
[Decisões específicas deste projeto]

Domain terminology
[Termos com definição clara — especialmente ambíguos]

External integrations
[APIs, webhooks, formatos esperados]

Component states
[Definir empty/loading/error/success pra componentes principais]

Out of scope
[O que NÃO fazer — features adiadas, componentes intocáveis]
```

---

## Validação

1. **Caracteres < 10.000.** Se exceder, corte detalhes de schema primeiro.
2. **Conflitos com Workspace.** Se contradiz, avise explicitamente. Project tem prioridade, mas conflito causa confusão.
3. **"Out of scope" obrigatória.** Sem isso, Lovable refatora o que não deveria.
4. **Apresente e peça confirmação antes de finalizar.**
