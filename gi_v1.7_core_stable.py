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


class GIBreak(Exception):
    pass


class GIContinue(Exception):
    pass

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


    if (
        (v.startswith('"') and v.endswith('"')) or
        (v.startswith("'") and v.endswith("'"))
    ):
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




          # BREAK / CONTINUE

        elif line == "break":
            raise GIBreak()

        elif line == "continue":
            raise GIContinue()


        # FOR

        elif line.startswith("for "):

            header = line[4:].strip()

            if " in " not in header:
                raise GIRuntimeError("Invalid for syntax")

            var, expr = header.split(" in ", 1)
            var = var.strip()
            expr = expr.strip()

            block = []

            i += 1
            depth = 1

            while i < len(lines) and depth > 0:

                current = lines[i].strip()

                if current.startswith("for "):
                    depth += 1

                elif current.startswith("while "):
                    depth += 1

                elif current.startswith("if "):
                    depth += 1

                elif current == "end":
                    depth -= 1
                    if depth == 0:
                        break

                block.append(lines[i])
                i += 1

            iterable = get_value(expr)

            if isinstance(iterable, int):
                iterable = range(iterable)

            for item in iterable:
                variables[var] = item

                try:
                    execute(block)

                except GIBreak:
                    break

                except GIContinue:
                    continue


        # IF / ELIF / ELSE

        elif line.startswith("if "):


            branches = []
            condition = line[3:].strip()
            block = []

            i += 1
            depth = 1

            while i < len(lines) and depth > 0:

                current = lines[i].strip()

                if current.startswith("if "):
                    depth += 1

                elif current.startswith("while "):
                    depth += 1

                elif current == "end":
                    depth -= 1
                    if depth == 0:
                        break

                if depth == 1 and (
                    current.startswith("elif ") or
                    current == "else"
                ):
                    branches.append((condition, block))

                    if current.startswith("elif "):
                        condition = current[5:].strip()
                    else:
                        condition = None

                    block = []

                else:
                    block.append(lines[i])

                i += 1

            branches.append((condition, block))

            executed = False

            for cond, branch in branches:
                if cond is None or check_condition(cond):
                    execute(branch)
                    executed = True
                    break


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



        # INDEX / DICT ASSIGNMENT

        elif "[" in line and "]" in line and "=" in line:

            left,right=line.split("=",1)
            left=left.strip()

            # Only indexed assignment: a[0] = x / d["key"] = x
            if "[" in left and "]" in left:

                name=left.split("[",1)[0].strip()
                index=left.split("[",1)[1].split("]",1)[0].strip()

                if name in variables:

                    obj=variables[name]
                    value=get_value(right)

                    if isinstance(obj, dict):
                        key=index.strip().strip('"').strip("'")
                        obj[key]=value

                    elif isinstance(obj, list):
                        idx=int(get_value(index))
                        obj[idx]=value

            else:
                variables[left]=get_value(right)


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
