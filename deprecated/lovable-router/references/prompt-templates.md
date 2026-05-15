# Prompt Templates — Gerar Prompts pro Lovable

Templates otimizados para gerar prompts que o Lovable executa com alta precisão.
Cada template segue a estrutura: Objetivo → Schema Changes → RLS → Exemplos → Constraints.

---

## Regras Gerais

1. **3-4 mudanças por prompt** — Lovable confunde com 5+. Se precisa de mais, quebre em prompts sequenciais.
2. **Plan Mode primeiro** — Prefixe com "Plan:" pra Lovable desenhar a solução antes de implementar.
3. **Referência ao que existe** — "Na tabela orders existente, adicione..." é melhor que "Crie uma coluna..."
4. **Nomeie explicitamente** — "Crie a tabela `user_preferences`" em vez de "crie uma tabela pra preferências"
5. **RLS sempre** — Se o prompt cria tabela sem mencionar RLS, Lovable pode não criar policies.
6. **Contexto de uso** — Diga COMO o frontend vai usar os dados novos.

---

## Template 1: Nova Tabela

```
Plan: Criar tabela [nome_tabela] para [objetivo].

Schema:
- Tabela: [nome_tabela]
  - id: uuid (PK, gen_random_uuid())
  - [campo1]: [tipo] — [descrição]
  - [campo2]: [tipo] — [descrição]
  - [campo_fk]: uuid (FK → [tabela_ref].id, ON DELETE [CASCADE/SET NULL])
  - created_at: timestamptz (default now())
  - updated_at: timestamptz (trigger auto-update)

RLS:
- SELECT: usuários autenticados veem apenas seus próprios registros (user_id = auth.uid())
- INSERT: usuários autenticados podem criar apenas para si mesmos
- UPDATE: apenas o dono pode editar
- DELETE: [apenas o dono / ninguém / admin]

Uso no frontend:
- [Página/componente] vai listar [nome_tabela] do usuário logado
- [Formulário] vai permitir criar novo registro
- [Ação] vai atualizar [campo]

Constraints:
- NÃO alterar tabelas existentes: [listar]
- NÃO criar novas páginas, apenas a tabela e suas policies
```

---

## Template 2: Alterar Tabela Existente

```
Plan: Adicionar [campos/mudanças] na tabela [nome_tabela].

Mudanças:
1. Adicionar coluna [nome]: [tipo], default [valor], [NOT NULL?]
   - Motivo: [por que precisa]
2. [Outra mudança se necessário]

RLS: [Manter policies existentes / Adicionar policy pra nova coluna]

Uso:
- [Componente X] vai mostrar [novo campo]
- [Formulário Y] vai permitir editar [novo campo]

Constraints:
- NÃO remover colunas existentes
- NÃO alterar tipos de colunas existentes
- Dados existentes devem ter default pra nova coluna
```

---

## Template 3: RLS Policy

```
Plan: [Criar/alterar] RLS policy na tabela [nome_tabela].

Contexto atual:
- Tabela [nome_tabela] tem [descrever policies atuais ou "nenhuma policy"]
- Problema: [descrever o gap de segurança ou requisito]

Policy desejada:
- Nome: [policy_name]
- Operação: [SELECT/INSERT/UPDATE/DELETE]
- Condição: [descrever quem pode fazer o quê]
  - Exemplo: "Apenas o dono (user_id = auth.uid()) pode SELECT seus registros"
  - Exemplo: "Admin (role = 'admin' em profiles) pode SELECT todos"

Uso: [por que essa policy é necessária — qual cenário de negócio]

Constraints:
- NÃO alterar policies existentes que funcionam
- Usar (select auth.uid()) com parênteses pra performance
```

---

## Template 4: Edge Function

```
Plan: Criar edge function [nome_function] para [objetivo].

O que a function recebe:
- Método: [POST/GET]
- Body: { [campo1]: [tipo], [campo2]: [tipo] }
- Headers: [Authorization bearer token / API key / nenhum]

O que a function faz:
1. [Passo 1 — ex: validar input]
2. [Passo 2 — ex: chamar API externa X]
3. [Passo 3 — ex: salvar resultado na tabela Y]

O que a function retorna:
- Sucesso: { [shape do response] }
- Erro: { error: string }

Segurança:
- [Requer auth / API key / público]
- [Rate limiting se necessário]

Constraints:
- NÃO criar novas tabelas — usar [tabela existente]
- Edge function NÃO deve ter lógica de UI
```

---

## Template 5: Storage Policy

```
Plan: Configurar storage bucket [nome_bucket] para [objetivo].

Bucket:
- Nome: [nome_bucket]
- Público: [sim/não]
- Tamanho máximo: [ex: 5MB]
- Tipos permitidos: [ex: image/png, image/jpeg, application/pdf]

Policies:
- Upload: [quem pode — ex: usuários autenticados, apenas pro próprio user_id]
- Download: [quem pode — ex: público / apenas dono / membros do mesmo team]
- Delete: [quem pode — ex: apenas dono]

Uso:
- [Componente] vai permitir upload de [tipo de arquivo]
- [Página] vai exibir [arquivos] do bucket

Constraints:
- NÃO alterar buckets existentes: [listar]
```

---

## Template 6: Mudança Mista (Banco + Frontend)

Quando a mudança envolve tanto schema quanto UI. Gerar UM prompt que cobre tudo pra manter sincronia.

```
Plan: [Objetivo que envolve banco + UI].

1. Banco:
   - [Mudanças de schema — usar templates acima]
   - [RLS se necessário]

2. Frontend:
   - [Componente/página que precisa ser criado/alterado]
   - [Como usa os novos dados]
   - [Estados: empty, loading, filled, error]

3. Integração:
   - [Como frontend conecta com os novos dados via supabase client]

Constraints:
- [O que não alterar]
- [Limitar escopo — máximo 3-4 mudanças totais]
```

---

## Prompt Sequencial (quando precisa de mais de 4 mudanças)

Se o escopo excede 4 mudanças, quebre em prompts sequenciais:

```
Prompt 1: "Plan: Criar tabelas X e Y com RLS básico"
  → Esperar Lovable aplicar → Verificar

Prompt 2: "Plan: Adicionar edge function Z que usa tabelas X e Y"
  → Esperar Lovable aplicar → Verificar

Prompt 3: "Plan: Criar página que consome dados de X e Y via function Z"
  → Esperar Lovable aplicar → Verificar
```

Ordem: schema → functions → frontend. Cada prompt referencia o que o anterior criou.

---

## Refinamento (quando Lovable erra)

Se o Lovable não aplicou corretamente:

```
A mudança anterior [criou/alterou] [o que], mas:
- [Problema 1: ex: "RLS policy está faltando na tabela X"]
- [Problema 2: ex: "Coluna Y foi criada como text, deveria ser integer"]

Corrija:
1. [Correção específica 1]
2. [Correção específica 2]

NÃO altere nada além do que foi listado acima.
```

Seja explícito sobre o erro e a correção. Lovable tende a "melhorar" coisas quando o prompt é vago.
