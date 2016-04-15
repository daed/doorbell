from switch import button_state
from camera import click
from push import push
from dropbox import upload
import time

while True:
    if button_state():
        camera = click()
        time.sleep(1.0)
        push()
        camera.wait()
        upload()
