'''
Программа получает на вход последовательность целых неотрицательных чисел,
каждое число записано в отдельной строке.
Последовательность завершается числом 0,
при считывании которого программа должна закончить свою работу и
вывести количество членов последовательности (не считая завершающего числа 0).
Числа, следующие за числом 0, считывать не нужно.

Формат ввода
Вводится последовательность целых чисел, заканчивающаяся числом 0.
'''
n = int(input())
lst = []
while n != 0:
    lst.append(n)
    n = int(input())
print(len(lst))