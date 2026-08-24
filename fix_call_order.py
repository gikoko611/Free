path="gi.py"

with open(path) as f:
    data=f.read()

old="""              scope_stack.append(variables.copy())
              variables.clear()

              values=[]

              for a in args:
                  values.append(get_value(a))

              for n,v in zip(
                  functions[name]["params"],
                  values
              ):
                  variables[n]=v
"""

new="""              values=[]

              for a in args:
                  values.append(get_value(a))

              scope_stack.append(variables.copy())
              variables.clear()

              for n,v in zip(
                  functions[name]["params"],
                  values
              ):
                  variables[n]=v
"""

if old not in data:
    print("block not found")
else:
    data=data.replace(old,new)
    print("call order fixed")

with open(path,"w") as f:
    f.write(data)
