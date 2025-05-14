"""
Завдання 3 (розбиття масивів):

Створи матрицю 4×4 зі значеннями від 0 до 15.

    Розділи її по вертикалі на дві частини

    Розділи її по горизонталі на дві частини

    Розділи її по стовпцях на три частини:

        перша містить 1 стовпець

        друга — 1 стовпець

        третя — 2 стовпці

.vsplit(n) .hsplit(n)
Підказка: використай split() з axis=1.
"""

import numpy as np
npa = np.arange(16).reshape(4, 4)
print(npa)

slised = np.split(npa, 2, axis=1)
print(slised)

print("______________", end="\n\n")
npa1, npa2, npa3 = np.split(npa, [1,2], axis=0)
print(npa1)
print(npa2)
print(npa3)

print("______________", end="\n\n")
npa = np.hsplit(npa, [1, 2])
print(npa)


npa = np.arange(36).reshape(6, 6)
print(npa)
slised = np.split(npa, 3, axis=0)
print(slised[0])
print(slised[1])
print(slised[2])
