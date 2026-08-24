from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''        # LIST ASSIGNMENT

        elif "[" in line and "]" in line and "=" in line and not line.split("=",1)[1].strip().startswith("["):

            left,right=line.split("=",1)

            name=left.split("[",1)[0].strip()

            index=left.split("[",1)[1].split("]",1)[0].strip()

            if name in variables:

                variables[name][int(get_value(index))]=get_value(right)
'''

new = '''        # INDEX / DICT ASSIGNMENT

        elif "[" in line and "]" in line and "=" in line:

            left,right=line.split("=",1)

            name=left.split("[",1)[0].strip()
            index=left.split("[",1)[1].split("]",1)[0].strip()

            if name in variables:

                obj=variables[name]
                value=get_value(right)

                if isinstance(obj, dict):
                    key=index.strip().strip('"').strip("'")
                    obj[key]=value

                elif isinstance(obj, list):
                    idx=int(get_value(index))
                    obj[idx]=value
'''

if old not in s:
    print("[GI] Dict assignment target not found")
    raise SystemExit(1)

s=s.replace(old,new,1)
p.write_text(s)

print("[GI] v1.7 dict assignment added")
