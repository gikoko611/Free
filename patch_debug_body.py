p="gi.py"

with open(p) as f:
    s=f.read()

old='''              if name in functions:

                  old=variables.copy()
'''

new='''              if name in functions:

                  print("DEBUG BODY", functions[name]["code"])

                  old=variables.copy()
'''

if old in s:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("debug body added")
else:
    print("pattern not found")
