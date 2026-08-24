from pathlib import Path

p = Path("gi.py")
lines = p.read_text().splitlines()

for i, line in enumerate(lines):
    if 'print("GI Language v0.9")' in line:
        lines[i] = '        print("GI Language v1.6")'

# Remove unsafe global result print
lines = [
    line for line in lines
    if line.strip() != "if result is not None:" and
       line.strip() != "print(result)"
]

p.write_text("\n".join(lines) + "\n")
print("[GI] Version/result fix applied")
