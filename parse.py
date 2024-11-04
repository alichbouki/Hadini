from datetime import *
from helpers import *

def parseHtml(html: str):
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
        
    # print(dates)
    
    sessions = data.removeprefix("AjouterRDV").split("AjouterRDV")
    sessions.pop(0)
    
    calendar = {
        "1":[],
        "2":[],
        "3":[],
        "4":[],
        "5":[],
        "6":[],
        "7":[],
    }

    for session in sessions:
        id = sessions.index(session)
        
        session = session.replace("'", '').removeprefix('(').removesuffix(')')
        data = session.split(',')
        session = [data[1], data[2], data[3], data[4].replace("  - ", "")]
        
        classDate = date(
            int(dates[int(data[0])-1][2]), 
            int(dates[int(data[0])-1][1]),
            int(dates[int(data[0])-1][0])
        )
        classStartTime = time(int(session[0]), int(session[1]))
        
        calendar[str(data[0])].append({
            "class": session[3],
            "startingHour": datetime.combine(classDate, classStartTime),
            "classDuration": session[2]
        })
        
        sessions[id] = session
    
    return calendar    
        
    # print(calendar)
    