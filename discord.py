import requests
import json
import constants


# function to create discord thread
def create_thread(channel_id, name, message):
    base_url = "{}/{}/threads".format(constants.BASE_URL, channel_id)
    payload = {
        "name": name,
        "auto_archive_duration": 4320,
        "message": {"content": message},
        "applied_tags": [],
    }
    body = json.dumps(payload)

    r = requests.post(base_url, headers=constants.DISCORD_HEADER, data=body)
    return json.loads(r.text)


# function to send message in the given thread ID
def send_thread_message(thread_id, message):
    base_url = "{}/{}/messages".format(constants.BASE_URL, thread_id)
    payload = {
        "content": message
    }
    body = json.dumps(payload)

    r = requests.post(base_url, headers=constants.DISCORD_HEADER, data=body)
    return json.loads(r.text)
