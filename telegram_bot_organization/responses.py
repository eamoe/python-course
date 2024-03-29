from datetime import datetime
import creator
import reader
import action
import remover
import updater



def sample_responses(input_text):
    user_message = str(input_text).lower()
    global_action = action.get_action()

    # Show items
    if user_message in ("/showdepartments"):
        return reader.show_items("departments")
    if user_message in ("/showsalaries"):
        return reader.show_items("salaries")
    if user_message in ("/showemployees"):
        return reader.show_items("employees")

    # Create item
    if user_message in ("/createdepartment") or global_action == "create_department":
        response = creator.create_item("departments", global_action, user_message)
        return response
    if user_message in ("/createsalary") or global_action == "create_salary":
        response = creator.create_item("salaries", global_action, user_message)
        return response
    if user_message in ("/createemployee") or global_action in ["add_first_name", "add_middle_name", "add_dept_name", "add_salary_amount", "create_employee"]:
        response = creator.create_item("employees", global_action, user_message)
        return response
    
    # Delete item
    if user_message in ("/deletedepartment") or global_action == "get_dept_id":
        response = remover.delete_item("departments", global_action, user_message)
        return response
    if user_message in ("/deletesalary") or global_action == "get_salary_id":
        response = remover.delete_item("salaries", global_action, user_message)
        return response
    if user_message in ("/deleteemployee") or global_action == "get_employee_id":
        response = remover.delete_item("employees", global_action, user_message)
        return response

    # Update item
    if user_message in ("/updatedepartment") or global_action in ["get_dept_id_upd", "get_dept_name_upd"]:
        response = updater.update_item("departments", global_action, user_message)
        return response
    if user_message in ("/updatesalary") or global_action in ["get_salary_id_upd", "get_salary_amount_upd"]:
        response = updater.update_item("salaries", global_action, user_message)
        return response
    if user_message in ("/updateemployee") or global_action in ["update_last_name", "update_first_name", "update_middle_name", "update_dept_name", "update_salary_amount", "update_employee"]:
        response = updater.update_item("employees", global_action, user_message)
        return response

    return "I don't understand you!"
