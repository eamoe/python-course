from datetime import datetime
import org_constants
import reader


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("/showdepartments"):
        return reader.show_items("departments")

    if user_message in ("/showsalaries"):
        return reader.show_items("salaries")
    
    if user_message in ("/showemployees"):
        return reader.show_items("employees")

    if user_message in ("who are you", "who are you?"):
        return "I'm an Eugene's bot!"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if int(user_message) > 28 or int(user_message) < 0:
        return "Допустимые значения от 1 до 28!"

    return "I don't understand you!"
