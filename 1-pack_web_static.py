#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Create a .tgz archive from the content of web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.exists("versions"):
        local("mkdir versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name
