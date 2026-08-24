from pathlib import Path

p = Path("gi.py")
s = p.read_text()

s = s.replace(
"functions = {}\n",
"""functions = {}
VERSION = "1.6"

class GIReturn(Exception):
    def __init__(self, value):
        self.value = value

"""
)

s = s.replace(
"def execute(lines):",
"""def execute(lines):
    global variables, functions, modules"""
)

s = s.replace(
'elif line.startswith("say "):',
'''elif line.startswith("return "):
            value = get_value(line[7:].strip())
            raise GIReturn(value)

        elif line.startswith("while "):
            condition = line[6:].strip()
            block=[]
            i+=1
            while i < len(lines) and lines[i].strip()!="end":
                block.append(lines[i])
                i+=1

            count=0
            while check_condition(condition):
                execute(block)
                count+=1
                if count > 10000:
                    break

        elif line.startswith("say "):'''
)

p.write_text(s)
print("GI V1.6 patch applied")
