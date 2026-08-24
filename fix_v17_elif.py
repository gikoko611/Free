from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''        # IF

        elif line.startswith("if "):
'''

new = '''        # IF / ELIF / ELSE

        elif line.startswith("if "):

'''

if old not in s:
    print("[GI] IF target not found")
    raise SystemExit(1)

# We will replace the complete IF block up to FUNCTION CALL.
start = s.index(old)
end_marker = '''        # FUNCTION CALL
'''
end = s.index(end_marker, start)

new_block = '''        # IF / ELIF / ELSE

        elif line.startswith("if "):

            branches = []
            condition = line[3:].strip()
            block = []

            i += 1
            depth = 1

            while i < len(lines) and depth > 0:

                current = lines[i].strip()

                if current.startswith("if "):
                    depth += 1

                elif current.startswith("while "):
                    depth += 1

                elif current == "end":
                    depth -= 1
                    if depth == 0:
                        break

                if depth == 1 and (
                    current.startswith("elif ") or
                    current == "else"
                ):
                    branches.append((condition, block))

                    if current.startswith("elif "):
                        condition = current[5:].strip()
                    else:
                        condition = None

                    block = []

                else:
                    block.append(lines[i])

                i += 1

            branches.append((condition, block))

            executed = False

            for cond, branch in branches:
                if cond is None or check_condition(cond):
                    execute(branch)
                    executed = True
                    break


        # FUNCTION CALL

'''

s = s[:start] + new_block + s[end + len(end_marker):]

p.write_text(s)
print("[GI] v1.7 elif support added")
