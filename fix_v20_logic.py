from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = '''def check_condition(c):
    c = c.strip()

    for op in [">=", "<=", "!=", "==", ">", "<"]:
        if op in c:
            a, b = c.split(op, 1)
            a = get_value(a)
            b = get_value(b)

            if op == ">=":
                return a >= b
            if op == "<=":
                return a <= b
            if op == "!=":
                return a != b
            if op == "==":
                return a == b
            if op == ">":
                return a > b
            if op == "<":
                return a < b

    return bool(get_value(c))
'''

new = '''def check_condition(c):
    c = c.strip()

    # NOT
    if c.startswith("not "):
        return not check_condition(c[4:].strip())

    # OR
    parts = c.split(" or ")
    if len(parts) > 1:
        return any(check_condition(x) for x in parts)

    # AND
    parts = c.split(" and ")
    if len(parts) > 1:
        return all(check_condition(x) for x in parts)

    for op in [">=", "<=", "!=", "==", ">", "<"]:
        if op in c:
            a, b = c.split(op, 1)
            a = get_value(a)
            b = get_value(b)

            if op == ">=":
                return a >= b
            if op == "<=":
                return a <= b
            if op == "!=":
                return a != b
            if op == "==":
                return a == b
            if op == ">":
                return a > b
            if op == "<":
                return a < b

    return bool(get_value(c))
'''

if old not in s:
    print("[GI] check_condition pattern not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

# Add logical expressions to get_value()
marker = '''    # INTEGER
    if v.lstrip("-").isdigit():
        return int(v)
'''

insert = '''    # LOGICAL EXPRESSIONS
    if v.startswith("not "):
        return not check_condition(v[4:].strip())

    if " and " in v or " or " in v:
        return check_condition(v)

    # INTEGER
    if v.lstrip("-").isdigit():
        return int(v)
'''

if marker not in s:
    print("[GI] get_value insertion point not found")
    raise SystemExit(1)

s = s.replace(marker, insert, 1)

p.write_text(s)
print("[GI] v2.0 logical expressions added")
