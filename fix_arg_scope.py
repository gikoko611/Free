path="gi.py"

with open(path) as f:
    data=f.read()

old="""scope_stack.append(variables.copy())
variables.clear()

for n,a in zip(
    functions[name]["params"],
    args
):
    variables[n]=get_value(a)
"""

new="""values=[]

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

count=data.count(old)

data=data.replace(old,new)

with open(path,"w") as f:
    f.write(data)

print("patched:",count,"locations")
