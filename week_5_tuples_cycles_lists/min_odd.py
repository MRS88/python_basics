'''Выведите значение наименьшего нечетного элемента списка, гарантируется,
что хотя бы один нечётный элемент в списке есть.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''

lst = list(map(int, input().split()))
print(min(filter(lambda x: x % 2 == 1, lst)))