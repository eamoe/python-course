# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Например:
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from ast import Str


def getNumber():
    number = None
    try:
        number = int(input('Введите число: '))
    except:
        print('Недопустимое значение!')
    return number

def factorial(n):
    fact = 1
    for factor in range(1, n + 1):
        fact *= factor
    return fact

def getFactorialList(number):
    factList = []
    for x in range(1, number + 1):
        factList.append(factorial(x))
    return factList

userNumber = getNumber()

if userNumber == None:
    print('Вы ввели не число. Попробуйте еще раз.')
else:
    print(getFactorialList(userNumber))