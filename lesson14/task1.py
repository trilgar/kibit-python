"""
Завдання 1:

Напишіть програму, яка створює словник з інформацією про улюблених тварин ваших друзів.

Ваше завдання:

    Запитайте у користувача імена трьох друзів.
    Для кожного друга запитайте улюблену тварину.
    Створіть словник, де ключем буде ім'я друга, а значенням — назва тварини.
    Виведіть створений словник на екран.

    "Oleg" -> "Cat"
    "Anna" -> "Leopard"

    pet_dictionary = {key: value, key2: value2, ke}
    print()

    first_friend = input("Введіть імʼя першого друга: ")

    print(pet_dictionary["Mike"])
"""

first_name = input("ведіть імья першого друга: ")
first_pet = input("ведить назву першої тваринки: ")

second_name = input("ведіть імья другого друга: ")
second_pet = input("ведить назву другой тваринки: ")

third_name = input("ведіть імья третього друга: ")
third_pet = input("ведить назву третьої тваринки: ")

pet_dictionary = {first_name: first_pet, second_name: second_pet, third_name: third_name}
print(pet_dictionary)

print(pet_dictionary["Hans"])

