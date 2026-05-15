# Tech Catalog — Ferramentas Tecnicas Pre-Catalogadas

Consulte este arquivo no **Step 2** antes de fazer web search. Se o tema esta aqui, use direto.

---

## AI & Agent Tooling

### GEO (Generative Engine Optimization)
- **O que e:** SEO para agentes de IA — otimizar conteudo pra ser encontrado/consumido por LLMs
- **Referencia:** Conceito de Omer (criador do Agent Tools / inference.sh)
- **Aplicacao:** Descriptions de skills, READMEs, package metadata
- **Skill relacionada:** geo-optimizer

### skills.sh (Vercel)
- **O que e:** Diretorio aberto de skills pra Claude Code (91K+ skills)
- **CLI:** `npx skills add/find/list/update/init`
- **Formato:** SKILL.md com YAML frontmatter
- **Ranking:** Find Skills (open source) indexa e recomenda skills

### inference.sh
- **O que e:** Plataforma de Omer com 150+ ferramentas de IA via CLI
- **Padrao:** CLI-first — agente usa `inference app run -p <tool>`
- **Exemplo de:** Composicao emergente — agente descobre e encadeia comandos

## Web Search & Data

### Tavily
- **O que e:** Web search especializada para agentes de IA
- **API:** REST, retorna resultados ranqueados com score
- **Uso tipico:** Research phase do SDD, reference-finder deep search
- **Custo:** Pay per search (API key necessaria)

### Exa
- **O que e:** Web search semantica para agentes
- **Diferencial:** Busca por significado, nao por keywords
- **Uso tipico:** Encontrar papers, artigos, implementacoes similares

## Video & Media

### Remotion
- **O que e:** Framework React para criar videos programaticamente
- **Stack:** React + TypeScript, renderiza videos como componentes
- **Uso tipico:** Videos de marketing, data visualizations animadas, social media content
- **Referencia:** remotion-dev/remotion no GitHub

### FFmpeg
- **O que e:** CLI para manipulacao de video/audio
- **Uso tipico:** Conversao de formato, extracao de audio, resize, compress
- **Wrappable:** Sim — candidato ideal pra cli-skill-wrapper

### ImageMagick
- **O que e:** CLI para manipulacao de imagens
- **Uso tipico:** Resize, crop, format conversion, watermarks
- **Wrappable:** Sim

## Frontend

### Motion (ex-Framer Motion)
- **O que e:** Biblioteca de animacoes para React
- **Uso tipico:** Transicoes de pagina, hover effects, layout animations
- **Referencia:** motion.dev

### ProseMirror / TipTap
- **O que e:** Framework para editores rich-text
- **ProseMirror:** Lower-level, mais controle
- **TipTap:** Abstraction sobre ProseMirror, mais facil de usar
- **Referencia:** Novel (steven-tey/novel) — implementacao minimalista

### shadcn/ui
- **O que e:** Componentes React copiados pro projeto (nao instalados como dependencia)
- **Base:** Radix UI + Tailwind CSS
- **Diferencial:** Voce "owna" o codigo — customizavel sem limites

## Backend & Database

### Supabase
- **O que e:** Backend-as-a-Service baseado em PostgreSQL
- **Features:** Auth, RLS, Realtime, Storage, Edge Functions
- **Skill relacionada:** supabase-db-architect

### Resend
- **O que e:** Servico de envio de e-mails
- **API:** REST, SDK pra Node/Python
- **Uso tipico:** Transactional emails (confirmacao, reset password)
