"""
Мета:
Ознайомитися з використанням циклу while у Python для виконання повторюваних дій, включаючи перевірки та обчислення.

Завдання:

Напишіть програму, яка обчислює факторіал числа.
Ваше завдання:

    Запитати у користувача число n (натуральне число).
    Використовуючи цикл while, обчислити факторіал числа n і вивести результат.

    Підказка: Факторіал числа n дорівнює добутку всіх чисел від 1 до n:
    sum = 1
    1* 1 = 1
    sum = 1
    1 * 2 = 2
    sum= 2
    sum * 3 = 2* 3 = 6
    sum = 6

    n! = 1 * 2 * 3 * ... * n

    while
"""

n = int(input("Введіть будь яке натуральне число: "))
print(n)
i = 1
sum = 1

while i <= n:
    sum = sum * i
    i += 1
print("Сума натуральних чисел: " + str(sum))
