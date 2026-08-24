p="gi.py"

with open(p) as f:
    s=f.read()

start=s.find('            elif line.startswith("while ")')
if start == -1:
    start=s.find('          elif line.startswith("while ")')

end=s.find('          elif line.startswith("say ")', start)

if start==-1 or end==-1:
    print("marker not found")
    exit()

new='''          elif line.startswith("while "):

              condition = line[6:].strip()
              block=[]

              i+=1
              depth=1

              while i < len(lines) and depth>0:

                  current=lines[i].strip()

                  if current.startswith("while "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  block.append(lines[i])
                  i+=1

              count=0

              while check_condition(condition):
                  execute(block)
                  count+=1

                  if count > 10000:
                      break


'''

s=s[:start]+new+s[end:]

with open(p,"w") as f:
    f.write(s)

print("while fixed")
