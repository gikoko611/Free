from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = '''        # FUNCTION CALL

        elif "(" in line and line.endswith(")"):

            name=line.split("(")[0]

            argtext=line.split("(",1)[1][:-1]

            args=[]

            if argtext.strip():
                args=[x.strip() for x in argtext.split(",")]

            if name in functions:

                block=functions[name]["code"]

                try:
                    execute(block)

                except GIReturn as e:
                    if e.value is not None:
                        print(e.value)
'''

new = '''        # FUNCTION CALL

        elif "(" in line and line.endswith(")"):

            name=line.split("(")[0]

            argtext=line.split("(",1)[1][:-1]

            args=[]

            if argtext.strip():
                args=[x.strip() for x in argtext.split(",")]

            if name in functions:

                old=variables.copy()

                for n,a in zip(
                    functions[name]["params"],
                    args
                ):
                    variables[n]=get_value(a)

                try:
                    execute(
                        functions[name]["code"]
                    )

                except GIReturn as e:
                    if e.value is not None:
                        print(e.value)

                variables=old
'''

if old not in s:
    print("Target not found")
else:
    s=s.replace(old,new)
    p.write_text(s)
    print("Function call parameter patch OK")
