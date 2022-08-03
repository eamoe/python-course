import constants

def get_file_name(menu_item):
    match menu_item:
        case 0:
            return "departments"
        case 1:
            return "employees"
        case 2:
            return "salaries"
        case __:
            return -1
    

def command_handler(main_menu_item, sub_menu_item):
    file_name = f"{get_file_name(main_menu_item)}.json"
    # Show list of items
    if sub_menu_item == 0:
        print(f"Вот список данных из таблицы: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")
    # Create a new item
    elif sub_menu_item == 1:
        print(f"Добавили новую запись в таблицу: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")
    # Update an item
    elif sub_menu_item == 2:
        print(f"Изменили запись в таблице: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")
    # Remove an item
    elif sub_menu_item == 3:
        print(f"Удалили запись из таблицы: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")