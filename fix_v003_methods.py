from pathlib import Path

p = Path("gi_0.0.3-dev.py")
s = p.read_text()

marker = '    # FUNCTION RETURN VALUE\n'

insert = '''    # BUILTIN / LIST METHODS
    if "(" in v and v.endswith(")"):
        call = v.split("(", 1)[0].strip()
        argtext = v.split("(", 1)[1][:-1].strip()

        # len(value)
        if call == "len":
            return len(get_value(argtext))

        # object.method(...)
        if "." in call:
            objname, method = call.split(".", 1)

            if objname in variables:
                obj = variables[objname]
                args = split_args(argtext) if argtext else []
                values = [get_value(x) for x in args]

                if method == "append" and isinstance(obj, list):
                    obj.append(values[0] if values else None)
                    return None

                if method == "remove" and isinstance(obj, list):
                    if values:
                        obj.remove(values[0])
                    return None

                if method == "pop" and isinstance(obj, list):
                    return obj.pop(values[0] if values else -1)

                if method == "clear" and isinstance(obj, list):
                    obj.clear()
                    return None

                if method == "count" and isinstance(obj, list):
                    return obj.count(values[0] if values else None)

                if method == "index" and isinstance(obj, list):
                    return obj.index(values[0])

                if method == "upper" and isinstance(obj, str):
                    return obj.upper()

                if method == "lower" and isinstance(obj, str):
                    return obj.lower()

'''

if marker not in s:
    raise SystemExit("[GI] get_value insertion point not found")

s = s.replace(marker, insert + marker, 1)
p.write_text(s)

print("[GI] v0.0.3-dev list/string methods added")
