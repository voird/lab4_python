import re
import numpy as np


filename = "D:/лабораторные работы по питону/4/polynomial.txt"
a, b = 0, 10  # Задаем нужный отрезок [a, b]
degree, coefficients = read_polynomial(filename)
write_table_values(filename, a, b, degree, coefficients)
