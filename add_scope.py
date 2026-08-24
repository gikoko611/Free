from pathlib import Path

p = Path("gi.py")
s = p.read_text()

s = s.replace(
"variables = {}\nfunctions = {}",
"variables = {}\nscope_stack = []\nfunctions = {}"
)

p.write_text(s)

print("Scope stack added")
