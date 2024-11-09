from datetime import *

def formatData(data: dict) -> dict:
    dates = data["dates"]
    sessions = data["sessions"]
    
    now = datetime.now().isoformat()
    
    calendar = {
        "updatedOn": now,
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
        
        startingTime = datetime.combine(classDate, classStartTime).isoformat(),
        endingTime = datetime.combine(classDate, classStartTime) + timedelta(minutes = int(session[2]))
        
        calendar[str(data[0])].append({
            "class": session[3],
            "startingTime": startingTime,
            "endingTime": endingTime.isoformat(),
            "classDuration": session[2]
        })
        
        sessions[id] = session
    
    return calendar