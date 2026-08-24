from pathlib import Path

p=Path("gi.py")
s=p.read_text()

s=s.replace(
'''                old=variables.copy()

                variables.clear()

                for n,a in zip(
''',
'''                old=variables.copy()

                for n,a in zip(
'''
)

s=s.replace(
'''                variables.clear()
                variables.update(old)

                if result is not None:
                    print(result)
''',
'''                variables.clear()
                variables.update(old)

                if result is not None:
                    print(result)
'''
)

p.write_text(s)

print("Scope restore fixed")
