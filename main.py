from selenium import webdriver
from jproperties import Properties

configs = Properties()

LOGIN_BTN_ID = "#Button1"
USERNAME_FIELD_ID = "#Username"
PASSWORD_FIELD_ID = "#Password"

LOGIN_URL = "https://universitic.ueuromed.org/konosys/PC_MV_login.aspx"

with open('.env', 'rb') as config_file:
    configs.load(config_file)

USERNAME = str(configs.get("USERNAME").data).replace("\"", "")
PASSWORD = str(configs.get("PASSWORD").data).replace("\"", "")


browser = webdriver.Firefox()
browser.get(LOGIN_URL)

browser.find_element('css selector', USERNAME_FIELD_ID).send_keys(USERNAME)
browser.find_element('css selector', PASSWORD_FIELD_ID).send_keys(PASSWORD)
browser.find_element("css selector", LOGIN_BTN_ID).click()

while input() != 'e':
    pass

browser.quit()