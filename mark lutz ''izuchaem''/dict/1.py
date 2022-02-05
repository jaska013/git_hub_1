# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# print(D['food'])

# bob1 = dict(name = 'bob', job = 'dev', age = 40)
# print(bob1)
#
# bob2 = ['name', 'age', 'job']
# bob3 = ['bob smith', 40, 'dev']
# bob4 = dict(zip(['name', 'age', 'job'],['bob smith', 40, 'dev']))
# print(bob4)
#
# rec = { 'name': { 'first' :  'Bob' , 'last' : 'Smith'},
#         'jobs': ['dev', 'mgr'],
#         'age': 40.5 }
# print(rec)
# print(rec['name']['last'])
#
#
#
# d = {1:'a', 2:'b', 3:'c'}
# d[4] = 'e'
# d[99] = 'ee'
# print(d)
# if not 23 in d:
#     print('missing')


# D = {'а': 1, 'с' : 3, 'b' : 2}
# for key in sorted (D) :
#     print(key, '=>', D[key])


# x = 1
# while x < 7:
#     print('*' * x)
#     x += 1
#
#
# squares = [x ** 2 for x in sorted([1,4,2,5,3,6])]
# print(squares)

# t = (1,2,3,4,5,6,7)
# print(t[0])
# t[2] = 4
# print(t[2])

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
l = list(sorted(D.keys()))
print(len(D))
print(l)