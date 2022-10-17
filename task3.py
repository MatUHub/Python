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

for i in range (len(sp1)):
     sp2.append(sp1[i]-int(sp1[i]))

max = sp2[0]
min = sp2[0]

for i in range(len(sp2)):
    if(sp2[i] != 0):
     if max < sp2[i]: max = sp2[i]
     if min > sp2[i]: min = sp2[i]

max = round(max, 3)     
min = round(min, 3)

print(f'максимальное значение дробной части в списке {max}')
print(f'минимальное значение дробной части в списке {min}')

dif = max - min

print(f'разница между максимальным и минимальным значением дробной части {round(dif, 3)}')