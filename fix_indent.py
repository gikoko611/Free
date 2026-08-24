p="gi.py"

with open(p) as f:
    s=f.read()

start=s.find("          # WHILE")
end=s.find("          # SAY", start)

if start!=-1 and end!=-1:
    s=s[:start]+s[end:]

    insert='''          # WHILE

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

    s=s.replace("          # SAY", insert+"          # SAY",1)

with open(p,"w") as f:
    f.write(s)

print("fixed")
