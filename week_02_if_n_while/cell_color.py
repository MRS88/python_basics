'''
Заданы две клетки шахматной доски. 
Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.

Формат ввода
Вводятся 4 числа - координаты клеток.
'''
col1, row1, col2, row2 = int(input()), int(input()), int(input()), int(input())
abs_col = abs(col1 - col2)
abs_row = abs(row1 - row2)
if (abs_col % 2 == 0 and abs_row % 2 == 0) or \
    (abs_col % 2 == 1 and abs_row % 2 == 1):
    print('YES')
else:
    print('NO')
