#tuple = кортеж это те же списки но в круглых скобках , из кортежа можно извлекать эл-ты и брать срезу

a = (1,2,3,4,5,6,5,6,7,8,9)
print(a[0:3])
print(a[:3])
print(a[1:])
print(a[2::2])
print(a[::2])

# изменять его эл-ты нельзя
#a[1] = 11 Error

# tuple нет методов добавления и удаления эл-тов

nested = (1,2,3, ['a','b','c'], 4)
nested[3][1]= "abbos"
nested[3][0]= "avzal"
nested[3][2]="said"
print(nested)

# опреция умножения приводит к тому что кортеж повторяется
a = (1,2,3,4,5)
print(a*2)

# Функции кортежей COUNT LEN
a = (1,2,3,4,5,5,44,4,3,5,7)
print(a.count(5), len(a))

print("max:", max(a)) # показывает самый большой эл-т
print("min:", min(a)) # показывает самый маленький эл-т

import random
a = [random.randint(0,100) for i in range(10)]
b = tuple(a)
print(b)
print('max =',max(b), 'min =',min(b))


import random
a = [random.randint(0,5) for k in range(10)]
b = [random.randint(-5,0) for j in range(10)]
c = a+b
print(c)
print(c.count(0))

a = ('one', 'two', 'three')
c = ','.join(a)
print(c)
























































