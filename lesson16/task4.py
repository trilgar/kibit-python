"""
🧩 Завдання: Клуб за інтересами

У клубі є загальний девіз, але кожен учасник може мати особистий псевдонім.

Ваше завдання:

    Створити клас ClubMember, у якому:

        Є поле класу motto = "Знання — сила!".

        У конструкторі створюється поле екземпляра nickname, яке передається як аргумент.

    Створити 2 учасники: anna = ClubMember("Анна"), ivan = ClubMember("Іван").

    Вивести девіз клубу через обох учасників.

    Змінити девіз через ClubMember.motto → "Питання — шлях до істини.".

    Змінити девіз тільки для Івана через ivan.motto = "Я знаю все!".

    Вивести девіз через Анну та Івана ще раз.

    Видалити ivan.motto і знову вивести обидва девізи.

    class NameOfCLass:
        name  =

        def __init__():
            self.name = "

    obj = NameOfClass("Kittens are cool")
    obj = NameOfClass()

"""
class ClubMember:
    motto = "Знання — сила!"

    def sharemotto(self):
        print(self.motto)

obj = ClubMember()
obj.motto = "мова сила"
obj2 = ClubMember()

obj.sharemotto()
obj2.sharemotto()


ClubMember.motto = "Kittens are cool"
obj.sharemotto()
obj2.sharemotto()
