path="gi.py"

with open(path) as f:
    data=f.read()

marker='''    # LIST INDEX

    if "[" in v and v.endswith("]"):
'''

insert='''    # DICTIONARY VALUE

    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0].strip()

        key=v.split("[",1)[1][:-1].strip()

        if name in variables:

            obj=variables[name]

            if isinstance(obj, dict):

                key=key.strip('"').strip("'")

                return obj[key]


'''

if marker in data:
    data=data.replace(marker,insert+marker,1)

    with open(path,"w") as f:
        f.write(data)

    print("DICT READ ADDED")
else:
    print("MARKER NOT FOUND")
