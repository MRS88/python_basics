'''Дан список чисел. Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов одного знака нет -
не выводите ничего. Если таких пар соседей несколько - выведите первую пару.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''

lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i] / lst[i - 1] > 0:
        print(lst[i-1], lst[i])
        break