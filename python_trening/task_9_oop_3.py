#создание класса с 1 аргументом
class Soda:
    def __init__(self, add):
        self.add = add

#реализация метода
    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}') #f-строка

        else:
            print("Обычная газировка")

#создание 2х объектов
drink1 = Soda(None)
drink2 = Soda('ваниль')

#вызов метода для каждого объекта
drink1.show_my_drink()
drink2.show_my_drink()