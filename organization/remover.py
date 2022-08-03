import reader

def delete_item(file_name):
    path = 'organization/' + file_name + '.csv'
    return delete(path, file_name)


def delete(path, file_name):
    if file_name == "departments":
        reader.read_departments(path)
    if file_name == "salaries":
        reader.read_salaries(path)
    if file_name == "employees":
        reader.read_employees(path)
    dept_id = input("\n\nУкажите ID удаляемой записи: ")
    with open(path, "r") as file:
        lines = file.readlines()
    with open(path, "w") as file:
        for line in lines:
            line_list = line.split(";")
            if line_list[0] == dept_id:
                pass
            else:
                file.write(line)
    return f"Запись с кодом {dept_id} удалена!"




def delete_salary():
    return 1


def delete_employee():
    return 1
