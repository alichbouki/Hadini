from selenium import webdriver
from helpers import *

def fetchHtml(loginData: dict) -> str:
    LOGIN_BTN_ID = "#Button1"
    USERNAME_FIELD_ID = "#Username"
    PASSWORD_FIELD_ID = "#Password"

    LOGIN_URL = "https://universitic.ueuromed.org/konosys/PC_MV_login.aspx"
    CALENDAR_URL = "https://universitic.ueuromed.org/konosys/interfaces/MonPlanning_Utilisateur_Lot.aspx"

    USERNAME = str(loginData["login"]).replace("\"", "")
    PASSWORD = str(loginData["password"]).replace("\"", "")
    
    logDebug("Starting a new Firefox instance....")

    browser = webdriver.Firefox()
    browser.get(LOGIN_URL)
    
    logDebug("Logging in...")

    browser.find_element('css selector', USERNAME_FIELD_ID).send_keys(USERNAME)
    browser.find_element('css selector', PASSWORD_FIELD_ID).send_keys(PASSWORD)
    browser.find_element("css selector", LOGIN_BTN_ID).click()

    logDebug("Logging in completed.")
    logDebug("Fetching calendar HTML src...")

    browser.get(CALENDAR_URL)

    htmlSrc = browser.page_source

    logDebug("HTML fetched.")
    
    if getConf("IS_DEV"):
        with open("./tmp/index.html", 'w') as htmlFile:
            htmlFile.write(htmlSrc)
            htmlFile.close()

    browser.quit()
    
    return htmlSrc