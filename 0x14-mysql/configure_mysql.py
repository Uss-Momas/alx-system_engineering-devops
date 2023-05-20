#!/usr/bin/python3
from fabric.api import *
import os


env.user = "ubuntu"
env.hosts = ['34.202.159.196', '34.207.211.106']
env.key_filename = '~/.ssh/id_rsa'


def do_send(archive_path):
    try:
        if os.path.exists(archive_path):
            put(archive_path, '~/')
            return True
    except Except:
        return False
