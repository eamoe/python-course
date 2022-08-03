from turtle import clear
import constants
import creator
import os
import reader

clear = lambda: os.system('clear')

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
    file_name = get_file_name(main_menu_item)
    # Show list of items
    if sub_menu_item == 0:
        reader.show_items(file_name)
        print(f"Вот список данных из таблицы: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")
    # Create a new item
    elif sub_menu_item == 1:
        message = creator.create_item(file_name)
        clear()
        input(f"{message}\nНажмите Enter, чтобы продолжить!")
    # Update an item
    elif sub_menu_item == 2:
        print(f"Изменили запись в таблице: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")
    # Remove an item
    elif sub_menu_item == 3:
        print(f"Удалили запись из таблицы: {constants.main_menu_items[main_menu_item]}")
        input("Нажмите Enter, чтобы продолжить!")