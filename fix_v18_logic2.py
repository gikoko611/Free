from pathlib import Path

p = Path("gi_v1.8.py")
s = p.read_text()

start = s.find("def get_value(v):")
end = s.find("\ndef split_args", start)

if start == -1 or end == -1:
    print("[GI] get_value block not found")
    raise SystemExit(1)

block = s[start:end]

old = '''    # LOGICAL OPERATORS
    if " or " in v:
        parts = v.split(" or ")
        return any(bool(get_value(x)) for x in parts)

    if " and " in v:
        parts = v.split(" and ")
        return all(bool(get_value(x)) for x in parts)

    if v.startswith("not "):
        return not bool(get_value(v[4:].strip()))
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
'''

# Keep get_value logic unchanged; fix check_condition separately.
if old not in block:
    print("[GI] Logic block not found")
    raise SystemExit(1)

# Find check_condition
cs = s.find("def check_condition")
ce = s.find("\ndef execute", cs)

if cs == -1 or ce == -1:
    print("[GI] check_condition block not found")
    raise SystemExit(1)

new_check = '''def check_condition(c):

    c = c.strip()

    # OR
    if " or " in c:
        return any(check_condition(x) for x in c.split(" or "))

    # AND
    if " and " in c:
        return all(check_condition(x) for x in c.split(" and "))

    # NOT
    if c.startswith("not "):
        return not check_condition(c[4:].strip())

    for op in ["==", "!=", ">=", "<=", ">", "<"]:
        if op in c:
            a, b = c.split(op, 1)
            a = get_value(a.strip())
            b = get_value(b.strip())

            if op == "==":
                return a == b
            if op == "!=":
                return a != b
            if op == ">=":
                return a >= b
            if op == "<=":
                return a <= b
            if op == ">":
                return a > b
            if op == "<":
                return a < b

    return bool(get_value(c))

'''

s = s[:cs] + new_check + s[ce:]

p.write_text(s)
print("[GI] v1.8 condition logic fixed")
