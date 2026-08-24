p="gi.py"

with open(p) as f:
    lines=f.readlines()

out=[]
i=0
done=False

while i < len(lines):

    if lines[i].strip() == 'elif line.startswith("while "):' and not done:

        out.extend([
'''          elif line.startswith("while "):
''',
'''              condition = line[6:].strip()
''',
'''              block=[]
''',
'''
              i+=1
''',
'''
              depth=1
''',
'''
              while i < len(lines) and depth>0:
''',
'''
                  current=lines[i].strip()
''',
'''
                  if current.startswith("while "):
                      depth+=1
''',
'''
                  if current=="end":
                      depth-=1
                      if depth==0:
                          break
''',
'''
                  block.append(lines[i])
                  i+=1
''',
'''
              count=0
              while check_condition(condition):
                  execute(block)
                  count+=1
                  if count > 10000:
                      break
'''
        ])

        done=True

        while i < len(lines) and lines[i].strip()!="elif line.startswith(\"say \"):":
            i+=1

        continue

    out.append(lines[i])
    i+=1


with open(p,"w") as f:
    f.writelines(out)

print("nested while replaced" if done else "not found")
