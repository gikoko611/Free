p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
skip=False

for line in lines:
    if line.lstrip().startswith('elif line.startswith("while ")'):
        skip=True
        continue

    if skip:
        if line.lstrip().startswith('elif line.startswith("say ")'):
            skip=False
            out.append(line)
        else:
            continue
    else:
        out.append(line)

with open(p,"w") as f:
    f.writelines(out)

print("old while removed")
