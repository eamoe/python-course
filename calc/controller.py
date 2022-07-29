import model
import view
import constants

def start_calc():
    form = view.create_calc_form()
    data = constants.empty_string
    mode_key = constants.calc_mode_default

    while True:
        # Get current calc state
        button, value = form.Read()
        
        # Clear button handler
        if button == constants.clear_button_text:
            data = constants.empty_string
            view.update_form_data(form, data)
        
        # Remove button handler
        elif button == constants.remove_button_text:
            data = data[:-1]
            view.update_form_data(form, data)
        
        # Max input handler
        elif len(data) == constants.max_input_length:
            pass

        # Combobox handler
        elif button == constants.combobox_key:
            mode_key = view.get_mode_key(view.get_mode_value(mode_key), form)
        
        # Calculate button handler
        elif button == constants.calculate_button_text:
            data = model.calculate(data, mode_key)
            view.update_form_data(form, data)
        
        # Close window handler
        elif button == constants.quit_button_text or button == None:
            break

        # Continue input handler
        else:
            data += button
            view.update_form_data(form, data)