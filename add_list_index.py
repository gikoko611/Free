path="gi.py"

with open(path,"r") as f:
    data=f.read()

old='''    if v in variables:
        return variables[v]


    # FUNCTION RETURN VALUE
'''

new='''    if v in variables:
        return variables[v]


    # LIST INDEX

    if "[" in v and v.endswith("]"):

        name = v.split("[",1)[0]

        index = v.split("[",1)[1][:-1]

        if name in variables:

            arr = variables[name]

            idx = int(get_value(index))

            return arr[idx]


    # FUNCTION RETURN VALUE
'''

if old in data:
    data=data.replace(old,new)
    with open(path,"w") as f:
        f.write(data)
    print("LIST INDEX ADDED")
else:
    print("TARGET NOT FOUND")
