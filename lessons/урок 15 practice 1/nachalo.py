table = {1975: 'Holy Grail' , # Ключ: Значение
         1979: 'Life of Brian',
         1983: 'The Meaning of Life'}
# year = 1983
# movie = table[year]
# print(movie)

for year in table:
    print(str(year) +'\t' + str(table[year]))

'''
creating a dictionary

konkatenaciya ne rabotaet

'''
k = dict.fromkeys('ab',0)
d = dict.fromkeys('cd',1)
print(k)
print(d)