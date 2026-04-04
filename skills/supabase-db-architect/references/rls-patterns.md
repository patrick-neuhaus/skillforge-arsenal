# Padrões de RLS — Referência completa

## Os dois caminhos de acesso

**Client-side (Lovable, apps frontend)** → Usa key `anon`/`sb_publishable_*` ou `authenticated` → RLS APLICADO → Toda query filtrada por policies.

**Server-side (n8n, Edge Functions, cron jobs)** → Usa key `service_role`/`sb_secret_*` → RLS BYPASSADO → Acesso total.

---

## Padrão 1: Dados do usuário (mais comum)

```sql
CREATE TABLE public.leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT,
  status TEXT DEFAULT 'new',
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

ALTER TABLE public.leads ENABLE ROW LEVEL SECURITY;

-- SEMPRE use (select auth.uid()) com parênteses pra caching
CREATE POLICY "Users manage own leads" ON public.leads
  FOR ALL
  USING ((select auth.uid()) = user_id)
  WITH CHECK ((select auth.uid()) = user_id);

-- Index pra performance da RLS policy
CREATE INDEX idx_leads_user_id ON public.leads(user_id);
```

## Padrão 2: Multi-tenancy por organização

```sql
CREATE TABLE public.organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE TABLE public.organization_members (
  organization_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  role TEXT NOT NULL DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member', 'viewer')),
  PRIMARY KEY (organization_id, user_id)
);

-- Index crucial pra performance das subqueries RLS
CREATE INDEX idx_org_members_user ON public.organization_members(user_id);

CREATE TABLE public.campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  status TEXT DEFAULT 'draft',
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

ALTER TABLE public.campaigns ENABLE ROW LEVEL SECURITY;

-- Membros veem campanhas da sua org
CREATE POLICY "Org members see campaigns" ON public.campaigns
  FOR SELECT
  USING (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
    )
  );

-- Admins e owners podem modificar
CREATE POLICY "Org admins manage campaigns" ON public.campaigns
  FOR ALL
  USING (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
      AND role IN ('owner', 'admin')
    )
  )
  WITH CHECK (
    organization_id IN (
      SELECT organization_id FROM public.organization_members
      WHERE user_id = (select auth.uid())
      AND role IN ('owner', 'admin')
    )
  );
```

## Padrão 3: Tabelas server-only (n8n)

```sql
CREATE TABLE public.follow_up_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue_item_id UUID NOT NULL,
  status TEXT NOT NULL,
  error_message TEXT,
  created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Habilite RLS como rede de segurança, mesmo sem policies
-- Se alguém acidentalmente consultar com anon key, não vê nada
ALTER TABLE public.follow_up_logs ENABLE ROW LEVEL SECURITY;
```

## Padrão 4: JWT custom claims + MFA enforcement

```sql
-- Acesso baseado em role via app_metadata
CREATE POLICY "Admins have full access" ON public.settings
  FOR ALL
  USING (
    (select auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
  );

-- Exigir MFA (AAL2) pra operações sensíveis
CREATE POLICY "MFA required for billing" ON public.billing
  FOR ALL
  USING (
    (select auth.jwt() ->> 'aal') = 'aal2'
    AND (select auth.uid()) = user_id
  );
```

## Padrão 5: Dados públicos com escrita restrita

```sql
-- Todos leem, só dono escreve
CREATE POLICY "Public read" ON public.articles
  FOR SELECT
  USING (published = true);

CREATE POLICY "Owner manages" ON public.articles
  FOR ALL
  USING ((select auth.uid()) = author_id)
  WITH CHECK ((select auth.uid()) = author_id);
```

---

## Dicas de performance de RLS

1. **SEMPRE** use `(select auth.uid())` e `(select auth.jwt())` com parênteses — habilita initPlan caching (até 100x+ melhoria)
2. Indexe colunas usadas em subqueries de RLS (`user_id`, `organization_id`)
3. Evite JOINs complexos em policies — rodam em cada checagem de linha
4. Pra dados acessados frequentemente, considere `security_definer` function que cache membership
5. Teste policies manualmente:
   ```sql
   SET ROLE authenticated;
   SET request.jwt.claims = '{"sub": "user-uuid-aqui"}';
   SELECT * FROM tabela; -- deve retornar só dados do usuário
   RESET ROLE;
   ```

## Checklist de RLS

- [ ] Toda tabela exposta ao client tem RLS habilitado
- [ ] Tabelas server-only tem RLS habilitado sem policies (deny-all)
- [ ] Nenhuma policy usa `USING (true)` sem justificativa documentada
- [ ] Toda policy usa `(select auth.uid())` com parênteses (não `auth.uid()` direto)
- [ ] Indexes existem nas colunas filtradas por RLS
- [ ] Policies cobrem todas as operações necessárias (SELECT, INSERT, UPDATE, DELETE)
- [ ] Testado com `SET ROLE` simulando diferentes usuários
