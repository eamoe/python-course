import reader
from datetime import datetime as dt
import action

def update_item(file_name, global_action, user_message):
    path = 'telegram_bot_organization/' + file_name + '.csv'
    if file_name == "departments":
        return update_department(path, global_action, user_message)
    if file_name == "salaries":
        return update_salary(path, global_action, user_message)
    if file_name == "employees":
        return update_employee(path, global_action, user_message)


def update_department(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += reader.read_departments(path)
        response_str += f"Укажите ID изменяемой записи"
        action.set_action("get_dept_id_upd")
        return response_str
    if global_action == "get_dept_id_upd":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("get_dept_name_upd")
        response_str += f"Укажите новое название отдела"
        return response_str
    if global_action == "get_dept_name_upd":
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        dept_id = temp_data_list[0]
        user_dept_name = temp_data_list[1]
        with open(path, "r") as file:
            lines = file.readlines()
        with open(path, "w") as file:
            for line in lines:
                    line = line.strip("\n")
                    line_list = line.split(";")
                    if line_list[0] == dept_id:
                        new_dept_id = line_list[0]
                        new_dept_name = user_dept_name
                        new_created = line_list[2]
                        new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                        file.write('{};{};{};{}\n'
                            .format(new_dept_id, new_dept_name, new_created, new_updated))
                    else:
                        file.write(line + "\n")
        action.write_temp_data("")
        action.set_action("")
        return f"Запись с ID {dept_id} обновлена!"


def update_salary(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += reader.read_salaries(path)
        response_str += f"Укажите ID изменяемой записи"
        action.set_action("get_salary_id_upd")
        return response_str
    if global_action == "get_salary_id_upd":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("get_salary_amount_upd")
        response_str += f"Укажите новое значение оклада"
        return response_str
    if global_action == "get_salary_amount_upd":
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        salary_id = temp_data_list[0]
        salary_amount = temp_data_list[1]
        with open(path, "r") as file:
            lines = file.readlines()
        with open(path, "w") as file:
            for line in lines:
                    line = line.strip("\n")
                    line_list = line.split(";")
                    if line_list[0] == salary_id:
                        new_salary_id = line_list[0]
                        new_amount = float(salary_amount)
                        new_created = line_list[2]
                        new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                        file.write('{};{};{};{}\n'
                            .format(new_salary_id, new_amount, new_created, new_updated))
                    else:
                        file.write(line + "\n")
        action.write_temp_data("")
        action.set_action("")
        return f"Запись с ID {salary_id} обновлена!"


def update_employee(path, global_action, user_message):
    response_str = ""
    if global_action == "":
        response_str += reader.read_employees(path)
        response_str += f"Укажите ID изменяемой записи"
        action.set_action("update_last_name")
        return response_str
    if global_action == "update_last_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_first_name")
        response_str += f"Фамилия"
        return response_str
    if global_action == "update_first_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_middle_name")
        response_str += f"Имя"
        return response_str
    if global_action == "update_middle_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_dept_name")
        response_str += f"Отчество"
        return response_str
    if global_action == "update_dept_name":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_salary_amount")
        response_str += f"\nСписок департаментов\n".upper()
        response_str += reader.show_items("departments")
        response_str += "Укажите ID департамента"
        return response_str
    if global_action == "update_salary_amount":
        temp_data = action.read_temp_data() + user_message + ';'
        action.write_temp_data(temp_data)
        action.set_action("update_employee")
        response_str += f"\nСписок окладов\n".upper()
        response_str += reader.show_items("salaries")
        response_str += "Укажите ID оклада"
        return response_str
    if global_action == "update_employee":
        temp_data = action.read_temp_data() + user_message + ';'
        temp_data_list = str(temp_data).split(";")
        employee_id = temp_data_list[0]
        last_name = temp_data_list[1]
        first_name = temp_data_list[2]
        middle_name = temp_data_list[3]
        dept_id = temp_data_list[4]
        salary_id = temp_data_list[5]
        with open(path, "r") as file:
            lines = file.readlines()
        with open(path, "w") as file:
            for line in lines:
                    line = line.strip("\n")
                    line_list = line.split(";")
                    if line_list[0] == employee_id:
                        new_employee_id = employee_id
                        new_last_name = last_name
                        new_first_name = first_name
                        new_middle_name = middle_name
                        new_dept_id = dept_id
                        new_salary_id = salary_id
                        new_created = line_list[6]
                        new_updated = str(dt.now().date()) + ' ' + str(dt.now().strftime('%H:%M:%S'))
                        file.write('{};{};{};{};{};{};{};{}\n'
                            .format(new_employee_id, new_last_name, new_first_name, new_middle_name, new_dept_id, new_salary_id, new_created, new_updated))
                    else:
                        file.write(line + "\n")
        action.write_temp_data("")
        action.set_action("")
        return f"Запись с кодом {employee_id} обновлена!"
