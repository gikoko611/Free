#!/usr/bin/env python3

import sys

variables = {}


def get_value(value):
    value = value.strip()

    if value in variables:
        return variables[value]

    if value.isdigit():
        return int(value)

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    return value


def check_condition(condition):
    parts = condition.split()

    if len(parts) != 3:
        return False

    left = get_value(parts[0])
    op = parts[1]
    right = get_value(parts[2])

    if op == ">":
        return left > right

    if op == "<":
        return left < right

    if op == "==":
        return left == right

    return False


def execute(lines):
    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue

        if line.startswith("if "):

            condition = line[3:]
            block = []

            i += 1

            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1

            if check_condition(condition):
                execute(block)


        elif line.startswith("repeat "):

            count = int(line.split()[1])
            block = []

            i += 1

            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1

            for _ in range(count):
                execute(block)


        elif line.startswith("say "):

            print(get_value(line[4:]))


        elif "=" in line:

            name, value = line.split("=", 1)
            variables[name.strip()] = get_value(value)


        i += 1


def run(filename):

    with open(filename) as f:
        lines = f.readlines()

    execute(lines)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("GI Language v0.2")
        exit()

    run(sys.argv[1])
