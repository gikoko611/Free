p="gi.py"

with open(p) as f:
    s=f.read()

old='''          elif "(" in line and line.endswith(")") and "=" not in line:

              name=line.split("(")[0]
'''

new='''          elif "(" in line and line.endswith(")") and "=" not in line:

              print("CALLING", line)

              name=line.split("(")[0]
'''

if old in s:
    s=s.replace(old,new,1)
    with open(p,"w") as f:
        f.write(s)
    print("call debug added")
else:
    print("not found")
