'''
Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, 
или слово NO в противном случае. Операцией возведения в степень пользоваться нельзя!
'''
n = int(input())
while n > 1:
    n /= 2
if n == 1:
    print('YES')
else:
    print('NO')