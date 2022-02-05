# from random import randint, random
#
# a = randint(0,100)
# print(a)

# from random import randint
# a = [['h', i*2, i**2] for i in range(5)] # hello - kak element range eto kolichestvo etix elementov
# print(a)
# a = [randint(0,100) for i in range(10)]
# print(a)

# from random import randint
# a = [1,2,3,4,5,6,7,8,9]
# print(a)

for i in range(len(a)-1): # agar -1 qoyilsa ohirgi elemet teyilmidi
    print(a[i])
a[-1] = a[-2] + a[0]
print(a[-1])
