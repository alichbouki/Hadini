from fetch import fetchHtml
from helpers import *
from parse import parseHtml
    
loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

with open("./tmp/index.html", 'r') as htmlFile:
    htmlSrc = htmlFile.read()

# htmlSrc = fetchaHtml(loginData)
# logDebug(htmlSrc)

calendar = parseHtml(htmlSrc)