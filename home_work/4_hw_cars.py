# Задача №4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен.")

    def stop(self):
        print("Автомобиль заглушен.")

    def set_year(self,new_year):#здесь мы добавляем новый атрибут, поэтому указываем после self
        self.year = new_year #старый атрибут становится новым атрибутом

    def set_type(self,new_type):
        self.type = new_type

    def set_color(self, new_color):
        self.color = new_color

car1 = Car("white","opel",2025)
car2 = Car("red","getz",2008)
car3 = Car("grey","lacetti",2016)

car1.start()
car2.stop()
car3.set_year(2026) #а здесь я вызываю функцию со значением нового атрибута
print(car3.year)
car2.set_type("i20")
print(car2.type)
car1.set_color("blue")
print(car1.color)

