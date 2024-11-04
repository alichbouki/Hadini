from fetch import fetchHtml
from helpers import *
from parse import parseHtml
    
loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

htmlSrc = fetchHtml(loginData)
calendar = parseHtml(htmlSrc)

print(calendar)