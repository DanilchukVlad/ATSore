import requests
from telegrampack import config


def send_message(text: str, channel_id: int):
    token = config.TOKEN
    url = "https://api.telegram.org/bot"
    # channel_id = -1001658195990
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })


def send_photo(text_photo: str, link: str, channel_id: int):
    token = config.TOKEN
    url = "https://api.telegram.org/bot"
    # channel_id = -1001658195990
    url += token
    method = url + "/sendPhoto"

    files = {'photo': open(text_photo, 'rb')}

    r = requests.post(method, files=files, data={
        "chat_id": channel_id,
        "caption": link
          })
