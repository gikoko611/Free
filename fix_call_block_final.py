from pathlib import Path

p=Path("gi.py")
s=p.read_text()

start=s.index("              if len(args) > len(params):")
end=s.index("# MODULE CALL", start)

new="""              if len(args) > len(params):
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

s=s[:start]+new+s[end:]

p.write_text(s)
print("Final call block fixed")
