'''В списке все элементы попарно различны. Поменяйте местами минимальный и
максимальный элемент этого списка.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.'''


lst = list(map(int, input().split()))
min_lst = lst.index(min(lst))
max_lst = lst.index(max(lst))
lst[min_lst], lst[max_lst] = lst[max_lst], lst[min_lst]
print(*lst)
