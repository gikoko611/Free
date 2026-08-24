import json


def load(name):

    with open(name) as f:
        data=json.load(f)

    print(data)
