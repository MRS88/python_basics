'''Дан список чисел. Выведите все элементы списка,
которые больше предыдущего элемента.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке'''

lst = list(map(int, input().split()))
print(*[lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]])
