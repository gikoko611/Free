from pathlib import Path

p = Path("gi.py")
lines = p.read_text().splitlines()

start = 326 - 1
end = 378 - 1

new_block = '''        # FUNCTION CALL

        elif "(" in line and line.endswith(")") and "=" not in line:

            name=line.split("(")[0]

            argtext=line.split("(",1)[1][:-1]

            args=[]

            if argtext.strip():
                args=split_args(argtext)

            if name not in functions:
                print("[GI Error] Function not found:", name)
                continue

            params=functions[name]["params"]

            if len(args) < len(params):
                print("[GI Error] Missing argument")
                continue

            if len(args) > len(params):
                print("[GI Error] Too many arguments")
                continue

            old=variables.copy()

            for n,a in zip(
                functions[name]["params"],
                args
            ):
                variables[n]=get_value(a)

            result=None

            try:
                execute(
                    functions[name]["code"]
                )
            except GIReturn as e:
                result=e.value

            variables.clear()
            variables.update(old)

            # return value ignored for statement call


        # MODULE CALL
'''.splitlines()

lines[start:end] = new_block

p.write_text("\\n".join(lines) + "\\n")
print("[GI] FUNCTION CALL block rebuilt")
