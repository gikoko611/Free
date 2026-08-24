import re

path="gi.py"

with open(path) as f:
    data=f.read()

pattern=r'''for n,a in zip\(
\s*functions\[name\]\["params"\],
\s*args
\s*\):
\s*variables\[n\]=get_value\(a\)'''

replacement='''values=[]

              for a in args:
                  values.append(get_value(a))

              for n,v in zip(
                  functions[name]["params"],
                  values
              ):
                  variables[n]=v'''

data,newcount=re.subn(pattern,replacement,data)

print("patched:",newcount,"locations")

with open(path,"w") as f:
    f.write(data)
