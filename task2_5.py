print('задача 2, программа реализует RLE алгоритм')
sp = 'aaaaaaabbbbbbbbcccccccdddddddtttttttt'
print(f'исходное значение: {sp}')
count = 0
sp2 = []
for i in sp:
    sp2.append(i)
symbol = sp2[0]
sp2 = []
for i in sp:
    if symbol == i:
        count = count + 1
    else:
        sp2.append(count)
        sp2.append(symbol)
        symbol = i
        count = 1
sp2.append(count)
sp2.append(symbol)
sp = []

print(f'модуль сжатия: {sp2}')

for i in range(len(sp2)):
    if i % 2 == 0:
        for j in range(sp2[i]):
            sp.append(sp2[i + 1])
sp = ''.join(sp)
print(f'модуль восстановления: {sp}')