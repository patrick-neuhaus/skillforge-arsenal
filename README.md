# Skillforge Arsenal

Coleção pessoal de 40 skills para Claude Code — prompts especializados que transformam o Claude em ferramentas focadas para tarefas específicas.

## O que são Skills?

Skills são instruções estruturadas (em Markdown) que ensinam o Claude a executar tarefas complexas de forma consistente. Cada skill define um fluxo de trabalho, princípios, regras e outputs esperados.

## Skills disponíveis (40)

### Produto & Discovery
| Skill | Descrição |
|-------|-----------|
| [product-discovery-prd](skills/product-discovery-prd/) | Conduz discovery de produto e gera PRDs otimizados para Lovable e outras ferramentas |
| [product-marketing-context](skills/product-marketing-context/) | Cria e atualiza documento de contexto de marketing de produto (ICP, posicionamento, messaging) |
| [lovable-knowledge](skills/lovable-knowledge/) | Gera Workspace/Project Knowledge otimizados para configurar o Lovable |
| [lovable-router](skills/lovable-router/) | Classifica e roteia mudanças em projetos Lovable (código direto vs prompt Lovable) |
| [ux-audit](skills/ux-audit/) | Auditorias de UX/UI em apps web e mobile, baseadas em heurísticas |
| [ui-design-system](skills/ui-design-system/) | Gera design tokens e design.json completo (cores, tipografia, espaçamento, componentes) |

### Engenharia & Arquitetura
| Skill | Descrição |
|-------|-----------|
| [sdd](skills/sdd/) | Spec Driven Development — pipeline anti-vibecoding de 4 fases (research → spec → implement → review) |
| [n8n-architect](skills/n8n-architect/) | Arquitetura, construção, debug e otimização de automações n8n |
| [supabase-db-architect](skills/supabase-db-architect/) | Arquitetura de banco Supabase/PostgreSQL para apps de pequeno/médio porte |
| [component-architect](skills/component-architect/) | Planeja arquitetura de componentes com atomic design, composição e shadcn/ui |
| [react-patterns](skills/react-patterns/) | Audita e implementa padrões modernos React/Next.js (Server Components, App Router, Suspense) |
| [architecture-guard](skills/architecture-guard/) | Valida implementações contra regras arquiteturais e convenções do projeto |
| [pattern-importer](skills/pattern-importer/) | Clona repos de referência, analisa padrões e gera documentos de padrão (few-shot learning) |
| [cli-skill-wrapper](skills/cli-skill-wrapper/) | Transforma qualquer API em CLI tool otimizada para agentes de IA |
| [prompt-engineer](skills/prompt-engineer/) | Cria, valida e otimiza prompts para qualquer LLM |

### Code Review & Qualidade
| Skill | Descrição |
|-------|-----------|
| [trident](skills/trident/) | Pipeline de 3 agentes para code review profundo (Scan → Verify → Judge) |
| [code-dedup-scanner](skills/code-dedup-scanner/) | Escaneia codebase para encontrar componentes e padrões reutilizáveis antes de criar novo código |

### Segurança & Infraestrutura
| Skill | Descrição |
|-------|-----------|
| [security-audit](skills/security-audit/) | Pipeline de 3 agentes para auditoria de segurança (Code, VPS ou Web) |
| [vps-infra-audit](skills/vps-infra-audit/) | Pipeline de 3 agentes para auditoria de infraestrutura VPS |

### SEO & Marketing
| Skill | Descrição |
|-------|-----------|
| [seo](skills/seo/) | Audita, planeja e implementa estratégias de SEO completas (técnico, on-page, off-page, conteúdo) |
| [ai-seo](skills/ai-seo/) | Otimiza conteúdo para motores de busca com IA (AEO, GEO, LLMO) |
| [copy](skills/copy/) | Escreve, revisa e otimiza copy para 8 canais (landing, social, email, cold-email, WhatsApp, blog, UX, ads) |
| [competitor-alternatives](skills/competitor-alternatives/) | Cria páginas de comparação com concorrentes e alternativas para SEO e vendas |
| [site-architecture](skills/site-architecture/) | Planeja e reestrutura hierarquia de páginas, navegação, URLs e linking interno |
| [free-tool-strategy](skills/free-tool-strategy/) | Planeja e avalia ferramentas gratuitas para marketing (engineering as marketing) |
| [launch-strategy](skills/launch-strategy/) | Planeja lançamentos de produto, feature announcements e estratégia go-to-market |
| [sales-enablement](skills/sales-enablement/) | Cria colateral de vendas: pitch decks, one-pagers, objection handling, demo scripts |
| [geo-optimizer](skills/geo-optimizer/) | Otimiza descrições e metadados para Generative Engine Optimization (GEO) |

### Gestão & Comunicação
| Skill | Descrição |
|-------|-----------|
| [tech-lead-pm](skills/tech-lead-pm/) | Gestão de projetos e liderança técnica para líder de primeira viagem com equipe junior |
| [comunicacao-clientes](skills/comunicacao-clientes/) | Ensina a escrever melhor para clientes via WhatsApp/Telegram |

### Pesquisa & Conhecimento
| Skill | Descrição |
|-------|-----------|
| [reference-finder](skills/reference-finder/) | Fundamenta temas com referências consagradas: livros, frameworks, artigos |
| [skill-builder](skills/skill-builder/) | Cria, modifica e otimiza skills do Claude Code |
| [context-tree](skills/context-tree/) | Sistema hierárquico de gestão de conhecimento com scoring e decay |
| [context-guardian](skills/context-guardian/) | Monitora, analisa e gerencia uso da context window |

### Documentos & Arquivos
| Skill | Descrição |
|-------|-----------|
| [pdf](skills/pdf/) | Leitura, criação, merge, split e manipulação de PDFs |
| [docx](skills/docx/) | Cria, lê e edita documentos Word (.docx) |
| [pptx](skills/pptx/) | Cria, lê e edita apresentações PowerPoint (.pptx) |
| [xlsx](skills/xlsx/) | Cria, lê e edita planilhas (.xlsx, .csv, .tsv) |

### Orquestração & Utilidades
| Skill | Descrição |
|-------|-----------|
| [maestro](skills/maestro/) | Orquestrador que conhece todas as 40 skills e compõe chains automaticamente |
| [schedule](skills/schedule/) | Cria tarefas agendadas que rodam sob demanda ou em intervalo |

## Como usar

### No Claude Desktop (Habilidades Pessoais)
Essas skills já estão configuradas como "Habilidades pessoais" no Claude Desktop. Basta invocar pelo nome na conversa.

### No Claude Code (CLI)
Copie a pasta da skill desejada para `.claude/commands/<skill-name>/` no seu projeto:

```bash
cp -r skills/n8n-architect ~/.claude/commands/n8n-architect
```

### Estrutura de cada skill
```
skills/<nome>/
├── SKILL.md          # Prompt principal da skill
├── references/       # Base de conhecimento acumulada (algumas skills)
├── scripts/          # Scripts auxiliares (algumas skills)
└── ...               # Arquivos de suporte específicos
```

## Licença

Uso pessoal. Skills de documentos (pdf, docx, pptx, xlsx) possuem licença própria — veja `LICENSE.txt` dentro de cada uma.
