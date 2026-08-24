#!/usr/bin/env python3

import sys
import os
import importlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import installer

variables = {}
functions = {}
modules = {}


def get_value(v):

    v = v.strip()

    if v in variables:
        return variables[v]

    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]

    if v.isdigit():
        return int(v)

    return v



def check_condition(c):

    p = c.split()

    if len(p) != 3:
        return False

    a = get_value(p[0])
    op = p[1]
    b = get_value(p[2])

    if op == "==":
        return a == b

    if op == ">":
        return a > b

    if op == "<":
        return a < b

    return False



def execute(lines):

    global variables

    i = 0

    while i < len(lines):

        line = lines[i].strip()


        if not line:
            i += 1
            continue



        # IMPORT

        if line.startswith("import "):

            name=line.split()[1]

            modules[name]=importlib.import_module(
                "modules."+name
            )

            print("[GI] Module:",name)



        # FUNCTION CREATE

        elif line.startswith("function "):

            parts=line.split()

            name=parts[1]
            params=parts[2:]

            block=[]

            i+=1

            while lines[i].strip()!="end":
                block.append(lines[i])
                i+=1


            functions[name]={
                "params":params,
                "code":block
            }



        # FUNCTION CALL

        elif line.split()[0] in functions:

            parts=line.split(maxsplit=1)

            name=parts[0]

            args=[]

            if len(parts)>1:
                args.append(parts[1])


            old=variables.copy()


            for n,a in zip(
                functions[name]["params"],
                args
            ):
                variables[n]=get_value(a)


            execute(
                functions[name]["code"]
            )


            variables=old



        # IF

        elif line.startswith("if "):

            condition=line[3:]

            block=[]

            i+=1

            while lines[i].strip()!="end":
                block.append(lines[i])
                i+=1


            if check_condition(condition):
                execute(block)



        # MODULE CALL

        elif "." in line and not line.startswith("say "):

            p=line.split()

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



        # RUN

        elif line.startswith("run "):

            os.system(
                get_value(line[4:])
            )



        # SAY

        elif line.startswith("say "):

            print(
                get_value(line[4:])
            )



        # VARIABLE

        elif "=" in line:

            k,v=line.split("=",1)

            variables[k.strip()]=get_value(v)



        i+=1



def run(file):

    with open(file) as f:
        execute(f.readlines())



def repl():

    print("GI Language v0.8")
    print("Type exit to quit")

    while True:

        try:
            code = input("GI> ")

            if code == "exit":
                break

            execute([code])

        except Exception as e:
            print("GI Error:", e)



if __name__=="__main__":

    if len(sys.argv)<2:
        repl()

    elif sys.argv[1] == "install":

        if len(sys.argv) < 3:
            print("Usage: gi install package")
        else:
            installer.install(sys.argv[2])

    elif sys.argv[1] == "--version":
        print("GI Language v0.9")

    else:
        run(sys.argv[1])
