# Scanning Strategies — Busca por Similaridade

Consulte este arquivo no **Step 2.2** para buscas alem de nome exato.

---

## Estrategia 1: Busca por Funcionalidade

Quando o nome nao ajuda, busque pelo que o codigo FAZ:

| Funcionalidade desejada | Grep patterns |
|------------------------|---------------|
| Formatacao de data | `format.*[Dd]ate\|date.*format\|toLocaleDateString` |
| Formatacao de moeda | `format.*[Cc]urrency\|toFixed\|Intl.NumberFormat` |
| Validacao de email | `email.*valid\|regex.*email\|\.email()` |
| Auth check | `isAuth\|checkAuth\|useAuth\|getUser\|getSession` |
| Fetch de dados | `use.*Query\|useSWR\|useEffect.*fetch\|server.*action` |
| Upload de arquivo | `upload\|formData\|multipart\|file.*input` |
| Paginacao | `page.*size\|offset\|limit\|cursor\|pagination` |
| Sorting | `sort\|order.*by\|orderBy\|sortBy` |
| Filtering | `filter\|where\|search\|query.*param` |
| Modal/Dialog | `[Mm]odal\|[Dd]ialog\|isOpen\|onClose\|overlay` |
| Toast/Notification | `toast\|notify\|alert\|snackbar\|notification` |

## Estrategia 2: Busca por Assinatura

Buscar funcoes com assinaturas similares:

```bash
# Funcoes que recebem e retornam o mesmo tipo
grep -rn "function.*string.*:.*string\|=>.*string" src/lib/ src/utils/

# Hooks com mesmo padrao de retorno
grep -rn "return \[.*set" src/hooks/ --include="*.ts" --include="*.tsx"

# Components com props similares
grep -rn "interface.*Props" src/components/ --include="*.tsx" | grep -i "keyword"
```

## Estrategia 3: Busca por Imports

Quem importa o que — revela o que ja e reutilizado:

```bash
# Top 10 mais importados (ja sao reutilizaveis)
grep -rn "from '@/" src/ --include="*.ts" --include="*.tsx" |
  sed "s/.*from '\(.*\)'.*/\1/" | sort | uniq -c | sort -rn | head -10

# Quem importa um modulo especifico
grep -rn "from.*moduleName" src/ --include="*.ts" --include="*.tsx"
```

## Estrategia 4: Busca no Design System

### shadcn/ui
```bash
# Componentes ja instalados
ls src/components/ui/ 2>/dev/null

# Componentes disponiveis mas nao instalados
npx shadcn@latest add --list 2>/dev/null
```

### Verificar registry completo
Antes de criar qualquer componente UI, checar se shadcn tem:
- Accordion, Alert, Avatar, Badge, Button, Calendar, Card, Checkbox
- Combobox, Command, DataTable, DatePicker, Dialog, Drawer
- DropdownMenu, Form, HoverCard, Input, Label, Menubar
- NavigationMenu, Popover, Progress, RadioGroup, ScrollArea
- Select, Separator, Sheet, Skeleton, Slider, Switch
- Table, Tabs, Textarea, Toast, Toggle, Tooltip

## Estrategia 5: Busca em Dependencias

```bash
# Listar todas as dependencias instaladas
cat package.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for k in sorted({**d.get('dependencies',{}), **d.get('devDependencies',{})}.keys()):
    print(k)
" 2>/dev/null || cat package.json | grep -A 100 '"dependencies"' | grep '"' | head -30

# Checar se uma lib especifica esta instalada
grep '"lib-name"' package.json
```

### Libs comuns que ja resolvem problemas

| Problema | Lib que provavelmente ja esta instalada |
|----------|----------------------------------------|
| Datas | date-fns, dayjs, luxon |
| Validacao | zod, yup, valibot |
| HTTP | axios, ky (ou fetch nativo) |
| Estado global | zustand, jotai, Redux |
| Estado server | @tanstack/react-query, swr |
| Animacao | framer-motion, motion |
| Forms | react-hook-form, formik |
| Icons | lucide-react, @heroicons/react |
| Tabelas | @tanstack/react-table |
| Charts | recharts, visx |
| Rich text | tiptap, lexical |
| DnD | @dnd-kit, react-beautiful-dnd |
