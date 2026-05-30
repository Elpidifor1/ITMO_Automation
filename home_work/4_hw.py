# Задача №1
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width + self.height)

rectangle_1 = Rectangle(3,2)
rectangle_2 = Rectangle(7, 6)
rectangle_3 = Rectangle(10, 1)


print("Площадь 1 прямоугольника - ", rectangle_1.area(), "Периметр 1 прямоугольника - ", rectangle_1.perimeter())
print("Площадь 1 прямоугольника - ", rectangle_2.area(), "Периметр 1 прямоугольника - ", rectangle_2.perimeter())
print("Площадь 1 прямоугольника - ", rectangle_3.area(), "Периметр 1 прямоугольника - ", rectangle_3.perimeter())

# Задача №2
class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a+self.b

    def multiplication(self):
        return self.a*self.b

    def subtraction(self):
        return self.a-self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "На ноль делить нельзя!"

num1 = Math(1,-8.6)
num2 = Math(2,0)
num3 = Math(-13895,879)

print("Результаты математических действий для первого набора чисел: сложение", num1.addition(), "умножение:", num1.multiplication(), "вычитание:", num1.subtraction(), "деление:", num1.division())
print("Результаты математических действий для второго набора чисел: сложение", num2.addition(), "умножение:", num2.multiplication(), "вычитание:", num2.subtraction(), "деление:", num2.division())
print("Результаты математических действий для третьего набора чисел: сложение", num3.addition(), "умножение:", num3.multiplication(), "вычитание:", num3.subtraction(), "деление:", num3.division())

#Задача №3
class Elements:
    def __init__(self,text,type = "Кнопка", loc = ""):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f"Клик по кнопке {self.text}")

text_box = Elements("Text Box")
check_box = Elements("Check Box")
radio_button = Elements("Radio Button")
web_tables = Elements("Web Tables")
buttons = Elements("Buttons")
links = Elements("Links")
broken_links = Elements("Broken Links - Images")
upload_download = Elements("Upload and Download")
dynamic_properties = Elements("Dynamic Properties")

print(text_box.text)
print(check_box.text)
print(radio_button.text)
print(web_tables.text)
print(buttons.text)
print(links.text)
print(broken_links.text)
print(upload_download.text)
print(dynamic_properties.text)

text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
broken_links.click()
upload_download.click()
dynamic_properties.click()
