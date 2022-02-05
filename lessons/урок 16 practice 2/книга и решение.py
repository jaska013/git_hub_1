# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c+=1

# n = int(input())
# stars = "*"
# while len(stars) <= n:
#     print(stars)
#     stars += '*'


# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#
#     # reshenie
#
#         i < 5     i % 2 == 0      i > 2
#
# i = 0    *        **
#
# i = 1    *
#
# i = 2    *        **
#
# i = 3    *                         ***
#
# i = 4    *        **               ***



# x = int(input())
# h = 60
# b = 115
# a = x+b
# k = a//h
# k1 = a%h
#
# print(k)
# print(k1)


# A = int(input())
# B = int(input())
# H = int(input())
# if B > H >= A:
#     print('norm')
# elif H < A < B:
#     print('nedo')
# elif H > B > A:
#     print('pere')

# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
#     print('visokos')
# else:
#     print('obichniy')

# a = int(input())
# b = int(input())
# c = int(input())
# k = (a+b+c)/2
# print(k)

# s = 0
# a = 1
# while a != 0:
#     a = int(input())
#     if a ==0:
#         break
#     s += a
# print(s)

#
# a = int(input())
# b = int(input())
# while a or b / a or b == 0:
#     if a < b:
#         print(a)
#     elif a > b:
#         print(b)


# i = 0
# while i < 5:
#     a,b = input()
#
#     a = int(a)
#     b = int(b)
#     if (a==0) and (b==0):
#         break
#     print(a*b)
#     i +=1


# a = 0
# while a <= 100:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a >=10 and a<=100:
#         print(a)
#     else:
#         break


# for i in 2,3,4,5:
#     print(i*i)

# n = int(input())
# for i in range(n):
#     print('*' * n)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end="")
#     print()

# a = 7
# b = 10
# c = 5
# d = 6
# for i in range(1,10+1):
#     for j in range(1,10+1):
#         print(i*j, end=' ')
#     print()

# summa = 0
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i % 2 == 1:
#         summa += i
# print(summa)

#
# summa = 0
# a = int(input())
# b = int(input())
# if a % 2 ==0:
#     a +=1
# for i in range(a,b+1,2):
#         summa += i
# print(summa)


# sum = 0
# s = []
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if i % 3 ==0:
#         sum += i
#         s.append(i)
# print(sum)
# print(s)
# print(len(s))
# print(sum/len(s))



# genome = 'CCATCTGC'
# count = 0
# for i in genome:
#     if i == 'C':
#         count += 1
# print(count)

# genome = 'CCATCTGC'
# print(genome.count('C'))


# genome = 'ccatctgc'
# i = 1
# k = 6
# print(genome[i])
# print(genome[k])

# s = 'atGGcc'
# p = 'cc'
# print(s.upper())
# print(s.lower())
# print(s.count('G'))
# print(s.count(p))
# print(s.find(p))
# print(s.replace('c','C'))
# print(s)


# k = 'agTtcAGtc'
# print(k.upper().count('gt'.upper()))

# s = 'acggtgttat'
# m = s.upper()
# count = 0
# for i in m:
#     if i == 'G' or i == 'C':
#         count +=1
# k = (count/len(s))*100
# print(k)


# s = 'acggtgttat'
# count = 0
# for i in s:
#     if i == 'c':
#         count +=1
#     elif i == 'g':
#         count +=1
# print((count/len(s))*100)

#abcd efg hijklmnop qrst uvw xy z
# s = 'abcdefghijk'
# print(len(s))
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

# s = input()
# i = 0
# j = len(s)-1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#         break
#     i += 1
#     j -= 1
#     if is_palindrom:
#         print('YES')
#     else:
#         print('No')

# s = input()
# r = s[::-1]
# if s ==r:
#     print('is_palindrom')
# else:
#     print('isn`t_palindrom')
#
# s = 'aaaabbсaa'
# count = 0
# i = 0
# j = len(s)-1
# while i < j:
#     if s[i] == s[j]:
#         count +=1
#
#     else:
#         count += 0

#
# students = ['olga', 'pasha', 'mot', 'anton', 'vanya', 'mariya']
# print(students.index('olga'))
# all_students = sorted(students)
# print(all_students)
#
# st = ['olga', 'pasha', 'mot', 'anton', 'vanya', 'mariya']
# st.sort()
# print(st)
#
# st1 = ['olga', 'pasha', 'mot', 'anton', 'vanya', 'mariya']
# st1.reverse()
# print(st1)
# print(st1[::-1])



# a = [2, 'b', 32]
# b = a
# print(a)
# print(b)
# a[0]= 55
# print(a)
# print(b)
# b[2] = 10
# print(a)
# print(b)


# a = [1, 2, 3]
# b = a
# # значения списка b?
# print(b)
# a[1] = 10
# # значения списка b?
# print(b)
# b[0] = 20
# # значения списка a?
# print(a)
#
# a = [5, 6]
# # значения списка b?
# print(b)


# a = [i*i for i in range(5)]
# print(a)

# s = 'ivan ivanov ivanovich'
# print(s.split())
#
#
#
# b = [4, -1, 9, 3]
# print(b.)


# x = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#         {
#             'x' :10,
#             'y' :20,
#             'z' :30
#         },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]
# print(x[2]["bar"]["z"])




a = [a+b for a in 'list' for b in 'soup']
print(a)









































































































































































































