'''Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''


input_lst, my_lst = list(map(int, input().split())), []
if len(input_lst) % 2 == 1:
    for i in range(1, len(input_lst), 2):
        my_lst.append(input_lst[i])
        my_lst.append(input_lst[i-1])
    my_lst.append(input_lst.pop())
else:
    for i in range(1, len(input_lst) + 1, 2):
        my_lst.append(input_lst[i])
        my_lst.append(input_lst[i-1])
print(*my_lst)
