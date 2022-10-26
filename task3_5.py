print('задача 3, программа удаляет из текста все слова содеражщие "абв"')
with open('file.txt', encoding='utf-8') as data:
 sp = data.read()
 print(f'Исходный текст: {sp}')
sp = sp.split()
count = 0
countA = 0
countB = 0
countV = 0
for i in range(len(sp)):
    for j in sp[i]:

        if count == 3:
            sp[i] = ''
            count = 0
            break
        if j == 'а':
            if countA != 1:
               count = count + 1
               countA = countA + 1
            else:
                count = 0
                countA = 0
                countB = 0
                countV = 0

        elif j == 'б':
            if countB != 1:
                count = count + 1
                countB = countB + 1
            else:
                count = 0
                countA = 0
                countB = 0
                countV = 0
        elif j == 'в':
            if countV != 1:
                count = count + 1
                countV = countV + 1
            else:
                count = 0
                countA = 0
                countB = 0
                countV = 0
        else:
            count = 0
            countA = 0
            countB = 0
            countV = 0
for i in sp:
    if i == '': sp.remove(i)

sp = ' '.join(sp)
print(f'Текст после исключений слов с "абв": {sp}')