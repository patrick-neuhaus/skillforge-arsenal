# Workspace Knowledge — Coleta e Template

Referência para gerar Workspace Knowledge do Lovable.
Workspace Knowledge se aplica a TODOS os projetos do workspace. Setup feito uma vez, revisado a cada 3-6 meses.

**Limite:** 10.000 caracteres.

---

## Coleta — Perguntas em blocos de 2-3

Apresente em blocos. NÃO despeje todas de uma vez.

### Bloco 1 — Stack e libs

- Stack base? (React + TypeScript strict?)
- Libs de UI? (shadcn/ui, Material UI, Chakra?)
- Estado do cliente? (Zustand, Redux, TanStack Query?)
- Validação? (Zod, Yup, manual?)
- Estilização? (Tailwind, CSS Modules?)

### Bloco 2 — Padrões de código

- Naming: camelCase variáveis? PascalCase componentes? kebab-case arquivos?
- Exports: named ou default?
- const vs let?
- Comentários em qual idioma?

### Bloco 3 — Arquitetura

- Chamadas de API: direto do componente ou service layer?
- Estrutura de pastas? (/components, /services, /hooks, /utils, /types)
- Valores monetários: cents (inteiro) ou decimal?
- Mutations: optimistic update ou espera resposta?

### Bloco 4 — Testes e qualidade

- Testes unitários pra hooks/utils?
- Browser testing do Lovable?
- Linter após mudanças significativas?

### Bloco 5 — Localização e brand voice

- UI text em qual idioma?
- Formato de data? (DD/MM/YYYY)
- Formato de números? (vírgula ou ponto decimal)
- Tom: formal, informal, técnico?
- Sentence case ou Title Case pra headings?

### Bloco 6 — "Never do" (guardrails globais)

- O que o Lovable NUNCA deve fazer sem pedir?
- Padrões deprecated a evitar?
- Libs proibidas?

---

## Template de Geração

Inclua APENAS seções com conteúdo real. Remova seções vazias.

```
Coding standards
- [TypeScript strict, const, unknown não any, etc]

Naming conventions
- [camelCase, PascalCase, kebab-case]

Styling
- [Tailwind, regras de CSS]

Libraries
- [libs obrigatórias e preferidas, com versões se relevante]

Architecture
- [service layer, pastas, patterns]

Testing
- [o que testar, quando rodar]

Localization
- [idioma UI, formato data/número, idioma código]

Brand voice
- [tom, convenções de copy, CTAs, mensagens de erro]

General rules
- NEVER [ação proibida 1]
- NEVER [ação proibida 2]
- NEVER [ação proibida 3]
- ALWAYS [regra obrigatória 1]
- ALWAYS [regra obrigatória 2]
```

---

## Validação

1. **Contagem de caracteres.** Se > 10.000, corte. Prioridade: General Rules > Architecture > Libraries > Coding Standards > resto.
2. **Checklist de completude:**
   - Tem "General rules" com pelo menos 3 "NEVER"? Se não, pergunte.
   - Tem libs definidas? Sem isso, Lovable escolhe sozinho.
   - Tem naming? Sem isso, inconsistente entre projetos.
3. **Apresente e peça confirmação antes de finalizar.**
