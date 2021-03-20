'''
Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. 
Выведите одно из четырех слов: rectangular для прямоугольного треугольника, 
acute для остроугольного треугольника, obtuse для тупоугольного треугольника 
или impossible, если треугольника с такими сторонами не существует 
(считаем, что вырожденный треугольник тоже невозможен).

Формат ввода
Вводятся три целых числа.
'''
a, b, c = int(input()), int(input()), int(input())
sides = sorted([a, b, c], reverse=True)
if sides[0] < sides[1] + sides[2] and sides[0] > sides[1] - sides[2]:
    if sides[0] ** 2 == sides[1] ** 2 + sides[2] ** 2:
        print('rectangular')
    elif sides[0] ** 2 > sides[1] ** 2 + sides[2] ** 2:
        print('obtuse')
    elif sides[0] ** 2 < sides[1] ** 2 + sides[2] ** 2:
        print('acute')
else:
    print('impossible')
