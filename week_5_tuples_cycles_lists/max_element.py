'''Дан список чисел. Выведите значение наибольшего элемента в списке,
а затем индекс этого элемента в списке. Если наибольших элементов несколько,
выведите их значение и индекс первого из них.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.'''

lst = list(map(int, input().split()))
print(max(lst), lst.index(max(lst)))