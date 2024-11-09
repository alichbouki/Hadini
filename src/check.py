
def checkChanges(oldCalendar: dict, newCalendar: dict) -> list:
    changes = []

    for dayNum in oldCalendar.keys():
        if dayNum != "updatedOn":
            # print(dayNum)
            if oldCalendar[dayNum] != newCalendar[dayNum]:
                changes.append({
                    "day": dayNum,
                    "oldData": oldCalendar[dayNum],
                    "newData": newCalendar[dayNum]
                })
                
    return changes