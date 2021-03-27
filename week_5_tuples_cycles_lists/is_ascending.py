'''Дан список. Определите, является ли он монотонно возрастающим
(то есть верно ли, что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.
Решение оформите в виде функции IsAscending(A).В данной функции должен быть
один цикл while, не содержащий вложенных условий и циклов —
используйте схему линейного поиска.'''


def IsAscending(lst):
    count = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            count += 1
        else:
            count -= 1
    return 'YES' if len(lst) - 1 == count else 'NO'


lst = list(map(int, input().split()))
print(IsAscending(lst))
