#!/usr/bin/python3
# Fabfile used to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["34.232.78.233", "54.146.69.106"]


def do_clean(number=0):
    """Deleting out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is either 0 or 1, keeps only the most recent archive.
    If number is 2, keeps the most and second-most recent archives,
    etcetera.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
