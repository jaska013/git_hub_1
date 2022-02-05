# set = множества

num_set = [1,2,3,4,5,6]
print(num_set)

num_set = set([1,2,3,4,5,6,6,5,4,3,2])
print(num_set)

# set = set()
# print(type(set))

# чтобы получить доступ к эл-там множества нужно прибегнуть к циклу
# month = ['jan', 'feb', 'march', 'ap', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']
# a = []
# for i in month:
#     print(i)
#     if 'jan' in month:
#         a.append(i)
#         print(a)


# функция .add

month = set(['jan', 'feb', 'march', 'ap', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec'])
month.add('sosika')
print(month)

# удаление эл-та  .discard - .remove - .pop()
a = {1,2,3,4,5,6}
a.remove(3)
a.discard(7)
a.pop()
print(a)

# объединение = .union - |

a = {1,2,3,4,5}
b= {"a","b","c","d","e"}
c = a.union(b)
print(c)

d = {1,2,3,4}
g = {1,6,7,8}
h = d | g
print(h)


# пересечение множеств

x = {1,2,3}
y = {3,4,5}
print(x.intersection(y))
print(x & y)

print(x - y)
print(y - x)
c = x.copy()
print(c)


p = {1,2,3,4}
o = {3,4,5}
print(p.isdisjoint(o))


a = [1,2,3,4,1,1,2,3,0,]

b = set(a)
print("len(a)=", len(a), "len(b)=", len(b))


dic = {'criro':7, 'leo':10, 'ney':11, 'kross':8}



























