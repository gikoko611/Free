path="gi.py"

with open(path,"r") as f:
    lines=f.readlines()

out=[]
skip=False

for line in lines:

    if line.strip()=="# LIST ASSIGNMENT":
        skip=True
        continue

    if skip:
        if line.strip()=="# VARIABLE":
            skip=False

            out.extend([
"          # LIST ASSIGNMENT\n",
"\n",
"          elif \"=\" in line and \"[\" in line:\n",
"\n",
"              k,v=line.split(\"=\",1)\n",
"\n",
"              name=k.split(\"[\",1)[0].strip()\n",
"\n",
"              index=k.split(\"[\",1)[1][:-1]\n",
"\n",
"              if name in variables:\n",
"\n",
"                  variables[name][int(get_value(index))]=get_value(v)\n",
"\n",
"\n",
"          # VARIABLE\n"
            ])

            continue
        else:
            continue

    out.append(line)

with open(path,"w") as f:
    f.writelines(out)

print("VARIABLE BLOCK FIXED")
