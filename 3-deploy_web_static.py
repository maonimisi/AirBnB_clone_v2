#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from datetime import datetime
from os.path import exists, isdir
from fabric.api import env, local, put, run

env.hosts = ['54.157.172.41', '54.174.165.251']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def deploy():
    """Distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    do_deploy(archive_path)
