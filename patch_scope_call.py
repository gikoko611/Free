from pathlib import Path

p = Path("gi.py")
s = p.read_text()

s = s.replace(
"""              old=variables.copy()

              for n,a in zip(
""",
"""              scope_stack.append(variables.copy())
              variables.clear()

              for n,a in zip(
"""
)

s = s.replace(
"""              variables.clear()
              variables.update(old)

              return result
""",
"""              variables.clear()
              variables.update(scope_stack.pop())

              return result
"""
)

s = s.replace(
"""            old=variables.copy()

            for n,a in zip(
""",
"""            scope_stack.append(variables.copy())
            variables.clear()

            for n,a in zip(
"""
)

s = s.replace(
"""            variables.clear()
            variables.update(old)

            # return value ignored for statement call
""",
"""            variables.clear()
            variables.update(scope_stack.pop())

            # return value ignored for statement call
"""
)

p.write_text(s)

print("Scope call patched")
