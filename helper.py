import os
def remove_file(path):
    if os.path.exists(path):
        os.remove(path)

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def rename(name_a, name_b):
    if os.path.exists(name_a):
        os.rename(name_a, name_b)
