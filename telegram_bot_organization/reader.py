def show_items(file_name):
    path = 'telegram_bot_organization/' + file_name + '.csv'
    if file_name == "departments":
        return read_departments(path)
    if file_name == "salaries":
        return read_salaries(path)
    if file_name == "employees":
        return read_employees(path)


def read_departments(path):
    departments_str = ""
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        departments_str += f"ID: {list_items[0]}\n"
        departments_str += f"Наименование: {list_items[1]}\n"
        departments_str += f"Создан: {list_items[2]}\n"
        departments_str += f"Изменен: {list_items[3]}\n\n"
    data.close()
    return departments_str


def read_salaries(path):
    salaries_str = ""
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        salaries_str += f"ID: {list_items[0]}\n"
        salaries_str += f"Оклад: {list_items[1]}\n"
        salaries_str += f"Создан: {list_items[2]}\n"
        salaries_str += f"Изменен: {list_items[3]}\n\n"
    data.close()
    return salaries_str


def read_employees(path):
    employees_str = ""
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        employees_str += f"ID: {list_items[0]}\n"
        employees_str += f"Фамилия: {list_items[1]}\n"
        employees_str += f"Имя: {list_items[2]}\n"
        employees_str += f"Отчество: {list_items[3]}\n"
        employees_str += f"Отдел: {get_dept_name(list_items[4])}\n"
        employees_str += f"Оклад: {get_salary_amount(list_items[5])}\n"
        employees_str += f"Создан: {list_items[6]}\n"
        employees_str += f"Изменен: {list_items[7]}\n\n"
    data.close()
    return employees_str


def get_dept_name(dept_id):
    dept_name = f"запись {dept_id} не найдена"
    path = 'telegram_bot_organization/' + "departments" + '.csv'
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        if list_items[0] == dept_id:
            dept_name = list_items[1]
    data.close()
    return dept_name


def get_salary_amount(salary_id):
    dept_name = f"запись {salary_id} не найдена"
    path = 'telegram_bot_organization/' + "salaries" + '.csv'
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        if list_items[0] == salary_id:
            dept_name = list_items[1]
    data.close()
    return dept_name