import os
import shutil


def remkdir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)
