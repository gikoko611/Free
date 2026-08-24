from pathlib import Path

p=Path("gi.py")
s=p.read_text()

s=s.replace(
'''            parts=line.split()

            name=parts[1]
            params=parts[2:]
''',
'''            header=line[9:].strip()

            name=header.split("(")[0]

            params_text=header.split("(",1)[1].rstrip(")")

            params=[]

            if params_text.strip():
                params=[x.strip() for x in params_text.split(",")]
'''
)

s=s.replace(
'''                  block=functions[name]["body"]
''',
'''                  block=functions[name]["code"]
'''
)

p.write_text(s)
print("Function syntax patch OK")
