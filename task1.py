print('задача 1, программа найдет сумму элементов списка стоящих на нечетной позиции')
sp1 = []
sp2 = []
a = 0
b = 0

try:
 count = int(input('Введите размер списка '))
except:
 print('Введено не целое число, поробуйте снова')
 exit()

while a < count:
    try:
        n = int(input('Введите число '))
        a = a + 1
        sp1.append(n)
    except:
        print('Введено не целое число, поробуйте снова')
    
print(f'Получившися список чисел {sp1}')

for i in range(len(sp1)):
    if (i%2 != 0): sp2.append(sp1[i])

for i in range(len(sp2)):
    b = b + sp2[i]
print(f'Сумма элементов списка стоящих на нечетной позиции {b}')