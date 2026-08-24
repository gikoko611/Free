#!/usr/bin/env python3
import sys
from iko import IkoInterpreter

def main():
    if len(sys.argv) < 2:
        print("အသုံးပြုပုံ: python iko_runner.py <file.iko>")
        return

    filename = sys.argv[1]
    interpreter = IkoInterpreter()
    interpreter.run_file(filename)

if __name__ == "__main__":
    main()
