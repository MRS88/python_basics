'''
Определите сумму всех элементов последовательности, завершающейся числом 0.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит,
а служит как признак ее окончания).
'''
n = int(input())
res = 0
lst = []
while n != 0:
    lst.append(n)
    n = int(input())
print(sum(lst))
