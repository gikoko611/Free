from pathlib import Path

p=Path("gi.py")
lines=p.read_text().splitlines()

# Python list index = line number - 1
start=297   # line 298
end=322     # before line 323

new_block=[
"              if len(args) > len(params):",
"                  print(\"[GI Error] Too many arguments\")",
"                  continue",
"",
"              old=variables.copy()",
"",
"              for n,a in zip(",
"                  functions[name][\"params\"],",
"                  args",
"              ):",
"                  variables[n]=get_value(a)",
"",
"              result=None",
"",
"              try:",
"                  execute(",
"                      functions[name][\"code\"]",
"                  )",
"",
"              except GIReturn as e:",
"                  result=e.value",
"",
"              variables.clear()",
"              variables.update(old)",
""
]

lines[start:end]=new_block

p.write_text("\n".join(lines)+"\n")
print("Lines fixed")
