# iko.py
import re
import sys

class IkoInterpreter:
    def __init__(self):
        self.variables = {}      # Variable သိမ်းမယ်
        self.functions = {}      # Function သိမ်းမယ် (နောက်မှထည့်)
        self.output_lines = []   # Output တွေစုမယ်

    def parse_line(self, line):
        """iko-mm lang ရဲ့ စာကြောင်းတစ်ကြောင်းကို ခွဲခြမ်းမယ်"""
        line = line.strip()
        if not line or line.startswith("#"):
            return  # Comment ကို ကျော်မယ်

        # 1. ပြရန် -> `ပြော` (say) 
        if line.startswith("ပြော"):
            content = line[3:].strip()
            if content.startswith('"') and content.endswith('"'):
                self.output_lines.append(content[1:-1])
            elif content in self.variables:
                self.output_lines.append(str(self.variables[content]))
            else:
                self.output_lines.append(content)

        # 2. Variable သိမ်းရန် -> `သိမ်း` (set)
        elif line.startswith("သိမ်း"):
            parts = line[3:].split("=")
            if len(parts) == 2:
                var_name = parts[0].strip()
                value = parts[1].strip()
                
                # စာသား (String)
                if value.startswith('"') and value.endswith('"'):
                    self.variables[var_name] = value[1:-1]
                # နံပါတ် (Number) - မြန်မာဂဏန်းကိုပါ ထောက်ပံ့မယ်
                else:
                    # မြန်မာဂဏန်း -> အင်္ဂလိပ်ဂဏန်း ပြောင်း
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

        # 3. ဂဏန်းတွက်ရန် -> `တွက်` (calc)
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

        # 4. Input လက်ခံရန် -> `မေး` (ask)
        elif line.startswith("မေး"):
            prompt = line[3:].strip()
            if prompt.startswith('"') and prompt.endswith('"'):
                prompt = prompt[1:-1]
            user_input = input(prompt + " ")
            return user_input  # ဒီတစ်ခါတော့ ပြန်ပေးမယ် (နောက်မှ သိမ်းဖို့)

        # 5. Loop -> `ထပ်` (loop) - ရိုးရိုး ၅ ကြိမ်လောက်
        elif line.startswith("ထပ်"):
            parts = line[3:].strip().split()
            if len(parts) >= 2 and parts[1] == "ကြိမ်":
                try:
                    count = int(parts[0])
                    return {"loop": count}  # Loop အတွက် အချက်ပြမယ်
                except:
                    pass

        else:
            self.output_lines.append(f"မသိသော အမိန့်: {line}")

        return None

    def run(self, code):
        """iko-mm lang Code ကို စီမံဆောင်ရွက်မယ်"""
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            result = self.parse_line(line)
            
            # Loop အတွက်
            if result and isinstance(result, dict) and "loop" in result:
                count = result["loop"]
                loop_body = []
                i += 1
                # Loop အတွင်းစာကြောင်းတွေကို စုမယ်
                while i < len(lines) and not lines[i].strip().startswith("ဆုံး"):
                    loop_body.append(lines[i])
                    i += 1
                # Loop ကို လည်စေမယ်
                for _ in range(count):
                    for body_line in loop_body:
                        self.parse_line(body_line)
                # "ဆုံး" ကို ကျော်မယ်
                if i < len(lines) and lines[i].strip().startswith("ဆုံး"):
                    i += 1
                continue
            
            i += 1
        
        # Output တွေကို အကုန်ပြမယ်
        for out in self.output_lines:
            print(out)
        self.output_lines = []  # ပြီးရင် ရှင်းမယ်

    def run_file(self, filename):
        """.iko ဖိုင်ကို ဖတ်ပြီး Run မယ်"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            self.run(code)
        except FileNotFoundError:
            print(f"ဖိုင် '{filename}' ကိုရှာမတွေ့ပါ")
        except Exception as e:
            print(f"အမှားတစ်ခုဖြစ်ပွားခဲ့သည်: {e}")
