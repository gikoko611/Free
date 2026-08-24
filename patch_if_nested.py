p="gi.py"

with open(p) as f:
    s=f.read()

old="""              while lines[i].strip()!="end":
                  block.append(lines[i])
                  i+=1
"""

new="""              depth=1

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
"""

if old not in s:
    print("old block not found")
else:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("nested if patched")
