import os


def get(name):

    value = os.environ.get(name)

    if value:
        print(value)
    else:
        print("")
