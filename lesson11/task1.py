"""
Завдання 1: Робота зі списком

    Створіть список чисел від 1 до 10 за допомогою функції list().
    Отримайте третій елемент списку.
    Замініть значення п’ятого елемента списку на 99.
    Виведіть довжину списку за допомогою функції len().
    Виведіть увесь список після змін.

Очікуваний результат:

    Створений список має виглядати так: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Третій елемент: 3
    Після зміни п’ятого елемента: [1, 2, 3, 4, 99, 6, 7, 8, 9, 10]
    Довжина списку: 10

strings = ["Hello", "World", "Maxim", 1, 10.4, True]
5th_element = strings[4]
print(strings[4])
strings[4] = -500
range(start, stop, step)
strings[]

strings.append("Hello")
strings.remove("Maxim")
"""



num_list = list(range(1, 11, 1))
print(num_list)

third_element = num_list[2]
print(third_element)

num_list[4] = 99
print(num_list)

print(len(num_list))

num_list.append(15)
print(num_list)

num_list.remove(99)
print(num_list)