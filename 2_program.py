import re
import numpy as np

def read_polynomial(filename):
    with open(filename, 'r') as file:
        polynomial_str = file.readline().strip()

    matches = re.findall(r'(-?\d*)\s*\*?\s*x\^(\d+)', polynomial_str)

    coefficients = [int(match[0]) if match[0] else 1 for match in matches]
    degree = max(int(match[1]) for match in matches)

    return degree, coefficients

def write_table_values(filename, a, b, degree, coefficients):
    with open(filename, 'a') as file:
        file.write(f"Полином: {' + '.join([f'{coeff} * x^{exp}' for exp, coeff in enumerate(coefficients)])}\n")
        file.write(f"Степень: {degree}\n")
        file.write("x\t\tf(x)\n")

        for x in np.arange(a, b + 1, 1):
            f_x = sum(coeff * (x ** exp) for exp, coeff in enumerate(coefficients))
            file.write(f"{x}\t\t{f_x}\n")

filename = "D:/лабораторные работы по питону/4/polynomial.txt"
a, b = 0, 10
degree, coefficients = read_polynomial(filename)
write_table_values(filename, a, b, degree, coefficients)
