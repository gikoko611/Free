from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''    if v in variables:
        return variables[v]

    if v.startswith('"') and v.endswith('"'):
'''

new='''    if v in variables:
        return variables[v]

    # FUNCTION RETURN VALUE

    if "(" in v and v.endswith(")"):
        name=v.split("(",1)[0]

        argtext=v.split("(",1)[1][:-1]

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

            result=None

            try:
                execute(
                    functions[name]["code"]
                )

            except GIReturn as e:
                result=e.value

            variables.clear()
            variables.update(old)

            return result


    if v.startswith('"') and v.endswith('"'):
'''

if old not in s:
    print("Target not found")
else:
    s=s.replace(old,new)
    p.write_text(s)
    print("Return value patch OK")
