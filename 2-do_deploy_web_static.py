#!/usr/bin/python3
"""
fabric script based on 1-pack_web_static.py
that distributes an archive to a web server.
"""
from fabric.api import env, put, run
import os.path
env.hosts = ["34.202.233.237", "100.25.109.68"]


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

        print("New version deployed!")
        return True
    except Exception:
        return False
