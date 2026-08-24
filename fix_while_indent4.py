p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
i=0

while i < len(lines):

    if 357 <= i+1 <= 386:
        i+=1
        continue

    out.append(lines[i])
    i+=1


insert=[
'          elif line.startswith("while "):\n',
'\n',
'              condition = line[6:].strip()\n',
'              block=[]\n',
'\n',
'              i+=1\n',
'              depth=1\n',
'\n',
'              while i < len(lines) and depth>0:\n',
'                  current=lines[i].strip()\n',
'\n',
'                  if current.startswith("while "):\n',
'                      depth+=1\n',
'\n',
'                  if current=="end":\n',
'                      depth-=1\n',
'                      if depth==0:\n',
'                          break\n',
'\n',
'                  block.append(lines[i])\n',
'                  i+=1\n',
'\n',
'              count=0\n',
'\n',
'              while check_condition(condition):\n',
'                  execute(block)\n',
'                  count+=1\n',
'                  if count > 10000:\n',
'                      break\n',
'\n'
]

# insert before SAY
for n,line in enumerate(out):
    if 'elif line.startswith("say ")' in line:
        out[n:n]=insert
        break

with open(p,"w") as f:
    f.writelines(out)

print("while block inserted")
