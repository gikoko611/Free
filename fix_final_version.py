from pathlib import Path

p = Path("gi.py")
s = p.read_text()

s = s.replace(
    'print("GI Language v0.9")',
    'print("GI Language v1.6")'
)

marker = 'if __name__=="__main__":'
if marker in s and 'result = None\n\nif __name__=="__main__":' not in s:
    s = s.replace(
        marker,
        'result = None\n\n' + marker,
        1
    )

p.write_text(s)
print("[GI] Final version/result fix applied")
