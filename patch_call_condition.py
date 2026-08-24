from pathlib import Path

p=Path("gi.py")
s=p.read_text()

old='''        elif "(" in line and line.endswith(")"):
'''

new='''        elif "(" in line and line.endswith(")") and "=" not in line:
'''

if old not in s:
    print("Target not found")
else:
    s=s.replace(old,new,1)
    p.write_text(s)
    print("Function call condition fixed")
