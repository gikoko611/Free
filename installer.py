import os

PACKAGE_DIR = "packages"


def install(name):

    path = os.path.join(PACKAGE_DIR, name)

    if os.path.exists(path):
        print("[GI] Package already exists")
        return

    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write(
'''def run():
    print("Hello from GI package")
'''
        )

    print("[GI] Installed:", name)
