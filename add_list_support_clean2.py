path="gi.py"

with open(path) as f:
    data=f.read()

marker='''    if v in variables:
        return variables[v]


'''

insert='''    # LIST VALUE

    if v.startswith("[") and v.endswith("]"):

        inside=v[1:-1]

        if not inside.strip():
            return []

        return [
            get_value(x.strip())
            for x in split_args(inside)
        ]


    # LIST INDEX

    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0]

        index=v.split("[",1)[1][:-1]

        if name in variables:

            arr=variables[name]

            idx=int(get_value(index))

            return arr[idx]


'''

if marker in data:
    data=data.replace(marker, marker+insert,1)

    with open(path,"w") as f:
        f.write(data)

    print("LIST SUPPORT RESTORED")

else:
    print("MARKER NOT FOUND")
