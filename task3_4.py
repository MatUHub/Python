from random import random

print('задача 3, программа случайным образом формирует список коэффициентов многочлена и записывает в файл file.txt')
st = []
try:
 k = int(input('введите значение коэффициента '))
except:
 print('введено не натуральное число, поробуйте снова')
 exit()
for i in range(k):
    koef = int(random() * 100)
    if i == 0:
           if koef != 0:
            st.append(f'{koef}x^{k}')
    if k - i == 1:
        if koef != 0:
            st.append(f'+{koef}x')
            koef = int(random() * 100)
            if koef != 0:
             st.append(f'+{koef}')
        st.append('=0')
    elif i > 0:
        if koef != 0:
         st.append(f'+{koef}x^{k-i}')

stp = ''.join(st)
print(f'многочлен равен {stp}')

with open('file.txt', 'w') as data:
    data.write(stp)
print('многочлен записан в файл file.txt')    