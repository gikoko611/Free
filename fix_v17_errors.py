from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0].strip()

        key=v.split("[",1)[1][:-1].strip()

        if name in variables:

            obj=variables[name]

            if isinstance(obj, dict):

                key=key.strip('"').strip("'")

                return obj[key]
'''

new = '''    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0].strip()

        key=v.split("[",1)[1][:-1].strip()

        if name in variables:

            obj=variables[name]

            if isinstance(obj, dict):

                key=key.strip('"').strip("'")

                try:
                    return obj[key]
                except KeyError:
                    raise GIRuntimeError(
                        "Dictionary key not found: " + key
                    )
'''

if old not in s:
    print("[GI] Dict error target not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

old_class = '''class GIReturn(Exception):
    def __init__(self, value):
        self.value = value
'''

new_class = '''class GIReturn(Exception):
    def __init__(self, value):
        self.value = value


class GIRuntimeError(Exception):
    pass
'''

if old_class not in s:
    print("[GI] Runtime error class target not found")
    raise SystemExit(1)

s = s.replace(old_class, new_class, 1)

p.write_text(s)
print("[GI] v1.7 error handling base added")
