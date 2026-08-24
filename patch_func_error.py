from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = '''              if name in functions:

                  old=variables.copy()
'''

new = '''              if name not in functions:
                  print("[GI Error] Function not found:", name)
                  continue

              params=functions[name]["params"]

              if len(args) < len(params):
                  print("[GI Error] Missing argument")
                  continue

              if len(args) > len(params):
                  print("[GI Error] Too many arguments")
                  continue

              old=variables.copy()
'''

if old in s:
    s=s.replace(old,new)
    p.write_text(s)
    print("Function error patch applied")
else:
    print("Still not found, checking raw spaces")
