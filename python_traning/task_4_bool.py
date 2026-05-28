print(10>9) #True
print(10==9) #False
print(10<9) #False

#можно переменным присваивать значения типа bool
#тем самым использовать перемнные как средство управления (переключатель действия)

a=True
if a: #здесь можно было бы написать "если а = тру", но опускают
    print('a=True')
else:
    print('a != True')

a=False
if a:
    print('a=True')
else:
    print('a != True')