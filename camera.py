import subprocess


def click():
    cmd = ['/usr/bin/fswebcam', '-S', "40", 'image.jpg']
    subprocess.Popen(cmd)
