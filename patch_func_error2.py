from pathlib import Path

p = Path("gi.py")
s = p.read_text()

old = "              if name in functions:\n"

new = """              if name not in functions:
                  print("[GI Error] Function not found:", name)
                  continue

              params=functions[name]["params"]

              if len(args) < len(params):
                  print("[GI Error] Missing argument")
                  continue

              if len(args) > len(params):
                  print("[GI Error] Too many arguments")
                  continue

"""

if old in s:
    s=s.replace(old,new,1)
    p.write_text(s)
    print("Function error patch applied")
else:
    print("Target line not found")
