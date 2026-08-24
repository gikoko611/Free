p="gi.py"

with open(p) as f:
    s=f.read()

old='''              else:
                  execute(else_block)


          # FUNCTION CALL
'''

new='''              else:
                  execute(else_block)

              i+=1


          # FUNCTION CALL
'''

if old in s:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("if index fixed")
else:
    print("not found")
