p="gi.py"

with open(p) as f:
    s=f.read()

old='''      if v in variables:
          return variables[v]
'''

new='''      # LIST INDEX

      if "[" in v and v.endswith("]"):

          name=v.split("[",1)[0]

          index=v.split("[",1)[1][:-1]

          if name in variables:

              return variables[name][int(index)]


      if v in variables:
          return variables[v]
'''

if old in s:
    s=s.replace(old,new,1)

with open(p,"w") as f:
    f.write(s)

print("INDEX added")
