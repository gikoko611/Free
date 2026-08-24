import re

p="gi.py"

with open(p) as f:
    s=f.read()

if "# LIST INDEX" not in s:

    pattern=r'(def get_value\(v\):\n\n      v = v\.strip\(\)\n)'

    insert=r'''\1

      # LIST INDEX

      if "[" in v and v.endswith("]"):

          name=v.split("[",1)[0]

          index=v.split("[",1)[1][:-1]

          if name in variables:

              return variables[name][int(index)]

'''

    s=re.sub(pattern, insert, s, count=1)

    with open(p,"w") as f:
        f.write(s)

print("forced")
