'''
По данному целому числу N распечатайте все квадраты натуральных чисел,
не превосходящие N, в порядке возрастания.

Формат ввода
Вводится натуральное число.
'''
n = int(input())
count = 1
while count <= n:
    if count**(1/2) % 1 == 0:
        print(count, end=' ')
    count += 1