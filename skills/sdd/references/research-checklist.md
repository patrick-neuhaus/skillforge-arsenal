# Research Checklist — O que investigar na Phase 1

Consulte este arquivo no **Phase 1 (Research)** para não esquecer nenhuma investigação.

---

## Checklist de Investigação

### 1. Stack & Config
- [ ] Framework e versão (package.json → dependencies)
- [ ] TypeScript config (tsconfig.json — strict mode? paths?)
- [ ] Bundler/build (next.config.*, vite.config.*, etc.)
- [ ] Linter/formatter configurados (.eslintrc, .prettierrc, biome.json)

### 2. Área de Mudança
- [ ] Quais arquivos serão afetados? (listar com paths exatos)
- [ ] Quais arquivos adjacentes podem ser impactados?
- [ ] Existe código similar no projeto? (buscar padrões reutilizáveis)
- [ ] Qual o tamanho estimado da mudança? (LOC)

### 3. Convenções do Projeto
- [ ] Naming: PascalCase? camelCase? kebab-case? (componentes, funções, arquivos)
- [ ] Imports: path aliases (@/...)? barrel files? named exports?
- [ ] Estado: Zustand? Context? Redux? Server state (React Query)?
- [ ] Data fetching: Server Components? API routes? Server Actions?
- [ ] Testes: Jest? Vitest? Playwright? Co-located ou pasta separada?
- [ ] Error handling: try/catch genérico? classes custom? error boundaries?

### 4. Dependencies & Integrations
- [ ] O que toca na área de mudança? (imports, exports, types)
- [ ] Há APIs externas envolvidas? (Supabase, Stripe, etc.)
- [ ] Há migrações de banco necessárias?
- [ ] Há env vars novas necessárias?

### 5. Pesquisa Externa (Video 4 insight)
- [ ] Ler documentação relevante das libs/serviços usados (NÃO a doc inteira — só a parte relevante)
- [ ] Buscar padrões de implementação em repos de referência (usar técnica .tmp — ver `tmp-technique.md`)
- [ ] Checar Stack Overflow, GitHub issues por edge cases conhecidos
- [ ] Se usando lib nova: buscar exemplo mínimo funcional antes de projetar a spec
- [ ] Documentar trechos úteis e code snippets no prd.md (seção "External References")

### 6. Over-Engineering Check
- [ ] Existe solução mais simples já no codebase? (grep por padrões similares)
- [ ] Alguma lib instalada já resolve isso? (checar package.json)
- [ ] A abordagem proposta é mais complexa que o necessário?
- [ ] Se sim, documentar a alternativa mais simples no prd.md

### 7. Issue Breakdown (Video 2 insight)
Se a feature é grande (>15 mudanças estimadas):
- [ ] Quebre em issues atômicas (1 issue = 1 comportamento ou 1 página)
- [ ] Cada issue deve ser implementável independentemente
- [ ] Defina ordem de implementação das issues
- [ ] Gere spec.md separado por issue (ou spec-part1.md, spec-part2.md)

---

## Layered Agents (Video 2 — para features full-stack)

Se a feature cruza camadas (banco + API + frontend), considere dividir a research por camada:

| Camada | Foco da Research | Output |
|--------|-----------------|--------|
| **Data** | Schema, migrations, RLS, queries | Seção "Database Changes" no prd.md |
| **API** | Routes, server actions, validação | Seção "API Changes" no prd.md |
| **UI** | Components, state, UX flow | Seção "Frontend Changes" no prd.md |

Cada camada pode virar uma seção distinta no spec.md, facilitando implementação por "agente especializado" (ou em batches se contexto for limitado).

---

## Output da Research

O output deve ser um `prd.md` seguindo o formato em `prd-example.md`. Campos obrigatórios:
1. Context (problema + impacto)
2. Codebase Analysis (stack + arquivos + conventions + dependencies)
3. Constraints (limitações técnicas e de escopo)
4. Scope (IN + OUT explícitos)
