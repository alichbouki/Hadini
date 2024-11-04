from selenium import webdriver
from jproperties import Properties

configs = Properties()

LOGIN_BTN_ID = "#Button1"
USERNAME_FIELD_ID = "#Username"
PASSWORD_FIELD_ID = "#Password"

LOGIN_URL = "https://universitic.ueuromed.org/konosys/PC_MV_login.aspx"
CALENDAR_URL = "https://universitic.ueuromed.org/konosys/interfaces/MonPlanning_Utilisateur_Lot.aspx"

with open('.env', 'rb') as configFile:
    configs.load(configFile)
    configFile.close()

USERNAME = str(configs.get("USERNAME").data).replace("\"", "")
PASSWORD = str(configs.get("PASSWORD").data).replace("\"", "")

browser = webdriver.Firefox()
browser.get(LOGIN_URL)

browser.find_element('css selector', USERNAME_FIELD_ID).send_keys(USERNAME)
browser.find_element('css selector', PASSWORD_FIELD_ID).send_keys(PASSWORD)
browser.find_element("css selector", LOGIN_BTN_ID).click()

browser.get(CALENDAR_URL)

htmlSrc = browser.page_source

print(htmlSrc)

with open("./tmp/index.html", 'x') as htmlFile:
    htmlFile.write(htmlSrc)
    htmlFile.close()

while input() != 'e':
    pass

browser.quit()