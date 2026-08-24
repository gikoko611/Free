from pathlib import Path

p = Path("gi_0.0.3-dev.py")
s = p.read_text()

# 1. Add len() to get_value
needle = '    # FUNCTION RETURN VALUE\n'

if 'if v.startswith("len(")' not in s:
    pos = s.find(needle)
    if pos == -1:
        raise SystemExit("[GI] get_value insertion point not found")

    code = '''    # BUILT-IN LENGTH
    if v.startswith("len(") and v.endswith(")"):
        target = get_value(v[4:-1].strip())
        return len(target)

'''
    s = s[:pos] + code + s[pos:]

# 2. Add collection method handler before normal FUNCTION CALL
needle = '          # FUNCTION CALL'
pos = s.find(needle)

if pos == -1:
    raise SystemExit("[GI] FUNCTION CALL section not found")

if '# COLLECTION METHOD CALL' not in s:
    code = '''          # COLLECTION METHOD CALL

          elif "." in line and "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):

              objname = line.split(".", 1)[0].strip()
              method_part = line.split(".", 1)[1]
              method = method_part.split("(", 1)[0].strip()
              argtext = method_part.split("(", 1)[1][:-1].strip()

              if objname not in variables:
                  raise GIRuntimeError("Unknown object: " + objname)

              obj = variables[objname]
              args = split_args(argtext) if argtext else []

              if method == "append":
                  if not isinstance(obj, list):
                      raise GIRuntimeError("append() requires a list")
                  if len(args) != 1:
                      raise GIRuntimeError("append() expects 1 argument")
                  obj.append(get_value(args[0]))

              elif method == "remove":
                  if not isinstance(obj, list):
                      raise GIRuntimeError("remove() requires a list")
                  if len(args) != 1:
                      raise GIRuntimeError("remove() expects 1 argument")
                  obj.remove(get_value(args[0]))

              elif method == "clear":
                  if not isinstance(obj, list):
                      raise GIRuntimeError("clear() requires a list")
                  obj.clear()

              else:
                  raise GIRuntimeError("Unknown collection method: " + method)

'''
    s = s[:pos] + code + s[pos:]

p.write_text(s)
print("[GI] v0.0.3 collection operations patch applied")
