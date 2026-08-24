path="gi.py"

with open(path,"r") as f:
    data=f.read()

start=data.find("          # LIST ASSIGNMENT")
end=data.find("          # VARIABLE", start)

if start != -1 and end != -1:

    block='''          # LIST ASSIGNMENT

          elif "=" in line and "[" in line:

              k,v=line.split("=",1)

              name=k.split("[",1)[0].strip()

              index=k.split("[",1)[1][:-1]

              if name in variables:

                  variables[name][int(get_value(index))]=get_value(v)


'''

    data=data[:start]+block+data[end:]

    with open(path,"w") as f:
        f.write(data)

    print("REBUILT")
else:
    print("BLOCK NOT FOUND")
