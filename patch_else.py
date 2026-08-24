p="gi.py"

with open(p) as f:
    lines=f.readlines()

start=None
end=None

for i,l in enumerate(lines):
    if 'elif line.startswith("if ")' in l:
        start=i
    if start is not None and 'execute(block)' in l:
        end=i+1
        break

new=[
'          elif line.startswith("if "):\n',
'\n',
'              condition=line[3:]\n',
'\n',
'              block=[]\n',
'              else_block=[]\n',
'\n',
'              i+=1\n',
'              depth=1\n',
'              in_else=False\n',
'\n',
'              while i < len(lines) and depth>0:\n',
'                  current=lines[i].strip()\n',
'\n',
'                  if current.startswith("if "):\n',
'                      depth+=1\n',
'\n',
'                  if current=="end":\n',
'                      depth-=1\n',
'                      if depth==0:\n',
'                          break\n',
'\n',
'                  if current=="else" and depth==1:\n',
'                      in_else=True\n',
'                  elif in_else:\n',
'                      else_block.append(lines[i])\n',
'                  else:\n',
'                      block.append(lines[i])\n',
'\n',
'                  i+=1\n',
'\n',
'              if check_condition(condition):\n',
'                  execute(block)\n',
'              else:\n',
'                  execute(else_block)\n'
]

lines=lines[:start]+new+lines[end:]

with open(p,"w") as f:
    f.writelines(lines)

print("else patched")
