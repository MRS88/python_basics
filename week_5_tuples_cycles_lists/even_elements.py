'''Выведите все четные элементы списка.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''

for even in input().split(' '):
    if int(even) % 2 == 0:
        print(even, end=' ')