'''
Дано целое число, не меньшее 2. 
Выведите его наименьший натуральный делитель, отличный от 1.

Формат ввода
Вводится целое положительное число.
'''
n = int(input())
count = 2
while count <= n:
    if n % count == 0:
        print(count)
        break
    count += 1