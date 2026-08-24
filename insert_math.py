p="gi.py"

with open(p) as f:
    lines=f.readlines()

for i,l in enumerate(lines):
    if l.strip()=="return v":
        pos=i
        break
else:
    print("return v not found")
    exit()

code=[
"      # BASIC MATH\n",
"      for op in [\"+\",\"-\",\"*\",\"/\"]:\n",
"          if op in v:\n",
"              try:\n",
"                  a,b=v.split(op,1)\n",
"                  a=get_value(a)\n",
"                  b=get_value(b)\n",
"\n",
"                  if op==\"+\":\n",
"                      return a+b\n",
"                  elif op==\"-\":\n",
"                      return a-b\n",
"                  elif op==\"*\":\n",
"                      return a*b\n",
"                  elif op==\"/\":\n",
"                      return a//b\n",
"              except:\n",
"                  pass\n",
"\n"
]

lines=lines[:pos]+code+lines[pos:]

with open(p,"w") as f:
    f.writelines(lines)

print("math inserted")
