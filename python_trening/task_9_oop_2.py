class Page:
    def __init__(self,url):
        self.url = url

    #реализуем метод get(), который выводит на печать url
    def get(self):
        print(self.url)

#создаем объект home
home = Page('http://home.com')

#вызываем метод у объекта
home.get()