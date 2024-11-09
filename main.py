from src.fetch import *
from src.helpers import *
from src.parse import *
from src.format import *

import json

loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

htmlSrc = fetchHtml(loginData)
if getConf("IS_DEV"):
    with open("./tmp/index.html", 'r') as file:
        htmlSrc = file.read()
    
data = parseHtml(htmlSrc)
newCalendar = formatData(data)

with open("./storage/data.json", 'r') as file:
    oldCalendar = json.loads(file.read)
