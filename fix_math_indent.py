p="gi.py"

with open(p) as f:
    s=f.read()

s=s.replace("      # BASIC MATH\n","    # BASIC MATH\n")
s=s.replace("      for op in [\"+\",\"-\",\"*\",\"/\"]:\n","    for op in [\"+\",\"-\",\"*\",\"/\"]:\n")
s=s.replace("          if op in v:\n","        if op in v:\n")
s=s.replace("              try:\n","            try:\n")
s=s.replace("                  a,b=v.split(op,1)\n","                a,b=v.split(op,1)\n")
s=s.replace("                  a=get_value(a)\n","                a=get_value(a)\n")
s=s.replace("                  b=get_value(b)\n","                b=get_value(b)\n")
s=s.replace("                  if op==\"+\":\n","                if op==\"+\":\n")
s=s.replace("                  elif op==\"-\":\n","                elif op==\"-\":\n")
s=s.replace("                  elif op==\"*\":\n","                elif op==\"*\":\n")
s=s.replace("                  elif op==\"/\":\n","                elif op==\"/\":\n")
s=s.replace("                      return a+b\n","                    return a+b\n")
s=s.replace("                      return a-b\n","                    return a-b\n")
s=s.replace("                      return a*b\n","                    return a*b\n")
s=s.replace("                      return a//b\n","                    return a//b\n")
s=s.replace("              except:\n","            except:\n")
s=s.replace("                  pass\n","                pass\n")

with open(p,"w") as f:
    f.write(s)

print("math indent fixed")
