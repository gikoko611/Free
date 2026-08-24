p="gi.py"

with open(p) as f:
    s=f.read()

s=s.replace(
'''          elif line.startswith("if "):''',
'''        elif line.startswith("if "):'''
)

with open(p,"w") as f:
    f.write(s)

print("fixed")
