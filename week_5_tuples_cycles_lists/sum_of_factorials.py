'''По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.

Формат ввода
Вводится натуральное число n.'''

from math import factorial

res = 0
for i in range(1, int(input())+1):
    res += factorial(i)
print(res)
