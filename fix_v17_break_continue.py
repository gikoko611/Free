from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

# Add control-flow exceptions
marker = 'class GIReturn(Exception):'
if 'class GIBreak(Exception):' not in s:
    insert = '''class GIBreak(Exception):
    pass

class GIContinue(Exception):
    pass

'''
    s = s.replace(marker, insert + marker, 1)

# Add commands before RETURN/SAY
marker = '        elif line.startswith("return "):'
if 'raise GIBreak()' not in s:
    block = '''        elif line == "break":
            raise GIBreak()

        elif line == "continue":
            raise GIContinue()

'''
    s = s.replace(marker, block + marker, 1)

# Make WHILE catch break/continue
old = '''                if check_condition(condition):
                    execute(block)
                else:
                    execute(else_block)
'''
new = '''                if check_condition(condition):
                    try:
                        execute(block)
                    except GIBreak:
                        pass
                    except GIContinue:
                        pass
                else:
                    execute(else_block)
'''
if old in s and 'except GIBreak:' not in s:
    s = s.replace(old, new, 1)

# Make FOR catch break/continue
old_for = '''                    variables[var] = item
                    execute(block)
'''
new_for = '''                    variables[var] = item
                    try:
                        execute(block)
                    except GIBreak:
                        break
                    except GIContinue:
                        continue
'''
if old_for in s and 'except GIBreak:' not in old_for:
    s = s.replace(old_for, new_for, 1)

p.write_text(s)
print("[GI] v1.7 break/continue added")
