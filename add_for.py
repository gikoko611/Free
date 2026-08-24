p="gi.py"

with open(p) as f:
    s=f.read()

marker="        # SAY"

code='''        # FOR

        elif line.startswith("for "):

            parts=line.split()

            var=parts[1]

            count=int(get_value(parts[3]))

            block=[]

            i+=1

            while i < len(lines):

                current=lines[i].strip()

                if current=="end":
                    break

                block.append(lines[i])

                i+=1

            for n in range(count):

                variables[var]=n

                execute(block)


'''

if "# FOR" not in s:
    s=s.replace(marker, code+marker,1)

with open(p,"w") as f:
    f.write(s)

print("FOR added")
