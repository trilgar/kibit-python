"""
Завдання 4:

Напишіть програму, яка використовує лямбда-функції.

Ваше завдання:

    Створіть лямбда-функцію square, яка підносить число до квадрату.
    Створіть лямбда-функцію multiply, яка множить два числа.
    Використайте ці функції для обчислення значень та виведіть результати.

Приклад роботи програми:

print(square(5))  # Очікуваний результат: 25
print(multiply(3, 4))  # Очікуваний результат: 12

print_name = lambda name = "Olexii": print("Hello, " + name)
print_name("Oleg")
print_name()
"""
square = lambda x=2: x**2
multiply = lambda x=4, y=1: x * y


print(square(5))
print(multiply(3, 4))
print(square())
print(multiply(y = 3))