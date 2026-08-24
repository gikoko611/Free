from pathlib import Path

p = Path("gi_0.0.2.py")
s = p.read_text()

marker = '''          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

insert = '''          # RETURN
          elif line.startswith("return "):
              value = get_value(line[7:].strip())
              raise GIReturn(value)

          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

if marker not in s:
    print("[GI] Exact FUNCTION CALL marker not found")
    raise SystemExit(1)

s = s.replace(marker, insert, 1)

# Remove later duplicate RETURN handler
needle = '''          elif line.startswith("return "):
              value = get_value(line[7:].strip())
              raise GIReturn(value)
'''

first = s.find(needle)
second = s.find(needle, first + len(needle))

if second != -1:
    s = s[:second] + s[second + len(needle):]

p.write_text(s)
print("[GI] v0.0.2 return priority fixed")
