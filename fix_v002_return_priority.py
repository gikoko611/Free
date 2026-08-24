from pathlib import Path

p = Path("gi_0.0.2.py")
s = p.read_text()

old = '''          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

new = '''          # RETURN
          elif line.startswith("return "):
              value = get_value(line[7:].strip())
              raise GIReturn(value)

          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

if old not in s:
    print("[GI] FUNCTION CALL insertion point not found")
    raise SystemExit(1)

s = s.replace(old, new, 1)

# Remove the old RETURN handler so it does not duplicate
old_return = '''          elif line.startswith("return "):
              value = get_value(line[7:].strip())
              raise GIReturn(value)
'''

# Keep the first occurrence, remove the second
first = s.find(old_return)
second = s.find(old_return, first + len(old_return))

if second != -1:
    s = s[:second] + s[second + len(old_return):]

p.write_text(s)
print("[GI] v0.0.2 return priority fixed")
