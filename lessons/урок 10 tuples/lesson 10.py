#tuple  -  кортеж = упорядоченное но неизменяемое коллеция произвольных данных

# lst = [1, 4, 5, 6, 2, 3]
# print(sorted(lst))  # упорядоченность списка

# import sys
#
# lst = [ i for i in range(10_000)] # список весит больше кортеж
# tp = (i for i in range(10_000)) # кортеж весит меньше чем список
#
# print(sys.getsizeof(lst))
# print(sys.getsizeof(tp))

# print(list(lst))
# print(tuple(tp))
# print(dir(list))
# print(dir(tuple))



# 1
tuple1 = ()
tuple2 = tuple()
tuple3 = "a",
tuple4 = ("a",)
tuple5 = 'a', 'b', 'c'
str1 = " I'm a Batman "
tuple6 = ('a', 'b', 'c')
tuple7 = ('a',)
list1 = [1,2,3,4,5]
tuple8 = tuple(list1)


#2
tuple9 = ("abc", 1, 4.56, [1,2,3], True)
print(tuple9)
tuple9[3].extend(list1)
print(tuple9)

str1, int1, float1, lst2, bool1 = tuple9
print(f"{str1=}, {int1=}, {float1=}, {lst2=}, {bool1=}")

user = ("3456", "Jasko", "15")
user_id, nickname, age = user
print(f"{user_id=}, {nickname=}, {age=}")

user = user * 1 # повтор кортежа
print(user)

new_user = user + ("Warrior",) # прибавить можно только кортеж!
print(new_user)

new_user = new_user[:2] + ("GUN",) + new_user[2:]
print(new_user)
str1 = ' '.join(new_user)
print(str1)

str2 = ''
for i in range(len(tuple9)):
    str2 += ' ' + str(tuple9[i])

print(str2)

lst2 = list(str1.split('a'))
tuple10 = tuple(str1.split())
print(tuple10)
print(lst2)

print(tuple10[::-1])
print(tuple10.index("3456"))
print(tuple10.count("Warrior"))

player_id = tuple10[tuple10.index("3456")]
print(type(player_id))
print(player_id)

lst3 = list(tuple6[::-1])
lst4 = list(zip(list1, lst3))
lst5 = tuple(zip(list1, lst3))
lst6 = dict(zip(list1, lst3))
tuple11 = []
print(lst4)
print(lst5)
print(lst6)
# zip функция

lst7 = sorted(lst4, key=lambda x: x[1])
print(lst7)


#домашнее задание

#world of tanks

#id = int(random)
#type = list1[random]+list2[random]
#gun = list4[random]+list5[random]
#country = str(list3[random])
#members = int(list6[random])
#horses_force = int(list7[ranpm])







