p="gi.py"

with open(p) as f:
    s=f.read()

start=s.index("          # IF")
end=s.index("          # FUNCTION CALL")

new='''          # IF

          elif line.startswith("if "):

              condition=line[3:]

              block=[]

              i+=1
              depth=1

              while i < len(lines) and depth>0:

                  current=lines[i].strip()

                  if current.startswith("if "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  block.append(lines[i])
                  i+=1

              if check_condition(condition):
                  execute(block)


'''

s=s[:start]+new+s[end:]

with open(p,"w") as f:
    f.write(s)

print("indent fixed")
