p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]

for line in lines:
    if "print('CALLING'," in line:
        continue
    if "print('DEBUG CALL'," in line:
        continue
    out.append(line)

with open(p,"w") as f:
    f.writelines(out)

print("debug removed")
