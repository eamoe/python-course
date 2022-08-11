import org_constants

def show_menu():
    menu_str = ""
    menu_str += "Департаменты\n".upper()
    menu_str += "/showdepartments" + " - " + "список" + "\n"
    menu_str += "/createdepartment" + " - " + "добавить" + "\n"
    menu_str += "/updatedepartment" + " - " + "обновить" + "\n"
    menu_str += "/deletedepartment" + " - " + "удалить" + "\n"

    menu_str += "Сотрудники\n".upper()
    menu_str += "/showemployees" + " - " + "список" + "\n"
    menu_str += "/createemployee" + " - " + "добавить" + "\n"
    menu_str += "/updateemployee" + " - " + "обновить" + "\n"
    menu_str += "/deleteemployee" + " - " + "удалить" + "\n"

    menu_str += "Зарплаты\n".upper()
    menu_str += "/showsalaries" + " - " + "список" + "\n"
    menu_str += "/createsalary" + " - " + "добавить" + "\n"
    menu_str += "/updatesalary" + " - " + "обновить" + "\n"
    menu_str += "/deletesalary" + " - " + "удалить" + "\n"
    
    return menu_str


def menu_handler():
    return 'Chosen menu item'