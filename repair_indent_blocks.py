path="gi.py"

with open(path) as f:
    data=f.read()

# fix extra indentation
data=data.replace(
"""              values=[]

                for a in args:
                    values.append(get_value(a))

                for n,v in zip(
                    functions[name]["params"],
                    values
                ):
                    variables[n]=v
""",
"""              values=[]

              for a in args:
                  values.append(get_value(a))

              for n,v in zip(
                  functions[name]["params"],
                  values
              ):
                  variables[n]=v
"""
)

data=data.replace(
"""              values=[]

                for a in args:
                    values.append(get_value(a))

                scope_stack.append(variables.copy())
                variables.clear()
""",
"""              values=[]

              for a in args:
                  values.append(get_value(a))

              scope_stack.append(variables.copy())
              variables.clear()
"""
)

with open(path,"w") as f:
    f.write(data)

print("indent repaired")
