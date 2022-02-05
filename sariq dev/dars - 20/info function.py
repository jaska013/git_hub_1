# def avto_info(company, model, color, transmission, year, price=None):
#     avto = {'company':company,
#             'model':model,
#             'color':color,
#             'transmission':transmission,
#             'year':year,
#             'price':price}
#     return print(avto)
#
# avto1 = avto_info('GM','Malibu','avto','black',2022,32000)
# avto2 = avto_info('GM','Gentra','avto','white',2022,23000)
# avto3 = avto_info('GM','Cobalt','mechanic','gray',2022,18000)
# avtolar = [avto1, avto2, avto3]
#
# print('Online store: ')
# for avto in avtolar:
#     if avto == 'price':
#         price = avto['price']
#     else:
#         price = 'not in sale'
#     print(f"{avto['color']} {avto['model']} {avto['transmission']}")


'''range functsiyasini ozimmi varinatm'''
def oraliq(min,max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar
oraliq(0,5)

# def oraliq1(max):
#     sonlar = []
#     while max <= 0:
#         sonlar.append(max)
#         max -= 1
#     return print(sorted(sonlar,reverse=True))
# oraliq1(15)

# a = []
# for i in range(5):
#     a.append(i)
#     a = sorted(a,reverse=False)
# print(a)