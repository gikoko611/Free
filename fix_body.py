from pathlib import Path

p=Path("gi.py")
s=p.read_text()

s=s.replace('functions[name]["body"]','functions[name]["code"]')

p.write_text(s)

print("body -> code fixed")
