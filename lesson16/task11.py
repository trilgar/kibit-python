"""
Практичне завдання: Клас Potion — магічне зілля
💡 Завдання:

Створіть клас Potion, який описує магічне зілля з певною силою (power), що виражається цілим числом.

Перевантажте наступні арифметичні оператори:

    + — злиття двох зіль: створюється нове зілля з сумарною силою.

    - — ослаблення: від сили одного зілля віднімається сила іншого, результат — нове зілля.

    * — посилення: сила зілля множиться на силу іншого.

    str() — повертає рядок на кшталт "Зілля сили: 25"

🔧 Умови:

    Якщо після віднімання сила зілля < 0 — сила вважається рівною 0.

    Усі операції повертають новий об’єкт Potion.

    Додатково перевизначте метод __repr__, щоб зручно виводити об'єкти у консоль.
"""

class Potion:
    def __init__(self, power, name):
        self.power = power
        self.name = name

    def __str__(self):
        return f"Strength of the {self.name} potion is {self.power}"

    def __add__(self, other):
        if not isinstance(other, Potion):
            print("Cannot add other type than Potion")
            return self
        print("Adding two potions")
        name  = self.name + " " + other.name
        power = self.power + other.power
        return Potion(power, name)

    def __sub__(self, other):
        if not isinstance(other, Potion):
            print("Cannot substract other type than Potion")
            return self
        print("Substracting two potions")
        name  = self.name + " " + other.name
        power = self.power - other.power
        if power < 0:
            power = 0
        return Potion(power, name)

    def __mul__(self, other):
        if not isinstance(other, Potion):
            print("Cannot multiply other type than Potion")
            return self
        print("Multiplying two potions")
        name = self.name + " " + other.name
        power = self.power * other.power
        return Potion(power, name)


strength_potion = Potion(10, "Strong")

weakness_potion = Potion(0, "Weakness")

small_strength_potion = Potion(3, "small strength")

print(strength_potion * weakness_potion)