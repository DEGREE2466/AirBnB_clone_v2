#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the contents of the web_static
All the archives must be stored in the folder versions
The name of the archive is web_static_<year><month><day><hour><minute><second>.tgz
"""
from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates the .tgz archive"""
    try:
        if isdir('versions') is False:
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archiveName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archiveName))
        return archiveName
    except:
        return None
