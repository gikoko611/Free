path="gi.py"

with open(path) as f:
    lines=f.readlines()

out=[]
skip=False

for line in lines:
    if "values=[]" in line:
        indent=line[:len(line)-len(line.lstrip())]
        out.append(line)
        skip=True
        continue

    if skip and (
        "for a in args:" in line or
        "values.append(get_value(a))" in line or
        "for n,v in zip(" in line or
        'functions[name]["params"]' in line or
        "values" == line.strip() or
        "):" == line.strip() or
        "variables[n]=v" in line
    ):
        if "for a in args:" in line:
            out.append(indent+"for a in args:\n")
        elif "values.append" in line:
            out.append(indent+"    values.append(get_value(a))\n")
        elif "for n,v in zip(" in line:
            out.append(indent+"for n,v in zip(\n")
        elif 'functions[name]["params"]' in line:
            out.append(indent+"    functions[name][\"params\"],\n")
        elif line.strip()=="values":
            out.append(indent+"    values\n")
        elif line.strip()=="):":
            out.append(indent+"):\n")
        elif "variables[n]=v" in line:
            out.append(indent+"    variables[n]=v\n")
        continue

    if skip and "result=None" in line:
        skip=False
        out.append(line)
        continue

    out.append(line)

with open(path,"w") as f:
    f.writelines(out)

print("indent fixed 2")
