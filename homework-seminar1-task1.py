#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def getNumber():
    try:
        number = int(input('Введите число: '))
    except:
        print('Введенное число не является целым!')
        number = -1
    return number

def getWeekday(dayNumber):
    dayweek = None
    match dayNumber:
        case 1:
            dayweek = 'понедельник'
        case 2:
            dayweek = 'вторник'
        case 3:
            dayweek = 'среда'
        case 4:
            dayweek = 'четверг'
        case 5:
            dayweek = 'пятница'
        case 6:
            dayweek = 'суббота'
        case 7:
            dayweek = 'воскресенье'
        case _:
            dayweek = 'число не соответствует ни одному дню недели!'
    return dayweek

def isHoliday(weekday):
    if weekday == 'суббота' or weekday == 'воскресенье':
        print('Это выходной день!')
    else:
        print('Это не выходной день!')

userNumber = getNumber()
userWeekday = getWeekday(userNumber)
print(f'Соответствующий день недели - {userWeekday}')
isHoliday(userWeekday)