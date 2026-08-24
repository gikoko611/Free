from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

# Add runtime error class if missing
marker = '''class GIContinue(Exception):
    pass
'''

if "class GIRuntimeError" not in s:
    s = s.replace(
        marker,
        marker + '''

class GIRuntimeError(Exception):
    pass
''',
        1
    )

# Replace run() with safe runtime reporting
start = s.find("def run(file):")
end = s.find("\ndef repl():", start)

if start == -1 or end == -1:
    print("[GI] run() target not found")
    raise SystemExit(1)

new_run = '''def run(file):

    try:
        with open(file) as f:
            execute(f.readlines())

    except GIReturn as e:
        return e.value

    except GIRuntimeError as e:
        print("[GI Error]", e)

    except FileNotFoundError:
        print("[GI Error] File not found:", file)

    except Exception as e:
        print("[GI Error]", type(e).__name__ + ":", e)


'''

s = s[:start] + new_run + s[end+1:]

p.write_text(s)
print("[GI] v1.7 runtime error handling cleaned")
