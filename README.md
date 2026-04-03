# Skillforge Arsenal

Coleção pessoal de skills para Claude Code — prompts especializados que transformam o Claude em ferramentas focadas para tarefas específicas.

## O que são Skills?

Skills são instruções estruturadas (em Markdown) que ensinam o Claude a executar tarefas complexas de forma consistente. Cada skill define um fluxo de trabalho, princípios, regras e outputs esperados.

## Skills disponíveis

### Produto & Discovery
| Skill | Descrição |
|-------|-----------|
| [product-discovery-prd](skills/product-discovery-prd/) | Conduz discovery de produto e gera PRDs otimizados para Lovable e outras ferramentas |
| [lovable-knowledge](skills/lovable-knowledge/) | Gera Workspace/Project Knowledge otimizados para configurar o Lovable |
| [ux-audit](skills/ux-audit/) | Auditorias de UX/UI em apps web e mobile, baseadas em heurísticas |

### Engenharia & Arquitetura
| Skill | Descrição |
|-------|-----------|
| [n8n-architect](skills/n8n-architect/) | Arquitetura e padrões para automações n8n |
| [supabase-db-architect](skills/supabase-db-architect/) | Arquitetura de banco Supabase/PostgreSQL para apps de pequeno/médio porte |
| [repo-review](skills/repo-review/) | Pipeline de 3 agentes para detecção profunda de bugs em codebase |
| [prompt-engineer](skills/prompt-engineer/) | Cria, valida e otimiza prompts para qualquer LLM |

### Segurança & Infraestrutura
| Skill | Descrição |
|-------|-----------|
| [security-audit](skills/security-audit/) | Pipeline de 3 agentes para auditoria de segurança (VPS ou Code) |
| [vps-infra-audit](skills/vps-infra-audit/) | Pipeline de 3 agentes para auditoria de infraestrutura VPS |

### Gestão & Comunicação
| Skill | Descrição |
|-------|-----------|
| [tech-lead-pm](skills/tech-lead-pm/) | Gestão de projetos e liderança técnica para líder de primeira viagem |
| [comunicacao-clientes](skills/comunicacao-clientes/) | Ensina a escrever melhor para clientes via WhatsApp/Telegram |

### Pesquisa & Conhecimento
| Skill | Descrição |
|-------|-----------|
| [reference-finder](skills/reference-finder/) | Fundamenta temas com referências consagradas: livros, frameworks, artigos |
| [skill-builder](skills/skill-builder/) | Cria, modifica e otimiza skills do Claude |

### Documentos & Arquivos
| Skill | Descrição |
|-------|-----------|
| [pdf](skills/pdf/) | Leitura, criação, merge, split e manipulação de PDFs |
| [docx](skills/docx/) | Cria, lê e edita documentos Word (.docx) |
| [pptx](skills/pptx/) | Cria, lê e edita apresentações PowerPoint (.pptx) |
| [xlsx](skills/xlsx/) | Cria, lê e edita planilhas (.xlsx, .csv, .tsv) |

### Utilidades
| Skill | Descrição |
|-------|-----------|
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
