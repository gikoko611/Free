p="gi.py"

with open(p) as f:
    s=f.read()

s=s.replace(
'''if len(parts)>1:
                args.append(parts[1])''',
'''if len(parts)>1:
                args=parts[1].split()'''
)

s=s.replace(
'''execute(
                    functions[name]["code"]
                )''',
'''try:
                    result = execute(
                        functions[name]["code"]
                    )
                except GIReturn as r:
                    result = r.value'''
)

with open(p,"w") as f:
    f.write(s)

print("Function return patch OK")
