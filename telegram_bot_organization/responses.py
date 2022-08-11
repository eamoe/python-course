from datetime import datetime
from operator import is_
import creator
import reader
import action



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


    return "I don't understand you!"
