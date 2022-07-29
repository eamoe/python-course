from statistics import mode
from PySimpleGUI import *
import constants


def get_mode_value(mode_key):
    return constants.calc_modes[mode_key]


def get_mode_key(mode_value, form = None):
    if form != None:
        mode_value = form.find_element(constants.combobox_key).get()
    if mode_value == constants.calc_modes[0]:
        mode_key = 0
    elif mode_value == constants.calc_modes[1]:
        mode_key = 1
    elif mode_value == constants.calc_modes[2]:
        mode_key = 2
    else:
        mode_key = 0
    return mode_key


def get_layout():

    layout =    [[Text(constants.calc_mode_label, size = (20, 1), font = ('Lucida', 18), justification = 'left')],

                [Combo([get_mode_value(0), get_mode_value(1), get_mode_value(2)],
                        default_value = get_mode_value(0),
                        key = constants.combobox_key,
                        size = (17, 1),
                        font = 'Lucida 15',
                        enable_events = True)],

		        [Txt(constants.empty_string * 10)],

                [Text(constants.empty_string,
                    size = (25, 2),
                    font = ('Helvetica', 22),
                    text_color = 'black',
                    key = 'input',
                    background_color='white')],

		        [Txt(constants.empty_string * 10)],

		        [ReadFormButton(constants.clear_button_text), ReadFormButton(constants.remove_button_text), ReadFormButton('i')],
		        [ReadFormButton('+'), ReadFormButton('-'), ReadFormButton('/'), ReadFormButton('*')],
                [ReadFormButton('6'), ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9')],
                [ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('4'), ReadFormButton('5')],
                [ReadFormButton('0'), ReadFormButton('.'), ReadFormButton('1'), ReadFormButton(constants.calculate_button_text)]]
    
    return layout


def create_calc_form():
    
    theme('GreenMono')
    
    form = FlexForm(constants.app_name,
                    default_button_element_size = (5, 2),
				    auto_size_buttons = False,
                    grab_anywhere = False)
    
    form.Layout(get_layout())
    
    return form


def update_form_data(form, data):
    form.FindElement('input').Update(data)