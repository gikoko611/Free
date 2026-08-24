p="gi.py"

with open(p) as f:
    s=f.read()

old="""def run(file):

    with open(file) as f:
        execute(f.readlines())
"""

new="""def run(file):

    with open(file) as f:
        try:
            execute(f.readlines())
        except GIReturn as e:
            return e.args[0]
"""

if old not in s:
    print("old block not found")
else:
    s=s.replace(old,new)
    with open(p,"w") as f:
        f.write(s)
    print("run patched")
