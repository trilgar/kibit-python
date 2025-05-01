"""
🧪 Завдання 1. Декоратор-таймер
🧾 Умова:

Напишіть декоратор @timed, який вимірює час виконання функції й виводить його у мілісекундах.

Потім використайте цей декоратор для прикрасування функції, яка:

    або сортує великий список чисел,

    або виконує якісь обчислення (наприклад, знаходить всі прості числа до 10000).

🔧 Підказка:

    Використовуйте time.time() або time.perf_counter().

    for i in range(n)

    def func(*args, **kwargs):
        hello_world(*args, **kwargs)

    def hello_world(name, surname):
        pass
    def hello(name, surname):
        pass

    func(1,3,4,5,5,6,67,77)
    func(surname = "Zarytskyi", name = "Oleksii")


"""
import time

def timed(f):
    def time_wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        result = f(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Func took time: {end_time-start_time}")
        return result
    return time_wrapped

@timed
def loop(n):
    for i in range(n):
        print(1)


@timed
def count_hello(name, surname):
    for i in range(1000000):
        print("Calculating hello")

    return f"Hello, {name}, {surname}"

loop(1000000)
count_hello("Oleg", "Mongol")