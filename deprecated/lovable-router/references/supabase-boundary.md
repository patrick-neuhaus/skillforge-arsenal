# Supabase Boundary — O que Lovable Gerencia

Mapeamento claro do que o Lovable controla vs o que pode ser editado diretamente.

---

## O que o Lovable Gerencia (NÃO editar direto)

### Migrations (`supabase/migrations/`)
- Arquivos SQL gerados automaticamente pelo Lovable
- Cada prompt que altera banco gera uma nova migration
- Editar diretamente quebra a cadeia de migrations — Lovable perde track do estado

### Types (`src/integrations/supabase/types.ts` ou `database.types.ts`)
- Gerado automaticamente baseado no schema atual
- Reflete exatamente o que está no banco
- Se editar manualmente, próximo prompt do Lovable sobrescreve

### Edge Functions (`supabase/functions/`)
- Criadas e deployadas pelo Lovable
- Versionamento integrado com o projeto
- Editar fora do Lovable pode causar conflito no deploy

### Storage Buckets e Policies
- Configurados via migrations do Lovable
- Policies de acesso vinculadas ao auth

### RLS Policies
- Parte das migrations
- Vinculadas ao schema e ao auth
- Alteração direta pode criar inconsistência entre migration history e estado real

### Database Functions e Triggers
- Criados via migrations
- Se criar fora do Lovable, a migration não sabe que existe

---

## O que PODE Editar Direto

### Código Frontend (100% seguro)
- Componentes React (`src/components/`)
- Pages (`src/pages/`)
- Custom hooks (`src/hooks/`) — exceto hooks que alteram schema
- Utils (`src/lib/`, `src/utils/`)
- Styles (Tailwind, CSS)
- Assets (`public/`, `src/assets/`)

### Configurações do App
- `vite.config.ts`
- `tsconfig.json`
- `tailwind.config.ts`
- `postcss.config.js`
- `.env` (variáveis de ambiente locais)
- `package.json` (adicionar dependências)

### Arquivos de Instrução
- `AGENTS.md` / `CLAUDE.md`
- `.cursorrules` / `.cursor/rules/`

### Queries Supabase no Frontend (com cuidado)
- `.from('tabela').select()` — OK se tabela/colunas existem
- `.from('tabela').insert()` — OK se RLS permite
- `.rpc('function')` — OK se function existe
- **NÃO OK:** queries que assumem colunas/tabelas que não existem

---

## Zona de Risco (editar com cuidado)

### Custom Types que Espelham Schema
- Se criou types manuais que replicam o shape do banco
- Problema: banco muda via Lovable, types manuais ficam desatualizados
- Solução: usar os types gerados sempre que possível

### Hooks com Lógica de Supabase
- `useQuery` / `useMutation` customizados
- Seguro se: query usa schema existente
- Risco se: assume dados que precisam de migration

### Validações de Formulário
- `zod` / `yup` schemas que espelham tabela
- Seguro se: validação client-side complementar
- Risco se: deveria ser CHECK constraint no banco

---

## Fluxo Correto: Banco → Frontend

```
1. Prompt pro Lovable: "Plan: Crie tabela X com campos A, B, C e RLS"
   ↓ Lovable gera: migration + types + (opcionalmente) componentes

2. Pull mudanças pro repo local
   ↓ git pull ou sync

3. Verificar:
   - Migration gerada em supabase/migrations/
   - Types atualizados
   - RLS policies criadas

4. Ajustar frontend direto (se necessário):
   - Refinar componentes que Lovable gerou
   - Criar componentes novos que usam os dados
   - Adicionar lógica de UI específica

5. Commitar tudo junto
```

---

## Sinais de Dessincronização

Se qualquer um desses sintomas aparecer, provavelmente houve edição direta no banco:

| Sintoma | Causa Provável |
|---------|---------------|
| `database.types.ts` não reflete o schema real | Tabela/coluna criada fora do Lovable |
| Migration falha no deploy | Migration manual conflita com Lovable |
| Types mostram campos que não existem na UI | Schema alterado sem atualizar frontend |
| RLS bloqueando sem razão aparente | Policy criada manualmente com lógica incorreta |
| Edge function com erro de deploy | Function editada fora do Lovable |

### Como Resolver Dessincronização

1. **Opção A (simples):** Prompt pro Lovable descrevendo o estado desejado — ele regenera
2. **Opção B (avançada):** `supabase db reset` + reaplicar migrations — DESTRUTIVO, só em dev
3. **Opção C (parcial):** Prompt pro Lovable "sincronizando" o que foi feito: "A tabela X já existe no banco com campos A, B, C. Gere a migration e types correspondentes."
