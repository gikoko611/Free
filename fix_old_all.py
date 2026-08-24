path="gi.py"

with open(path) as f:
    data=f.read()

data=data.replace(
"variables.update(old)",
"variables.update(scope_stack.pop())"
)

with open(path,"w") as f:
    f.write(data)

print("old removed")
