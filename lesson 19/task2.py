"""
Завдання 2 (зміна форми та транспонування):

Створи масив з чисел від 0 до 11.
Перетвори його у матрицю 3×4, а потім:

    Перетвори її назад в одновимірний масив

    Змініть форму на 4×3

    Транспонуй отриману матрицю

np.arange()
np.array(range(0 , 11))
Підказка: використай reshape, ravel і transpose.

cat.name = "Felix"
"""

import numpy as np

npa = np.arange(12)
print(npa)

npa = npa.reshape(3, 4)
print(npa)

npa = npa.ravel()
print(npa)

mpa = npa.reshape(4,3)
print(mpa)
print(mpa.shape)

print()
print()
npa.shape = (4,3)
print(npa)
print()

transposed = npa.transpose()
print(transposed)


