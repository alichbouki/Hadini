from fetch import fetchHtml
from helpers import *
from parse import parseHtml
import json
    
loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

htmlSrc = fetchHtml(loginData)
# with open("./tmp/index.html", 'r') as file:
#     htmlSrc = file.read()
    
calendar = parseHtml(htmlSrc)

with open("./storage/data.json", 'w') as file:
    json.dump(calendar, file)

# print(calendar)