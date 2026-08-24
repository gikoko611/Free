from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]
'''

new = '''    if (
        (v.startswith('"') and v.endswith('"')) or
        (v.startswith("'") and v.endswith("'"))
    ):
        return v[1:-1]
'''

if old not in s:
    print("[GI] String target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)
p.write_text(s)

print("[GI] Single-quote string fixed")
