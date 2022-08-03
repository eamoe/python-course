#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#Например:
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

def get_position_of_x_occurrence(input_list, value, occurrence_number):
    
    current_occurrence = 0
    current_position = 0
    found_position = -1

    for element in input_list:
        if element == value:
            current_occurrence += 1
            if current_occurrence == occurrence_number:
                found_position = current_position
        current_position += 1
    
    return found_position

#user_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
#user_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
#user_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
#user_list = ["123", "234", 123, "567"]
#user_list = []
user_list = ["a", "a", "a", "b", "c", "a", "a", "a", "a", "d", "b", "e"]

print(f'Исходный список {user_list}')

user_element = input('Какой элемент ищем? ')
occurrence = int(input('Какое вхождение? '))

print(f"{occurrence} вхождение элемента '{user_element}' находится на позиции {get_position_of_x_occurrence(user_list, user_element, occurrence)}")