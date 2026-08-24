#!/usr/bin/env python3

import sys
import os

variables = {}
functions = {}
modules = {}


def get_value(value):

    value = value.strip()

    if value in variables:
        return variables[value]

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    if value.startswith("[") and value.endswith("]"):
        return value[1:-1].split(",")

    if value.isdigit():
        return int(value)

    return value



def check_condition(condition):

    parts = condition.split()

    if len(parts) != 3:
        return False

    left = get_value(parts[0])
    op = parts[1]
    right = get_value(parts[2])

    if op == "==":
        return left == right

    if op == ">":
        return left > right

    if op == "<":
        return left < right

    return False



def execute(lines):

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue


        # IF ELSE

        if line.startswith("if "):

            condition = line[3:]
            true_block = []
            false_block = []

            i += 1

            while i < len(lines) and lines[i].strip() not in ["else","end"]:
                true_block.append(lines[i])
                i += 1


            if i < len(lines) and lines[i].strip() == "else":

                i += 1

                while i < len(lines) and lines[i].strip() != "end":
                    false_block.append(lines[i])
                    i += 1


            if check_condition(condition):
                execute(true_block)
            else:
                execute(false_block)



        # WHILE

        elif line.startswith("while "):

            condition = line[6:]
            block = []

            i += 1

            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1


            count = 0

            while check_condition(condition) and count < 100:
                execute(block)
                count += 1



        # RUN

        elif line.startswith("run "):

            os.system(get_value(line[4:]))



        # SAY

        elif line.startswith("say "):

            print(get_value(line[4:]))



        # VARIABLE

        elif "=" in line:

            name,value = line.split("=",1)

            variables[name.strip()] = get_value(value)



        i += 1



def run(filename):

    with open(filename) as f:
        execute(f.readlines())



if __name__ == "__main__":

    if len(sys.argv)<2:
        print("GI Language v0.5")
        exit()

    run(sys.argv[1])
