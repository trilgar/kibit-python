"""
Завдання 3:

Напишіть програму, яка визначає, чи присутній певний продукт у словнику, що містить список покупок.

Ваше завдання:

    Створити словник із назвами продуктів та їх кількістю.
    Запитати у користувача назву продукту.
    Перевірити, чи є такий продукт у словнику, і вивести відповідне повідомлення.
"""

groceries = {
    "oil": 123,
    "carrots": 456,
    "apple": 59,
    "milk": 45,
    "orbit": 15
}
print(groceries)


name_of_product = input("Enter name of searched product: ")

if name_of_product in groceries:
    print(f"Product found. It's price is {groceries[name_of_product]}")
else:
    print(f"Product not found")


for name, price in groceries.items():
    if name == name_of_product:
        print(f"Product found. It's price is {price}")
        break
else:
    print(f"Product not found")
