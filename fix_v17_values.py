from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]

    if v.isdigit():
        return int(v)
'''

new = '''    # BOOLEAN VALUES

    if v == "true" or v == "True":
        return True

    if v == "false" or v == "False":
        return False


    # STRING VALUES

    if (
        (v.startswith('"') and v.endswith('"')) or
        (v.startswith("'") and v.endswith("'"))
    ):
        return v[1:-1]


    # INTEGER VALUES

    if v.lstrip("-").isdigit():
        return int(v)
'''

if old not in s:
    print("[GI] VALUE target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

p.write_text(s)
print("[GI] v1.7 string/boolean values added")
