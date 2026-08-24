from pathlib import Path

p = Path("gi_0.0.3-dev.py")
s = p.read_text()

marker = '''    # FUNCTION RETURN VALUE
    if "(" in v and v.endswith(")"):
'''

insert = '''    # BUILT-IN COLLECTION FUNCTIONS
    if v.startswith("len(") and v.endswith(")"):
        target = get_value(v[4:-1].strip())
        return len(target)

    # FUNCTION RETURN VALUE
    if "(" in v and v.endswith(")"):
'''

if marker not in s:
    raise SystemExit("[GI] FUNCTION RETURN marker not found")

s = s.replace(marker, insert, 1)

marker2 = '''          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

insert2 = '''          # COLLECTION METHOD CALL

          elif "." in line and "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):

              objname = line.split(".", 1)[0].strip()
              method = line.split(".", 1)[1].split("(", 1)[0].strip()
              argtext = line.split("(", 1)[1][:-1].strip()

              if objname in variables:
                  obj = variables[objname]
                  args = split_args(argtext) if argtext else []

                  if method == "append" and isinstance(obj, list):
                      if len(args) != 1:
                          raise GIRuntimeError("append() expects 1 argument")
                      obj.append(get_value(args[0]))

                  elif method == "remove" and isinstance(obj, list):
                      if len(args) != 1:
                          raise GIRuntimeError("remove() expects 1 argument")
                      obj.remove(get_value(args[0]))

                  elif method == "clear" and isinstance(obj, list):
                      obj.clear()

                  else:
                      raise GIRuntimeError("Unknown collection method: " + method)

              else:
                  raise GIRuntimeError("Unknown object: " + objname)

          # FUNCTION CALL

          elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):
'''

if marker2 not in s:
    raise SystemExit("[GI] FUNCTION CALL marker not found")

s = s.replace(marker2, insert2, 1)

p.write_text(s)
print("[GI] v0.0.3 collection operations added")
