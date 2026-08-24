from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

# OR support
if 'if " or " in c:' not in s:
    needle = '''    if " and " in c:
        return all(check_condition(x) for x in c.split(" and "))
'''
    replacement = '''    if " or " in c:
        return any(check_condition(x) for x in c.split(" or "))

    if " and " in c:
        return all(check_condition(x) for x in c.split(" and "))
'''
    if needle not in s:
        print("[GI] AND block not found")
        raise SystemExit(1)
    s = s.replace(needle, replacement, 1)

# get_value logical expressions
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

if 'if " and " in v or " or " in v:' not in s:
    if marker not in s:
        print("[GI] INTEGER marker not found")
        raise SystemExit(1)
    s = s.replace(marker, insert, 1)

p.write_text(s)
print("[GI] v2.0 logic patch applied")
