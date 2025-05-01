"""
Завдання 2. Декоратор логування викликів
🧾 Умова:

Напишіть декоратор @logged, який буде:

    виводити в консоль назву функції,

    список аргументів, з якими її викликали,

    результат виконання.

Потім використайте цей декоратор для функцій:

    greet(name), яка повертає рядок "Привіт, {name}!"

    multiply(a, b), яка повертає добуток двох чисел.


    func.__name__
"""

def logged(f):
    def qwe(*args, **kwargs):
        print(f"Назва функції: {f.__name__} ")
        print(f"Аргументи з якими її викликали: {args, kwargs}")
        result = f(*args, **kwargs)
        print(result)
        return result
    return qwe

@logged
def loop(n):
    for i in range(n):
        print(1)
@timed
@logged
def count_hello(name, surname):
    for i in range(2):
        print("Calculating hello")

loop(2)
count_hello("Oleg", surname = "Mongol")