from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''    if v in variables:
        return variables[v]
'''

new='''    if v in variables:
        return variables[v]

    print("[GET_VALUE MISS]", v, "VARS=", variables)
'''

if old in s:
    s=s.replace(old,new,1)
    p.write_text(s)
    print("debug value OK")
else:
    print("not found")
