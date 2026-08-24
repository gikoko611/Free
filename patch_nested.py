p="gi.py"

with open(p) as f:
    s=f.read()

old="""              block=[]

              i+=1

              while lines[i].strip()!="end":
                  block.append(lines[i])
                  i+=1
"""

new="""              block=[]

              i+=1
              depth=1

              while i < len(lines) and depth > 0:
                  current=lines[i].strip()

                  if current.startswith("if ") or current.startswith("function "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  block.append(lines[i])
                  i+=1
"""

if old in s:
    s=s.replace(old,new,1)
    with open(p,"w") as f:
        f.write(s)
    print("nested if patched")
else:
    print("pattern not found")
