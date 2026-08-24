from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

marker = '''    # LIST INDEX
'''

insert = '''    # STRING / LIST / DICT INDEX
    if "[" in v and v.endswith("]"):
        name = v.split("[", 1)[0].strip()
        index = v.split("[", 1)[1][:-1].strip()

        if name in variables:
            obj = variables[name]
            idx = get_value(index)

            if isinstance(obj, str):
                return obj[int(idx)]

            if isinstance(obj, list):
                return obj[int(idx)]

            if isinstance(obj, dict):
                key = index.strip('"').strip("'")
                return obj[key]

'''

if marker not in s:
    print("[GI] Index marker not found")
    raise SystemExit(1)

# Avoid duplicate patch
if "# STRING / LIST / DICT INDEX" in s:
    print("[GI] String index already present")
    raise SystemExit(0)

s = s.replace(marker, insert + marker, 1)

p.write_text(s)
print("[GI] v1.9 string indexing added")
