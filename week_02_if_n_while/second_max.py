'''
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности,
то есть элемента, который будет наибольшим, если из последовательности
удалить одно вхождение наибольшего элемента.
'''
n = int(input())
lst = []
while n != 0:
    lst.append(n)
    n = int(input())
lst.remove(max(lst))
print(max(lst))
