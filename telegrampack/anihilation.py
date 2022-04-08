from selenium import webdriver
from time import sleep
from telegrampack.telegram_api import TgApi
import requests

tg = TgApi()


def take_screenshot():
    message = 'Внимание!'

    browser = webdriver.Chrome()

    browser.get("https://www.bezlimit.ru/")

    sleep(1)


def send_photo_telegram():
    files = {'photo': open('../autotest/StoreTestScreen.png', 'rb')}
    token = '5156460237:AAEt1if6meaEGae-8lVWp20Egj4TnBdDdEs'
    chat_id = '-1001658195990' # если у вас группа то будет так chat_id = "-1009999999"
    r = requests.post("https://api.telegram.org/bot"+token+"/sendPhoto?chat_id=" + chat_id, files=files)
    if r.status_code != 200:
        raise Exception("post_text error")
