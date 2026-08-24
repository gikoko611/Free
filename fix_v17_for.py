from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

marker = '''        # IF / ELIF / ELSE

        elif line.startswith("if "):
'''

if marker not in s:
    print("[GI] FOR target not found")
    raise SystemExit(1)

block = '''        # FOR

        elif line.startswith("for "):

            header = line[4:].strip()

            if " in " not in header:
                raise GIRuntimeError("Invalid for syntax")

            var, expr = header.split(" in ", 1)
            var = var.strip()
            expr = expr.strip()

            block = []

            i += 1
            depth = 1

            while i < len(lines) and depth > 0:

                current = lines[i].strip()

                if current.startswith("for "):
                    depth += 1

                elif current.startswith("while "):
                    depth += 1

                elif current.startswith("if "):
                    depth += 1

                elif current == "end":
                    depth -= 1
                    if depth == 0:
                        break

                block.append(lines[i])
                i += 1

            iterable = get_value(expr)

            if isinstance(iterable, int):
                iterable = range(iterable)

            for item in iterable:
                variables[var] = item
                execute(block)


        # IF / ELIF / ELSE

        elif line.startswith("if "):

'''

s = s.replace(marker, block, 1)

p.write_text(s)
print("[GI] v1.7 for loop added")
