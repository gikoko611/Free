p="gi.py"

with open(p) as f:
    s=f.read()

marker="#!/usr/bin/env python3"

first=s.find(marker)
second=s.find(marker, first+1)

if second != -1:
    s=s[:second]
    with open(p,"w") as f:
        f.write(s)
    print("duplicate interpreter removed")
else:
    print("no duplicate found")
