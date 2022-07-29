from ast import operator
import constants

# Importing "cmath" for complex number operations
import cmath

# Importing fractions for rational number operations
from fractions import Fraction


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
    rational_numbers_list = extract_rational_numbers(data)
    r_1 = initialize_rational_number(rational_numbers_list[0], rational_numbers_list[1])
    r_2 = initialize_rational_number(rational_numbers_list[2], rational_numbers_list[3])
    operation = get_operation(data)
    
    match operation:
        case '/':
            result = r_1 / r_2
        case '*':
            result = r_1 * r_2
        case '-':
            result = r_1 - r_2
        case '+':
            result = r_1 + r_2
        case default:
            pass

    return result


def extract_rational_numbers(data):
    temp = data.replace("/", "|").replace("*", "|").replace("-", "|").replace("+", "|")
    temp_list = temp.split("|")
    return temp_list


def initialize_rational_number(numerator, denominator):
    rational_number = Fraction(int(numerator), int(denominator))
    return rational_number


def get_operation(data):
    temp = str(data).split("/")
    temp = temp[1][1:]
    temp = temp[:-1]
    if temp == '':
        temp = '/'
    return temp


def calc_complex_numbers(data):
    complex_operation_list = extract_complex_numbers(data)
    operation = complex_operation_list[1]
    z_1 = initialize_complex_number(complex_operation_list[0])
    z_2 = initialize_complex_number(complex_operation_list[2])

    match operation:
        case '/':
            result = z_1 / z_2
        case '*':
            result = z_1 * z_2
        case '-':
            result = z_1 - z_2
        case '+':
            result = z_1 + z_2
        case default:
            pass

    real = result.real
    imag = result.imag

    if imag < 0:
        result_str = str(round(real, 3)) + str(round(imag, 3)) + constants.imaginary_unit
    else:
        result_str = str(round(real, 3)) + '+' + str(round(imag, 3)) + constants.imaginary_unit

    return result_str


def extract_complex_numbers(data):
    temp = data.replace("(", "|").replace(")", "|")
    temp = temp[1:]
    temp = temp[:-1]
    temp_list = temp.split("|")
    return temp_list


def initialize_complex_number(complex_number_str):
    
    if complex_number_str.find('+') != -1:
        temp_list = complex_number_str.split('+')
        real = float(temp_list[0])
        imag = float(temp_list[1][:-1])
    elif complex_number_str.find('-') != -1:
        temp_list = complex_number_str.split('-')
        real = float(temp_list[0])
        imag = float(temp_list[1][:-1])*(-1)
        

    

    complex_number = complex(real, imag)

    return complex_number