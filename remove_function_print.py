p="gi.py"

with open(p) as f:
    s=f.read()

old="""                  if result is not None:
                      print(result)
"""

new="""                  # return value handled by expression
"""

if old not in s:
    print("not found")
else:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("function print removed")
