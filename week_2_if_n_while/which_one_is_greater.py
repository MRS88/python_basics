'''
Даны два целых числа. Программа должна вывести число "1", если первое число больше второго, число "2", 
если второе больше первого или число "0", если они равны.

Формат ввода
Вводятся два целых числа.

Формат вывода
Выведите ответ на задачу.

Примечания
Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
'''
a, b = int(input()), int(input())
if a >= b: print('1' if a > b else '0')
else: print('2')
