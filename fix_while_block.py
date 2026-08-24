p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
i=0
done=False

while i < len(lines):

    if lines[i].strip() == '# SAY' and not done:

        # SAY comment ကိုထား
        out.append(lines[i])
        i+=1

        # return/while အပိုင်းကို ကျော်ပြီး say မတိုင်ခင်နေရာက ရှာ
        while i < len(lines) and 'elif line.startswith("say ")' not in lines[i]:
            i+=1

        continue

    if 'elif line.startswith("while ")' in lines[i] and not done:

        block=[
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

        out.extend(block)
        done=True

        while i < len(lines) and 'elif line.startswith("say ")' not in lines[i]:
            i+=1

        continue

    out.append(lines[i])
    i+=1


with open(p,"w") as f:
    f.writelines(out)

print("while block fixed" if done else "not found")
