'''Дано несколько чисел. Подсчитайте, сколько из них равны нулю,
и выведите это количество.

Формат ввода
Cначала вводится число N, затем вводится ровно N целых чисел.'''

zeros = 0
for i in range(int(input())):
    if int(input()) == 0:
        zeros += 1
print(zeros)
