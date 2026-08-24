from pathlib import Path

p=Path("gi.py")
s=p.read_text()

start=s.index("if len(args) > len(params):")
end=s.index("# MODULE CALL", start)

block=s[start:end]

new="""if len(args) > len(params):
                  print("[GI Error] Too many arguments")
                  continue

              old=variables.copy()

              for n,a in zip(
                  functions[name]["params"],
                  args
              ):
                  variables[n]=get_value(a)

              result=None

              try:
                  execute(
                      functions[name]["code"]
                  )

              except GIReturn as e:
                  result=e.value

              variables.clear()
              variables.update(old)

"""

# keep the indentation before the first if
prefix=block[:block.index("if len(args) > len(params):")]

s=s[:start]+new+s[end:]

p.write_text(s)
print("Call block fixed")
