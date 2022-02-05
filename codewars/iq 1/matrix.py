# stolbik = 3
# element_vnutri = 4
# a = [[0] * element_vnutri for i in range(stolbik)]
# print(a)



# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# print('a =',a) # vsya matrica v odnu stroku
# print('a[1] =',a[1]) # 2-ya stroka polnostyu
# print('a[1][2] =',a[1][2]) # 2-ya stroka 3-iy element
# print('a[0][-1] =',a[0][-1]) # posledniy element 1-oy stroki
#
# stolbik = []
# for row in a:
#     stolbik.append(row[2])
#
# print('3-iy stolbik =',stolbik)
#
#
# b = [1,2,3], [4,5,6], [7,8,9]
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         print(b[i][j], end=' ')
#     print()


# stolbik = 3
# elements_in = 2
# matrica = [[0] * elements_in for i in range(stolbik)]
# for i in range(stolbik):
#     for j in range(elements_in):
#         matrica[i][j] = 2
#
# print(matrica)

# import random
# n = int(input('enter numbers: '))
# m = int(input('enter numbers: '))
# matrix = [[0] * m for i in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0,100)
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()

