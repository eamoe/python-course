# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
# Например:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

def unique_numbers(numbers_list):
    numbers_set = set()
    for element in numbers_list:
        numbers_set.add(element)
    return numbers_set

def get_range(numbers_set):
    first_element = numbers_set.pop()
    current_element = first_element
    while len(numbers_set) != 0:
        next_element  = numbers_set.pop()
        if (next_element - current_element) == 1:
            current_element = next_element
    return [first_element, current_element]


        

numbers_list = [1, 5, 2, 3, 4, 1, 7]

print(f"Исходный список: {numbers_list}")
print(f"Возрастающая последовательность: {get_range(unique_numbers(numbers_list))}")