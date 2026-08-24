path="gi.py"

with open(path) as f:
    data=f.read()

data=data.replace(
"""variables.clear()
variables.update(old)""",
"""variables.clear()
variables.update(scope_stack.pop())"""
)

with open(path,"w") as f:
    f.write(data)

print("scope fix applied")
