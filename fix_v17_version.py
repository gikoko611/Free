from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

s = s.replace('print("GI Language v1.6")', 'print("GI Language v1.7")')
s = s.replace('VERSION = "1.6"', 'VERSION = "1.7"')

p.write_text(s)
print("[GI] v1.7 version fixed")
