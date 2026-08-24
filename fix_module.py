from pathlib import Path

p = Path("gi.py")
lines = p.read_text().splitlines()

start = next(i for i, x in enumerate(lines) if x.strip() == "# MODULE CALL")
end = next(i for i in range(start + 1, len(lines))
           if lines[i].strip() == "# RUN")

block = '''        # MODULE CALL

        elif "." in line and not line.startswith("say "):

            p=shlex.split(line)

            call=p[0]

            if "." in call:

                mod,func=call.split(".",1)

                args=p[1:]

                if mod in modules:

                    result=getattr(
                        modules[mod],
                        func
                    )(*args)

                    if result is not None:
                        print(result)


'''.splitlines()

lines[start:end] = block

p.write_text("\\n".join(lines) + "\\n")
print("[GI] Module CALL block fixed")
