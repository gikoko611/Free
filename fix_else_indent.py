p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if l.strip()=="# IF":
        start=i+2
        break

for i in range(start,len(lines)):
    if l.strip().startswith("# FUNCTION CALL"):
        end=i-1
        break

new="""        elif line.startswith("if "):

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


"""

lines=lines[:start]+new.splitlines(True)+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("if else indent fixed")
