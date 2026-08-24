from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]

    if v.isdigit():
        return int(v)
'''

new = '''    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]

    if v == "true":
        return True

    if v == "false":
        return False

    if v.lstrip("-").isdigit():
        return int(v)
'''

if old not in s:
    print("[GI] VALUE target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

old_cond = '''    if op == "==":
        return a == b

    if op == ">":
        return a > b

    if op == "<":
        return a < b

    return False
'''

new_cond = '''    if op == "==":
        return a == b

    if op == "!=":
        return a != b

    if op == ">":
        return a > b

    if op == "<":
        return a < b

    if op == ">=":
        return a >= b

    if op == "<=":
        return a <= b

    return False
'''

if old_cond not in s:
    print("[GI] CONDITION target not found")
    raise SystemExit(1)

s = s.replace(old_cond, new_cond, 1)

p.write_text(s)
print("[GI] v1.7 boolean/comparison support added")
