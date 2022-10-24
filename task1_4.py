print('задача 1, программа составляет список простых множителей числа')
try:
   n = int(input('введите число: '))
except:
    print('введено не натуральное число, попробуйте снова')
    exit()
b = n 
a = True
sp = []
i = 1
while a:
    if n == 1: a = False
    i = i + 1
    if n%i == 0:
        n = n / i
        sp.append(i)
        i = 1
print(f'список простых множителей числа {b} равно {sp}')
