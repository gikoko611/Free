p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if "try:" in l and i>260 and i<290:
        start=i
        break

for i in range(start, len(lines)):
    if "result=e.value" in lines[i]:
        end=i+1
        break

new=[
"                try:\n",
"                    execute(\n",
"                        functions[name][\"code\"]\n",
"                    )\n",
"\n",
"                except GIReturn as e:\n",
"                    result=e.value\n"
]

lines=lines[:start]+new+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("try block fixed")
