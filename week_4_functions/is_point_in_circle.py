'''Даны пять действительных чисел: x, y, xc, yc, r.
Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
возвращающую True, если точка принадлежит кругу и False, если не принадлежит.
'''

from math import sqrt


def IsPointInCircle(x, y, xc, yc, r):
    section = sqrt((xc - x)**2 + (yc - y)**2)
    return 'YES' if section <= r else 'NO'


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())
print(IsPointInCircle(x, y, xc, yc, r))
