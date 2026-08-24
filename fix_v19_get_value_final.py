from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

start = s.index("def get_value(v):")
end = s.index("\ndef split_args", start)

new = '''def get_value(v):
    v = v.strip()

    # VARIABLE
    if v in variables:
        return variables[v]

    # STRING
    if (
        (v.startswith('"') and v.endswith('"')) or
        (v.startswith("'") and v.endswith("'"))
    ):
        return v[1:-1]

    # BOOLEAN
    if v == "true":
        return True

    if v == "false":
        return False

    # INTEGER
    if v.lstrip("-").isdigit():
        return int(v)

    # INDEX ACCESS: list / string / dict
    if "[" in v and v.endswith("]"):
        name = v.split("[", 1)[0].strip()
        index = v.split("[", 1)[1][:-1].strip()

        if name in variables:
            obj = variables[name]

            if isinstance(obj, dict):
                key = index.strip('"').strip("'")
                return obj[key]

            idx = get_value(index)
            return obj[int(idx)]

    # LIST LITERAL
    if v.startswith("[") and v.endswith("]"):
        inside = v[1:-1].strip()

        if not inside:
            return []

        return [
            get_value(x.strip())
            for x in split_args(inside)
        ]

    # DICTIONARY LITERAL
    if v.startswith("{") and v.endswith("}"):
        try:
            return ast.literal_eval(v)
        except (ValueError, SyntaxError):
            pass

    # FUNCTION RETURN VALUE
    if "(" in v and v.endswith(")"):
        name = v.split("(", 1)[0].strip()
        argtext = v.split("(", 1)[1][:-1]

        if name in functions:
            args = split_args(argtext) if argtext.strip() else []

            old = variables.copy()

            for n, a in zip(functions[name]["params"], args):
                variables[n] = get_value(a)

            result = None

            try:
                execute(functions[name]["code"])
            except GIReturn as e:
                result = e.value

            variables.clear()
            variables.update(old)

            return result

    # BASIC MATH
    for op in ["+", "-", "*", "/"]:
        if op in v:
            try:
                a, b = v.split(op, 1)
                a = get_value(a)
                b = get_value(b)

                if op == "+":
                    return a + b
                elif op == "-":
                    return a - b
                elif op == "*":
                    return a * b
                elif op == "/":
                    return a // b
            except Exception:
                pass

    return v

'''

s = s[:start] + new + s[end:]

p.write_text(s)
print("[GI] v1.9 get_value final cleanup applied")
