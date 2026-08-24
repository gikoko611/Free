path="gi.py"

with open(path,"r") as f:
    lines=f.readlines()

out=[]
added=False

for line in lines:

    if line.strip()=="# VARIABLE" and not added:

        out.append("""          # LIST ASSIGNMENT

          elif "=" in line and "[" in line:

              k,v=line.split("=",1)

              name=k.split("[",1)[0].strip()

              index=k.split("[",1)[1][:-1]

              if name in variables:

                  variables[name][int(get_value(index))]=get_value(v)


""")
        added=True

    out.append(line)

with open(path,"w") as f:
    f.writelines(out)

if added:
    print("LIST ASSIGN ADDED")
else:
    print("VARIABLE MARK NOT FOUND")
