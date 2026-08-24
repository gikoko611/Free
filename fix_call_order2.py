import re

path="gi.py"

with open(path) as f:
    data=f.read()

pattern=r'''scope_stack\.append\(variables\.copy\(\)\)
\s*variables\.clear\(\)

\s*values=\[\]

\s*for a in args:
\s*values\.append\(get_value\(a\)\)'''

replacement='''values=[]

              for a in args:
                  values.append(get_value(a))

              scope_stack.append(variables.copy())
              variables.clear()'''

data,count=re.subn(pattern,replacement,data)

print("patched:",count)

with open(path,"w") as f:
    f.write(data)
