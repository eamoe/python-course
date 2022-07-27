# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Например:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Например:
# 1+2*3 => 7;
# (1+2)*3 => 9;


from unittest import result


sum         = lambda x, y: x + y
multiply    = lambda x, y: x * y
divide      = lambda x, y: x / y
sub         = lambda x, y: x - y


def calc(operation, x, y):
    return operation(x, y)


def calc_expression(single_expression):
    first_number = int(single_expression[0])
    operator = single_expression[1]
    second_number = int(single_expression[2])
    if operator == '/':
        result = calc(divide, first_number, second_number)
    elif operator == '*':
        result = calc(multiply, first_number, second_number)
    elif operator == '-':
        result = calc(sub, first_number, second_number)
    elif operator == '+':
        result = calc(sum, first_number, second_number)
    return int(result)


def calc_parenthesis_expressions(expression_str):
    result_str = expression_str
    for i in range(0, len(expression_str) - 1):
        single_exression = ""
        if expression_str[i] == '(':
            j = i + 1
            while expression_str[j] != ')':
                single_exression += expression_str[j]
                j = j + 1
            parenthesis_expression_result = calc_expression(single_exression)
            result_str = result_str.replace(f"({single_exression})", str(parenthesis_expression_result))
    return result_str


def calc_div_expressions(expression_str):
    result_str = expression_str
    for i in range(0, len(expression_str) - 1):
        single_exression = ""
        if expression_str[i] == '/':
            single_exression = expression_str[i - 1] + expression_str[i] + expression_str[i + 1]
            expression_result = calc_expression(single_exression)
            result_str = result_str.replace(f"{single_exression}", str(expression_result))
    return result_str


def calc_multiply_expressions(expression_str):
    result_str = expression_str
    for i in range(0, len(expression_str) - 1):
        single_exression = ""
        if expression_str[i] == '*':
            single_exression = expression_str[i - 1] + expression_str[i] + expression_str[i + 1]
            expression_result = calc_expression(single_exression)
            result_str = result_str.replace(f"{single_exression}", str(expression_result))
    return result_str


def calc_sub_expressions(expression_str):
    result_str = expression_str
    for i in range(0, len(expression_str) - 1):
        single_exression = ""
        if expression_str[i] == '-':
            single_exression = expression_str[i - 1] + expression_str[i] + expression_str[i + 1]
            expression_result = calc_expression(single_exression)
            result_str = result_str.replace(f"{single_exression}", str(expression_result))
    return result_str


def calc_sum_expressions(expression_str):
    result_str = expression_str
    for i in range(0, len(expression_str) - 1):
        single_exression = ""
        if expression_str[i] == '+':
            single_exression = expression_str[i - 1] + expression_str[i] + expression_str[i + 1]
            expression_result = calc_expression(single_exression)
            result_str = result_str.replace(f"{single_exression}", str(expression_result))
    return result_str


expression_str = "(1+2)/3+(4-2)*2"

calc_parhenthesis_str = calc_parenthesis_expressions(expression_str)
calculated_expression = calc_sum_expressions(calc_sub_expressions(calc_multiply_expressions(calc_div_expressions(calc_parhenthesis_str))))
print(f"Выражение: {expression_str}")
print(f"Результат: {calculated_expression}")