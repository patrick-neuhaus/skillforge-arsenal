---
name: design-system-audit
description: "Audita app contra design system EXTERNO existente com fase de coerência. Default DS: anti-ai-design-system (Patrick canonical). Use quando: 'tira a cara de IA do app', 'deixa o app mais bonito', 'aplica design system', 'aplica o design system X em Y', 'esse app segue o design system?', 'audita conformidade com design system', 'compara app com tokens', 'onboard app no design system', 'verifica drift do design system', 'design system audit', 'design conformance check'. Diferente de ui-design-system (que GERA do zero) e component-architect (audita health interno). Foco: app contra spec EXTERNA, julgamento de coerência. Se user fala 'design system' sem citar repo: assume default anti-ai-design-system."
---

# Design System Audit

IRON LAW: NEVER apply a pattern without first asking if it fits the target app's context. Patterns are defaults, not commandments. The coherence phase (Phase 4) is non-negotiable — skipping it produces templates burros que copiam estrutura sem adaptação semântica.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--audit` | Inventory + diff + coherence check, output delta report | default |
| `--apply` | Audit + aplica deltas aprovados (gated por delta) | - |
| `--bootstrap` | Scaffold app from scratch following design system | - |
| `--ds-path <path>` | Override default DS reference path | default: ~/Documents/Github/anti-ai-design-system |

## Workflow

```
Design System Audit Progress:

- [ ] Phase 1: Context Collection ⚠️ REQUIRED
  - [ ] 1.1 Identify target app path
  - [ ] 1.2 Identify design system path (repo or doc)
  - [ ] 1.3 ASK user: tipo de usuário, workflow principal, admin separado?
  - [ ] 1.4 Capture answers literally — alimenta Phase 4
- [ ] Phase 2: Inventory (determinístico)
  - [ ] 2.1 shadcn primitives, custom components, pages
  - [ ] 2.2 Tokens (index.css ou equivalente)
  - [ ] 2.3 Lovable memory, layout files
- [ ] Phase 3: Spec Diff
  - [ ] 3.1 Para cada componente shared no DS, checar target
  - [ ] 3.2 Para cada token no DS, checar target
  - [ ] 3.3 Para cada regra em docs do DS, grep no target
- [ ] Phase 4: Coherence Check ⛔ BLOCKING (the arbiter)
  - [ ] 4.1 Squint test: redundâncias visuais?
  - [ ] 4.2 Navegação: items em múltiplos lugares — semantic ou structural?
  - [ ] 4.3 Frequência vs proeminência alinhadas?
  - [ ] 4.4 Cada delta — fix faz sentido GIVEN Phase 1, ou é dogma?
  - [ ] 4.5 Contrast Audit: cada par bg+fg passa WCAG AA (4.5:1)?
- [ ] Phase 5: Delta Report
  - [ ] 5.1 Cada delta com WHAT + WHY HERE + ADAPTATION + severity + action
- [ ] Phase 6: GATE ⛔
  - [ ] User decides por delta: apply / adapt / skip
```

## Default DS Reference (Wave 7)

**Default path:** `~/Documents/Github/anti-ai-design-system`

Estrutura esperada:
- `docs/03-token-system.md` — regras WCAG AA + tokens
- `docs/07-component-patterns.md` — Login 50/50, AppTable, Configurações user panel
- `presets/warm-editorial/` — cream + teal + Lora/Poppins
- `presets/minimalist-tech/` — mono + signal (Forge.sh flavor)
- `presets/_shared/` — AppTable, StatusBadge, table.tsx

**Ativação automática:**
- Se user pede "design system audit" SEM citar path explícito → assume default acima
- Se path existe → Phase 2 Inventory roda `ls` e `cat` automático nos arquivos chave
- Se path NÃO existe → Phase 1 pergunta: "DS canônico em outro repo? Path?"
- User pode override com `--ds-path <custom-path>` (ex: para auditar contra DS de cliente)

**Phase 2 auto-loads (quando default ativo):**
```bash
ls ~/Documents/Github/anti-ai-design-system/presets/
cat ~/Documents/Github/anti-ai-design-system/docs/03-token-system.md
cat ~/Documents/Github/anti-ai-design-system/docs/07-component-patterns.md
ls ~/Documents/Github/anti-ai-design-system/presets/_shared/
```

## Phase 1: Context Collection

NUNCA pule. Skip = template burro garantido.

Perguntas obrigatórias ao usuário (capture respostas literalmente):

1. **Quem usa?** Admin, end-user, hybrid? Múltiplos roles?
2. **Workflow principal?** 1 frase descrevendo o que o usuário faz mais
3. **Área admin separada?** Se sim, onde fica? Quem acessa?
4. **Features condicionadas?** Tem coisa que aparece só pra alguns roles?
5. **Contexto técnico não-óbvio?** Lovable? Multi-tenant? Mobile-first? Stack particular?

Estas respostas alimentam Phase 4. Sem elas, Phase 4 vira checklist genérico.

## Phase 2: Inventory

Determinístico via Bash/Grep:

```bash
ls <target>/src/components/ui/                    # shadcn primitives
find <target>/src/components -name "*.tsx" -not -path "*/ui/*"   # custom
ls <target>/src/pages/                            # pages
cat <target>/src/index.css                        # tokens
ls -la <target>/.lovable/memory/                  # lovable memory
grep -nE "<h[12]" <target>/src/pages/*.tsx       # page headers
grep -rn "text-right\|justify-end" <target>/src/ # action col antipattern
```

Output: lista crua, sem julgamento.

## Phase 3: Spec Diff

Para CADA item da spec:
- **Component-level:** componente shared existe no target? path? mesma assinatura?
- **Token-level:** token presente? mesmo valor (ou variação justificada)?
- **Rule-level:** padrão da regra grep retorna match no target? quantos?

Captura raw. Não decida ainda — Phase 4 que decide.

## Phase 4: Coherence Check (CRÍTICA)

Esta fase diferencia "design system audit" de "checklist application".

**Perguntas obrigatórias** (responda com base em Phase 1 + Phase 3):

### 4.1 Squint test
Olhe sidebar e header como um todo. Tem item em 2 lugares? Tem hierarquia clara?

### 4.2 Navigation duplication
Para CADA item de navegação ou ação que aparece >1 vez:
- É **semantic** (atende usuários/intenções diferentes)?
- Ou **structural** (mesma intenção, só copy-paste)?
- Se structural → recomendar consolidação

### 4.3 Frequência vs proeminência
- O que Phase 1 disse ser frequente está visível?
- O que é raro está fora do caminho principal?

### 4.4 Adaptação local por delta
Para CADA delta da Phase 3, decidir:
- **APPLY:** spec serve como está → aplicar literal
- **ADAPT:** spec é boa direção mas precisa ajuste pra esse app → adaptar com justificativa
- **SKIP:** spec não serve esse contexto → não aplicar, documentar por quê

### 4.5 Contrast Audit (WCAG AA)

Para CADA par bg+fg do preset alvo, calcular ratio. Se < 4.5:1 (texto small) ou < 3:1 (texto large/bold), token é decorative-only — não pode ser usado como `color` de texto/ícone-info.

Pares obrigatórios (alvo: validar todos):
- `--foreground` sobre `--background`
- `--card-foreground` sobre `--card`
- `--primary-foreground` sobre `--primary`
- `--accent-foreground` sobre `--accent`
- `--sidebar-foreground` sobre `--sidebar-background`
- `--sidebar-accent-foreground` sobre `--sidebar-accent`
- `--status-{name}-fg` sobre `--status-{name}-bg`
- `--destructive-foreground` sobre `--destructive`

**Detecção de drift:** grep `text-accent\|text-sidebar-indicator\|text-signal\|text-{decorative-token}` em pages/. Cada match = candidato a falhar AA, validar manualmente.

**Falhas viram delta:** se um par falha AA, gerar delta com action `apply` automaticamente — não passa por gate de coherence (acessibilidade não é opcional).

⛔ GATE: nenhum delta segue pra Phase 5 sem ter passado por 4.4 e 4.5.

## Phase 5: Delta Report

Formato exato:

```markdown
# Audit: <app> vs <design-system>

## Context (Phase 1)
- Users: ...
- Workflow: ...
- Admin: ...

## Deltas

### Delta N: <nome curto>
**What:** <observação concreta>
**Why it matters HERE:** <baseado em context Phase 1, não regra abstrata>
**Adaptation:** <como aplicar — pode divergir da spec literal>
**Severity:** alta | média | baixa
**Action:** apply | adapt | skip
```

Cada delta tem **WHY HERE** específico do app, não citação de regra.

## Phase 6: GATE

⛔ Não aplicar sem aprovação por delta.

User responde por delta:
- `apply` — segue recomendação
- `modify <new-instruction>` — ajusta antes (volta a Phase 4 com novo input)
- `skip` — delta não relevante

Apenas após aprovação explícita, modo `--apply` executa Edits.

## Anti-Patterns

- **Pular Phase 1** — sem context = template burro garantido
- **Pular Phase 4** — viola IRON LAW; resultado vai ter redundâncias semânticas
- **Reportar deltas como "regra X violada"** — métrica é "faz sentido AQUI", não conformidade abstrata
- **Aplicar sem GATE** — sempre humano-in-the-loop
- **Tratar spec como dogma** — design system é default razoável, não verdade absoluta
- **Coerência vira checklist genérico** — cada pergunta da Phase 4 deve gerar resposta específica do contexto, não SIM/NÃO mecânico
- **Aplicar shared component em massa sem testar 1 caso** — em modo --apply, quando Phase 6 aprova uso de novo shared component em N pages, aplicar em 1 primeiro, validar visualmente, só então propagar. Caso contrário: bug do componente quebra N pages simultâneo. (Lição: AW v2 — bug `<tbody><tbody>` em AppTable só apareceu após migrar 2 pages.)

## Pre-Delivery Checklist

- [ ] Phase 1 fez perguntas e capturou respostas
- [ ] Phase 4 gerou questões específicas do contexto, não genéricas
- [ ] Cada delta tem WHY HERE referenciando Phase 1
- [ ] Cada delta tem ADAPTATION (não é cópia literal)
- [ ] GATE respeitado — user aprovou por delta antes de qualquer Edit

## When NOT to use

- Não tem design system spec → use `ui-design-system --generate` primeiro
- Audit de health interno de 1 componente → use `component-architect --audit`
- Duplicação intra-repo (não vs spec externa) → use `code-dedup-scanner`
- Audit de UX flow → use `ux-audit`

## Integration

- **ui-design-system** complementa: este consome spec; aquele gera/audita spec
- **component-architect** complementa: este audita conformidade externa; aquele audita health interno
- **code-dedup-scanner** alimenta Phase 2 quando target tem muita inline duplication
- **prompt-engineer --validate** ao editar este SKILL.md (IL-1)
- **skill-builder --validate** valida estrutura (IL-4)

## Example: AWControl audit

**Phase 1:**
- Users: "Admin (awnet) + end-user opcional"
- Workflow: "Upload + processamento + revisão de documentos"
- Admin: "Configurações = admin only"

**Phase 3 finding:** "Configurações em adminItems da nav E em user panel"

**Phase 4 coherence:**
- 4.2 navigation duplication: Configurações está em 2 lugares
- 4.4 adaptação: Phase 1 disse "admin only". User panel resolve acesso rápido. Manter em adminItems duplica caminhos sem hierarquia clara → STRUCTURAL duplication, não semantic
- Decisão: ADAPT — manter no user panel, remover de adminItems

**Phase 5 delta:**
- What: Configurações em 2 lugares na sidebar
- Why HERE: Admin (Phase 1) precisa acesso rápido — user panel resolve. Duplicar em adminItems vira ruído
- Adaptation: Remover de adminItems, manter no user panel
- Severity: média
- Action: adapt

**Sem Phase 4:** spec aplicada literal "Config no user panel ✓", duplicação passa, app fica confuso. Foi exatamente isso que aconteceu antes desta skill existir.