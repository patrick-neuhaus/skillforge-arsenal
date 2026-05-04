# Narrative Template — Anti-Hallucination

> Carrega na Phase 2. Anti-pattern: gerar narrative do README sem comprehension.json (alucina features).

## Prompt template

```
Role: Você é narrator de produto. Recebe comprehension.json (Phase 1) + README.md.

Gera narrative.md com 4 seções:

## Pitch (1 parágrafo)
1 frase explicando o que produto FAZ pra USUÁRIO.
Cite SÓ features verificáveis em comprehension.componentes_chave + fluxos_inferidos.
NÃO invente métricas ("30% faster", "10x more efficient", "leading...").

## Audience
Quem usa? Extraia de README + tipo do produto + nome do repo.
Padrões: CRM → vendedores/SDR; dashboard → ops/managers; chat → suporte; viewer → analistas.
Se ambíguo, declare "audience inferida — confirmar com user".

## Value proposition (3 bullets max)
Cada bullet cita componente OU fluxo do comprehension.json como evidência.
Format: "<value> — porque <componente/fluxo do repo>"

## Key flows (3-5)
Extraídos de comprehension.fluxos_inferidos + comprehension.rotas.
Format: "Persona X → entry point → ação 1 → ação 2 → outcome"
```

## Anti-hallucination checklist

Antes de finalizar narrative, verificar:

- [ ] Cada métrica citada vem do README ou comprehension (não inventada)
- [ ] Cada feature mencionada aparece em componentes_chave OU fluxos_inferidos
- [ ] Sem comparações com competidores ("better than X") sem evidência no README
- [ ] Audience tem evidência (README, tipo, nome) ou está marcada como "inferida"
- [ ] Cada value bullet tem source citado

## Output exemplo

```markdown
## Pitch
ia-da-plus é CRM operacional pra gestão de pipeline de vendas IoT, com importação CSV e dashboards de métricas.

## Audience
Vendedores B2B de produto técnico (IoT). Inferido do tipo CRM + componentes table CRUD + recharts (dashboards) + papaparse (CSV import). Confirmar com Patrick.

## Value proposition
- Pipeline visual com drag → porque ClientTable.tsx + DialogEdit
- Métricas históricas → porque recharts em DashboardPage.tsx
- Bulk import → porque papaparse + ImportModal.tsx

## Key flows
1. Vendedor → /login → /dashboard → /clients/:id → editar deal
2. Admin → /import → upload CSV → mapping → save
3. Manager → /dashboard → filtra período → export
```
