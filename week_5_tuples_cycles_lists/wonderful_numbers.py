'''Найдите и выведите все двузначные числа, которые равны удвоенному
произведению своих цифр.

Формат ввода
Программа не требует ввода данных с клавиатуры,
просто выводит список искомых чисел.'''

for i in range(10, 100):
    if 2 * (i // 10) * (i % 10) == i:
        print(i)