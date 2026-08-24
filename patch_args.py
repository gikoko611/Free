from pathlib import Path

p=Path("gi.py")
s=p.read_text()

insert='''

def split_args(s):

    args=[]
    current=""
    depth=0

    for c in s:

        if c=="(":
            depth+=1

        elif c==")":
            depth-=1

        if c=="," and depth==0:
            args.append(current.strip())
            current=""
        else:
            current+=c

    if current.strip():
        args.append(current.strip())

    return args

'''

marker="def check_condition(c):"

if insert not in s:
    s=s.replace(marker,insert+"\n"+marker)

s=s.replace(
'args=[x.strip() for x in argtext.split(",")]',
'args=split_args(argtext)'
)

p.write_text(s)

print("Nested argument parser OK")
