from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old1 = '''            if name not in functions:
                print("[GI Error] Function not found:", name)
                continue
'''

new1 = '''            if name not in functions:
                print("[GI Error] Function not found:", name)
                i += 1
                continue
'''

old2 = '''            if len(args) < len(params):
                print("[GI Error] Missing argument")
                continue
'''

new2 = '''            if len(args) < len(params):
                print("[GI Error] Missing argument")
                i += 1
                continue
'''

old3 = '''            if len(args) > len(params):
                print("[GI Error] Too many arguments")
                continue
'''

new3 = '''            if len(args) > len(params):
                print("[GI Error] Too many arguments")
                i += 1
                continue
'''

changed = 0

for old, new in [(old1,new1),(old2,new2),(old3,new3)]:
    if old in s:
        s = s.replace(old, new, 1)
        changed += 1

p.write_text(s)

print(f"[GI] v1.7 function error-loop fix applied ({changed}/3)")
