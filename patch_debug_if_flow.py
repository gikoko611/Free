p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
done=False

for line in lines:
    out.append(line)

    if line.strip()=="execute(else_block)":
        indent=line[:len(line)-len(line.lstrip())]
        out.append(indent+"print('AFTER IF INDEX', i, 'NEXT', lines[i].strip() if i < len(lines) else 'END')\n")
        done=True

with open(p,"w") as f:
    f.writelines(out)

print("added" if done else "not found")
