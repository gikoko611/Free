from pathlib import Path

p = Path("gi_0.0.2.py")
lines = p.read_text().splitlines()

# Remove every existing RETURN handler
clean = []
skip = False

for line in lines:
    if line.strip() == 'elif line.startswith("return ")':
        skip = True
        continue

    if skip:
        if 'raise GIReturn(value)' in line:
            skip = False
            continue
        if line.strip() and not line.startswith(" "):
            skip = False

    clean.append(line)

lines = clean

# Find FUNCTION CALL
pos = None
for i, line in enumerate(lines):
    if line.strip() == "# FUNCTION CALL":
        pos = i
        break

if pos is None:
    print("[GI] FUNCTION CALL not found")
    raise SystemExit(1)

# Use same indentation as FUNCTION CALL comment
indent = lines[pos][:len(lines[pos]) - len(lines[pos].lstrip())]

return_block = [
    indent + '# RETURN',
    indent + 'elif line.startswith("return "):',
    indent + '    value = get_value(line[7:].strip())',
    indent + '    raise GIReturn(value)',
    ''
]

lines[pos:pos] = return_block

p.write_text("\n".join(lines) + "\n")

print("[GI] v0.0.2 return priority fixed")
