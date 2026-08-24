path="gi.py"

with open(path,"r") as f:
    data=f.read()

data=data.replace(
"        elif \"=\" in line:\n",
"          elif \"=\" in line:\n"
)

with open(path,"w") as f:
    f.write(data)

print("ONE LINE FIXED")
