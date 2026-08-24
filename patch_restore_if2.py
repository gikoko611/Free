p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
added=False

if_code = '''
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


'''

for line in lines:
    if "# FUNCTION CALL" in line and not added:
        out.append(if_code)
        added=True
    out.append(line)

if added:
    with open(p,"w") as f:
        f.writelines(out)
    print("IF restored")
else:
    print("FUNCTION CALL not found")
