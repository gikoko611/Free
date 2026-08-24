from pathlib import Path

p=Path("gi.py")
s=p.read_text()

s=s.replace('''    print("[GET_VALUE MISS]", v, "VARS=", variables)
''','')

p.write_text(s)

print("Value debug removed")
