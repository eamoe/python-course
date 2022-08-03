def delete_item(file_name):
    path = 'organization/' + file_name + '.csv'
    if file_name == "departments":
        return delete_department(path)
    elif file_name == "salaries":
        return delete_salary(path)
    elif file_name == "employees":
        return delete_employee(path)


def delete_department():
    return 1


def delete_salary():
    return 1


def delete_employee():
    return 1
