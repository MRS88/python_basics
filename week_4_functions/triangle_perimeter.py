'''
Напишите функцию, вычисляющую длину отрезка по координатам его концов.
С помощью этой функции напишите программу, вычисляющую периметр треугольника
по координатам трех его вершин.

Формат ввода
На вход программе подается 6 целых чисел — координат x₁, y₁, x₂, y₂, x₃, y₃
вершин треугольника. Все числа по модулю не превосходят 30 000.'''

from math import sqrt


def perimeter(ax, ay, bx, by, cx, cy):
    ab = sqrt((bx-ax)**2 + (by-ay)**2)
    ac = sqrt((cx-ax)**2 + (cy-ay)**2)
    bc = sqrt((cx-bx)**2 + (cy-by)**2)
    return ab + ac + bc


ax, ay = int(input()), int(input())
bx, by = int(input()), int(input())
cx, cy = int(input()), int(input())

print(perimeter(ax, ay, bx, by, cx, cy))
