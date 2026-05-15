# GEO Examples — Antes e Depois

Consulte este arquivo no **Step 3** para ver exemplos reais de otimizacao GEO.

---

## Exemplo 1: skill-builder

**Antes (generico):**
```yaml
description: "A skill for building other Claude Code skills."
```
Score: 2/15 (core capability ok, zero keywords)

**Depois (GEO-otimizado):**
```yaml
description: "Create, improve, and optimize Claude Code skills with battle-tested
techniques. Expert guidance on skill architecture, progressive loading, workflow
design, description optimization (GEO), and packaging. Use when user wants to:
create skill, build skill, new skill, improve skill, refactor skill, debug skill,
package skill, evolve skill, write SKILL.md, 'transforma isso numa skill', 'quero
automatizar esse processo', 'a skill tá ruim', 'a skill não tá funcionando', update
skill, edit skill, test skill, optimize description, scaffold skill, init skill,
validate skill. Na dúvida entre skill e prompt: 'Instruções persistentes pro Claude
(skill) ou prompt avulso?'"
```
Score: 14/15

**O que mudou:**
- Core capability: "A skill for building" → "Create, improve, and optimize"
- Verbos: 0 → 12 (create, improve, optimize, refactor, debug, package, evolve...)
- Substantivos: 1 → 8 (skill, architecture, loading, workflow, description, GEO...)
- Frases PT-BR: 0 → 4 ("transforma isso numa skill", "quero automatizar"...)
- Frases EN: 0 → 6 (create, build, improve, refactor, scaffold, validate)
- Diferenciacao: 0 → 1 ("Na duvida entre skill e prompt")

---

## Exemplo 2: security-audit

**Antes:**
```yaml
description: "Audit security of applications."
```
Score: 3/15

**Depois:**
```yaml
description: "Pipeline de 3 agentes pra auditoria de segurança de aplicação.
Dois modos: VPS (segurança do servidor via SSH) e Code (segurança do código via
GitHub). Use esta skill SEMPRE que o usuário mencionar: segurança, security, OWASP,
'tá seguro?', 'tem vulnerabilidade?', RLS, 'dados expostos', 'token vazando',
'secrets', XSS, injection, autenticação insegura, 'qualquer um acessa', 'audit de
segurança', 'meu app é seguro?', 'revisa a segurança'..."
```
Score: 13/15

---

## Exemplo 3: Skill Publica Top (ui-ux-pro-max, 222K installs)

```yaml
description: "UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings,
20 charts, 8 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter,
Tailwind). Actions: plan, build, create, design, implement, review, fix, improve,
optimize, enhance, refactor, check UI/UX code."
```
Score: 13/15

**Por que funciona:**
- Numeros concretos (50, 21, 8) = credibilidade + keywords numericas
- Lista de stacks = keywords de framework (React, Vue, Svelte...)
- "Actions:" = lista pura de verbos (12 verbos!)
- Curto (237 chars) mas denso — sem palavras desperdicadas

---

## Exemplo 4: Skill Publica Ruim

```yaml
description: "A powerful and comprehensive tool that helps developers create
beautiful and functional web applications with modern best practices."
```
Score: 1/15

**Por que falha:**
- "powerful and comprehensive" — adjetivos de marketing, zero valor pra agente
- "helps developers" — generico, nao diz O QUE faz
- "beautiful and functional" — subjetivo, nao e keyword buscavel
- "modern best practices" — vago, nao especifica quais
- Zero verbos de acao, zero substantivos de dominio, zero frases naturais

---

## Padroes que Funcionam

### Padrao 1: Core + Actions + Triggers
```
[O que faz]. [Tecnicas/features]. Use when: [frases naturais PT-BR + EN].
NAO use pra [diferenciacao].
```

### Padrao 2: Rede de Keywords (ui-ux-pro-max style)
```
[Dominio]. [Numeros concretos]. [Lista de stacks/tecnologias].
Actions: [lista de verbos].
```

### Padrao 3: Problema→Solucao
```
[Problema que resolve]. [Como resolve]. SEMPRE que: [sintomas que o usuario descreve].
```

## Checklist Final

Antes de aprovar uma description otimizada:

- [ ] Score >= 12/15
- [ ] Under 1024 caracteres
- [ ] Primeira frase = core capability (nao adjetivo)
- [ ] 5+ verbos de acao
- [ ] 5+ substantivos de dominio
- [ ] Frases em PT-BR E EN
- [ ] Diferenciacao clara
- [ ] Zero adjetivos de marketing
- [ ] Teste mental: "Se eu digitasse [frase-X], essa skill acionaria?" pra cada frase listada
