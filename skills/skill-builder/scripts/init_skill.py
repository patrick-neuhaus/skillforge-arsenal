#!/usr/bin/env python3
"""
Skill Initializer — Scaffolds a new skill with best-practice structure.

Usage:
    python init_skill.py <skill-name> --path <directory>

Examples:
    python init_skill.py my-analyzer --path ./skills
    python init_skill.py code-reviewer --path /path/to/skills
"""

import sys
import re
from pathlib import Path


SKILL_TEMPLATE = '''---
name: {skill_name}
description: "[TODO: Keyword bombing — inclua: (1) capability principal na 1ª frase, (2) 5+ action verbs, (3) 5+ object nouns, (4) frases naturais de trigger. Toda info de 'quando usar' vai AQUI, não no body.]"
---

# {skill_title}

IRON LAW: [TODO: Qual o ÚNICO erro que o modelo mais provavelmente vai cometer? Escreva uma regra que previna.]

## Options

| Option | Description | Default |
|--------|-------------|---------|
| (nenhum por enquanto) | | |

## Workflow

```
{skill_title} Progress:

- [ ] Step 1: [Entender] ⚠️ REQUIRED
  - [ ] 1.1 [Sub-step]
  - [ ] 1.2 [Sub-step]
- [ ] Step 2: [Executar]
  - [ ] ⛔ GATE: Confirmar com usuário antes de prosseguir
- [ ] Step 3: [Entregar]
  - [ ] Pre-delivery checklist
```

## Step 1: [Entender] ⚠️ REQUIRED

[Use question-style instructions, não diretivas vagas.]

Pergunte:
- [Pergunta específica sobre o input]
- [Pergunta sobre o contexto]
- [Pergunta sobre o output esperado]

## Step 2: [Executar]

[O trabalho principal da skill.]

⛔ **Confirmation Gate:** Apresente o plano ao usuário antes de executar.

## Step 3: [Entregar]

[Defina formato e estrutura do output.]

### Pre-Delivery Checklist

- [ ] [Check específico e verificável]
- [ ] [Check específico e verificável]
- [ ] Sem placeholders restantes (TODO, FIXME)

## Anti-Patterns

- [O que o Claude faria no "modo preguiçoso"? Proíba explicitamente.]
- [Outro anti-pattern do domínio]

## When NOT to use

- [Situação em que outra skill é mais apropriada]
'''


def title_case(name):
    """Convert kebab-case to Title Case."""
    return ' '.join(word.capitalize() for word in name.split('-'))


def validate_name(name):
    """Validate skill name format."""
    if not re.match(r'^[a-z0-9-]+$', name):
        return "Name must be kebab-case (lowercase letters, digits, hyphens only)"
    if name.startswith('-') or name.endswith('-') or '--' in name:
        return "Name cannot start/end with hyphen or have consecutive hyphens"
    if len(name) > 64:
        return f"Name too long ({len(name)} chars, max 64)"
    return None


def init_skill(skill_name, path):
    """Create a new skill directory with scaffold template."""
    error = validate_name(skill_name)
    if error:
        print(f"Error: {error}")
        return None

    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    # Create SKILL.md
    skill_title = title_case(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    ).lstrip('\n')

    (skill_dir / 'SKILL.md').write_text(skill_content, encoding='utf-8')
    print(f"Created SKILL.md")

    # Create resource directories
    for dirname in ('scripts', 'references'):
        (skill_dir / dirname).mkdir(exist_ok=True)
        print(f"Created {dirname}/")

    print(f"\nSkill '{skill_name}' initialized at {skill_dir}")
    print()
    print("Next steps:")
    print("  1. Fill all [TODO] items in SKILL.md")
    print("  2. Write description with keyword bombing (references/description-guide.md)")
    print("  3. Set the Iron Law")
    print("  4. Add scripts/ and references/ as needed")
    print("  5. Run validate.py when ready")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: python init_skill.py <skill-name> --path <directory>")
        print()
        print("Examples:")
        print("  python init_skill.py my-skill --path ./skills")
        print("  python init_skill.py code-reviewer --path /custom/path")
        sys.exit(1)

    result = init_skill(sys.argv[1], sys.argv[3])
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
