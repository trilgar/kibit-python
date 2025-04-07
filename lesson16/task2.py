"""
🧩 Завдання 2: Збереження числа

Напишіть програму, яка дозволяє зберегти і показати число у полі екземпляра.

Ваше завдання:

    Створити клас NumberHolder з двома методами:

        set_number(self, n) — зберігає число у полі number.

        show_number(self) — виводить збережене число.

    Створити екземпляр класу.

    Запитати у користувача число.

    Використати метод set_number для збереження числа.

    Викликати метод show_number для виводу числа.
"""

class NumberHolder:
    def __init__(self, n):
        self.n = n

    def show_number(self):
        print(self.n)

abc = NumberHolder(4)
abc1 = NumberHolder(5)
abc.show_number()
abc1.show_number()