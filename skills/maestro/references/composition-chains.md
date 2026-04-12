# Composition Chains — Pipelines Validados

Consulte este arquivo no **Phase 2** quando o intent do usuário cruzar múltiplas skills.

---

## Modelo recomendado por fase de chain

Quando uma chain envolve **plan → implement → review**, troca de modelo entre fases é o padrão correto. Não use Opus high pra tudo — desperdiça budget e degrada contexto.

| Fase | Modelo recomendado | Thinking | Por quê |
|------|-------------------|----------|---------|
| Research / Discovery | Sonnet medium ou Opus high | think hard | Investigação ampla, ainda não decisional |
| Spec / Plano | **Opus high** | **ultrathink** | Decisões caras, multi-sistema, custo de errar é alto |
| Implement | **Sonnet medium** (fresh session com a spec) | default | Spec elimina ambiguidade. Sonnet executa bem o que tá bem-bounded. Use `/model opusplan` pra automatizar o handoff. |
| Review (trident) | Sonnet medium ou Sonnet high | think hard | 3-agent pipeline já compensa raciocínio |
| Architecture decisions | Opus high | ultrathink | Decisão única, custo alto se errar |

**Anti-padrão:** rodar a chain inteira em Opus high → queima usage limit em ~1h e degrada contexto bem antes do compact (degradação reportada a partir de ~40% pelo próprio Opus 4.6 1M).

**Regra de bump:** bump thinking antes de bump model. Sonnet medium + ultrathink frequentemente > Opus high + default.

---

## Chains por Cenário

### Feature Nova (do zero ao deploy)
```
1. code-dedup-scanner --check → reusables found
2. sdd --phase research       → prd.md (~30% context)
   └─ (optional) pattern-importer → pattern doc
   └─ context-guardian --handoff → /clear
3. sdd --phase spec           → spec.md (~30% context)
   └─ context-guardian --handoff → /clear
4. sdd --phase implement      → código (~40% context)
   └─ context-guardian --handoff → /clear
5. architecture-guard --scan  → structural violations
6. trident --mode all-local   → bug review (~35% context)
```
**Handoff:** prd.md → spec.md → código → diff para guard + trident
**Quando:** Feature complexa, >3 arquivos, precisa de planejamento

### Feature Nova (frontend React)
```
1. sdd --phase research       → prd.md
   └─ context-guardian --handoff → /clear
2. component-architect --plan → component tree + interfaces
3. sdd --phase spec           → spec.md (incorpora component tree)
   └─ context-guardian --handoff → /clear
4. react-patterns --scaffold  → componentes base
5. sdd --phase implement      → código completo
   └─ context-guardian --handoff → /clear
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

### Criar Skill Nova (com GEO)
```
1. reference-finder --find    → referências do domínio (~25% context)
2. skill-builder --full       → SKILL.md + references/ (~40% context)
3. prompt-engineer --validate → validação dos prompts internos (~20% context)
   └─ /clear
4. geo-optimizer --optimize   → description otimizada (~15% context)
5. trident --skill            → review como produto (~25% context)
```
**Handoff:** Referências → contexto para skill-builder → prompts validados → description GEO → product review
**Quando:** Criando skill para domínio que o usuário não domina completamente

### Bug Fix
```
1. trident --mode unstaged    → identify bugs (~30% context)
2. sdd --phase spec           → spec de fix (pode ser inline, sem prd.md)
3. sdd --phase implement      → fix aplicado
4. trident --mode all-local   → confirmar fix (~30% context)
```
**Quando:** Bug reportado ou encontrado em review

### Conteúdo SEO + IA (Google + LLMs)
```
1. seo --keyword              → keyword research + canibalização (~25% context)
2. seo --content              → estratégia de conteúdo (~20% context)
3. copy --mode blog-seo       → draft do conteúdo (~25% context)
4. ai-seo                     → otimização pra citação em LLMs (~15% context)
```
**Handoff:** Keywords → estrutura de conteúdo → copy → otimização AEO/GEO/LLMO
**Quando:** Conteúdo precisa rankear no Google E ser citado por ChatGPT/Perplexity/Claude
**Por que não só seo:** Google ranking ≠ LLM citation. ai-seo cuida da camada de visibilidade em respostas geradas por IA.

### Produto Novo
```
1. product-discovery-prd      → PRD (~30% context)
   └─ /clear
2. ui-design-system --generate → design.json
3. sdd --phase spec           → spec técnico baseado no PRD
   └─ context-guardian --handoff → /clear
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

### Editar Projeto Lovable
```
1. lovable-router --route     → classificar mudança (código vs banco)
   ├─ Rota Código:
   │   └─ sdd / react-patterns / component-architect → implementar direto
   │   └─ trident --review
   └─ Rota Banco:
       └─ (opcional) supabase-db-architect → design schema
       └─ prompt-engineer → prompt otimizado pro Lovable
       └─ Pós-Lovable: verificar + ajustar código se necessário
```
**Handoff:** classificação → implementação direta OU prompt pro Lovable → verificação
**Quando:** Qualquer mudança em projeto construído com Lovable

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
| code-dedup-scanner | sdd --research | reusables found |
| pattern-importer | sdd --research | pattern document |
| architecture-guard | trident | structural violations |
| skill-builder | geo-optimizer | SKILL.md draft pra otimizar description |
| context-guardian --handoff | /clear | handoff document |

---

## Chains Novas (v2)

### Evoluir Skill
```
1. skill-builder --evolve     → skill melhorada (~30% context)
2. prompt-engineer --validate → prompts internos validados (~20% context)
3. geo-optimizer --optimize   → description otimizada (~15% context)
```
**Quando:** Melhorar skill existente (description, structure, references)

### Guard Pipeline (validação pré-merge)
```
1. code-dedup-scanner --check → verificar reutilizáveis
2. architecture-guard --scan  → violações estruturais
3. trident --mode all-local   → bugs e qualidade
```
**Quando:** Validação completa antes de merge. Cada pode rodar independente.

### Context Management
```
1. context-guardian --check   → status 🟢/🟡/🔴
2. (se 🔴) context-guardian --handoff → handoff document
3. /clear
4. Retomar com handoff como primeiro prompt
```
**Quando:** Conversa longa, chains pesadas, entre fases SDD

### API → CLI → Skill
```
1. cli-skill-wrapper --analyze → design da CLI
2. cli-skill-wrapper --wrap    → script + SKILL.md básico
3. skill-builder --evolve      → melhorar SKILL.md gerado
4. geo-optimizer --optimize    → description GEO
```
**Quando:** Wrapar API pesada (MCP replacement ou API nova)

---

## Meta-Orchestration — Evoluindo o Arsenal

Chains especiais pra criar/evoluir/publicar skills do próprio arsenal.

### Criar Nova Skill
```
reference-finder → skill-builder --full → prompt-engineer --validate
→ context-guardian --handoff → /clear → geo-optimizer → trident --skill
```

### Evoluir Skill Existente
```
skill-builder --evolve → prompt-engineer --validate → geo-optimizer
→ prompt-engineer --validate + skill-builder --validate
```

### Publicar Skill no skills.sh
```
geo-optimizer --optimize → prompt-engineer --validate + skill-builder --validate → (publicação manual no skills.sh)
```
