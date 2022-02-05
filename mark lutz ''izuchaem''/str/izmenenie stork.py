# line = "i’mSPAMaSPAMlumberjack"
# k = line.split("SPAM")  # split i join v deystvii
# print(k)
# j = ' '.join(k)
# print(j)
#
# # podstanovka slov
# o = 'that is %d %s bird' % (2, 'ilhom')
# print(o)
#
# # %d %s i nezabivaem % mejdu strokoy i zamenoy
# # %s - str
# # %d - int
# # %g - float
# n = 'N1'
# g = 'taxtapul eshilari %s ' % n
# print(g)
#
# m = '%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'}
# print(m)
#
#
# reply = '''
# Greetings...
# Hello %(name)s!
# Your age is %(age) s'''
#
# values = { 'name' : 'Bob' , 'age' : 40} # Создание значений для подстановки
# print(reply % values)
#
# food = 'burger'
# qty = 10
# print(vars())
#
#
# h = '%(qty)d more %(food)s' % vars()
# print(h)
#
#
# K = 'Please give me %(qty)d %(food)s' % vars()
# print(K)
#
# #obrashay vnimanie na kovichki i zapyatie))
#
# template = '%s, %s and %s'
# print(template % ('hamburger', 'cheeseburger', 'donar' ))
#
#
#
# print('{motto}, {0}, {food}'.format(42, motto = 3.14, food = [1,2,3]))
#
# somelist = list('spam')
# print(somelist)
# L = 'first = {0[0]}, third = {0[2]}'.format(somelist)
# print(L)


print('{0:10} = {1:10}'.format('spam' , 123.4567))

import sys
k = 'Му {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'})
print(k)

data = dict(platform=sys.platform, kind='laptop')
print(data)

s = '{:,d} {:,d}'.format(9999999, 8888888)
print(s)


g ='{0:b}'.format((2 ** 16) - 1)
print(g)
'''
Числа (целые, с плавающей тачкой, десятичные, дроби, остальные)
 ------->      Поддерживают сложение, умножение и т.д.

Последовательности (строки, списки, кортежи)
 ------->      Поддерживают индексацию, нарезание, конкатенацию и т.д.
 
Отображения (словари)
 ------->      Поддерживают индексацию по ключу и т.д.'''


'''
Неизменяемые типы (числа, строки, кортежи, фиксированные множества)
Изменяемые типы (списки, словари, множества, байтовые массивы)
'''











































































