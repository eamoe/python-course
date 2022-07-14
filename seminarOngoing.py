from typing import List


def getUserInput(input_type = None):

    try:
        match input_type.lower():
            case 'integer':
                user_input = int(input('Введите целое число: '))
            case 'float':
                user_input = float(input('Введите вещественное число: '))
            case 'string':
                user_input = input('Введите строку: ')
            case _:
                user_input = None
    except:
        user_input = None
        print('Не удалось обработать введенное значение!')
    
    return user_input

user_input = getUserInput('integer')
print(f"Введенное значение: {user_input}")