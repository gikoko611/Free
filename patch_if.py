p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if "while lines[i].strip()!=\"end\":" in l and start is None:
        # ပထမဆုံးတွေ့တာက function create ဖြစ်နိုင်လို့ if အောက်ကကိုရှာမယ်
        pass

for i,l in enumerate(lines):
    if "elif line.startswith(\"if \"):" in l:
        start=i
        break

if start is None:
    print("if not found")
    exit()

for i in range(start,len(lines)):
    if "if check_condition(condition):" in lines[i]:
        end=i
        break

new=[
"          elif line.startswith(\"if \"):\n",
"\n",
"              condition=line[3:]\n",
"\n",
"              block=[]\n",
"              i+=1\n",
"              depth=1\n",
"\n",
"              while i < len(lines) and depth>0:\n",
"                  current=lines[i].strip()\n",
"\n",
"                  if current.startswith(\"if \") or current.startswith(\"function \"):\n",
"                      depth+=1\n",
"\n",
"                  if current==\"end\":\n",
"                      depth-=1\n",
"                      if depth==0:\n",
"                          break\n",
"\n",
"                  block.append(lines[i])\n",
"                  i+=1\n",
"\n",
"              if check_condition(condition):\n",
"                  execute(block)\n",
"\n"
]

lines=lines[:start]+new+lines[end+1:]

with open(p,"w") as f:
    f.writelines(lines)

print("if nested patched")
