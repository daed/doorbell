import subprocess


def upload():
    dropbox = ["/home/pi/Dropbox-Uploader/dropbox_uploader.sh", "upload", "/home/pi/doorbell/image.jpg", "doorbell.jpg"]
    subprocess.Popen(dropbox)
