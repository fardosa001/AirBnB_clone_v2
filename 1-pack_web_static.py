#!/usr/bin/python3
"""
fabric script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    creates a directory named function in
    a timestamped filename format.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {}  web_static".format(filename))
        return filename
    except:
        return None
