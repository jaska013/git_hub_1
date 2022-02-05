#sets = множества - полусписок полукортеж

set1 = set()
set2 = {'1', '2', '3', '4', '8', '5'} # eto seti
set3 = {} # это уже dictionary
print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3))

var = ''
for i in set2:
    print(i)
# в set нету упорядоченности, нельяза обращаться через id
if '1' in set2:
    var = '1'

print(f"{var=}")

set2.add(True)
set2.add("string")
print(set2)

#remove item

set2.pop() # тут удаляется 1-ый элемент
print(set2)
# set2.remove(1) # тут указывается "index" , при удалении элемента индекс должен совпадать
# print(set2)

set2.discard('string') # тут удаляется элемент если он имеется, если нет то программа идёт дальше
print(set2)

# intersection - пересечения

set4 = {i for i in range(5,15)}
set5 = {i for i in range(8,20)}
print(set4)
print(set5)
set_inter1 = set4 & set5 # тут показывает точку пересечения двух переменных
print(set_inter1)
set_inter2 = set4.intersection(set5)
print(set_inter2)

#union

set_inter1 = set4 | set5 # Объединение вид 1
print(set_inter1)
set_inter2 = set4.union(set5) #Объединение вид 2
print(set_inter2)

#difference
print(set4)
set_inter1 = set5 - set4
print(set_inter1)
set_inter2 = set4.difference(set5)
print(set_inter2)
print(set5)

#symmetric differnce
set_inter1 = set4 ^ set5
set_inter2 = set4.symmetric_difference(set5)
print(set_inter1)
print(set_inter2)

set6 = {i for i in range(3,10)}
set7 = {i for i in range(1,16)}
print(set6.issubset(set7)) # показывает находится ли искомое множество в другом множестве
print(set7.issuperset(set6)) # показывает включаетли искомое множество в другом множестве


print(dir(set))

#update - добавление множества
# print(set2)
# print(set6)
# set6.update(set2)
# print(set6)

print(set7)
print(set6)
set7.symmetric_difference_update(set6)
print(set7)
set7.update(['ab', 'bc', 'ca'])
set8 = set7.copy()
print(set8)


# set_id = set()
# while True:
#     set_id.add(6)

set9 = frozenset(set7) # эта фунция делает его неизменяемым
print(set9)
print(set9.isdisjoint(set7)) # слияние

print(set8)
set8.clear()
print(set8)

print(dir(dict))