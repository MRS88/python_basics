'''Дана строка. Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.'''

s = input()
a = s[s.find('h')+1:s.rfind('h')].replace('h', 'H')
print('{}{}{}'.format(s[:s.find('h')+1], a, s[s.rfind('h'):]))