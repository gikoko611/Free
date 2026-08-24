from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

start = s.find("def get_value(v):")
end = s.find("\ndef split_args", start)

if start == -1 or end == -1:
    print("[GI] get_value boundaries not found")
    raise SystemExit(1)

new = r'''def get_value(v):

    v = v.strip()

    # STRING LITERAL
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

    # VARIABLE INDEX ACCESS
    if "[" in v and v.endswith("]"):
        name = v.split("[", 1)[0].strip()
        index = v.split("[", 1)[1][:-1].strip()

        if name in variables:
            obj = variables[name]

            # DICTIONARY
            if isinstance(obj, dict):
                key = index.strip('"').strip("'")

                if key in variables:
                    key = variables[key]

                return obj[key]

            # LIST / STRING
            if isinstance(obj, (list, str)):
                idx = get_value(index)
                return obj[int(idx)]

    # VARIABLE
    if v in variables:
        return variables[v]

    # DICTIONARY LITERAL
    if v.startswith("{") and v.endswith("}"):
        try:
            return ast.literal_eval(v)
        except (ValueError, SyntaxError):
            pass

    # LIST LITERAL
    if v.startswith("[") and v.endswith("]"):
        inside = v[1:-1]

        if not inside.strip():
            return []

        return [
            get_value(x.strip())
            for x in split_args(inside)
        ]

    # FUNCTION RETURN VALUE
    if "(" in v and v.endswith(")"):

        name = v.split("(", 1)[0].strip()

        argtext = v.split("(", 1)[1][:-1]

        args = []

        if argtext.strip():
            args = split_args(argtext)

        if name in functions:

            old = variables.copy()

            for n, a in zip(
                functions[name]["params"],
                args
            ):
                variables[n] = get_value(a)

            result = None

            try:
                execute(
                    functions[name]["code"]
                )

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

            except:
                pass

    return v
'''

s = s[:start] + new + s[end:]

p.write_text(s)

print("[GI] v1.9 get_value cleaned")
