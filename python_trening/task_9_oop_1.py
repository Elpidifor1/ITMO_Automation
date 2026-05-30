#создать класс Input, принимающий  аргумент при инициализации (Loc)
class Input:

    def __init__(self, text, Loc):
        self.Loc = Loc
        self.text = text

class Button:

    def __init__(self, text, Loc):
        self.Loc = Loc
        self.text = text


class Title:

    def __init__(self, text, Loc):
        self.Loc = Loc
        self.text = text

class Link:

    def __init__(self, text, Loc):
        self.Loc = Loc
        self.text = text

#создать объект класса search
search = Input('поле поиска', 'Input#search')
loop = Button('кнопка поиска', 'Button#loop')
main_title = Title('большой заголовок', 'Title#main_title')
link1 = Title('ссылка на поисковик', 'Link#link1')


#вывести в консоль значение атрибута Loc объекта search
print(search.text, search.Loc)
print(loop.text,loop.Loc)
print(main_title.text,main_title.Loc)
print(link1.text,link1.Loc)

