'''
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E. 
Замок Иф сложен из кирпичей, размером A×B×C. 
Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие 
(очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

Формат ввода
Программа получает на вход числа A, B, C, D, E.

Формат вывода
Программа должна вывести слово YES или NO.
'''
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
brick, wall = sorted([a, b, c]), sorted([d, e])
if wall[0] >= brick[0] and wall[1] >= brick[1]:
    print('YES')
else:
    print('NO')