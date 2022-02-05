# import random
# num = random.randint(1,10)
# col = random.randint(1,2)
# print(num)
# print(col)
# i = 0
# while i < 5:
#     i += 1
#     guess = int(input('vashe chislo:'))
#     color = int(input('vvedite cvet: 1-krasniy ili 2-chorniy: '))
#     if guess > num:
#         print('chislo menshe tvoego.')
#         if color == col:
#             print('no ti ugadal cvet')
#         else:
#             print('ti ne ugadal cvet')
#     elif guess < num:
#         print('chislo bolshe tvoego.')
#         if color == col:
#             print('no ti ugadal cvet')
#         else:
#             print('ti ne ugadal cvet')
#     elif guess == num and col != color:
#         print('cvet ne ugadan no ugadan nomer')
#     elif guess == num and col == color:
#         print('yuhhhuuuu!',num, col)
#         break
#     if i < 5:
#         print('try again')
#     else:
#         print('eto bilo chislo', num, col, "game over")