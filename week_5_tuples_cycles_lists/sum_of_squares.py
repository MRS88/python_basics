'''По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

Формат ввода
Вводится натуральное число.'''

res = 0
for i in range(1, int(input())+1):
    res += i ** 2
print(res)
