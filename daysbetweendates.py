def isleapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysinmonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28
    else:
        return 0  # Invalid month

def nextDay(year, month, day):
    if day < daysinmonth(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            if day1 < day2:
                return True
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
