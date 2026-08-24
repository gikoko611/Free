p="gi.py"

with open(p) as f:
    s=f.read()

marker="          # FUNCTION CALL"

code=r'''
          # WHILE

          elif line.startswith("while "):

              condition=line[6:]

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


              while check_condition(condition):
                  execute(block)


'''

if marker in s:
    s=s.replace(marker,code+marker,1)

    with open(p,"w") as f:
        f.write(s)

    print("while added")
else:
    print("marker not found")
