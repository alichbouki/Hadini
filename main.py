from src.fetch import *
from src.helpers import *
from src.parse import *
from src.format import *
from src.check import *

import json

loginData = {
    "login": getConf("USERNAME"),
    "password": getConf("PASSWORD")
}

htmlSrc = ""

if getConf("IS_DEV"):
    with open("./tmp/index.html", 'r') as file:
        htmlSrc = file.read()
else: 
    htmlSrc = fetchHtml(loginData)
    
    
data = parseHtml(htmlSrc)
newCalendar = formatData(data)

oldCalendar = {}
with open("./storage/data.json", 'r') as file:
    oldCalendar = dict(json.loads(file.read()))

changes = checkChanges(oldCalendar, newCalendar)

with open("./storage/data.json", 'w') as file:
    file.write(json.dumps(newCalendar))