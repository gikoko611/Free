#!/usr/bin/env python3

import sys
import os
import importlib
import shlex
import ast

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import installer

variables = {}
functions = {}
VERSION = "1.6"

class GIReturn(Exception):
    def __init__(self, value):
        self.value = value

modules = {}


def get_value(v):

    v = v.strip()

    if v in variables:
        return variables[v]


    # DICTIONARY LITERAL

    if v.startswith("{") and v.endswith("}"):
        try:
            return ast.literal_eval(v)
        except (ValueError, SyntaxError):
            pass


    # LIST VALUE

    if v.startswith("[") and v.endswith("]"):

        inside=v[1:-1]

        if not inside.strip():
            return []

        return [
            get_value(x.strip())
            for x in split_args(inside)
        ]


    # DICTIONARY VALUE

    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0].strip()

        key=v.split("[",1)[1][:-1].strip()

        if name in variables:

            obj=variables[name]

            if isinstance(obj, dict):

                key=key.strip('"').strip("'")

                return obj[key]


    # LIST INDEX

    if "[" in v and v.endswith("]"):

        name=v.split("[",1)[0]

        index=v.split("[",1)[1][:-1]

        if name in variables:

            arr=variables[name]

            idx=int(get_value(index))

            return arr[idx]


    # FUNCTION RETURN VALUE

    if "(" in v and v.endswith(")"):
        name=v.split("(",1)[0]

        argtext=v.split("(",1)[1][:-1]

        args=[]

        if argtext.strip():
            args=split_args(argtext)

        if name in functions:

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

            return result


    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]

    if v == "true":
        return True

    if v == "false":
        return False

    if v.lstrip("-").isdigit():
        return int(v)

    # BASIC MATH
    for op in ["+","-","*","/"]:
        if op in v:
            try:
                a,b=v.split(op,1)
                a=get_value(a)
                b=get_value(b)

                if op=="+":
                    return a+b
                elif op=="-":
                    return a-b
                elif op=="*":
                    return a*b
                elif op=="/":
                    return a//b
            except:
                pass

    return v





def split_args(s):

    args=[]
    current=""
    depth=0

    for c in s:

        if c=="(":
            depth+=1

        elif c==")":
            depth-=1

        if c=="," and depth==0:
            args.append(current.strip())
            current=""
        else:
            current+=c

    if current.strip():
        args.append(current.strip())

    return args


def check_condition(c):

    p = c.split()

    if len(p) != 3:
        return False

    a = get_value(p[0])
    op = p[1]
    b = get_value(p[2])

    if op == "==":
        return a == b

    if op == "!=":
        return a != b

    if op == ">":
        return a > b

    if op == "<":
        return a < b

    if op == ">=":
        return a >= b

    if op == "<=":
        return a <= b

    return False



def execute(lines):
    global variables, functions, modules

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

            try:
                modules[name]=importlib.import_module(
                    "modules."+name
                )

            except ModuleNotFoundError:
                modules[name]=importlib.import_module(
                    "packages."+name
                )

            print("[GI] Module:",name)



        # FUNCTION CREATE

        elif line.startswith("function "):

            header=line[9:].strip()

            name=header.split("(")[0]

            params_text=header.split("(",1)[1].rstrip(")")

            params=[]

            if params_text.strip():
                params=[x.strip() for x in params_text.split(",")]

            block=[]

            i+=1

            depth=1

            while i < len(lines) and depth>0:

                  current=lines[i].strip()

                  if current.startswith("function ") or current.startswith("if "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  block.append(lines[i])
                  i+=1

            functions[name]={
                "params":params,
                "code":block
            }




          # IF

        elif line.startswith("if "):

              condition=line[3:]

              block=[]
              else_block=[]

              i+=1
              depth=1
              in_else=False

              while i < len(lines) and depth>0:

                  current=lines[i].strip()

                  if current.startswith("if "):
                      depth+=1

                  if current=="end":
                      depth-=1
                      if depth==0:
                          break

                  if current=="else" and depth==1:
                      in_else=True
                  elif in_else:
                      else_block.append(lines[i])
                  else:
                      block.append(lines[i])

                  i+=1

              if check_condition(condition):
                  execute(block)
              else:
                  execute(else_block)


        # WHILE

        elif line.startswith("while "):

            condition=line[6:].strip()
            block=[]

            i+=1
            depth=1

            while i < len(lines) and depth > 0:

                current=lines[i].strip()

                if current.startswith("while "):
                    depth+=1

                if current.startswith("if "):
                    depth+=1

                if current.startswith("function "):
                    depth+=1

                if current=="end":
                    depth-=1
                    if depth==0:
                        break

                block.append(lines[i])
                i+=1

            guard=0

            while check_condition(condition):

                execute(block)

                guard+=1
                if guard > 100000:
                    raise GIRuntimeError("While loop limit exceeded")


        # FUNCTION CALL

        elif "(" in line and line.endswith(")") and "=" not in line and not line.startswith("say "):

            name=line.split("(")[0]

            argtext=line.split("(",1)[1][:-1]

            args=[]

            if argtext.strip():
                args=split_args(argtext)

            if name not in functions:
                print("[GI Error] Function not found:", name)
                continue

            params=functions[name]["params"]

            if len(args) < len(params):
                print("[GI Error] Missing argument")
                continue

            if len(args) > len(params):
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

                  # return value ignored for statement call


        # MODULE CALL

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



        # RUN

        elif line.startswith("run "):

            os.system(
                get_value(line[4:])
            )



        # SAY

        elif line.startswith("return "):
            value = get_value(line[7:].strip())
            raise GIReturn(value)
        elif line.startswith("say "):

            print(
                get_value(line[4:])
            )



        # LIST ASSIGNMENT

        elif "[" in line and "]" in line and "=" in line and not line.split("=",1)[1].strip().startswith("["):

            left,right=line.split("=",1)

            name=left.split("[",1)[0].strip()

            index=left.split("[",1)[1].split("]",1)[0].strip()

            if name in variables:

                variables[name][int(get_value(index))]=get_value(right)


        # VARIABLE

        elif "=" in line:

            k,v=line.split("=",1)

            variables[k.strip()]=get_value(v)



        i+=1



def run(file):

    with open(file) as f:
        try:
            execute(f.readlines())
        except GIReturn as e:
            return e.args[0]



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



result = None

if __name__=="__main__":

    if len(sys.argv)<2:
        repl()

    elif sys.argv[1] == "install":

        if len(sys.argv) < 3:
            print("Usage: gi install package")
        else:
            installer.install(sys.argv[2])

    elif sys.argv[1] == "--version":
        print("GI Language v1.6")

    else:
        result = run(sys.argv[1])

if result is not None:
    print(result)
