# Программа проверяет является ли число положительным или отрицательным и выводит соответствующее сообщение.

num = 5

if num >= 0:
    print("Число большо или равно 0.")
else:
    print("Число отрицательно.")

# содержит ли str_2 в себе str_1? Программа отвечает "да" или "нет"

str_1 = 'test2'
str_2 = 'test1'
def task_yes_no(str_1,str_2):
    if str_1 in str_2:
        print("да")
    else:
        print("нет")

task_yes_no(str_1,str_2)


str_1 = 'test2' # это то же самое, что и предыдущая запись, но без оборачиыания в функцию
str_2 = 'test1'
if str_1 in str_2:
        print("да")
else:
        print("нет")


#еще одно доп условие - elif

num_float = -3.4

if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print("ноль")
else:
    print("отрицательное число")


permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print("печать запрещена")



def  student_status(year_of_study:int):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print("Наш студент еще бакалавр")
    elif year_of_study == 5 or year_of_study == 6: # elif year_of_study in range (5, 7):
        print("Наш студент уже магистр")
    elif year_of_study == 7 or year_of_study == 8 or year_of_study == 9: #elif 7 <= year_of_study <= 9:
        print("Наш стундент уже не студент, а целый аспирант")
    else:
        print("Введите корректный год обучения")



student_status(-2)

def hundreds(num):
    if num > 100 or num < -100:
        print("-")
    else:
        print("+")

hundreds(101)

