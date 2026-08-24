from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

start = s.find("def get_value(v):")
end = s.find("\ndef split_args", start)

if start == -1 or end == -1:
    print("[GI] get_value block not found")
    raise SystemExit(1)

block = s[start:end]

marker = '''    if v in variables:
        return variables[v]
'''

replacement = '''    if v in variables:
        return variables[v]

    # INDEX ACCESS: STRING / LIST / DICT
    if "[" in v and v.endswith("]"):
        name = v.split("[", 1)[0].strip()
        index = v.split("[", 1)[1][:-1].strip()

        if name in variables:
            obj = variables[name]

            if isinstance(obj, dict):
                key = index.strip('"').strip("'")
                return obj[key]

            idx = get_value(index)

            if isinstance(obj, (list, str)):
                return obj[int(idx)]
'''

if marker not in block:
    print("[GI] variable marker not found")
    raise SystemExit(1)

block = block.replace(marker, replacement, 1)

s = s[:start] + block + s[end:]
p.write_text(s)

print("[GI] v1.9 final index resolver fixed")
