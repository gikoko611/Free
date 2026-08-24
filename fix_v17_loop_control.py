from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

# Add loop-control exceptions after GIReturn
old = '''class GIReturn(Exception):
    def __init__(self, value):
        self.value = value
'''

new = '''class GIReturn(Exception):
    def __init__(self, value):
        self.value = value


class GIBreak(Exception):
    pass


class GIContinue(Exception):
    pass
'''

if old in s and "class GIBreak" not in s:
    s = s.replace(old, new, 1)

# Add handlers before FOR
marker = '''        # FOR

        elif line.startswith("for "):
'''

handlers = '''        # BREAK / CONTINUE

        elif line == "break":
            raise GIBreak()

        elif line == "continue":
            raise GIContinue()


        # FOR

        elif line.startswith("for "):
'''

if marker not in s:
    print("[GI] FOR target not found")
    raise SystemExit(1)

s = s.replace(marker, handlers, 1)

# Wrap FOR execute with loop-control handling
old_exec = '''            for item in iterable:
                variables[var] = item
                execute(block)
'''

new_exec = '''            for item in iterable:
                variables[var] = item

                try:
                    execute(block)

                except GIBreak:
                    break

                except GIContinue:
                    continue
'''

if old_exec not in s:
    print("[GI] FOR execution target not found")
    raise SystemExit(1)

s = s.replace(old_exec, new_exec, 1)

p.write_text(s)
print("[GI] v1.7 break/continue added")
