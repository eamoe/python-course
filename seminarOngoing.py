from typing import List


def getUserInput(inputType = None):

    try:
        match inputType.lower():
            case 'integer':
                userInput = int(input('Введите целое число: '))
            case 'float':
                userInput = float(input('Введите вещественное число: '))
            case 'string':
                userInput = input('Введите строку: ')
            case _:
                userInput = None
    except:
        userInput = None
        print('Не удалось обработать введенное значение!')
    
    return userInput

userInput = getUserInput('integer')
print(f"Введенное значение: {userInput}")