from pathlib import Path

p = Path("gi_v1.8.py")
s = p.read_text()

old = '''    # BASIC MATH
    for op in ["+","-","*","/"]:
'''

new = '''    # COMPARISON
    for op in ["==", "!=", ">=", "<=", ">", "<"]:
        if op in v:
            try:
                a, b = v.split(op, 1)
                a = get_value(a)
                b = get_value(b)

                if op == "==":
                    return a == b
                elif op == "!=":
                    return a != b
                elif op == ">=":
                    return a >= b
                elif op == "<=":
                    return a <= b
                elif op == ">":
                    return a > b
                elif op == "<":
                    return a < b
            except:
                pass

    # BASIC MATH
    for op in ["+","-","*","/"]:
'''

if old not in s:
    print("[GI] Target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

p.write_text(s)
print("[GI] v1.8 comparison evaluator added")
