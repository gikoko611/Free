from pathlib import Path

p=Path("gi.py")
s=p.read_text()

start=s.find("        # FUNCTION CALL\n\n        elif line.split()[0] in functions:")

end=s.find("        # IF", start)

if start != -1 and end != -1:
    s=s[:start] + s[end:]
    p.write_text(s)
    print("Old function call removed")
else:
    print("Old block not found")
