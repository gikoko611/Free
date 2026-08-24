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

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    if value.isdigit():
        return int(value)

    return value



def execute(lines):

    global variables

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue


        # IMPORT MODULE
        if line.startswith("import "):

            name = line.split()[1]

            try:
                modules[name] = importlib.import_module("modules." + name)
                print("[GI] Module:", name)

            except Exception as e:
                print("[GI] Import error:", e)



        # FUNCTION CREATE
        if line.startswith("function "):

            parts = line.split()

            name = parts[1]

            params = parts[2:]

            block = []

            i += 1

            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1

            functions[name] = {
                "params": params,
                "code": block
            }



        # FUNCTION CALL

        elif line.split()[0] in functions:

            parts = line.split(maxsplit=1)

            fname = parts[0]

            args = []

            if len(parts) > 1:
                args.append(parts[1])

            old_vars = variables.copy()

            func = functions[fname]


            for index,param in enumerate(func["params"]):

                if index < len(args):
                    variables[param] = get_value(args[index])


            execute(func["code"])


            variables = old_vars



        # RETURN

        elif line.startswith("return "):

            return get_value(line[7:])



        # MODULE FUNCTION

        elif "." in line:

            parts = line.split()

            call = parts[0]

            mod,func = call.split(".")

            args = parts[1:]

            if mod in modules:

                result = getattr(modules[mod],func)(*args)

                if result is not None:
                    print(result)



        # RUN

        elif line.startswith("run "):

            os.system(get_value(line[4:]))



        # SAY

        elif line.startswith("say "):

            print(get_value(line[4:]))



        # VARIABLE

        elif "=" in line:

            name,value = line.split("=",1)

            value = value.strip()

            # function return call
            if value in functions:

                old_vars = variables.copy()

                result = execute(functions[value]["code"])

                variables[name.strip()] = result

                variables.update(old_vars)

            else:
                variables[name.strip()] = get_value(value)


        i += 1



def run(filename):

    with open(filename) as f:
        execute(f.readlines())



if __name__ == "__main__":

    if len(sys.argv)<2:
        print("GI Language v0.6")
        exit()

    run(sys.argv[1])
