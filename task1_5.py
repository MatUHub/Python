from random import random

print('задача 1, игра в конфеты')
print('Наступил 2022 год, после долгих сражений между людьми и роботами наступило краткосрочное перемирие.'
      '\nОбоюдно было решено провести игру, победитель получает все.\nИз многих кандидатур решили выбрать именно Вас, не подведите, от результата игры зависит будущее человечества.')
print()
count = 2022
turn = 0
winer = ''
ran = int(random() * 10)
if ran >= 5:
    player1 = 'человек'
    player2 = 'бот'
else:
    player2 = 'человек'
    player1 = 'бот'
print(f'жребий брошен, первым ходит {player1}')



while count != 0:
      if turn == 0:
          if player1 == 'бот':
            a = int(random()*28)
            if count <= 28: a = count
            if count - a < 0: a = int(random()*count)
            count = count - a
            print(f'ход {player1} забрал: {a}')
            turn = 1
            winer = player1
          elif player1 == 'человек':
              try:
                a = int(input('введите число: '))
                if a > 28 or a < 1:
                    print('введено число более 28 или менее 1, попробуйте снова')
                    continue
              except:
                    print('введено не целое число, попробуйте снова')
                    continue
              if count - a < 0:
                  print('вы не можете взять конфет больше чем есть, попробуйте снова')
                  continue
              count = count - a
              turn = 1
              winer = player1
              print(f'ход {player1} забрал: {a}')
      else:
          if player2 == 'бот':
            a = int(random() * 28)
            if count <= 28: a = count
            if count - a < 0: a = int(random() * count)
            count = count - a
            print(f'ход {player2} забрал: {a}')
            turn = 0
            winer = player2
          elif player2 == 'человек':
              try:
                  a = int(input('введите число: '))
                  if a > 28 or a < 1:
                      print('введено число более 28 или менее 1, попробуйте снова')
                      continue
              except:
                  print('введено не целое число, попробуйте снова')
                  continue
              if count - a < 0:
                  print('вы не можете взять конфет больше чем есть, попробуйте снова')
                  continue
              count = count - a
              turn = 0
              print(f'ход {player2} забрал: {a}')
              winer = player2

      print(f'осталось {count} конфет')
if winer == 'бот':
    print('\nИз дальних уголков теперь не нашей планеты как будто раздаются голоса людей, котороые когда то жили на ней. \n'\
'Некоторые из людей ушли в подземелье и до конца времен будут скитаться по недрам земли, если их не обнаружат роботы и не уничтожат. \nМы знаем ' \
'Вы сделали все что смогли, не вините себя ... \nРоботы победили!')

else: print('\nРоботы покинули Землю и отправились в поисках планеты на которой они обретут свой дом. \nМы верили в Вас, поздарвляем! \nЛюди победили'
)



