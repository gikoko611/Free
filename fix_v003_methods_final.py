from pathlib import Path

p = Path("gi_0.0.3-dev.py")
s = p.read_text()

# Add len() support if not already present
if 'if v.startswith("len(")' not in s:
    marker = '    # FUNCTION RETURN VALUE'
    if marker not in s:
        raise SystemExit("[GI] get_value marker not found")

    insert = '''    # BUILTIN LENGTH
    if v.startswith("len(") and v.endswith(")"):
        target = get_value(v[4:-1].strip())
        return len(target)

'''
    s = s.replace(marker, insert + marker, 1)

# Find FUNCTION CALL block and insert BEFORE its elif
needle = '''          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

if '# COLLECTION METHOD STATEMENT' not in s:
    pos = s.find(needle)

    if pos == -1:
        raise SystemExit("[GI] FUNCTION CALL elif not found")

    patch = '''          elif "." in line and "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):

              objname = line.split(".", 1)[0].strip()
              method_part = line.split(".", 1)[1]
              method = method_part.split("(", 1)[0].strip()
              argtext = method_part.split("(", 1)[1][:-1].strip()

              if objname in variables:
                  obj = variables[objname]
                  args = split_args(argtext) if argtext else []
                  values = [get_value(x) for x in args]

                  if method == "append" and isinstance(obj, list):
                      if len(values) != 1:
                          raise GIRuntimeError("append() expects 1 argument")
                      obj.append(values[0])

                  elif method == "remove" and isinstance(obj, list):
                      if len(values) != 1:
                          raise GIRuntimeError("remove() expects 1 argument")
                      obj.remove(values[0])

                  elif method == "pop" and isinstance(obj, list):
                      obj.pop(values[0] if values else -1)

                  elif method == "clear" and isinstance(obj, list):
                      obj.clear()

                  else:
                      raise GIRuntimeError("Unknown collection method: " + method)

'''

    # IMPORTANT: convert elif -> new elif chain correctly
    s = s[:pos] + patch + s[pos:]

p.write_text(s)
print("[GI] v0.0.3-dev collection methods fixed")
