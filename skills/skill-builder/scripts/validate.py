#!/usr/bin/env python3
"""
Skill Validator — Comprehensive validation for Claude Code skills.

Checks structure, frontmatter, line count, and quality signals.

Usage:
    python validate.py <skill-directory>
    python validate.py <skill-directory> --verbose
"""

import sys
import re
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


ALLOWED_FRONTMATTER_KEYS = {
    'name', 'description', 'license', 'allowed-tools',
    'metadata', 'argument-hint', 'compatibility'
}

MAX_SKILL_LINES = 250
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024


def parse_frontmatter(content):
    """Extract and parse YAML frontmatter from SKILL.md content."""
    if not content.startswith('---'):
        return None, "No YAML frontmatter found (file must start with ---)"

    match = re.match(r'^---\r?\n(.*?)\r?\n---', content, re.DOTALL)
    if not match:
        return None, "Invalid frontmatter format (missing closing ---)"

    frontmatter_text = match.group(1)

    if HAS_YAML:
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
            if not isinstance(frontmatter, dict):
                return None, "Frontmatter must be a YAML dictionary"
            return frontmatter, None
        except yaml.YAMLError as e:
            return None, f"Invalid YAML in frontmatter: {e}"
    else:
        # Fallback: basic regex parsing without yaml module
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            m = re.match(r'^(\w[\w-]*):\s*(.+)$', line)
            if m:
                frontmatter[m.group(1)] = m.group(2).strip().strip('"').strip("'")
        return frontmatter, None


def validate_skill(skill_path, verbose=False):
    """
    Validate a skill directory. Returns (passed, warnings, errors).

    - errors: must fix before delivery
    - warnings: should fix, but not blocking
    """
    skill_path = Path(skill_path).resolve()
    errors = []
    warnings = []

    def error(msg):
        errors.append(msg)

    def warn(msg):
        warnings.append(msg)

    # --- SKILL.md exists ---
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, [], ["SKILL.md not found"]

    content = skill_md.read_text(encoding='utf-8')
    lines = content.splitlines()
    line_count = len(lines)

    # --- Frontmatter ---
    frontmatter, fm_error = parse_frontmatter(content)
    if fm_error:
        error(fm_error)
        return False, warnings, errors

    # Required fields
    if 'name' not in frontmatter:
        error("Missing 'name' in frontmatter")
    if 'description' not in frontmatter:
        error("Missing 'description' in frontmatter")

    # Unexpected keys
    unexpected = set(frontmatter.keys()) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        error(f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}")

    # Name validation
    name = frontmatter.get('name', '')
    if isinstance(name, str) and name.strip():
        name = name.strip()
        if not re.match(r'^[a-z0-9-]+$', name):
            error(f"Name '{name}' must be kebab-case (lowercase, digits, hyphens)")
        elif name.startswith('-') or name.endswith('-') or '--' in name:
            error(f"Name '{name}' has invalid hyphen placement")
        if len(name) > MAX_NAME_LENGTH:
            error(f"Name too long ({len(name)} chars, max {MAX_NAME_LENGTH})")

    # Description validation
    desc = frontmatter.get('description', '')
    if isinstance(desc, str) and desc.strip():
        desc = desc.strip()
        if '<' in desc or '>' in desc:
            error("Description cannot contain angle brackets")
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            error(f"Description too long ({len(desc)} chars, max {MAX_DESCRIPTION_LENGTH})")
        # GEO quality checks
        if len(desc) < 100:
            warn("Description under 100 chars — consider keyword bombing for better triggering")

    # --- Line count ---
    if line_count > MAX_SKILL_LINES:
        error(f"SKILL.md is {line_count} lines (max {MAX_SKILL_LINES}). Move content to references/")
    elif line_count > MAX_SKILL_LINES - 30:
        warn(f"SKILL.md is {line_count} lines — approaching the {MAX_SKILL_LINES}-line limit")

    # --- Quality signals (content-based) ---
    content_lower = content.lower()

    # Iron Law
    if 'iron law' not in content_lower:
        warn("No Iron Law found — consider adding one at the top")

    # Workflow checklist
    has_checklist = '- [ ]' in content or '- [x]' in content
    if not has_checklist:
        warn("No trackable workflow checklist found (- [ ] markers)")

    # Confirmation gates
    has_gates = 'confirmation gate' in content_lower or '⛔ gate' in content_lower or 'gate:' in content_lower
    if not has_gates:
        warn("No confirmation gates found — add before destructive/generative ops")

    # Anti-patterns section
    if 'anti-pattern' not in content_lower and 'anti pattern' not in content_lower:
        warn("No anti-patterns section found")

    # Roteiro de perguntas (question framework)
    has_questions = any(q in content_lower for q in ['ask:', 'pergunte:', 'roteiro de perguntas', 'key questions', 'question'])
    if not has_questions:
        warn("No question framework found — skills should ask structured questions when context is missing")

    # GEO quality: action verbs in description
    if isinstance(desc, str) and desc.strip():
        action_verbs = ['create', 'build', 'improve', 'analyze', 'review', 'generate', 'fix',
                        'optimize', 'audit', 'design', 'plan', 'implement', 'validate', 'check',
                        'criar', 'melhorar', 'analisar', 'revisar', 'gerar', 'corrigir', 'otimizar',
                        'auditar', 'planejar', 'implementar', 'validar', 'verificar', 'montar']
        verb_count = sum(1 for v in action_verbs if v in desc.lower())
        if verb_count < 3:
            warn(f"Description has only {verb_count} action verbs — aim for 5+ for better GEO triggering")

    # Progressive loading references
    has_load_refs = 'load references/' in content_lower or 'consulte references/' in content_lower or 'references/' in content_lower
    refs_dir = skill_path / 'references'
    if refs_dir.exists() and list(refs_dir.iterdir()) and not has_load_refs:
        warn("References exist but SKILL.md has no 'Load references/' pointers")

    # Unnecessary files
    for bad_file in ['README.md', 'CHANGELOG.md', 'INSTALLATION_GUIDE.md']:
        if (skill_path / bad_file).exists():
            warn(f"Unnecessary file: {bad_file} — skills are for agents, not humans to read about")

    # TODO/placeholder check
    todo_matches = re.findall(r'\[TODO[:\]]', content, re.IGNORECASE)
    if todo_matches:
        warn(f"Found {len(todo_matches)} [TODO] placeholder(s) — fill or remove before delivery")

    passed = len(errors) == 0
    return passed, warnings, errors


def main():
    verbose = '--verbose' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]

    if not args:
        print("Usage: python validate.py <skill-directory> [--verbose]")
        sys.exit(1)

    skill_path = args[0]
    passed, warnings, errors = validate_skill(skill_path, verbose)

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  [FAIL] {e}")
        print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  [WARN] {w}")
        print()

    if passed and not warnings:
        print("[PASS] Skill is valid! No issues found.")
    elif passed:
        print(f"[PASS] Skill is valid with {len(warnings)} warning(s).")
    else:
        print(f"[FAIL] Validation failed with {len(errors)} error(s).")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
