from datetime import *
from src.helpers import *

def parseHtml(html: str) -> dict:
    list1 = html.split("DessinePlanningSemaineEx")
    list2 = list1[1].split("afficheTout")
    
    data = list2[0]
    
    tmpDates = data.removeprefix('(').replace("'", '').split(')')[0].split(',')
    dates = []
    
    for session in range(0,7):
        dates.append(tmpDates[session])
        
    for _date in dates:
        id = dates.index(_date)
        
        date1 = _date.split("/")
        
        dates[id] = date1
        
    sessions = data.removeprefix("AjouterRDV").split("AjouterRDV")
    sessions.pop(0)
    
    return {"sessions": sessions, "dates": dates}
     
        