# Decision Matrix — Código vs Banco

Tabela completa de classificação para determinar se uma mudança em projeto Lovable deve ser feita diretamente (código) ou via prompt pro Lovable (banco).

---

## Princípio

O Lovable gerencia o estado do banco via migrations internas. Quando você cria/altera tabelas, RLS, edge functions ou storage policies pelo Lovable, ele:
1. Gera migration files automaticamente
2. Atualiza `database.types.ts` automaticamente
3. Mantém sincronia entre schema e código
4. Faz deploy integrado

Editar qualquer um desses artefatos diretamente QUEBRA essa sincronia.

---

## Tabela de Classificação Detalhada

### ✅ Rota Código (editar direto)

| Item | Exemplos | Por que é seguro |
|------|---------|-----------------|
| Componentes React | Criar/editar componente, mudar layout, adicionar estado | Não toca schema |
| Pages e rotas | Nova página, reorganizar rotas, lazy loading | Frontend puro |
| Custom hooks (sem supabase) | useLocalStorage, useDebounce, useMediaQuery | Sem interação com banco |
| Utils e helpers | formatDate, cn(), parseCurrency | Lógica pura |
| Styles e CSS | Tailwind classes, CSS modules, animações | Visual puro |
| Assets | Imagens, ícones, fontes | Arquivos estáticos |
| Configs do app | vite.config, tsconfig, .env (não secrets) | Build config |
| Constantes e enums | Status values, feature flags, labels | Frontend puro |
| Context providers | ThemeProvider, AuthContext (wrapper, não lógica) | Estado do app |
| Testes | Unit tests, integration tests | Não afeta banco |

### 🔀 Rota Banco (prompt pro Lovable)

| Item | Exemplos | Por que precisa do Lovable |
|------|---------|---------------------------|
| Tabelas e colunas | CREATE TABLE, ALTER TABLE, ADD COLUMN | Gera migration + types |
| Indexes | CREATE INDEX | Parte do schema |
| RLS policies | CREATE POLICY, ALTER POLICY | Integrado com auth |
| Edge functions | Nova função ou alterar existente | Deploy integrado |
| Storage policies | Permissões de upload/download | Acoplado ao auth |
| Database functions | CREATE FUNCTION (PL/pgSQL) | Parte do schema |
| Triggers | CREATE TRIGGER | Dependem de functions |
| Views | CREATE VIEW | Parte do schema |
| Enums no banco | CREATE TYPE ... AS ENUM | Usado em migrations |
| Foreign keys | ADD CONSTRAINT FOREIGN KEY | Relacionamentos |

### ⚠️ Zona Cinza (avaliar caso a caso)

| Item | Quando é CÓDIGO | Quando é BANCO |
|------|:---------------:|:--------------:|
| Queries inline (`supabase.from(...)`) | Query não muda, só como apresenta dados | Query precisa de coluna/tabela nova |
| Hooks com supabase client | Hook muda lógica de apresentação | Hook precisa de dados que não existem no schema |
| Types manuais | Tipo local pra UI (FormData, UIState) | Tipo que espelha schema — mudar via Lovable |
| Validações | Validação de form (zod/yup) | Validação que deveria ser CHECK constraint |
| Filtros e ordenação | .order(), .eq() em dados existentes | Precisa de index novo pra performance |
| Real-time subscriptions | Ativar/desativar listening | Precisa habilitar Realtime na tabela |

### ⛔ NUNCA editar

| Item | Por quê |
|------|---------|
| `database.types.ts` | Auto-gerado pelo Lovable. Será sobrescrito no próximo prompt |
| `supabase/migrations/*.sql` | Gerenciado pelo Lovable. Editar quebra o histórico de migrations |
| `.lovable/*` | Configs internas do Lovable |

---

## Árvore de Decisão Rápida

```
A mudança envolve...

1. Criar/alterar tabela, coluna, index?
   → 🔀 Prompt Lovable

2. Criar/alterar RLS policy?
   → 🔀 Prompt Lovable

3. Criar/alterar edge function ou database function?
   → 🔀 Prompt Lovable

4. Criar/alterar storage policy?
   → 🔀 Prompt Lovable

5. O código precisa de dados que NÃO existem no schema atual?
   → 🔀 Prompt Lovable (pra criar os dados) + ✅ Código (pra consumir)

6. A mudança é puramente visual/lógica/frontend?
   → ✅ Código direto

7. Não tem certeza?
   → Pergunta: "Essa mudança altera o contrato de dados (shape dos objetos do banco)?"
     → Sim: 🔀 Prompt Lovable
     → Não: ✅ Código direto
```

---

## Cenários Comuns

### "Quero adicionar um campo de status nos pedidos"
→ 🔀 Prompt Lovable (nova coluna na tabela orders + atualizar RLS se necessário)
→ DEPOIS ✅ Código (componente que mostra o status)

### "Quero mudar a cor do botão de salvar"
→ ✅ Código direto (CSS/Tailwind)

### "Quero adicionar filtro por data na listagem"
→ ⚠️ Avaliar:
  - Coluna de data já existe? → ✅ Código (.order(), .gte())
  - Precisa de index pra performance? → 🔀 Prompt Lovable (CREATE INDEX)
  - Precisa de coluna nova? → 🔀 Prompt Lovable

### "Quero restringir quem pode ver os relatórios"
→ 🔀 Prompt Lovable (nova RLS policy ou alterar existente)

### "Quero refatorar o componente de dashboard"
→ ✅ Código direto (sem mudar dados)

### "Quero adicionar upload de foto de perfil"
→ 🔀 Prompt Lovable (storage bucket + policy)
→ DEPOIS ✅ Código (componente de upload)

### "Quero criar uma edge function pra processar webhook"
→ 🔀 Prompt Lovable (edge function + deployment)
