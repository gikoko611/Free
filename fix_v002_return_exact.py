from pathlib import Path

p = Path("gi_0.0.2.py")
lines = p.read_text().splitlines()

return_positions = [
    i for i, line in enumerate(lines)
    if line.strip() == 'elif line.startswith("return ")'
]

print("[GI] RETURN handlers found:", len(return_positions))

if len(return_positions) < 1:
    raise SystemExit("[GI] RETURN handler not found")

# Keep the first RETURN handler only.
keep = return_positions[0]

out = []
i = 0

while i < len(lines):
    line = lines[i]

    if line.strip() == 'elif line.startswith("return ")':
        if i != keep:
            # Skip this return handler and its two body lines.
            i += 1
            while i < len(lines):
                if 'raise GIReturn(value)' in lines[i]:
                    i += 1
                    break
                i += 1
            continue

    out.append(line)
    i += 1

p.write_text("\n".join(out) + "\n")

print("[GI] RETURN cleanup complete")
