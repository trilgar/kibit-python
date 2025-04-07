"""
🧩 Завдання 1: Привітання від об’єкта

Напишіть програму, яка створює клас Greeter з методом say_hello.

Ваше завдання:

    Створити клас Greeter, у якому є метод say_hello, що виводить повідомлення "Привіт, я екземпляр класу!".

    Створити екземпляр класу.

    Викликати метод say_hello з екземпляра.

    class Name_Of_Class:
        def name_of_method(self):
            print("message")

        def name_of_method_2(self):
            print("message")

    name_of_variable = Greeter()

    self.name = value

    def __init__(self, arg1, arg2...)
"""

class Greeter:
    def say_hello(self):
        print(f"Привіт, я екземпляр класу!, моє імʼя - {self.name}")

    def set_greeter(self, name_of_greeter):
        self.name = name_of_greeter

    def __init__(self, name):
        self.name = name


abc = Greeter("Oleg")
abc.say_hello()

