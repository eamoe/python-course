#Вычислить число c заданной точностью d
#Например: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import numbers


def get_elements_number(precision):
    n = 0
    while abs(pow(-1, n)/ (2 * n + 1)) > precision / 10:
        n = n + 2
    return n

def leibniz_series(n):
    sum = 0
    for n in range(n):
        sum += pow(-1, n)/ (2 * n + 1)
    return sum


precision = float(input("Введите необходимую точность: "))

n = get_elements_number(precision)
print(4 * leibniz_series(n))