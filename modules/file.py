def write(name, text):

    with open(name, "w") as f:
        f.write(text)

    print("[GI] File saved:", name)



def read(name):

    with open(name) as f:
        print(f.read())
