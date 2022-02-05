'''
это всё для открытия и чтения файлов, открытие и закрытие
'''

# f = open("C:\\Users\\User\\PycharmProjects\\Prob\\alfavit.txt", 'r', encoding='utf-8')
# print(*f)


# f = open("C:\\Users\\User\\PycharmProjects\\Prob\\codewars\\cars.csv", 'r', encoding='utf-8')
# try:
#     print(*f)
# finally:
#     f.close()


# with open('C:\\Users\\User\\PycharmProjects\\Prob\\codewars\\cars.csv', 'r') as f:
#     print(*f)
#     f.closed


''' 
чтение файлов
'''
# with open('C:\\Users\\User\\PycharmProjects\\Prob\\codewars\\cars.csv', 'r', encoding='utf-8') as rfile:
#     var = rfile.read()
# print(var)


'''
чтение линий файлов:
 ---->  если пишем 'readline' то будет отображаться лишь первая строка файла,
 ---->  если пишем 'readlines', то будут отображаться все строки 
'''


# with open('C:\\Users\\User\\PycharmProjects\\Prob\\codewars\\cars.csv', 'r', encoding='utf-8') as rfile:
#     var = rfile.readlines()
# print(var)


# with open('C:\\Users\\User\\PycharmProjects\\Prob\\codewars\\cars.csv', 'r', encoding='utf-8') as rfile:
#     for line in rfile:
#         print(line)

''' 
для написания в файле новой информации:
 ----> используется "write" , "w" for writing new data into clearead file
 ----> используется "append", "a" for adding data into file
'''

# with open("bla_bla_1", "a", encoding="utf-8") as wfile:
#     wfile.write("print('hello ilhom')\n")

''' 
если такого файла нет кроме режима чтения, в остальных случаях будет создан новый файл
'''
# with open("bla_bla", "a", encoding="utf-8") as wfile:
#     wfile.write("print('hello ilhom')\n")






































































































































