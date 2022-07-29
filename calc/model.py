from email.policy import default

# importing "cmath" for complex number operations
import cmath


def calculate(data, mode_key = 0):
    match mode_key:
        case 0:
            return calc_real_numbers(data)
        case 1:
            return calc_rational_numbers(data)
        case 2:
            return calc_complex_numbers(data)
        case default:
            return "No mode"


def calc_real_numbers(data):
    result = eval(data)
    result = str(round(float(result), 3))
    return result


def calc_rational_numbers(data):
    return 1


def calc_complex_numbers(data):
    
    return 1