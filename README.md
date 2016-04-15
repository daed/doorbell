# doorbell
A raspberry pi doorbell app

To make work:

Set up Raspbian (I used NOOBS)

sudo apt-get update

sudo apt-get install python3 libopencv-dev python-opencv fswebcam python-pycurl libcurl4-openssl-dev libssl-dev

sudo pip3 install pycurl

git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
run dropbox-uploader.sh in Dropbox-Uploader directory and follow directions

Open a browser and go to https://instapush.im/.  Get an account.
- Set up event title as "Doorbell"
- The handler should be "msg"
- The push message should be "{msg}"
- change appID and appSecret in push.py to reflect the ones provided to you by
     Instapush

Set up instapush on your phone and log in.

Wire doorbell to pin 17 and a ground pin.
