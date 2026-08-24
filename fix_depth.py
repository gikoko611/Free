p="gi.py"

with open(p) as f:
    s=f.read()

s=s.replace("              depth=1\n", "            depth=1\n")
s=s.replace("              while i < len(lines) and depth>0:\n", "            while i < len(lines) and depth>0:\n")

with open(p,"w") as f:
    f.write(s)

print("indent fixed")
