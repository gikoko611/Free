p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if "depth=1" in l and i > 180 and i < 200:
        start=i
        break

for i in range(start, len(lines)):
    if "functions[name]={" in lines[i]:
        end=i
        break

new=[
"              depth=1\n",
"\n",
"              while i < len(lines) and depth>0:\n",
"\n",
"                  current=lines[i].strip()\n",
"\n",
"                  if current.startswith(\"function \") or current.startswith(\"if \"):\n",
"                      depth+=1\n",
"\n",
"                  if current==\"end\":\n",
"                      depth-=1\n",
"                      if depth==0:\n",
"                          break\n",
"\n",
"                  block.append(lines[i])\n",
"                  i+=1\n",
"\n",
]

lines=lines[:start]+new+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("function indentation fixed")
