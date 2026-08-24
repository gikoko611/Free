p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
done=False

for line in lines:
    out.append(line)

    if 'elif "(" in line and line.endswith(")") and "=" not in line:' in line:
        indent=line[:len(line)-len(line.lstrip())]
        out.append(indent+"    print('CALLING', line)\n")
        done=True

with open(p,"w") as f:
    f.writelines(out)

print("added" if done else "not found")
