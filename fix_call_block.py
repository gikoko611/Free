from pathlib import Path

p = Path("gi.py")
lines = p.read_text().splitlines()

start = 302   # line 303 old=variables.copy()
end = 324     # before comment

new_block = [
"            old=variables.copy()",
"",
"            for n,a in zip(",
"                functions[name][\"params\"],",
"                args",
"            ):",
"                variables[n]=get_value(a)",
"",
"            result=None",
"",
"            try:",
"                execute(",
"                    functions[name][\"code\"]",
"                )",
"",
"            except GIReturn as e:",
"                result=e.value",
"",
"            variables.clear()",
"            variables.update(old)",
]

lines[start:end] = new_block

p.write_text("\n".join(lines) + "\n")

print("Function call block restored")
