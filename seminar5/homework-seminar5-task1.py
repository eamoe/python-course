# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.

def get_polynomial(path):
    file = open(path, 'r')
    polynomial = file.readline()
    file.close()
    return polynomial


def get_polynomial_elements(polynomial_str):
    elements = str(polynomial_str).split(" + ")
    return elements


def create_degree_coeff_dictionary(elements):
    coeff_degree_dict = {}
    for element in elements:
        coeff = element.split("*")[0]
        if (len(element.split("x^")) > 1):
            degree = element.split("x^")[1]
        else:
            if element.find("x") == -1:
                degree = 0
            else:
                degree = 1
    
        if int(degree) in coeff_degree_dict:
            coeff_degree_dict[int(degree)] += int(coeff)
        else:
            coeff_degree_dict[int(degree)] = int(coeff)
    return coeff_degree_dict


def sum_polynomials(polynomial_1, polynomial_2):
    degrees_set = set()
    sum_polynomial = {}
    
    for key in polynomial_1.keys():
        degrees_set.add(key)
    
    for key in polynomial_2.keys():
        degrees_set.add(key)
    
    for element in degrees_set:
        value_1 = 0
        value_2 = 0
        if element in polynomial_1:
            value_1 = polynomial_1[element]
        if element in polynomial_2:
            value_2 = polynomial_2[element]
        sum_polynomial[element] = value_1 + value_2

    return sum_polynomial
    

def form_polynomial_srt(polynomial_dict):
    elements_list = []

    for key, value in polynomial_dict.items():
        if key == 0:
         elements_list.append(f"{value}")
        elif key == 1:
            elements_list.append(f"{value}*x")
        else:
            elements_list.append(f"{value}*x^{key}")

    elements_list.reverse()

    polynomial_str = ""
    i = 0
    for element in elements_list:
        if i == len(elements_list) -1:
            polynomial_str += f"{element}"
        else:
            polynomial_str += f"{element}" + " + "
        i += 1
    return polynomial_str


#Main program
polynomial_1 = get_polynomial('polynomial_1.txt')
polynomial_2 = get_polynomial('polynomial_2.txt')

degree_coeff_dict_1 = create_degree_coeff_dictionary(get_polynomial_elements(polynomial_1))
degree_coeff_dict_2 = create_degree_coeff_dictionary(get_polynomial_elements(polynomial_2))

print(f"Первый многочлен: {polynomial_1}")
print(f"Второй многочлен: {polynomial_2}")

sum_polynomial = form_polynomial_srt(sum_polynomials(degree_coeff_dict_1, degree_coeff_dict_2))
print(f"Сумма многочленов: {sum_polynomial}")

sum_file_path = 'sum_polynomial.txt'
with open(sum_file_path, 'w') as data:
    data.write(sum_polynomial)

print(f"Результат записан в файл: {sum_file_path}")