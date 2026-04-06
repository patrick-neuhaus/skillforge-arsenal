"""
Gera .zip de skills para upload no Claude.ai UI.
Uso:
  python zip-skills.py              # zipa todas
  python zip-skills.py trident      # zipa só a trident
  python zip-skills.py trident seo  # zipa trident e seo
"""
import zipfile, os, pathlib, sys

dist = pathlib.Path(__file__).parent / "dist"
dist.mkdir(exist_ok=True)
skills_dir = pathlib.Path(__file__).parent / "skills"

targets = sys.argv[1:] if len(sys.argv) > 1 else [d.name for d in sorted(skills_dir.iterdir()) if d.is_dir()]

count = 0
for name in targets:
    skill_dir = skills_dir / name
    if not skill_dir.is_dir():
        print(f"SKIP: {name} (não encontrado)")
        continue
    zip_path = dist / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(skill_dir):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for file in files:
                if file.endswith((".pyc", ".zip", ".gz", ".tar")):
                    continue
                full = pathlib.Path(root) / file
                zf.write(full, full.relative_to(skill_dir).as_posix())
    size = os.path.getsize(zip_path) // 1024
    print(f"  {name}.zip ({size}kb)")
    count += 1

print(f"\n{count} zip(s) em dist/")
