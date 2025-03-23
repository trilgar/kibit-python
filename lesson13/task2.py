"""
Завдання 2

Напишіть програму, яка демонструє операції над множинами.

Ваше завдання:

    Створіть дві множини setA та setB (можна взяти елементи “захардкожені” або ввести їх у коді).
    Виведіть на екран результат таких операцій:
        union (A ∪ B)
        intersection (A ∩ B)
        difference (A - B та B - A)
        symmetric_difference (A △ B)

        set(iterable)

        {8, 2, 9, "Hello"}

        union()
        intersection()
        difference()
        symmetric_difference()

        |
        &
        -
        ^
        result = 1 + 2
        result = A & B
"""

setA = {2, 5, 6}
setB = {3, 5, 9}
print("Set A: ", setA)
print("Set B: ", setB)

union = setA | setB
print("Union: ", union)

print("Intersection: ", setA.intersection(setB))

print("Difference: ", setA.difference(setB))

print("Symmetric difference: ", setA ^ setB)

setA.intersection_update(setB)
print(setA)