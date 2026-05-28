#определяем функцию
def add(x,y):
    return x+y #в табе или 4 пробелах

#вызываем функцию
print(add(1,2))

print(add('I a','m a tester.'))

def add2(a,b,c=2,d=3):
    return a+b+c+d

print(add2(1,1,1,1)) #1+1+1+1=4

print(add2(1,1)) #1+1+2+3=7

print(add2(2,2,0.3,4)) #2+2+0.3+4=8.3

print(add2(1,5,6)) #1+5+6+3=15

#print(add2(1,1,'ноль',1)) #а вот тут будет ошибка

def range_arg(a,b,c,d):
    return a+' '+b+' '+c+' '+d

print(range_arg('1','2','3','4'))

print(range_arg('1','2',d='3',c='4'))

print(range_arg('1','2',d='3','4'))

