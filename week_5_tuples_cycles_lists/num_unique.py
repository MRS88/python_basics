'''Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''

print(len(set(list(map(int, input().split())))))