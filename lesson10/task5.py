"""
Завдання 5 (Вкладені функції - створення математичної операції)

Напишіть програму, яка створює функцію для виконання математичної операції за допомогою вкладених функцій.

Ваше завдання:

    Створіть функцію make_multiplier(factor), яка приймає один аргумент factor і повертає іншу функцію.
    Вкладена функція повинна приймати число x і повертати його добуток на factor.
    Використовуючи make_multiplier, створіть дві функції:
        double = make_multiplier(2) (подвоєння числа)
        triple = make_multiplier(3) (потроєння числа)
    Запитайте у користувача число n і виведіть:
        n помножене на 2 (через double(n))
        n помножене на 3 (через triple(n))

make_multiplier(factor):
    multiplier(x)
    return x * factor
    return lambda x: x * factor

Приклад роботи програми:

Введіть число: 5
Подвоєне значення: 10
Потроєне значення: 15
"""
def make_multiplier(factor):
    def multiplier(y):
        return y * factor
    return multiplier

y = 5
double = make_multiplier(2)
triple = make_multiplier(3)

print("Подвоєне", double(y))
print("Потроєне", triple(y))