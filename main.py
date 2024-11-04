from fetch import fetchHtml
from helpers import *
    
loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

htmlSrc = fetchHtml(loginData)
print(htmlSrc)