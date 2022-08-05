#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from multiprocessing.sharedctypes import Value
import ongoing_experiments.library as l

def countListNumericalElements(user_list):
    number_counter = 0
    other_counter = 0

    for element in user_list:
        try:    
            if float(element):
                number_counter += 1
        except:
            other_counter += 1

    return (number_counter, other_counter)

def is_value_exists(user_list, number):
    check = False
    str_number = str(number)
    for element in user_list:
        if element == str_number:
            check = True
    
    return check

#Задаем элементы списка и формируем список
user_input = l.getUserInput('string', 'Введите список одной строкой, разделяя элементы знаком пробела: ')
user_list = user_input.split(' ')
print(f'\nСписок элементов: {user_list}')

#Вычисляем количество числовых и нечисловых элементов списка
counter_cortege = countListNumericalElements(user_list)
print(f'В списке {len(user_list)} элементов.\nИз них {counter_cortege[0]} числовых и {counter_cortege[1]} нечисловых.')


#Проверяем наличие элемента в списке
value = input('Какое значение необходимо найти? ')

if is_value_exists(user_list, value):
    print(f"В списке есть элемент '{value}'")
else:
    print(f"В списке нет элемента '{value}'")