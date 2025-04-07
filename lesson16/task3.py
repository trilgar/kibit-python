"""
🧩 Завдання: Ігровий персонаж

Створіть клас GameCharacter, який імітує появу та знищення персонажа у грі.

Ваше завдання:

    Реалізуйте клас GameCharacter, у якому:

        Конструктор __init__(self, name, hp=100) виводить: "Гравець [ім’я] з'явився з [hp] HP!".

        Метод take_damage(self, amount) зменшує hp на amount і виводить поточне значення HP.

        Деструктор __del__() виводить: "Гравець [ім’я] вибув з гри...".

    Запитайте у користувача ім’я гравця.

    Створіть об’єкт персонажа.

    Викличте метод take_damage() кілька разів.

    Видаліть об’єкт, щоб побачити деструктор у дії.
"""

class GameCharacter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp = self.hp - amount
        print(f"Гравець отримав урон: {amount}. Нова кількість здоровʼя: {self.hp}")
        if self.hp <= 0:
            self.__del__()

    def __del__(self):
        print(f"Гравець вибув {self.name} з гри")


abc = GameCharacter("Oleg", 100)
abc.take_damage(30)
abc.take_damage(20)
abc.take_damage(300)
