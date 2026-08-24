p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None

for i,l in enumerate(lines):
    if i>450 and l.strip()=="# IF":
        start=i
        break

if start is None:
    print("duplicate IF not found")
    exit()

# remove until FUNCTION CALL or end of file
end=start

for i in range(start+1,len(lines)):
    if "# FUNCTION CALL" in lines[i]:
        end=i
        break
else:
    end=len(lines)

lines=lines[:start]+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("duplicate IF removed")
