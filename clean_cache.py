import os

dir_path = '__pycache__'

def clean():
    dir_path = '__pycache__'
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            if name.endswith((".pyc")):
                os.remove(os.path.join(root, name))
            else:
                pass
clean()