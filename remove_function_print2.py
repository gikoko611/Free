p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if "if result is not None:" in l and i>280 and i<300:
        start=i
        break

if start is None:
    print("not found")
    exit()

end=start+2

lines=lines[:start]+[
"                  # return value ignored for statement call\n"
]+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("function print removed")
