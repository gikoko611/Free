import json


def load(name):

    with open(name) as f:
        data = json.load(f)

    return data



def save(name, data):

    with open(name, "w") as f:
        json.dump(data, f, indent=4)

    print("[GI] JSON saved:", name)
