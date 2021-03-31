'''Системный администратор вспомнил, что давно не делал архива
пользовательских файлов. Однако, объем диска, куда он может поместить архив,
может быть меньше чем суммарный объем архивируемых файлов.
Известно, какой объем занимают файлы каждого пользователя.
Напишите программу, которая по заданной информации о пользователях и
свободному объему на архивном диске определит максимальное число
пользователей, чьи данные можно поместить в архив.

Формат ввода
Программа получает на вход в одной строке число S – размер свободного места
на диске (натуральное, не превышает 10000), и число N – количество
пользователей (натуральное, не превышает 100), после этого идет N чисел -
объем данных каждого пользователя (натуральное, не превышает 1000), записанных
каждое в отдельной строке.

Формат вывода
Выведите наибольшее количество пользователей, чьи данные могут быть помешены в
архив.'''


s_n, vol = list(map(int, input().split())), []
size, users = s_n[0], s_n[1]
for i in range(users):
    vol.append(int(input()))
vol.sort()
count, total = 0, 0
for i in vol:
    total += i
    if size >= total:
        count += 1
print(count)