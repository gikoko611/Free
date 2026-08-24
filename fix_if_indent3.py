p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if "# IF" in l:
        start=i
    if start is not None and "# FUNCTION CALL" in l:
        end=i
        break

if start is None or end is None:
    print("markers not found")
    exit()

new="""          # IF

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


"""

new_lines=new.splitlines(True)

lines=lines[:start]+new_lines+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("if block fixed")
