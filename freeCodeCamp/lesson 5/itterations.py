# largest_so_far = -1
# print('before', largest_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print('after', largest_so_far)



# smallest_so_far = 1000
# for the_num_1 in [9,41,12,3,74,15]:
#     if the_num_1 < smallest_so_far:
#         smallest_so_far = the_num_1
# print(smallest_so_far)

# smallest = None
# for i in sorted([9,41,12,3,74,15]):
#     if smallest is None:
#         smallest = i
#     elif i < smallest:
#         smallest = i
# print(smallest)





# zork = 0
# for i in [9,12,41,3,74,12]:
#     zork  += i
#     print (zork)



# for value in [9,12,41,3,74,12]:
#     if value > 30:
#         print('large number', value)


count = 0
summary = 0.0
while True:
    a = input('enter a number:')
    if a == 'done':
        break
    try:
        a1 = float(a)
    except:
        print('try again')
        continue
    count += 1
    summary += a1
print('count =>', count, 'summary =>', summary)

