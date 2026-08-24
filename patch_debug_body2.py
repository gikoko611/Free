p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
done=False

for line in lines:
    out.append(line)

    if line.strip()=="if name in functions:" and not done:
        indent=line[:len(line)-len(line.lstrip())]
        out.append(indent+"    print('DEBUG BODY', functions[name]['code'])\n")
        done=True

with open(p,"w") as f:
    f.writelines(out)

print("debug inserted" if done else "not found")
