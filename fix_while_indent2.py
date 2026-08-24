p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
inside=False

for line in lines:

    if 'elif line.startswith("while ")' in line:
        inside=True
        out.append('          elif line.startswith("while "):\n')
        continue

    if inside:
        if 'elif line.startswith("say ")' in line:
            inside=False
            out.append(line)
        else:
            # while block ကို ဒီ patch က မပြင်ဘူး
            out.append(line)
    else:
        out.append(line)

with open(p,"w") as f:
    f.writelines(out)

print("while elif fixed")
