p="gi.py"

with open(p) as f:
    s=f.read()

old="""      if v.isdigit():
          return int(v)

      return v
"""

new="""      if v.isdigit():
          return int(v)

      # BASIC MATH EXPRESSION
      try:
          if any(op in v for op in ["+","-","*","/"]):
              parts=[]

              for op in ["+","-","*","/"]:
                  if op in v:
                      a,b=v.split(op,1)

                      a=get_value(a)
                      b=get_value(b)

                      if op=="+":
                          return a+b

                      if op=="-":
                          return a-b

                      if op=="*":
                          return a*b

                      if op=="/":
                          return a//b

      except:
          pass

      return v
"""

if old not in s:
    print("pattern not found")
else:
    s=s.replace(old,new,1)

    with open(p,"w") as f:
        f.write(s)

    print("math patched")
