#!/usr/bin/python3
"""
fabric script based on 2-do_deploy_web_static.py
that creates & distributes an archive to web servers.
"""
from fabric.api import execute, local, env, put, run
from datetime import datetime
from os.path import isdir
env.hosts = ["34.202.233.237", "100.25.109.68"]


def do_pack():
    """
    creates a directory named function in
    a timestamped filename format.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if isdir("versions") is False:
            local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {}  web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """
    deploys an archive to web servers.
    """

    if archive_path is None:
        return False

    try:
        put(archive_path, "/tmp/")

        filename = archive_path.split("/")[-1]
        extracted = filename.split(".")[0]
        foldername = "/data/web_static/releases/{}".format(extracted)

        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {}".format(filename, foldername))

        run("rm /tmp/{}".format(filename))

        run("mv {}/web_static/* {}".format(foldername, foldername))

        current_link = "/data/web_static/current"
        run("rm -rf {}".format(current_link))

        run("ln -s {} {}".format(foldername, current_link))

        return True
    except Exception:
        return False


def deploy():
    """
    creates & distributes an archive to web servers.
    """

    archive_path = do_pack()

    if archive_path is None:
        return False
    return do_deploy(archive_path)
