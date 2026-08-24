from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''            k,v=line.split("=",1)

            variables[k.strip()]=get_value(v)
'''

new='''            k,v=line.split("=",1)

            value=get_value(v)

            print("[DEBUG]", k.strip(), "=", value)

            variables[k.strip()]=value
'''

if old in s:
    s=s.replace(old,new)
    p.write_text(s)
    print("Debug variable OK")
else:
    print("Target not found")
