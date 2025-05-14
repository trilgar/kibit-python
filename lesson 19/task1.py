"""
Завдання 1 (робота з умовами та ітерацією):

Створи матрицю розміром 4×4 з випадковими числами від 0 до 1.
Виведи:

    всі елементи, менші за 0.3

    кількість таких елементів

    їх середнє значення

🔧 Підказка: використай A[A < 0.3], а також функції len() і mean().

import numpy as np

np.array([1, 2, 3, 4, 5])
np.zeros(10)
np.random.rand(16)

.reshape(4, 4)

hello = "123"
qwerty[mask]
"""
import numpy as np

qwerty = np.random.rand(16)
print(qwerty)
qwerty = qwerty.reshape(4,4)
print(qwerty)
mask = qwerty < 0.3
print(mask)
filtered = qwerty[mask]
print(filtered)
print(len(filtered))
if len(filtered) > 0:
    print(np.mean(filtered))
