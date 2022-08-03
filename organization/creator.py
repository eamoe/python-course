from unique_id import *
from datetime import datetime as dt

def generate_id():
    return get_unique_id(length = 5,
                        excluded_chars="{%!#}*->$;@~:&,^_<[]`=/'\?.()|+")


def create_department(path):
    print("Cоздание департамента".upper())
    dept_id = generate_id()
    dept_name = input("Введите название: ")
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    with open(path, 'a') as file:
        file.write('{};{};{};{}\n'
                    .format(dept_id, dept_name, created, updated))
    return f"Создан департамент:\n\nID = {dept_id}\nНаименование = {dept_name}\n"


def create_salary(path):
    print("Cоздание оклада".upper())
    salary_id = generate_id()
    salary = float(input("Введите сумму: "))
    created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
    with open(path, 'a') as file:
        file.write('{};{};{};{}\n'
                    .format(salary_id, salary, created, updated))
    return f"Создана новая запись в справочнике зарплат:\n\nID = {salary_id}\nСумма = {salary}\n"


def create_item(file_name):
    path = 'organization/' + file_name + '.csv'
    if file_name == "departments":
        return create_department(path)
    elif file_name == "salaries":
        return create_salary(path)