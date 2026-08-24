#!/usr/bin/env python3

import sys
import os
import importlib

variables = {}
functions = {}
modules = {}


def get_value(value):
    value = value.strip()

    if value in variables:
        return variables[value]

    if value.isdigit():
        return int(value)

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    return value


def execute(lines):

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue


        # IMPORT
        if line.startswith("import "):

            name = line.split()[1]

            try:
                modules[name] = importlib.import_module(
                    "modules." + name
                )

                print("[GI] Loaded module:", name)

            except Exception:
                print("[GI] Module error:", name)


        # FUNCTION CREATE
        elif line.startswith("function "):

            name = line.split()[1]
            block = []

            i += 1

            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])

                i += 1

            functions[name] = block


        # FUNCTION CALL
        elif line in functions:

            execute(functions[line])


        # RUN TERMINAL COMMAND
        elif line.startswith("run "):

            cmd = get_value(line[4:])
            os.system(cmd)


        # MODULE FUNCTION
        elif "." in line:

            parts = line.replace("()","").split(".")

            if len(parts) == 2:

                mod = parts[0]
                func = parts[1]

                if mod in modules and hasattr(modules[mod], func):
                    getattr(modules[mod], func)()


        # SAY
        elif line.startswith("say "):

            print(get_value(line[4:]))


        # VARIABLE
        elif "=" in line:

            name, value = line.split("=",1)

            variables[name.strip()] = get_value(value)


        i += 1



def run(file):

    with open(file) as f:
        code = f.readlines()

    execute(code)



if __name__ == "__main__":

    if len(sys.argv)<2:
        print("GI Language v0.3")
        exit()

    run(sys.argv[1])
