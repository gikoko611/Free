path="gi.py"

with open(path,"r") as f:
    data=f.read()

old='''          # VARIABLE

          elif "=" in line:

              k,v=line.split("=",1)

              variables[k.strip()]=get_value(v)
'''

new='''          # LIST ASSIGNMENT

          elif "=" in line and "[" in line:

              k,v=line.split("=",1)

              name=k.split("[",1)[0].strip()

              index=k.split("[",1)[1][:-1]

              if name in variables:

                  variables[name][int(get_value(index))]=get_value(v)


          # VARIABLE

          elif "=" in line:

              k,v=line.split("=",1)

              variables[k.strip()]=get_value(v)
'''

if old in data:
    data=data.replace(old,new)
    with open(path,"w") as f:
        f.write(data)
    print("LIST ASSIGN ADDED")
else:
    print("TARGET NOT FOUND")
