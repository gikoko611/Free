from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = 'elif "(" in line and line.endswith(")") and "=" not in line:'
new = 'elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):'

if old not in s:
    print("[GI] Target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

p.write_text(s)
print("[GI] SAY/FUNCTION parser conflict fixed")
