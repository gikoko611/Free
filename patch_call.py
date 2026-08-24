from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = '''        # MODULE CALL

        elif "." in line and not line.startswith("say "):
'''

new = '''        # FUNCTION CALL

        elif "(" in line and line.endswith(")"):

            name=line.split("(")[0]

            argtext=line.split("(",1)[1][:-1]

            args=[]

            if argtext.strip():
                args=[x.strip() for x in argtext.split(",")]

            if name in functions:

                block=functions[name]["body"]

                try:
                    execute(block)

                except GIReturn as e:
                    if e.value is not None:
                        print(e.value)


        # MODULE CALL

        elif "." in line and not line.startswith("say "):
'''

if old not in s:
    print("Target not found")
else:
    s=s.replace(old,new)
    p.write_text(s)
    print("Function call patch OK")
