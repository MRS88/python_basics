'''
Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов (число от 0 до 23), 
потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. 
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

С начала суток прошло N секунд. Выведите, что покажут часы.

Формат ввода
Вводится число N —  целое, неотрицательное.

Формат вывода
Выведите показания часов, соблюдая формат.

Примечания
Вывести числа можно поциферно.
'''
n = int(input())
sec = n % 60
minutes = n // 60 % 60
hours = n // 3600 % 24
print(f'{hours}:{minutes:02}:{sec:02}')
