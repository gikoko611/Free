p="gi.py"

with open(p) as f:
    s=f.read()

marker='''          # SAY
'''

while_code='''          # WHILE

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

if while_code not in s:
    s=s.replace(marker, while_code+marker, 1)

with open(p,"w") as f:
    f.write(s)

print("WHILE inserted")
