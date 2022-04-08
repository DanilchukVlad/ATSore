from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from telegrampack.telegram_api import TgApi
from telegrampack import chat
import requests
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/atsore/drivers/chromedriver_lnx')


def authorize(adress, login_path, login, password_path, password, button, path):
    driver.get(adress)
    tg = TgApi()

    answer = 0

    login_input = driver.find_element(By.XPATH, login_path)

    login_input.send_keys(login)

    password_input = driver.find_element(By.XPATH, password_path)

    password_input.send_keys(password)

    button_enter = driver.find_element(By.XPATH, button)

    button_enter.click()

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        answer = 0
        return answer
    except:
        message = f"Внимание! Возникла ОШИБКА при попытке авторизации!\n" \
                   f"{adress}"

        driver.get(adress)

        driver.get_screenshot_as_file("autotest/StoreTestScreen.png")

        tg.send_message(message, chat.STORE_ERROR_CHAT_ID)

        send_photo_telegram()

        answer = 1

        return answer


def page_test(adress, path):
    driver.get(adress)

    tg = TgApi()

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))

    except:


        message = f"Внимание! Возникла ОШИБКА при попытке открыть страницу!\n" \
                   f"{adress}"

        driver.get(adress)

        driver.get_screenshot_as_file("autotest/StoreTestScreen.png")

        tg.send_message(message, chat.STORE_ERROR_CHAT_ID)

        send_photo_telegram()



def send_photo_telegram():  # Отправка фото в телеграм
    files = {'photo': open('autotest/StoreTestScreen.png', 'rb')}

    token = '5156460237:AAEt1if6meaEGae-8lVWp20Egj4TnBdDdEs'

    chat_id = '-1001658195990'

    r = requests.post("https://api.telegram.org/bot"+token+"/sendPhoto?chat_id=" + chat_id, files=files)


if authorize('https://store.bezlimit.ru/', '//*[@id="loginform-login"]', 'autotest', '//*[@id="loginform-password"]', 'QualityAssurance', '//*[@id="login-form"]/button', '/html/body/div/div/div[4]/div[1]/div[1]/a[1]') == 0:
    time.sleep(5)

    page_test('https://store.bezlimit.ru/promo', '/html/body/div/div/div[4]/div[1]/div[1]/a[1]')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/promo/internet', '/html/body/div/div/div[3]/div/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/delivery', '/html/body/div[1]/div/a[3]')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/lottery/9', '/html/body/div/div/div[5]/div')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/promo/buy-phone', '/html/body/div[1]/div/div[4]/div[3]/div[2]/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/my/reservations', '/html/body/div/div/div[1]/div/div[1]/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/my/activations', '/html/body/div/div/div[1]/div/div[1]/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/bonus', '/html/body/div/div/div[1]/div/div[1]/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/app/news', '/html/body/div/div/div[3]/div[1]/a')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/profile', '/html/body/div[1]/div/div[3]/a[1]')

    time.sleep(5)

    page_test('https://store.bezlimit.ru/app/support', '/html/body/div[1]/div/a')

    driver.quit()
else:
    driver.quit()
