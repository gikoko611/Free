from pathlib import Path

p = Path("gi.py")
s = p.read_text()

s = s.replace(
    "import shlex",
    "import shlex\nimport ast",
    1
)

marker = '''    # LIST VALUE

    if v.startswith("[") and v.endswith("]"):
'''

replacement = '''    # DICTIONARY LITERAL

    if v.startswith("{") and v.endswith("}"):
        try:
            return ast.literal_eval(v)
        except (ValueError, SyntaxError):
            pass


    # LIST VALUE

    if v.startswith("[") and v.endswith("]"):
'''

if marker not in s:
    print("[GI] Dict literal target not found")
    raise SystemExit(1)

s = s.replace(marker, replacement, 1)

p.write_text(s)
print("[GI] Dictionary literal support added")
