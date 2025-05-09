"""
Завдання 3 (спрощене):

Напишіть програму, яка демонструє роботу з методами обробки списків.

Ваше завдання:

1. Створіть функцію modify_list(lst), яка приймає список чисел і виконує наступні операції:
   - Додає число 0 у кінець списку.
   - Вставляє число 100 на позицію з індексом 2.
   - Видаляє перше входження числа 7 (якщо воно є у списку).
   - Повертає змінений список.

2. Створіть функцію display_info(lst), яка приймає список чисел і виконує наступне:
   - Виводить на екран кількість входжень числа 2 (використовуючи метод *count()*).
   - Виводить на екран список у зворотному порядку (без зміни оригіналу).

3. Перевірте роботу обох функцій, використовуючи наступний тестовий список:
   [4, 2, 7, 2, 5, 7, 3]

Приклад роботи програми:

Початковий список:
    [4, 2, 7, 2, 5, 7, 3]

Після виконання функції modify_list(lst) має повернути:
    [4, 2, 100, 2, 5, 7, 3, 0]
    (спочатку додали 0, потім вставили 100 на позицію 2, а потім видалили перше входження 7)

Вивід функції display_info(lst) має бути таким:
    Кількість входжень числа 2: 2
    Список у зворотному порядку: [0, 3, 7, 5, 2, 100, 2, 4]

    nums.append(0)
    nums.insert(4, 3)
    nums.remove(7)

    nums.count(3)
    nums.reverse()
    reverse(nums)

    reversed_nums = nums[::-1]
"""


lst = [4, 2, 7, 2, 5, 7, 3]

def modify_list(lst):
    lst.append(0)
    lst.insert(2, 100)
    lst.remove(7)
    return lst

print(modify_list(lst))

def display_info(lst):
    c = lst.count(2)
    print("К-сть входжень числа 2: " + str(c))
    print(list(reversed(lst)))
    reversed_nums = lst[::-1]
    print(reversed_nums)

display_info(lst)
print(lst)
