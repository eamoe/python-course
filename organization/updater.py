import reader
from datetime import datetime as dt

def update_item(file_name):
    path = 'organization/' + file_name + '.csv'
    if file_name == "departments":
        return update_department(path)
    if file_name == "salaries":
        return update_salary(path)
    if file_name == "employees":
        return update_employee(path)


def update_department(path):
    reader.read_departments(path)
    dept_id = input("\n\nУкажите ID изменяемой записи: ")
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
                line = line.strip("\n")
                line_list = line.split(";")
                if line_list[0] == dept_id:
                    new_dept_id = line_list[0]
                    new_dept_name = input("Введите название отдела: ")
                    new_created = line_list[2]
                    new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                    file.write('{};{};{};{}\n'
                        .format(new_dept_id, new_dept_name, new_created, new_updated))
                else:
                    file.write(line + "\n")
    return f"Запись с кодом {dept_id} удалена!"


def update_salary(path):
    return 1


def update_employee(path):
    return 1