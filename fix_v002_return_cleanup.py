from pathlib import Path

p = Path("gi_0.0.2.py")
lines = p.read_text().splitlines()

out = []
seen_return = False
i = 0

while i < len(lines):
    line = lines[i]

    if line.strip() == 'elif line.startswith("return ")':
        if seen_return:
            # Remove this duplicate RETURN block
            i += 1
            while i < len(lines):
                if 'raise GIReturn(value)' in lines[i]:
                    i += 1
                    break
                i += 1
            continue

        seen_return = True

    out.append(line)
    i += 1

p.write_text("\n".join(out) + "\n")
print("[GI] v0.0.2 duplicate RETURN handlers cleaned")
