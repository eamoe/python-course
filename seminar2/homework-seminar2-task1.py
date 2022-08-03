#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Например:
# 6782 -> 23
# 0,56 -> 11

from math import floor

#Получаем число от пользователя
def getNumber():
    number = None
    try:
        number = float(input('Введите число: '))
    except:
        print('Недопустимое значение!')
    return number

#Получаем беззнаковое число
def toPositive(number):
    if number < 0:
        number = -1 * number
    return number

#Получаем целую часть вещественного числа
def getIntPart(number):
    return floor(number)

#Получаем дробную часть вещественного числа
def getFractionalPart(number):
    return int(str(number)[(len(str(int(number)))+1):])

#Получаем сумму цифр числа
def calcDigitSum(number):
    sum = 0
    for digit in str(number): 
      sum += int(digit)      
    return sum

userNumber = getNumber()

if userNumber == None:
    print('Вы ввели не число. Попробуйте еще раз.')
else:
    positiveUserNumber = toPositive(userNumber)
    
    intPart = getIntPart(positiveUserNumber)
    fractPart = getFractionalPart(positiveUserNumber)
    print(f'Целая часть введенное числа: {intPart}; дробная часть введенного числа: {fractPart}')

    print(f'Сумма цифр числа {userNumber} равна {calcDigitSum(intPart) + calcDigitSum(fractPart)}')