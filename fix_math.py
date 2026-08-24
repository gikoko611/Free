path="gi.py"

with open(path) as f:
    data=f.read()

old="""    # BASIC MATH
    for op in ["+","-","*","/"]:
        if op in v:
            try:
                a,b=v.split(op,1)
                a=get_value(a)
                b=get_value(b)

                if op=="+":
                    return a+b
                elif op=="-":
                    return a-b
                elif op=="*":
                    return a*b
                elif op=="/":
                    return a//b
            except:
                pass
"""

new="""    # BASIC MATH
    for op in ["+","-","*","/"]:
        if op in v:
            try:
                left,right=v.split(op,1)

                left=get_value(left.strip())
                right=get_value(right.strip())

                if op=="+":
                    return left+right

                if op=="-":
                    return left-right

                if op=="*":
                    return left*right

                if op=="/":
                    return left//right

            except:
                pass
"""

if old in data:
    data=data.replace(old,new)
else:
    print("math block not found")

with open(path,"w") as f:
    f.write(data)

print("math fixed")
