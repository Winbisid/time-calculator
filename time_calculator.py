# def add_time(start, duration):
#   new_time = 1
#   return new_time
import math

def add_time(*args):
    new_time = len(args)
    if len(args) < 2:
        return "Time is money. Don't waste mine."

    beginTime = args[0][0:-3]
    timeToAdd = args[1]
    beginDay = None
    if len(args) == 3:
        beginDay = args[2]

    dayOrNight = args[0][-2:]
    beginTimeHour = beginTime.split(':')[0]
    beginTimeMin = beginTime.split(':')[1]
    timeToAddHour = timeToAdd.split(':')[0]
    timeToAddMin = timeToAdd.split(':')[1]
    newHour = 0
    newMin = beginTimeMin
    dayCount = 0
    showDays = ''
    showDaysCount = ''
    day = None

    totalMins = int(beginTimeMin) + int(timeToAddMin)
    if totalMins >= 60:
        newMin = totalMins % 60
        newHour += 1
    else:
        newMin = totalMins

    if newMin < 10:
        newMin = f'0{newMin}'

    totalHours = int(beginTimeHour) + int(timeToAddHour)

    if (totalHours + newHour) / 12 >= 4:
        dayCount = int(math.floor((totalHours + newHour) / 12) / 2)
    elif (totalHours + newHour) / 12 >= 2:
        dayCount = 1

    if totalHours + newHour >= 12 and dayOrNight == 'PM':
        dayCount += 1

    timeLine = ((totalHours + newHour) / 12) % 2
    if timeLine >= 1 and dayOrNight == 'AM':
        dayOrNight = 'PM'
    elif timeLine >= 1 and dayOrNight == 'PM':
        dayOrNight = 'AM'

    newHour += totalHours % 12

    if dayCount == 1:
        showDaysCount = '(next day)'
    elif dayCount > 1:
        showDaysCount = (f'({dayCount} days later)')

    if beginDay and dayCount == 0:
        day = beginDay

    if beginDay and dayCount >= 1:
        day = beginDay.capitalize()
        daysOfTheWeek = {
            0: 'Sunday', 1: 'Monday', 2: 'Tuesday',
            3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

        for idx, d in daysOfTheWeek.items():
            if d == day:
                index = (idx + dayCount) % 7
                day = daysOfTheWeek[index]
                break

    if day:
        new_time = f'{newHour}:{newMin} {dayOrNight}, {day} {showDaysCount}'
    else:
        new_time = f'{newHour}:{newMin} {dayOrNight} {showDaysCount}'

    return new_time.strip()