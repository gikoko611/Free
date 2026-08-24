path="gi.py"

with open(path) as f:
    data=f.read()

target='''          # VARIABLE

          elif "=" in line:
'''

insert='''          # LIST ASSIGNMENT

          elif "[" in line and "]" in line and "=" in line:

              left,right=line.split("=",1)

              name=left.split("[",1)[0].strip()

              index=left.split("[",1)[1][:-1]

              if name in variables:

                  variables[name][int(get_value(index))]=get_value(right)


'''

if target in data:
    data=data.replace(target,insert+target,1)

    with open(path,"w") as f:
        f.write(data)

    print("LIST ASSIGN ADDED")
else:
    print("TARGET NOT FOUND")
