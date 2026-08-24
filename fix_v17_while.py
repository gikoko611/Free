from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

marker = '''        # FUNCTION CALL

        elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

block = '''        # WHILE

        elif line.startswith("while "):

            condition=line[6:].strip()
            block=[]

            i+=1
            depth=1

            while i < len(lines) and depth > 0:

                current=lines[i].strip()

                if current.startswith("while "):
                    depth+=1

                if current.startswith("if "):
                    depth+=1

                if current.startswith("function "):
                    depth+=1

                if current=="end":
                    depth-=1
                    if depth==0:
                        break

                block.append(lines[i])
                i+=1

            guard=0

            while check_condition(condition):

                execute(block)

                guard+=1
                if guard > 100000:
                    raise GIRuntimeError("While loop limit exceeded")


        # FUNCTION CALL

        elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

if marker not in s:
    print("[GI] WHILE target not found")
    raise SystemExit(1)

s=s.replace(marker, block, 1)

p.write_text(s)
print("[GI] v1.7 while loop added")
