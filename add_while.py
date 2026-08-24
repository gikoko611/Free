p="gi.py"

with open(p) as f:
    s=f.read()

mark="          # SAY\n"

code='''          # WHILE

          elif line.startswith("while "):

              condition=line[6:]

              block=[]

              i+=1

              while i < len(lines):

                  current=lines[i].strip()

                  if current=="end":
                      break

                  block.append(lines[i])

                  i+=1

              while check_condition(condition):
                  execute(block)


'''

s=s.replace(mark,code+mark,1)

with open(p,"w") as f:
    f.write(s)

print("WHILE added")
