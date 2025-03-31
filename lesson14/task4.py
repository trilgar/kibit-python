"""
Завдання 4:

Напишіть програму, яка об'єднує два словники.

Ваше завдання:

    Створити два словники з назвами міст та кількістю їх жителів.
    Об'єднати ці словники в один, використовуючи метод update().
    Вивести кінцевий словник на екран.
"""

cities1 = {
    "Kyiv": 20000000,
    "Zhytomyr": 150000,
    "Lviv": 500000,
    "Uzhgorod": 59000
}

cities2 = dict([["Chornobyl", 0], ["Chernivtsi", 100000], ["Vinnitsia", 600000]])

print(cities1)
print(cities2)

cities1.update(cities2)

print(cities1)

print(f"Population of Kyiv: {cities1['Kyiv']}")

print(f"Population of Chernihiv: {cities1.get('Chernihiv', 'City not found')}")