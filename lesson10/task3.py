"""
Завдання 3 (оновлене):

Напишіть програму, яка обчислює суму всіх чисел від 1 до n за допомогою рекурсії.

Ваше завдання:

    Створіть функцію sum_numbers(n), яка обчислює суму всіх чисел від 1 до n за допомогою рекурсії.
    Тобто так щоб усередині функції викликався сама функція.
    Запитайте у користувача число n.
    Виведіть отриману суму.

Приклад роботи програми:

Введіть число: 5
Сума чисел від 1 до 5 дорівнює 15.

(Оскільки 1 + 2 + 3 + 4 + 5 = 15)
"""


number = int(input("ведить ціле число: "))
def sum_numbers(n):
    if n == 1:
        return 1
    else: return n + sum_numbers(n-1)

print(sum_numbers(number))
