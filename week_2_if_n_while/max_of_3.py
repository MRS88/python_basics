'''
Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).

Формат ввода
Вводится три целых числа.
'''
a, b, c = int(input()), int(input()), int(input())
print(max(max(a, b), max(a, c)))
