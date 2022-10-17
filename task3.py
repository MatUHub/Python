print('задача 3, программа находит максимальное и минимальное значение дробной части элементов')
sp1 = []
sp2 = []
a = 0
dif = 0
try:
 count = int(input('Введите размер списка '))
except:
 print('Введено не целое число, поробуйте снова')
 exit()

while a < count:
    try:
        n = float(input('Введите число '))
        a = a + 1
        sp1.append(n)
    except:
        print('Введено не вещественное число, поробуйте снова')
    
print(f'Получившися список чисел {sp1}')

max = sp1[0]
min = sp1[0]

for i in range(len(sp1)):
    if max < sp1[i]: max = sp1[i]
    if min > sp1[i]: min = sp1[i]

print(f'максимальное чило в списке {max}')
print(f'минимальное  чило в списке {min}')

drob1 = max - int(max)
drob2 = min - int(min)

print(f'дробная часть максимального числа {round(drob1, 3)}')
print(f'дробная часть минимального числа {round(drob2, 3)}')

if drob1 <= drob2: dif = drob2 - drob1
else: dif = drob1 - drob2

print(f'разница между максимальным и минимальным значением дробной части {round(dif, 3)}')