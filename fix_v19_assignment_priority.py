from pathlib import Path

p = Path("gi_v1.9.py")
s = p.read_text()

needle = '''          # VARIABLE

          elif "=" in line:
'''

replacement = '''          # VARIABLE

          elif "=" in line:
              k, v = line.split("=", 1)
              variables[k.strip()] = get_value(v)
'''

if needle in s:
    s = s.replace(needle, replacement, 1)
    p.write_text(s)
    print("[GI] v1.9 assignment priority fixed")
else:
    print("[GI] Assignment block already fixed or pattern changed")
