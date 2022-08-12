from unique_id import *
from datetime import datetime as dt
import reader
import action

def generate_id():
    return get_unique_id(length = 5,
                        excluded_chars="{%!#}*->$;@~:&,^_<[]`=/'\?.()|+ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def create_item(file_name, global_action, user_message):
    path = 'telegram_bot_organization/' + file_name + '.csv'
    if file_name == "departments":
        return create_department(path, global_action, user_message)
    elif file_name == "salaries":
        return create_salary(path, global_action, user_message)
    elif file_name == "employees":
        return create_employee(path, global_action, user_message)


def create_department(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += f"Введите название:"
        action.set_action("create_department")
    elif global_action == "create_department":
        dept_id = generate_id()
        dept_name = str(user_message).capitalize()
        created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        with open(path, 'a') as file:
            file.write('{};{};{};{}\n'
                        .format(dept_id, dept_name, created, updated))
        response_str = f"Создан департамент:\nID = {dept_id}\nНаименование = {dept_name}\n"
        action.set_action("")
    return response_str


def create_salary(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += f"Введите сумму:"
        action.set_action("create_salary")
    elif global_action == "create_salary":
        salary_id = generate_id()
        salary = float(user_message)
        created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        with open(path, 'a') as file:
            file.write('{};{};{};{}\n'
                        .format(salary_id, salary, created, updated))
        response_str = f"Создана новая запись в справочнике зарплат:\nID = {salary_id}\nСумма = {salary}\n"
        action.set_action("")
    return response_str


def create_employee(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        action.write_temp_data("")
        action.set_action("add_first_name")
        return f"Укажите фамилию"
    elif global_action == "add_first_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("add_middle_name")
        return f"Укажите имя"
    elif global_action == "add_middle_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("add_dept_name")
        return f"Укажите отчество"
    elif global_action == "add_dept_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("add_salary_amount")
        response_str += f"\nСписок департаментов\n\n".upper()
        response_str += reader.show_items("departments")
        response_str += "Введите ID департамента:"
        return response_str
    elif global_action == "add_salary_amount":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("create_employee")
        response_str += f"\nСписок окладов\n\n".upper()
        response_str += reader.show_items("salaries")
        response_str += "Введите ID оклада:"
        return response_str
    elif global_action == "create_employee":
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        last_name = temp_data_list[0]
        first_name = temp_data_list[1]
        middle_name = temp_data_list[2]
        department_id = temp_data_list[3]
        salary_id = temp_data_list[4]
        action.write_temp_data("")
        employee_id = generate_id()
        created = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
        with open(path, 'a') as file:
            file.write('{};{};{};{};{};{};{};{}\n'
                        .format(employee_id, last_name, first_name, middle_name, department_id, salary_id, created, updated))
            response_str = f"Создана новая запись в справочнике сотрудников:\nID: {employee_id}\nФамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nКод департамента: {department_id}\nКод оклада: {salary_id}"
        action.set_action("")
        return response_str
