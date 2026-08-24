p="gi.py"

with open(p) as f:
    s=f.read()

marker='''              functions[name]={
                  "params":params,
                  "code":block
              }


          # FUNCTION CALL
'''

insert='''              functions[name]={
                  "params":params,
                  "code":block
              }


          # IF

          elif line.startswith("if "):

              condition=line[3:]

              block=[]
              else_block=[]

              i+=1
              depth=1
              in_else=False

              while i < len(lines) and depth>0:

                  current=lines[i].strip()

                  if current.startswith("if "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  if current=="else" and depth==1:
                      in_else=True
                  elif in_else:
                      else_block.append(lines[i])
                  else:
                      block.append(lines[i])

                  i+=1

              if check_condition(condition):
                  execute(block)
              else:
                  execute(else_block)


          # FUNCTION CALL
'''

if marker in s:
    s=s.replace(marker,insert,1)

    with open(p,"w") as f:
        f.write(s)

    print("IF restored")
else:
    print("marker not found")
