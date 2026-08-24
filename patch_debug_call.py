p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
done=False

for line in lines:
    out.append(line)

    if line.strip()=="if name in functions:" and 500 < len(out) < 550 and not done:
        indent=line[:len(line)-len(line.lstrip())]
        out.append(indent+"    print('DEBUG CALL', name, functions[name]['code'])\n")
        done=True

with open(p,"w") as f:
    f.writelines(out)

print("debug call inserted" if done else "not found")
