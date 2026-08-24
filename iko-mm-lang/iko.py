# iko.py
import re
import sys

class IkoInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output_lines = []

    def parse_line(self, line):
        line = line.strip()
        if not line or line.startswith("#"):
            return None

        # 1. ပြော (say)
        if line.startswith("ပြော"):
            content = line[3:].strip()
            if content.startswith('"') and content.endswith('"'):
                self.output_lines.append(content[1:-1])
            elif content in self.variables:
                self.output_lines.append(str(self.variables[content]))
            else:
                self.output_lines.append(content)

        # 2. သိမ်း (set)
        elif line.startswith("သိမ်း"):
            parts = line[3:].split("=")
            if len(parts) == 2:
                var_name = parts[0].strip()
                value = parts[1].strip()
                
                if value.startswith('"') and value.endswith('"'):
                    self.variables[var_name] = value[1:-1]
                else:
                    myanmar_digits = "၀၁၂၃၄၅၆၇၈၉"
                    english_digits = "0123456789"
                    trans = str.maketrans(myanmar_digits, english_digits)
                    value_eng = value.translate(trans)
                    
                    try:
                        self.variables[var_name] = int(value_eng)
                    except ValueError:
                        try:
                            self.variables[var_name] = float(value_eng)
                        except ValueError:
                            self.variables[var_name] = value

        # 3. တွက် (calc)
        elif line.startswith("တွက်"):
            expr = line[3:].strip()
            try:
                myanmar_digits = "၀၁၂၃၄၅၆၇၈၉"
                english_digits = "0123456789"
                trans = str.maketrans(myanmar_digits, english_digits)
                expr_eng = expr.translate(trans)
                result = eval(expr_eng)
                self.output_lines.append(f"အဖြေ: {result}")
            except Exception as e:
                self.output_lines.append(f"တွက်ရန် အမှား: {e}")

        # 4. မေး (ask)
        elif line.startswith("မေး"):
            prompt = line[3:].strip()
            if prompt.startswith('"') and prompt.endswith('"'):
                prompt = prompt[1:-1]
            user_input = input(prompt + " ")
            return user_input

        # 5. ထပ် (loop)
        elif line.startswith("ထပ်"):
            parts = line[3:].strip().split()
            if len(parts) >= 2 and parts[1] == "ကြိမ်":
                try:
                    count = int(parts[0])
                    return {"loop": count}
                except:
                    pass

        else:
            self.output_lines.append(f"မသိသော အမိန့်: {line}")

        return None

    def run(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            result = self.parse_line(line)
            
            if result and isinstance(result, dict) and "loop" in result:
                count = result["loop"]
                loop_body = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith("ဆုံး"):
                    loop_body.append(lines[i])
                    i += 1
                for _ in range(count):
                    for body_line in loop_body:
                        self.parse_line(body_line)
                if i < len(lines) and lines[i].strip().startswith("ဆုံး"):
                    i += 1
                continue
            
            i += 1
        
        for out in self.output_lines:
            print(out)
        self.output_lines = []

    def run_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            self.run(code)
        except FileNotFoundError:
            print(f"ဖိုင် '{filename}' ကိုရှာမတွေ့ပါ")
        except Exception as e:
            print(f"အမှားတစ်ခုဖြစ်ပွားခဲ့သည်: {e}")
