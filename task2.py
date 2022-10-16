print('задача 2, программа находит произведение пар чисел списка')
sp1 = []
sp2 = []
a = 0
ren = 0

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

if len(sp1)%2 == 0: ren = int(len(sp1)/2)
else: ren = int(len(sp1)//2+1)

for i in range(ren):
    sp2.append(sp1[i]*sp1[len(sp1)-i-1])

print(sp2)