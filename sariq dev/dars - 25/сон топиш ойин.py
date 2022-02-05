import random

a = int(input('Я загадал число попробуйте отгадать его: '))
count = 0
b = random.randint(1,10)
while True:
    if a == b:
        print('вы угадали число')
        count += 1
        break
    if a > b:
        print('Загаданное число меньше этого')
        c = int(input('try again: '))
        count += 1
        if a < b:
            print('Загаданное число больше этого')
            c = int(input('try again: '))
            count += 1
print('поздравляю')
print('число попыток =', count)