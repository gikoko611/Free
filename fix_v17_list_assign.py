from pathlib import Path

p = Path("gi_v1.7.py")
s = p.read_text()

old = '''        elif "[" in line and "]" in line and "=" in line:

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

new = '''        elif "[" in line and "]" in line and "=" in line:

            left,right=line.split("=",1)
            left=left.strip()

            # Only indexed assignment: a[0] = x / d["key"] = x
            if "[" in left and "]" in left:

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

            else:
                variables[left]=get_value(right)
'''

if old not in s:
    print("[GI] List/dict assignment target not found")
    raise SystemExit(1)

p.write_text(s.replace(old,new,1))
print("[GI] list literal / indexed assignment conflict fixed")
