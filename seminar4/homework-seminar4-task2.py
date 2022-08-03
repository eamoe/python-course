#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from ast import Str


def get_number():
    try:
        number = int(input("Введите натуральное число: "))
        return number
    except:
        print("Не удалось обработать введенное значение!")

number = get_number()

def find_factors(number):
    div = 2
    factors = list()
    while div <= number:
        if number % div == 0:
            factors.append(div)
            number = number / div
        else:
            div = div + 1
    return factors

def print_factors(factors):
    factors_str = ""
    i = 1
    for element in factors:
        if i < len(factors):
            factors_str = factors_str + str(element) + " * "
        else:
            factors_str += str(element)
        i += 1
    return factors_str

if number != None:
    if number <= 0:
        print("Это не натуральное число!")
    else:
        factors = find_factors(number)
        print(f"Разложение числа {number} на простые множители:")
        print(f"{number} = {print_factors(factors)}")