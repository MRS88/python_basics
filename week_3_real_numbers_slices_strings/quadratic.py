from math import sqrt
a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
x1 = (-b - sqrt(d)) / (2 * a)
x2 = (-b + sqrt(d)) / (2 * a)
if d > 0 and a > 0:
    print(x1, x2)
elif d > 0 and a < 0:
    print(x2, x1)
elif d == 0:
    print(-b / 2 * a)
