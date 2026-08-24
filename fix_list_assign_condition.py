path="gi.py"

with open(path) as f:
    data=f.read()

old='''          elif "[" in line and "]" in line and "=" in line:
'''

new='''          elif "[" in line and "]" in line and "=" in line and not line.split("=",1)[1].strip().startswith("["):
'''

if old in data:
    data=data.replace(old,new,1)

    with open(path,"w") as f:
        f.write(data)

    print("LIST ASSIGN CONDITION FIXED")
else:
    print("OLD CONDITION NOT FOUND")
