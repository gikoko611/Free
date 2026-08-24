path="gi.py"

with open(path) as f:
    data=f.read()

old='index=left.split("[",1)[1][:-1]'

new='index=left.split("[",1)[1].split("]",1)[0].strip()'

if old in data:
    data=data.replace(old,new,1)

    with open(path,"w") as f:
        f.write(data)

    print("INDEX FIXED")
else:
    print("NOT FOUND")
