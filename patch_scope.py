from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''                old=variables.copy()

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

new='''                old=variables.copy()

                variables.clear()

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

                if result is not None:
                    print(result)
'''

if old in s:
    s=s.replace(old,new)
    p.write_text(s)
    print("Function scope patch OK")
else:
    print("Target not found")
