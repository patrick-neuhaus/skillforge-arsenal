Patrick:

Cara, tanto no na pasta ali do, do disco c, quanto na pasta do Git, Hub. Do disco d, Você tem alguma memória? Inclusive alguma memória geral? Porque eu queria te perguntar o quê? Eu queria deixar 1 template no. L o VVABLE, que ele sirva pra todos os projetos. Então o que que teria que ter num projeto, pra deixar fixo, sei lá, sistema de login básico? 1, não sei. O que que eu consigo generalizar pra qualquer tipo de projeto. Que eu consigo deixar fixo no, pra eu só remixar ele, conectar no GitHub, e alterar com. Para ter o mínimo de gasto com crédito. Sacou? Entendeu a minha pergunta?

---

Claude:

Deixa eu checar as memórias primeiro.

Leu 3 arquivos, pesquisou 2 padrões
Leu 3 arquivos, pesquisou 2 padrões
Read
C:\Users\Patrick Neuhaus\.claude\projects\C--Users-Patrick-Neuhaus-Documents-Github\memory\MEMORY.md
File does not exist. Note: your current working directory is C:\Users\Patrick Neuhaus\Documents\Github.
Glob
*.md
No files found
Glob
*.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\references_ocr_technical_drawings.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\user_skills_interest.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\feedback_portuguese_always.md
Mostrar menos
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\user_profile_patrick.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\project_artemis_seo.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\project_copy_skill.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\feedback_skills_self_use.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\feedback_n8n_set_node_parse.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\project_skillforge_arsenal.md
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\MEMORY.md
Read
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\MEMORY.md
Ler 20 linhas
Read
C:\Users\Patrick Neuhaus\.claude\projects\D--DOCUMENTOS-Github\memory\user_profile_patrick.md
Ler 17 linhas
Mostrar menos

**Memórias:** no disco D (DOCUMENTOS/Github) tenho 10 memórias — teu perfil, feedbacks, projetos (Artemis SEO, skillforge-arsenal, copy skill), referências. No disco C (Documents/Github) não tenho nenhuma ainda — é a primeira sessão nesse working directory.

---

Agora, sobre o template Lovable universal. Entendi a ideia: um projeto-base que tu remixa, conecta no GitHub, e sai customizando — gastando crédito só no que é específico do cliente, não no boilerplate.

Aqui o que faz sentido fixar num template, dividido por camada:

### Auth & Segurança (o que tu já mencionou)
- **Supabase Auth completo** — login email/senha, magic link, OAuth (Google no mínimo), reset de senha
- **Proteção de rotas** — wrapper de rota autenticada, redirect pra login
- **RLS policies base** — `auth.uid() = user_id` nos patterns mais comuns (own-data, admin-bypass)
- **Perfil de usuário** — tabela `profiles` com trigger on_auth_user_created, avatar, nome

### Layout & Navegação
- **Shell da app** — sidebar colapsável + header + área de conteúdo (responsivo)
- **Páginas esqueleto** — Login, Register, Forgot Password, Dashboard (vazia), Settings/Profile, 404
- **Navegação tipada** — config de menu centralizada (fácil de customizar por projeto)

### Design System
- **shadcn/ui já configurado** — com tema customizável via CSS variables (troca cores do cliente em 1 arquivo)
- **Dark mode** toggle pronto
- **Toast/sonner** pra feedback
- **Loading states** — skeletons, spinners padronizados

### Infraestrutura de código
- **Supabase client** — singleton configurado, types gerados
- **React Query (TanStack Query)** — já wired com Supabase pra cache/invalidation
- **Estrutura de pastas** — `pages/`, `components/`, `hooks/`, `lib/`, `types/` — consistente
- **Error boundary** global

### Coisas que parecem boas mas **não** fixaria no template
- **Schema de banco específico** (além de profiles) — cada projeto tem domínio diferente, não generaliza
- **Integrações externas** (Stripe, n8n webhooks) — variam demais, melhor adicionar por projeto
- **RBAC complexo** (roles, permissions table) — nem todo projeto precisa, e quando precisa o modelo varia
- **Landing page** — cada cliente tem copy/design diferente, não economiza crédito

### O que mais economiza crédito Lovable

O auth + layout + design system são os campeões. Só o fluxo de auth (login, register, forgot password, proteção de rota, perfil) consome fácil 30-40% dos créditos de um projeto novo no Lovable. Se já vem pronto, tu usa crédito só pra:
1. Schema do domínio específico
2. Páginas de funcionalidade
3. Integrações

---

Quer que eu monte isso de fato? Posso detalhar o schema base (profiles + RLS), a estrutura de pastas, e os componentes — ou tu prefere alinhar com o Willy antes, já que é uma decisão que afeta o padrão de todos os projetos futuros?

---

Patrick: 

Seria bom alinhar com ele, mas ao mesmo tempo, já criar e mostrar pra ele, né? Então, tem como você fazer 1 pra mim? Pra eu enviar para o contendo ali o mínimo que você imagina, que daí além de criar isso, eu já conecto o GitHub e você já dá 1 olhada que eu já puxo aqui. O repositório e já mostro pro pro Willie já.

---

Claude:

Bora. Vou criar o template completo — tu remixa no Lovable, conecta o GitHub, e puxa aqui pra eu olhar.

Vou paralelizar com 3 agents escrevendo simultaneamente.

Create config and core files
Create config and core files
Agent
Create config and core files
All 18 files created successfully at `C:/Users/Patrick Neuhaus/Documents/Github/lovable-template/`. The `index.html` is visible in the preview panel.
Here is the complete file list:
Mostrar menos
**Root config files (9):**
- `package.json` -- dependencies and scripts
- `vite.config.ts` -- Vite with SWC React plugin, `@` alias, port 8080
- `tsconfig.json`, `tsconfig.app.json`, `tsconfig.node.json` -- TypeScript configs with path aliases
- `tailwind.config.ts` -- shadcn/ui theme with CSS variables and sidebar colors
- `postcss.config.js` -- PostCSS with Tailwind + Autoprefixer
- `components.json` -- shadcn/ui configuration
- `index.html` -- entry HTML (pt-BR)
**Environment (1):**
- `.env.example` -- Supabase URL and anon key placeholders
**Source files (7):**
- `src/main.tsx` -- React entry point
- `src/App.tsx` -- App with React Query, Router, Auth, Toaster, protected routes
- `src/index.css` -- Tailwind base with light/dark CSS variables
- `src/vite-env.d.ts` -- Vite type reference
- `src/lib/utils.ts` -- `cn()` utility (clsx + tailwind-merge)
- `src/integrations/supabase/client.ts` -- typed Supabase client
- `src/integrations/supabase/types.ts` -- Database types with profiles table
**Migration (1):**
- `supabase/migrations/00001_create_profiles.sql` -- profiles table with RLS and auto-create trigger
Note: `App.tsx` imports components that don't exist yet (`AuthProvider`, `ProtectedRoute`, `AppLayout`, page components, `sonner`). These are the stub directories created and ready to be populated -- `src/contexts/`, `src/components/layout/`, `src/components/ui/`, `src/pages/`, `src/hooks/`.
agentId: a0be89ca10e145492 (use SendMessage with to: 'a0be89ca10e145492' to continue this agent)
<usage>total_tokens: 42562
tool_uses: 20
duration_ms: 140349</usage>


---

Patrick:

ta usando skill?

---

Claude:

Create UI components batch
Create UI components batch
Agent
Create UI components batch
All 9 shadcn/ui component files written to `C:/Users/Patrick Neuhaus/Documents/Github/lovable-template/src/components/ui/`:
1. **button.tsx** - Button with variants (default, destructive, outline, secondary, ghost, link) and sizes (default, sm, lg, icon)
Mostrar menos
2. **input.tsx** - Input with standard styling and file input support
3. **label.tsx** - Label using @radix-ui/react-label
4. **card.tsx** - Card with Header, Title, Description, Content, Footer sub-components
5. **avatar.tsx** - Avatar with Image and Fallback using @radix-ui/react-avatar
6. **dropdown-menu.tsx** - Full dropdown menu with Sub, Content, Item, Label, Separator using @radix-ui/react-dropdown-menu
7. **separator.tsx** - Horizontal/vertical separator using @radix-ui/react-separator
8. **skeleton.tsx** - Skeleton loading placeholder with pulse animation
9. **sonner.tsx** - Toast notifications wrapper using sonner library
agentId: a77c0a341c28330bb (use SendMessage with to: 'a77c0a341c28330bb' to continue this agent)
<usage>total_tokens: 39660
tool_uses: 11
duration_ms: 82537</usage>

Não, tô escrevendo direto. Isso aqui é criação de boilerplate puro — não tem skill que cubra "gerar template Lovable do zero". As skills de Lovable (lovable-router, lovable-knowledge) são pra quando tu já tá dentro de um projeto existente.

Agora falta o último batch — auth, layout e páginas. Criando agora.

Create auth layout and pages
Create auth layout and pages
Agent
Create auth layout and pages
All 15 files written successfully to `C:/Users/Patrick Neuhaus/Documents/Github/lovable-template/`. Here is the structure created:
- `src/contexts/AuthContext.tsx` -- AuthProvider + useAuth hook (Supabase auth)
Mostrar menos
- `src/components/auth/LoginForm.tsx` -- Login card with email/password
- `src/components/auth/RegisterForm.tsx` -- Registration card with name/email/password
- `src/components/auth/ForgotPasswordForm.tsx` -- Password recovery with sent state
- `src/components/layout/ProtectedRoute.tsx` -- Route guard with loading spinner
- `src/components/layout/AppLayout.tsx` -- Shell with sidebar + header + outlet
- `src/components/layout/AppSidebar.tsx` -- Collapsible sidebar with NavLink items
- `src/components/layout/Header.tsx` -- Top bar with hamburger + user dropdown
- `src/pages/Login.tsx` -- Login page (redirects if authenticated)
- `src/pages/Register.tsx` -- Register page (redirects if authenticated)
- `src/pages/ForgotPassword.tsx` -- Forgot password page (redirects if authenticated)
- `src/pages/ResetPassword.tsx` -- Reset password page with confirmation
- `src/pages/Dashboard.tsx` -- Dashboard with welcome card
- `src/pages/Settings.tsx` -- Profile update + account info
- `src/pages/NotFound.tsx` -- 404 page
agentId: af49f2d618c64bdff (use SendMessage with to: 'af49f2d618c64bdff' to continue this agent)
<usage>total_tokens: 45463
tool_uses: 16
duration_ms: 82710</usage>

Template completo. Agora vou inicializar o Git e adicionar `.gitignore`.

Criou um arquivo, executou um comando
Criou um arquivo, executou um comando
Write
C:/Users/Patrick Neuhaus/Documents/Github/lovable-template/.gitignore
Bash
cd "C:/Users/Patrick Neuhaus/Documents/Github/lovable-template" && git init && git add -A && git status
Initialized empty Git repository in C:/Users/Patrick Neuhaus/Documents/Github/lovable-template/.git/
warning: in the working copy of '.env.example', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
Mostrar menos
warning: in the working copy of 'components.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'package.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'postcss.config.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/App.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/auth/ForgotPasswordForm.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/auth/LoginForm.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/auth/RegisterForm.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/layout/AppLayout.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/layout/AppSidebar.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/layout/Header.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/layout/ProtectedRoute.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/avatar.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/button.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/card.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/dropdown-menu.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/input.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/label.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/separator.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/skeleton.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/components/ui/sonner.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/contexts/AuthContext.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/index.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/integrations/supabase/client.ts', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/integrations/supabase/types.ts', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/lib/utils.ts', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/main.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/Dashboard.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/ForgotPassword.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/Login.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/NotFound.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/Register.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/ResetPassword.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/pages/Settings.tsx', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'supabase/migrations/00001_create_profiles.sql', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tailwind.config.ts', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tsconfig.app.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tsconfig.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tsconfig.node.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'vite.config.ts', LF will be replaced by CRLF the next time Git touches it
On branch master
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .env.example
	new file:   .gitignore
	new file:   components.json
	new file:   index.html
	new file:   package.json
	new file:   postcss.config.js
	new file:   src/App.tsx
	new file:   src/components/auth/ForgotPasswordForm.tsx
	new file:   src/components/auth/LoginForm.tsx
	new file:   src/components/auth/RegisterForm.tsx
	new file:   src/components/layout/AppLayout.tsx
	new file:   src/components/layout/AppSidebar.tsx
	new file:   src/components/layout/Header.tsx
	new file:   src/components/layout/ProtectedRoute.tsx
	new file:   src/components/ui/avatar.tsx
	new file:   src/components/ui/button.tsx
	new file:   src/components/ui/card.tsx
	new file:   src/components/ui/dropdown-menu.tsx
	new file:   src/components/ui/input.tsx
	new file:   src/components/ui/label.tsx
	new file:   src/components/ui/separator.tsx
	new file:   src/components/ui/skeleton.tsx
	new file:   src/components/ui/sonner.tsx
	new file:   src/contexts/AuthContext.tsx
	new file:   src/index.css
	new file:   src/integrations/supabase/client.ts
	new file:   src/integrations/supabase/types.ts
	new file:   src/lib/utils.ts
	new file:   src/main.tsx
	new file:   src/pages/Dashboard.tsx
	new file:   src/pages/ForgotPassword.tsx
	new file:   src/pages/Login.tsx
	new file:   src/pages/NotFound.tsx
	new file:   src/pages/Register.tsx
	new file:   src/pages/ResetPassword.tsx
	new file:   src/pages/Settings.tsx
	new file:   src/vite-env.d.ts
	new file:   supabase/migrations/00001_create_profiles.sql
	new file:   tailwind.config.ts
	new file:   tsconfig.app.json
	new file:   tsconfig.json
	new file:   tsconfig.node.json
	new file:   vite.config.ts
[rerun: b1]

Pronto. **42 arquivos**, tudo staged. Aqui o resumo do que ficou no template:

### Estrutura
```
lovable-template/
├── .env.example              # Supabase URL + anon key
├── package.json              # Vite + React + shadcn + Supabase + TanStack Query
├── vite/ts/tailwind configs  # Tudo configurado com path alias @/
├── components.json           # shadcn/ui config
├── supabase/
│   └── migrations/
│       └── 00001_create_profiles.sql  # profiles + RLS + trigger auto-create
└── src/
    ├── contexts/AuthContext.tsx        # signIn, signUp, signOut, reset, update
    ├── integrations/supabase/         # client tipado + types da DB
    ├── components/
    │   ├── auth/    (LoginForm, RegisterForm, ForgotPasswordForm)
    │   ├── layout/  (AppLayout, AppSidebar, Header, ProtectedRoute)
    │   └── ui/      (9 componentes shadcn: button, input, label, card, avatar, dropdown-menu, separator, skeleton, sonner)
    ├── pages/       (Login, Register, ForgotPassword, ResetPassword, Dashboard, Settings, NotFound)
    └── lib/utils.ts (cn helper)
```

### O que tu economiza ao remixar
- **Auth completo** (login, registro, forgot/reset password, proteção de rota) — isso sozinho come ~30-40% dos créditos num projeto novo
- **Layout com sidebar colapsável + header com dropdown do usuário**
- **Settings com update de perfil** (synca auth metadata + tabela profiles)
- **Design system** com CSS variables — troca as cores do cliente em 1 lugar (`src/index.css`)
- **Migration SQL** com RLS pronta

### Próximo passo
Cria o repo no GitHub, eu faço o push, e tu remixa no Lovable. Quer que eu crie o repo agora via `gh`?

Quer que eu crie o repo no GitHub e faça o push? Aí tu já importa no Lovable direto.

---

Patrick:

nao cara, quero que vc monte um prompt para mim para eu enviar isso para o lovable, nao ficou claro iusso? por isso falei sobre skill cara

dai ele cria esse de modelo, clono ele, vc verifica com o que vc fez ja que vc ja fez mesmo, e ai me fala o que achou, pode ser?

---

Claude:

Ah, entendi errado. Tu quer o **prompt pro Lovable criar o projeto**, não o código em si. Faz total sentido — o Lovable gera melhor que código manual e tu economiza ajustando via prompt ao invés de escrevendo.

Vou montar o prompt. O que eu já criei serve de benchmark pra quando tu clonar e eu comparar.

---

Aqui o prompt pra colar no Lovable:

---

**Cria um template base de aplicação web com as seguintes especificações:**

**Stack:** React + TypeScript + Vite + Tailwind CSS + shadcn/ui + Supabase + TanStack React Query + React Router v6

**Autenticação completa com Supabase Auth:**
- Páginas: Login, Registro (nome + email + senha), Esqueci minha senha, Redefinir senha
- AuthContext com provider que expõe: user, session, loading, signIn, signUp, signOut, resetPassword, updatePassword
- Proteção de rotas: componente ProtectedRoute que redireciona pra /login se não autenticado, com loading spinner
- Páginas de auth redirecionam pra / se já logado
- Todas as páginas de auth centralizadas na tela com Card do shadcn

**Tabela profiles no Supabase:**
- Campos: id (uuid, FK pra auth.users), full_name, avatar_url, updated_at, created_at
- RLS habilitado: usuário só vê e edita o próprio perfil
- Trigger que cria profile automaticamente no signup usando raw_user_meta_data (full_name e avatar_url)

**Layout da aplicação (rotas protegidas):**
- Sidebar colapsável à esquerda com navegação via NavLink (ícones do lucide-react). Items: Dashboard e Configurações
- Header fixo no topo com botão hamburger pra toggle da sidebar e dropdown do usuário no canto direito (avatar com iniciais, menu com "Configurações" e "Sair")
- Área de conteúdo principal com scroll independente e padding

**Páginas internas:**
- Dashboard: título + grid de cards (1 card de boas-vindas mostrando nome do usuário)
- Configurações: form pra atualizar nome completo (synca auth.updateUser + tabela profiles), campo email desabilitado, card separado mostrando data de criação da conta
- 404: página simples com botão pra voltar ao início

**Design:**
- Tema neutro com CSS variables (light e dark mode configurados)
- Cores de sidebar separadas (sidebar-background, sidebar-foreground, sidebar-accent, etc.)
- Toasts via sonner pra feedback de todas as ações (login, registro, erro, update de perfil)
- Textos da interface em português brasileiro

**Estrutura de código:**
- Separar: components/auth/, components/layout/, components/ui/, contexts/, pages/, integrations/supabase/, lib/
- Supabase client tipado com Database types incluindo a tabela profiles
- Formulários com useState simples (sem react-hook-form)

**NÃO incluir:** landing page, RBAC/roles, integração com Stripe ou APIs externas, i18n. Isso é um template base pra ser customizado por projeto.

---

Cola isso no Lovable, ele vai gerar o projeto. Depois clona e me avisa que eu comparo com o que montei aqui.

---

Patrick: 

e vc usou a skill do prompt engineer?

---

Claude:

Não, furei. Tu tá certo — prompt pra LLM (Lovable é LLM) cai direto no trigger de prompt-engineer. Vou rodar agora pra validar e melhorar o que montei.

Usou uma habilidade, executou um agent
Usou uma habilidade, executou um agent
Skill
Launching skill: anthropic-skills:prompt-engineer
Agent
Load prompt-engineer references
Perfect! I've successfully found and read all three reference files. Here's what I found:
## Summary of Files Found
Mostrar menos
### 1. **Rubric: system-prompt.yaml**
**Location:** `rubric/system-prompt.yaml`
This is a promptfoo validation rubric for system prompts with a production threshold of 75/100. It contains three tiers of criteria:
- **Core Criteria (weights 85-100):** R001-R004 covering role/context, output format, specific instructions, and edge case handling
- **Useful Criteria (weights 60-70):** R005-R006 covering few-shot examples and anti-patterns
- **Claude 4.x Calibration (weights 50-80):** C001-C003 addressing caps lock control, deprecated prefilling patterns, and KV cache strategy
- **Universal Criteria (weights 60-70):** U001-U002 for tool management and attention budget
Each criterion has specific scoring rubrics (e.g., Role specificity: specific+context=100, generic=50, none=0).
### 2. **System Prompts Reference: system-prompts.md**
**Location:** `references/system-prompts.md`
A practical guide for creating effective system prompts for agents and chatbots. Key sections:
- **Anatomy:** Five mandatory blocks in order: Role, Context, Instructions, Constraints, Output format
- **Complete template** showing the XML structure
- **Quality checklist** with 8 items (role in 1-2 lines, context completeness, instruction coverage, fallbacks, positive phrasing, etc.)
- **Anti-patterns** showing common mistakes with examples
- **Security considerations** (OWASP LLM) including prompt injection, leakage, excessive agency, and PII disclosure
### 3. **Create-Criteria Reference: create-criteria.md**
**Location:** `references/create-criteria.md`
Universal criteria applicable to any new prompt in `--create` mode (not type-specific). Contains:
- **9-criterion checklist** as a table with questions and red flags
- **Application guide:** read type-specific reference → use checklist during drafting → validate against criteria → fix red flags
- **Rationale:** explains why these 9 criteria cover the most common failure modes in production prompts
All three files are in your skill directory and ready to use for prompt validation and creation workflows.

Rodei a validação contra a rubric `system-prompt.yaml`. Aqui o resultado:

---

## Validation: Lovable Template Prompt
Type: system-prompt (prompt pra LLM code-gen)
Score: **62/100** [APPROVED WITH RESERVATIONS]
Threshold: 75 (production)

### Findings P0 (bloqueia)
- **R001 — Sem role/contexto.** O prompt pula direto pras specs sem dizer pro Lovable O QUE ele tá construindo e POR QUÊ. "Template base" aparece, mas sem contexto de reuso (remix, clonar, customizar por cliente). Lovable vai tratar como projeto final, não template.
- **R002 — Sem formato de output.** Não diz que quer migration SQL separada, que quer estrutura de pastas específica, que quer código limpo sem features hardcoded.

### Findings P1 (corrigir se possível)
- **R004 — Sem edge cases / fallbacks.** O que o Lovable faz se não souber algo? Não tem instrução de "na dúvida, mantenha simples".
- **R005 — Zero exemplos.** Nenhum input/output example. Pelo menos mostrar como o sidebar deve se comportar (colapsado = só ícones, expandido = ícone + label).
- **Excesso de HOW, falta de WHAT.** "AuthContext com provider que expõe: user, session, loading, signIn, signUp, signOut, resetPassword, updatePassword" — isso é implementação, não requisito. Lovable gera melhor quando tu diz O QUE quer, não COMO implementar.

### Findings P2 (melhoria)
- **U002 — Attention budget.** Tudo parece igualmente importante. Falta prioridade (auth é o core, layout é segundo, design é terceiro).
- Mistura PT-BR com termos técnicos em inglês sem consistência.

---

## Prompt melhorado

Apliquei os fixes de P0 e P1:

---

**Contexto:** Estou criando um template base que vou reusar em todos os meus projetos. A ideia é remixar esse projeto pra cada cliente novo — trocando apenas cores, nome e funcionalidades específicas do domínio. Tudo que é genérico (auth, layout, perfil) já vem pronto. Mantenha o código limpo e sem nada hardcoded que dificulte customização.

**Stack obrigatória:** React + TypeScript + Vite + Tailwind CSS + shadcn/ui + Supabase + TanStack React Query + React Router v6

**Prioridade 1 — Autenticação (Supabase Auth):**
- 4 páginas: Login, Registro, Esqueci minha senha, Redefinir senha
- Todas centralizadas na tela usando Card do shadcn
- Registro pede: nome completo, email, senha (mínimo 6 caracteres)
- Esqueci minha senha: envia magic link, mostra confirmação após envio
- Redefinir senha: 2 campos (nova senha + confirmação), valida se são iguais
- Se o usuário já está logado e acessa /login ou /register, redireciona pra /
- Rotas protegidas: se não logado, redireciona pra /login com loading spinner enquanto verifica sessão
- Criar um AuthContext que gerencia o estado de autenticação (user, session, loading) e expõe as funções de auth

**Prioridade 2 — Layout (rotas protegidas):**
- Sidebar à esquerda, colapsável. Expandida: ícone + texto. Colapsada: só ícone, centralizado
- 2 items de navegação: Dashboard (ícone LayoutDashboard) e Configurações (ícone Settings) — usar lucide-react
- Item ativo tem fundo destacado (usar cores de sidebar do tema)
- Header fixo no topo: botão hamburger à esquerda pra toggle do sidebar, avatar do usuário à direita com dropdown (Configurações + Sair)
- Avatar mostra iniciais do nome (ex: "Patrick Neuhaus" → "PN")
- Área de conteúdo com scroll independente e padding

**Prioridade 3 — Páginas internas:**
- Dashboard: título "Dashboard" + grid responsivo de cards. 1 card de boas-vindas mostrando o nome do usuário
- Configurações: formulário pra atualizar nome completo (salva tanto no auth metadata quanto na tabela profiles), campo de email readonly/desabilitado, card separado mostrando data de criação da conta formatada em pt-BR
- 404: "Página não encontrada" + botão "Voltar ao início"

**Prioridade 4 — Banco de dados (Supabase):**
- Tabela profiles: id (uuid, FK pra auth.users com cascade delete), full_name (text), avatar_url (text), updated_at (timestamptz), created_at (timestamptz)
- RLS: usuário só lê e edita o próprio registro
- Trigger on_auth_user_created que cria o profile automaticamente usando full_name e avatar_url do raw_user_meta_data do signup

**Design:**
- Tema neutro com CSS variables (light e dark mode). Cores facilmente trocáveis num único arquivo
- Cores de sidebar separadas das cores da app principal (sidebar-background, sidebar-foreground, sidebar-accent, etc.)
- Toast via sonner pra feedback de todas as ações (sucesso e erro)
- Todos os textos da interface em português brasileiro

**Estrutura de pastas:**
- components/auth/ (formulários), components/layout/ (sidebar, header, proteção de rota), components/ui/ (shadcn), contexts/ (AuthContext), pages/ (uma por rota), integrations/supabase/ (client + types), lib/ (utils)

**Restrições:**
- NÃO incluir: landing page, sistema de roles/RBAC, Stripe, APIs externas, i18n, react-hook-form
- Formulários com useState simples
- Na dúvida entre complexo e simples, escolha simples — esse é um ponto de partida, não produto final

---

Score estimado pós-fix: **~82/100**. Os P0 foram resolvidos (role/contexto + propósito de reuso). Os P1 principais também (priorização + "na dúvida, simples").

Cola esse no Lovable. Quando clonar, me avisa que eu comparo.