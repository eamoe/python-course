import reader
import action

def delete_item(file_name, global_action, user_message):
    path = 'telegram_bot_organization/' + file_name + '.csv'
    return delete(path, file_name, global_action, user_message)


def delete(path, file_name, global_action, user_message):
    response_str = ""
    if global_action == "":
        if file_name == "departments":
            response_str += reader.read_departments(path)
            action.set_action("get_dept_id")
        elif file_name == "salaries":
            response_str += reader.read_salaries(path)
            action.set_action("get_salary_id")
        elif file_name == "employees":
            response_str += reader.read_employees(path)
            action.set_action("get_employee_id")
    
        response_str += f"\nУкажите ID удаляемой записи"
        return response_str
    elif global_action in ["get_dept_id", "get_salary_id", "get_employee_id"]:
        record_id = user_message
        with open(path, "r") as file:
            lines = file.readlines()
        with open(path, "w") as file:
            for line in lines:
                line_list = line.split(";")
                if line_list[0] == record_id:
                    pass
                else:
                    file.write(line)
        action.set_action("")
        return f"Запись с ID {record_id} удалена!"
