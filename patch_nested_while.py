p="gi.py"

with open(p) as f:
    s=f.read()

old='''          elif line.startswith("while "):
              condition = line[6:].strip()
              block=[]
              i+=1
              while i < len(lines) and lines[i].strip()!="end":
                  block.append(lines[i])
                  i+=1

              count=0
              while check_condition(condition):
                  execute(block)
                  count+=1
                  if count > 10000:
                      break
'''

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

if old in s:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("nested while fixed")
else:
    print("not found")
