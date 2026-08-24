from pathlib import Path

p = Path("gi_v1.8.py")
s = p.read_text()

old = '''    # COMPARISON
    for op in ["==", "!=", ">=", "<=", ">", "<"]:
'''

new = '''    # LOGICAL OPERATORS
    if " or " in v:
        parts = v.split(" or ")
        return any(bool(get_value(x)) for x in parts)

    if " and " in v:
        parts = v.split(" and ")
        return all(bool(get_value(x)) for x in parts)

    if v.startswith("not "):
        return not bool(get_value(v[4:].strip()))

    # COMPARISON
    for op in ["==", "!=", ">=", "<=", ">", "<"]:
'''

if old not in s:
    print("[GI] Target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

p.write_text(s)
print("[GI] v1.8 logical operators added")
