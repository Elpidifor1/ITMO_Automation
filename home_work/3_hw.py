# Задача №2
def two_numbers(a,b):
    if a > b:
        print("Наибольшее число -", a)
    elif a==b:
        print('Введены одинаковые числа')
    else:
        print("Наибольшее число -", b)

two_numbers(15, -18989)

# Задача №3
def two_numbers_difference(a,b):
    if a - b == 135 or b - a == 135:
        print("Yes")
    else:
        print("No")

two_numbers_difference(135,  0)

# Задача №4
def months_seasons(x:int):
    if x == 1 or x == 2 or x == 12:
        print("зима")
    elif x in range (3, 6):
        print("весна")
    elif x in range (6, 9):
        print("лето")
    elif 9 <= x <= 11:
        print("осень")
    else:
        print("Вы ввели неверное значение, месяца с таким номером не существует.")

months_seasons(9)

# Задача №5
def three_numbers(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")

three_numbers(10.1, 20, 30)

# Задача №6
def positive_sum(numbers_list):
    result = 0
    for elem in numbers_list:
        if elem > 0:
            result = result + 1
        else:
            result = result
    return result

print(positive_sum(numbers_list = [1,2,-3,4,-5]))

# Задача №7
def days(months:int,years:int):
    if months <= 0 or years <= 0:
        print("Введите положительные значения")
    else:
        print((months + 12 * years) * 29)

days(1, 3)
