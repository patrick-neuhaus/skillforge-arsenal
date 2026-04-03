# Composition Chains — Pipelines Validados

Consulte este arquivo no **Phase 2** quando o intent do usuário cruzar múltiplas skills.

---

## Chains por Cenário

### Feature Nova (do zero ao deploy)
```
1. sdd --phase research       → prd.md (~30% context)
   └─ /clear
2. sdd --phase spec           → spec.md (~30% context)
   └─ /clear
3. sdd --phase implement      → código (~40% context)
   └─ /clear
4. trident --mode all-local   → review findings (~35% context)
```
**Handoff:** prd.md → spec.md → código → diff para trident
**Quando:** Feature complexa, >3 arquivos, precisa de planejamento

### Feature Nova (frontend React)
```
1. sdd --phase research       → prd.md
   └─ /clear
2. component-architect --plan → component tree + interfaces
3. sdd --phase spec           → spec.md (incorpora component tree)
   └─ /clear
4. react-patterns --scaffold  → componentes base
5. sdd --phase implement      → código completo
   └─ /clear
6. trident --mode all-local   → review
```
**Quando:** Feature de UI complexa com múltiplos componentes

### Design → Código
```
1. ui-design-system --generate → design.json (~25% context)
2. ui-design-system --apply    → Tailwind config / CSS variables
3. component-architect --plan  → component tree com tokens aplicados
```
**Handoff:** design.json → Tailwind config → component specs
**Quando:** Projeto novo ou redesign visual

### Auditoria Profunda (código)
```
1. trident --mode dir         → findings gerais (~35% context)
2. react-patterns --audit     → findings React-específicos (~25% context)
3. security-audit             → findings de segurança (~35% context)
```
**Nota:** Cada audit pode rodar independente. Ordenar por prioridade do usuário.
**Quando:** Pré-release, code freeze, onboarding em projeto existente

### Auditoria Profunda (infra + segurança)
```
1. vps-infra-audit            → findings de infra (~35% context)
   └─ /clear
2. security-audit             → findings de segurança (~35% context)
```
**Quando:** Auditoria de servidor antes de produção

### Conhecimento Novo → Preservação
```
1. reference-finder --find    → referências curadas
2. context-tree --add         → entries scored no tree
```
**Handoff:** Output do reference-finder → input do context-tree com scoring
**Quando:** Pesquisando domínio novo, aprendendo área desconhecida

### Criar Skill Nova
```
1. reference-finder --find    → referências do domínio (~25% context)
2. skill-builder --full       → SKILL.md + references/ (~40% context)
3. prompt-engineer --validate → validação dos prompts internos (~20% context)
```
**Handoff:** Referências → contexto para skill-builder → prompts para validação
**Quando:** Criando skill para domínio que o usuário não domina completamente

### Bug Fix
```
1. trident --mode unstaged    → identify bugs (~30% context)
2. sdd --phase spec           → spec de fix (pode ser inline, sem prd.md)
3. sdd --phase implement      → fix aplicado
4. trident --mode all-local   → confirmar fix (~30% context)
```
**Quando:** Bug reportado ou encontrado em review

### Produto Novo
```
1. product-discovery-prd      → PRD (~30% context)
   └─ /clear
2. ui-design-system --generate → design.json
3. sdd --phase spec           → spec técnico baseado no PRD
   └─ /clear
4. sdd --phase implement      → MVP
```
**Quando:** Validando ideia de produto, construindo MVP

### Database Design
```
1. supabase-db-architect      → schema + RLS + migrations
2. sdd --phase spec           → spec de integração backend
3. sdd --phase implement      → implementação
```
**Quando:** Novo módulo que precisa de schema

---

## Regras de Composição

### Context Window Budget
| Skills na chain | Budget por skill | Precisa /clear? |
|-----------------|-----------------|-----------------|
| 1 skill | ~40% | Não |
| 2 skills | ~25-30% cada | Geralmente não |
| 3+ skills | ~20-25% cada | Sim, entre fases pesadas |
| SDD (4 fases) | ~30% por fase | Sim, entre cada fase |

### Quando NÃO encadear
- Tarefa resolve com 1 skill → não complique
- Skills não produzem output que a próxima consome → são independentes, não chain
- Usuário só quer explorar → sugira skills, não chains

### Sinais de Chain
- "Quero fazer X E depois Y" → chain explícita
- "Quero implementar [feature complexa]" → SDD chain implícita
- "Preciso auditar tudo" → chain de audits paralelos
- "Quero criar do zero" → chain design → implement → review

### Handoff Documents
| De | Para | Documento |
|----|------|-----------|
| sdd --research | sdd --spec | prd.md |
| sdd --spec | sdd --implement | spec.md |
| sdd --implement | trident | git diff |
| reference-finder | context-tree | referências com scoring sugerido |
| ui-design-system | component-architect | design.json |
| product-discovery-prd | sdd | PRD completo |
| component-architect | sdd --spec | component tree + interfaces |
