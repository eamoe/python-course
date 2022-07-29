from email.policy import default
from statistics import mode


def calculate(data, mode_key = 0):
    match mode_key:
        case 0:
            return calc_real_numbers(data)
        case 1:
            return "Rational"
        case 2:
            return "Imaginary"
        case default:
            return "No mode"

def calc_real_numbers(data):
    result = eval(data)
    result = str(round(float(result), 3))
    return result