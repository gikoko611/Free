path="gi.py"

with open(path,"r") as f:
    data=f.read()

old='''    if v in variables:
        return variables[v]


    # LIST INDEX
'''

new='''    if v in variables:
        return variables[v]


    # LIST VALUE

    if v.startswith("[") and v.endswith("]"):

        inside = v[1:-1]

        if not inside.strip():
            return []

        return [
            get_value(x.strip())
            for x in split_args(inside)
        ]


    # LIST INDEX
'''

if old in data:
    data=data.replace(old,new)
    with open(path,"w") as f:
        f.write(data)
    print("LIST VALUE ADDED")
else:
    print("TARGET NOT FOUND")
