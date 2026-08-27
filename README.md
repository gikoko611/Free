# GI Language

GI Language is a simple scripting language designed to be easy to learn and run on Termux/Linux environments.

## Features

- Variables
- Functions
- Return values
- If / Else conditions
- While loops
- For loops
- Range support
- Lists
- Dictionaries
- Modules
- REPL mode

## Installation (Termux)

Install required packages:

    pkg update
    pkg install git python

Clone GI Language:

    git clone https://github.com/gikoko611/Free.git GI
    cd GI

Install GI command:

    chmod +x gi_v1.9_stable.py
    ln -sf ~/GI/gi_v1.9_stable.py $PREFIX/bin/gi

Check installation:

    gi --version

Example:

    GI Language v1.7

## Usage

Run a GI program:

    gi example.gi

## Example

Create a file:

    cat > example.gi <<'EOF'
    say "Hello GI"

    for i in range(5)
    say i
    end
    EOF

Run:

    gi example.gi

Output:

    Hello GI
    0
    1
    2
    3
    4

## Interactive Mode

Start GI:

    gi

Example:

    say "Hello"

Output:

    Hello

## Version

GI Language v1.7 stable

## Project Goal

GI Language is a lightweight programming language for simple scripting and learning.

## Repository

GitHub:
https://github.com/gikoko611/Free
