def task_1() -> None:
    a:int = 3
    b:float = 15.74
    c:str = 'auto'
    d:list = [100, 200, 'cat']
    e:bool = False
    print("Переменная", a, "относится к типу", type(a))
    print("Переменная", b, "относится к типу", type(b))
    print("Переменная", c, "относится к типу", type(c))
    print("Переменная", d, "относится к типу", type(d))
    print("Переменная", e, "относится к типу", type(e))

task_1()

def task_2()->list:
    a:list=[1,2,3,5,8,13,21]
    print(a[0:3])

task_2()
#это числа Фибоначчи

def task_3(x:int) -> int:
    return x**2

print(task_3(8))

