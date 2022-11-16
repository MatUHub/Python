import random

print("Программа 1, игра в 'Крестики-нолики'")
field = [['*','*','*'], ['*','*','*'], ['*','*','*']]
count = 0

def show_field():

    for i in range(len(field)):
        print()
        if i == 0:print('  1', '2', '3')
        for j in range(len(field[i])):
            if j == 0:
                print(f'{i + 1} {field[i][j]}', end=" ")
            else:print(field[i][j], end=" ")
    print()
def change_field_human(x,y):
    field[x][y] = "X"

def change_field_computer(x,y):
    field[x][y] = "0"

def human_move():
    print("Ход человека")
    while True:
        try:
            x = int(input('Введите строку поля: '))
            if x > 3 or x < 1:
                print('Введите значение от 1 до 3')
                continue
            y = int(input('Введите столбец поля: '))
            if y > 3 or y < 1:
                print('Введите значение от 1 до 3')
                continue
            x = x - 1
            y = y - 1
            if field[x][y] == "X" or field[x][y] == "0":
                print('Эта ячейка занята, выберите другую')
                continue
            change_field_human(x, y)
        except:
            print('Введено не целое число попытайтесь снова')
            continue
        return False

def computer_move():
    print('Ход компьютера')
    while True:
        
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if field[x][y] == "X" or field[x][y] == "0": continue
        else:
            change_field_computer(x, y)
            return False

def human_win():

    if field[0][0] == "X"  and  field[0][1] == "X" and field[0][2] == "X":
        print("Выиграл человек")
        exit()
    if field[1][0] == "X"  and  field[1][1] == "X" and field[1][2] == "X":
        print("Выиграл человек")
        exit()
    if field[2][0] == "X"  and  field[2][1] == "X" and field[2][2] == "X":
        print("Выиграл человек")
        exit()

    if field[0][0] == "X"  and  field[1][0] == "X" and field[2][0] == "X":
        print("Выиграл человек")
        exit()
    if field[0][1] == "X"  and  field[1][1] == "X" and field[2][1] == "X":
        print("Выиграл человек")
        exit()
    if field[0][2] == "X"  and  field[1][2] == "X" and field[2][2] == "X":
        print("Выиграл человек")
        exit()

    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        print("Выиграл человек")
        exit()
    if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
        print("Выиграл человек")
        exit()

def computer_win():
    if field[0][0] == "0" and field[0][1] == "0" and field[0][2] == "0":
        print("Выиграл компьютер")
        exit()
    if field[1][0] == "0" and field[1][1] == "0" and field[1][2] == "0":
        print("Выиграл компьютер")
        exit()
    if field[2][0] == "0" and field[2][1] == "0" and field[2][2] == "0":
        print("Выиграл компьютер")
        exit()

    if field[0][0] == "0" and field[1][0] == "0" and field[2][0] == "0":
        print("Выиграл компьютер")
        exit()
    if field[0][1] == "0" and field[1][1] == "0" and field[2][1] == "0":
        print("Выиграл компьютер")
        exit()
    if field[0][2] == "0" and field[1][2] == "0" and field[2][2] == "0":
        print("Выиграл компьютер")
        exit()

    if field[0][0] == "0" and field[1][1] == "0" and field[2][2] == "0":
        print("Выиграл компьютер")
        exit()
    if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
        print("Выиграл компьютер")
        exit()

def full_field():
    count = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '*':
                count = count + 1
    if count == 0:
        print('Свободные клетки закончились ничья!')
        exit()



show_field()
while True:
    
    human_win()
    computer_win()
    full_field()

    if count == 0:
        human_move()
    else:
        computer_move()
    if count == 0: count = 1
    else: count = 0
    show_field()