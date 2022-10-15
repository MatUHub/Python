from itertools import count


print('задание 3, программа определяет количество вхождений одно строки в другой')
a = input('введите первую строку ')
b = input('введите вторую строку ')
c = 0
if len(a) < len(b):
 c = len(a)
else:
 c = len(b)
count = 0

for i in range(c):
    if a[i] == b[i]: count = count + 1

print(f'количестов вхождений одной строки в другую равно {count}')
