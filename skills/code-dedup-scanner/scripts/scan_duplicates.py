#!/usr/bin/env python3
"""
Code Dedup Scanner — Find reusable code in a codebase.

Quick scan for potential duplicates by name, export, and pattern matching.
Designed to be invoked by the Claude Code agent as a deterministic pre-check.

Usage:
    python scan_duplicates.py <project-root> <keyword> [--type component|function|hook|query]
    python scan_duplicates.py <project-root> --exports
    python scan_duplicates.py <project-root> --top-imports

Examples:
    python scan_duplicates.py ./src Button --type component
    python scan_duplicates.py ./src formatDate --type function
    python scan_duplicates.py ./src --exports
    python scan_duplicates.py ./src --top-imports
"""

import sys
import re
from pathlib import Path
from collections import Counter


IGNORE_DIRS = {
    'node_modules', '.next', '.git', 'dist', 'build', '.tmp',
    '__pycache__', '.cache', 'coverage', '.turbo'
}

CODE_EXTENSIONS = {'.ts', '.tsx', '.js', '.jsx'}


def find_code_files(root):
    """Find all code files, respecting ignore list."""
    root = Path(root).resolve()
    for path in root.rglob('*'):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.suffix in CODE_EXTENSIONS and path.is_file():
            yield path


def search_by_keyword(root, keyword, file_type=None):
    """Search for keyword in file names and content."""
    results = []
    keyword_lower = keyword.lower()
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)

    for path in find_code_files(root):
        rel_path = path.relative_to(Path(root).resolve())
        matches = []

        # Name match
        if keyword_lower in path.stem.lower():
            matches.append(('name', 0, path.stem))

        # Content match
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
            lines = content.splitlines()
            for i, line in enumerate(lines, 1):
                if keyword_pattern.search(line):
                    # Check if it's a definition (export, function, const, class)
                    stripped = line.strip()
                    if any(stripped.startswith(kw) for kw in
                           ['export ', 'function ', 'const ', 'class ', 'interface ', 'type ']):
                        matches.append(('definition', i, stripped[:120]))
                    elif 'import' not in stripped.lower():
                        matches.append(('usage', i, stripped[:120]))
        except (OSError, UnicodeDecodeError):
            continue

        if matches:
            results.append((str(rel_path), matches))

    return results


def list_exports(root):
    """List all exported functions, components, and constants."""
    exports = []
    export_pattern = re.compile(
        r'export\s+(?:default\s+)?(?:function|const|class|interface|type)\s+(\w+)'
    )

    for path in find_code_files(root):
        rel_path = str(path.relative_to(Path(root).resolve()))
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
            for match in export_pattern.finditer(content):
                exports.append((match.group(1), rel_path))
        except (OSError, UnicodeDecodeError):
            continue

    return sorted(exports, key=lambda x: x[0].lower())


def top_imports(root, n=20):
    """Find the most imported modules (reuse hotspots)."""
    import_pattern = re.compile(r"from\s+['\"](@/[^'\"]+|\.{1,2}/[^'\"]+)['\"]")
    counter = Counter()

    for path in find_code_files(root):
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
            for match in import_pattern.finditer(content):
                counter[match.group(1)] += 1
        except (OSError, UnicodeDecodeError):
            continue

    return counter.most_common(n)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]

    if not args:
        print(__doc__)
        sys.exit(1)

    root = args[0]

    if '--exports' in flags:
        exports = list_exports(root)
        print(f"EXPORTS ({len(exports)} found):\n")
        for name, path in exports:
            print(f"  {name:40s} {path}")
        sys.exit(0)

    if '--top-imports' in flags:
        imports = top_imports(root)
        print(f"TOP IMPORTS (most reused modules):\n")
        for module, count in imports:
            print(f"  {count:4d}x  {module}")
        sys.exit(0)

    if len(args) < 2:
        print("Error: keyword required. Usage: scan_duplicates.py <root> <keyword>")
        sys.exit(1)

    keyword = args[1]
    results = search_by_keyword(root, keyword)

    if not results:
        print(f"No matches found for '{keyword}'.")
        print("Recommendation: CREATE — nothing similar exists in codebase.")
        sys.exit(0)

    print(f"MATCHES for '{keyword}' ({len(results)} files):\n")
    for filepath, matches in results:
        definitions = [m for m in matches if m[0] == 'definition']
        names = [m for m in matches if m[0] == 'name']
        usages = [m for m in matches if m[0] == 'usage']

        if names:
            print(f"  [NAME]  {filepath}")
        if definitions:
            for _, line, text in definitions[:3]:
                print(f"  [DEF]   {filepath}:{line}  {text}")
        if usages and not definitions:
            print(f"  [USE]   {filepath} ({len(usages)} usage(s))")

    print(f"\nTotal: {len(results)} file(s) with matches.")


if __name__ == "__main__":
    main()
