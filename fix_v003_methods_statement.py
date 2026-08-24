from pathlib import Path

p = Path("gi_0.0.3-dev.py")
s = p.read_text()

if "# COLLECTION METHOD STATEMENT" in s:
    print("[GI] Method statement patch already present")
    raise SystemExit

lines = s.splitlines(True)

# Find the actual FUNCTION CALL comment
idx = None
for i, line in enumerate(lines):
    if line.strip() == "# FUNCTION CALL":
        idx = i
        break

if idx is None:
    raise SystemExit("[GI] FUNCTION CALL comment not found")

patch = '''          # COLLECTION METHOD STATEMENT

          elif "." in line and "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):

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

lines.insert(idx, patch)
p.write_text("".join(lines))

print("[GI] v0.0.3-dev statement methods added")
