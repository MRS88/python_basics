'''
По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

Формат ввода
Вводится натуральное число.
'''
n = int(input())
res = 0
count = 1
while count <= n:
    res += count ** 2
    count += 1
print(res)
