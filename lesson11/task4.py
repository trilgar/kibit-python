"""
Завдання 4:

Напишіть програму, яка демонструє відмінності між присвоюванням, поверхневим копіюванням та глибоким копіюванням списків.

Ваше завдання:

1. Імпортуйте модуль copy (наприклад, `import copy`).

2. Створіть список original, який містить вкладений список, наприклад:
   original = [1, 2, [3, 4], 5]

3. Створіть три нові змінні:
   - assigned = original                # Присвоювання (посилання)
   - shallow_copied = original[:]       # Поверхневе копіювання (зріз)
   - deep_copied = copy.deepcopy(original)  # Глибоке копіювання

4. Змініть значення у вкладеному списку:
   - original[2][0] = 99

5. Виведіть на екран усі чотири списки (original, assigned, shallow_copied, deep_copied),
   щоб побачити, у яких випадках зміна відображається, а в яких – ні.

Приклад роботи програми (можливий варіант виводу):

Початковий список: [1, 2, [3, 4], 5]

Після зміни original[2][0] = 99:
    original:       [1, 2, [99, 4], 5]
    assigned:       [1, 2, [99, 4], 5]
    shallow_copied: [1, 2, [99, 4], 5]
    deep_copied:    [1, 2, [3, 4], 5]

Пояснення:
- assigned посилається на той самий список, що й original, тому зміни відображаються одразу.
- shallow_copied є поверхневою копією, але вкладені списки залишаються спільними.
- deep_copied є глибокою копією, тому внутрішній список було продубльовано, і зміни не відобразились.

list(nums)
nums[:]
nums.copy()

nums[1] = -1200
third_element = nums[3][1][1]  : [1,2,3, [3, [3,4] ]]
third_element[2]

"""
import copy


original = [1, 2, [3, 4, 1, 4],[4, 0, 2], 5]
print("Original before editing:")
print(original)
print()

original[2][2] = -400

assigned = original
shalow_copied = original.copy()
deep_copy = copy.deepcopy(original)

original[0] = 300

print(original)
print(assigned)
print(shalow_copied)
print(deep_copy)