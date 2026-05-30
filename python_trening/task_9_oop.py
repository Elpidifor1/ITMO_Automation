class Button: #class - ключевое слово для создания класса, Button - это его имя
    #начинается тело класса (атрибуты и методы)
    def __init__(self, text, link): #def __init__(self) - конструктор класса-стандартный метод для объявления атрибутов; этот метод-инициализатор, запускается сразу же после создания объекта
        #в скобках - атрибуты, а ниже - уже аргументы
        self.text = text
        self.link = link

#создаем экземпляры класса (как раз объекты)
home = Button('Домой','/home') #home - название объекта из класса Button, у которого 2 атрибута: текст = "Домой" и линк = "/home"
catalog_msk = Button("Каталог", "/msk/catalog")

#Получаем доступ к атрибутам
print(home.text) #имя объект точка название атрибута
print('Кнопка ' + home.text + " имеет ссылку " + home.link)
print("\n")
print('Кнопка ' + catalog_msk.text + " имеет ссылку " + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc): #метод инициализации, в него передаем 3 аргумента
        self.text = text
        self.link = link
        self.loc = loc

    def click(self): #метод клик
        return "Клик по локатору - {}".format(self.loc) #вместо фигурных скобок ставится какое-то значение, поставим сюда аргумент loc

    #создаем экземпляр класса
home_two = ButtonTwo("Домой", "/home", "button#home")

    #вызываем метод
print(home_two.click()) #обращаемся к имени объекта, через точку вызываем его метод