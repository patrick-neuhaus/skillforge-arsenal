# Import Workflow — Processo e Repos Curados

Consulte este arquivo no **Step 1** para encontrar repos de referencia e no **Step 2** para o processo de clone.

---

## Repos Curados por Dominio

### Auth & Users
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `steven-tey/dub` | Auth com NextAuth + Prisma, RBAC | Next.js 14, Prisma |
| `calcom/cal.com` | Multi-tenancy, team management | Next.js, Prisma |
| `supabase/supabase` | Auth com Supabase, RLS patterns | Next.js, Supabase |

### Rich Text Editor
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `steven-tey/novel` | TipTap editor minimalista | React, TipTap |
| `facebook/lexical` | Editor framework extensivel | React, Lexical |

### Dashboard & Admin
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `shadcn-ui/taxonomy` | App completo com shadcn | Next.js, shadcn |
| `sadmann7/skateshop` | E-commerce com admin panel | Next.js, Drizzle |

### Landing Pages & Marketing
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `shadcn-ui/ui` | Componentes de referencia | React, Tailwind |
| `dubinc/dub` | Landing page otimizada | Next.js, Tailwind |

### Automacao & Workflows
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `n8n-io/n8n` | Workflow engine, node system | Node.js, Vue |
| `triggerdotdev/trigger.dev` | Background jobs, event-driven | Next.js, Prisma |

### Real-time & Collaboration
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `liveblocks/liveblocks` | Real-time collaboration | React |
| `supabase/realtime` | Postgres changes via websocket | Elixir, Phoenix |

### File Upload & Media
| Repo | O que exemplifica | Stack |
|------|------------------|-------|
| `uploadthing/uploadthing` | File upload simplificado | Next.js |
| `remotion-dev/remotion` | Video programatico em React | React |

## Processo de Clone Otimizado

### Escolhendo o que Clonar

Nem sempre precisa do repo inteiro. Identifique:

```
1. Qual feature/padrao quer estudar?
   → Mapear pra pastas especificas

2. Exemplo: "Quero ver como novel faz o editor"
   → Preciso de: packages/core/src/ + packages/web/components/editor/
   → NAO preciso de: docs/, apps/web/app/, tests/

3. Estimar tamanho:
   → 3-5 arquivos relevantes = clone parcial (curl/degit)
   → 10+ arquivos = clone shallow (git clone --depth 1)
```

### Comandos por Cenario

```bash
# Cenario 1: Poucos arquivos (< 5)
mkdir -p .tmp/reference
curl -sL "https://raw.githubusercontent.com/user/repo/main/path/file.ts" \
  > .tmp/reference/file.ts

# Cenario 2: Pasta especifica
npx degit user/repo/path/to/folder .tmp/reference

# Cenario 3: Repo inteiro (shallow)
git clone --depth 1 https://github.com/user/repo .tmp/reference
rm -rf .tmp/reference/.git

# Cenario 4: Branch especifica
git clone --depth 1 --branch v2 https://github.com/user/repo .tmp/reference
rm -rf .tmp/reference/.git
```

### Tempo Maximo

Regra: nao gaste mais que 15 minutos analisando. Se em 15min nao extraiu o padrao, ou o repo e complexo demais ou voce esta buscando a coisa errada.

## O que Extrair

### Checklist de Extracao

- [ ] **Estrutura de pastas** — como organizam o feature
- [ ] **Tipos/Interfaces** — contracts entre componentes
- [ ] **Composicao** — como componentes se encaixam (props, context, hooks)
- [ ] **Edge cases** — o que eles tratam que voce talvez nao pensou
- [ ] **Decisoes nao-obvias** — por que fizeram assim? (ler comments, commits)
- [ ] **Dependencias** — quais libs usam e por que

### O que NÃO Extrair

- Codigo literal (copiar e colar)
- Estilos/CSS especificos
- Configuracoes de CI/CD
- Testes (a menos que o padrao de teste seja o objetivo)
