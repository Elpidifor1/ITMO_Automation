a: int = 5
b:str='строка'
c:list=[1,2]

def indent(s:str,width:int)->str:
    return " "*(max(0,width-len(s)))+s
#max - возвращает максимальное изначение из диапазона от 0 до width минус длина s

print(indent('123',123))
# т е сначала 120 (самое большое от нуля до 123 (123) минус длина s (3)) пробелов, а потом строка s (123)

s:str

def string_lenth(s:str='')->int:
    return len(s)

print(string_lenth('3'))

a:list = [1,2,3]
b:list=['ля','kz']

def long_list(a:list,b:list)->int:
    return max(len(a),len(b))

print(long_list(a,b))

list1:list = ['реки',"моря"]
z:str = 'озёра'

def add_list(list1:list,z:str)->list:
    list1.append(z)
    return list1

print(add_list(list1,z))

items2:list = 1,2,3,4

def sum_list(items2:list)->int:
    A=0
    for elem in items2:
        A=A+elem
    return A

print(sum_list(items2))

