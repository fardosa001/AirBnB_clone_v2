#!/usr/bin/python3
"""
fabric script based on 3-deploy_web_static.py
that deletes out-of-date archives.
"""
from fabric.api import *
from os.path import isdir
import os

env.hosts = ["34.202.233.237", "100.25.109.68"]

def do_clean(number=0):
    """
    deletes unnecessary archives in the
    versions and releases folders.
    """
    number = int(number)

    if number <= 1:
        number = 2
    else:
        number += 1

    local("cd versions; ls -t | tail -n +{} | xargs rm -rf --".format(number))

    run("cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf --".format(number))
