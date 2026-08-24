from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''        elif line.startswith("return "):

            value=line[7:]

            raise GIReturn(value)
'''

new='''        elif line.startswith("return "):

            value=get_value(line[7:])

            raise GIReturn(value)
'''

if old in s:
    s=s.replace(old,new)
    p.write_text(s)
    print("Return get_value patch OK")
else:
    print("Target not found")
