'''
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего
элемента.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит,
а служит как признак ее окончания).
'''
n = int(input())
count = 0
lst = []
while n != 0:
    lst.append(n)
    if len(lst) > 1:
        if lst[-1] > lst[-2]:
            count += 1
    else:
        pass
    n = int(input())
print(count)
