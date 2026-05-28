a=(1,'e',3,4)

def first_element(a): #а можно написать сразу def first_element(a=(1,2,3,4)):
    return a[1]

print(first_element(a))

def circle_area(r,pi=3.14):
    return pi*r**2

print(circle_area(3))
