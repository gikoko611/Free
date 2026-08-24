p="gi.py"

with open(p) as f:
    lines=f.readlines()

for i,l in enumerate(lines):
    if 'while lines[i].strip()!="end":' in l:
        if i > 180 and i < 200:
            start=i
            break
else:
    print("not found")
    exit()

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
"                  i+=1\n"
]

lines=lines[:start]+new+lines[start+3:]

with open(p,"w") as f:
    f.writelines(lines)

print("function block fixed")
