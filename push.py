import pycurl
import json
from io import BytesIO as StringIO


def push():
    # set this to Application ID from Instapush
    appID = "<FILL THIS IN>"

    # set this to the Application Secret from Instapush
    appSecret = "<FILL THIS IN>"

    # leave this set to DoorAlert unless you named your event something different in Instapush
    pushEvent = "Doorbell"

    # set this to what you want the push message to say
    pushMessage = "Ding dong!  Check doorbell.jpg on dropbox!"

    # use StringIO to capture the response from our push API call
    buffer = StringIO()

    # use Curl to post to the Instapush API
    c = pycurl.Curl()

    # set Instapush API URL
    c.setopt(c.URL, 'https://api.instapush.im/v1/post')

    # setup custom headers for authentication variables and content type
    c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
         'x-instapush-appsecret: ' + appSecret,
         'Content-Type: application/json'])

    # create a dictionary structure for the JSON data to post to Instapush
    json_fields = {}

    # setup JSON values
    json_fields['event'] = pushEvent
    json_fields['trackers'] = {}
    json_fields['trackers']['msg'] = pushMessage

    postfields = json.dumps(json_fields)

    # make sure to send the JSON with post
    c.setopt(c.POSTFIELDS, postfields)

    # set this so we can capture the resposne in our buffer
    c.setopt(c.WRITEFUNCTION, buffer.write)

    # uncomment to see the post that is sent
    # c.setopt(c.VERBOSE, True)
    c.perform()

    # capture the response from the server
    body = buffer.getvalue()

    # print the response
    print(body)

    # reset the buffer
    buffer.truncate(0)
    buffer.seek(0)

    # cleanup
    c.close()
