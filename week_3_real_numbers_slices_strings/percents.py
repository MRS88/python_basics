'''
Процентная ставка по вкладу составляет P процентов годовых, которые
прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите
размер вклада через год. При решении этой задачи нельзя пользоваться условными
инструкциями и циклами.

Формат ввода
Программа получает на вход целые числа P, X, Y.

Формат вывода
Программа должна вывести два числа: величину вклада через год в рублях и
копейках. Дробная часть копеек отбрасывается.
'''
p, x, y = int(input()), int(input()), int(input())
total = (x * 100 + y) * (100 + p) / 100
print(int(total // 100), int(total % 100))