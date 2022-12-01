import telebot
import key as k
import database as db

db.create_db()
db.create_table()


bot = telebot.TeleBot(k.API_TOKEN)

add = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Бот запущен!")

@bot.message_handler(commands=['add'])
def add_message(message):
    text = message.text
    text = text.split()
    print(len(text))
    table = text[1]
    name = text[2]
    year_of_manufacture = text[3]
    mileage = text[4]
    color = text[5]
    engine_power = text[6]
    drive = text[7]
    db.add_data_to_table(table, name, year_of_manufacture, mileage, color, engine_power, drive)
    bot.send_message(message.chat.id, "Данные добавлены!")

@bot.message_handler(commands=['addinfo'])
def add_message(message):
    bot.send_message(message.chat.id,"Для добавления в таблицу данных введите команду /add и значения заданной последовательности -> table name year_of_manufacture mileage color engine_power drive")

@bot.message_handler(commands=['show'])
def show_message(message):
    text = message.text
    text = text.split()
    db.show_data(text[1])
    show_data = db.show_value
    for i in show_data: bot.send_message(message.chat.id,i)
    
@bot.message_handler(commands=['showinfo'])
def show_message(message):
    bot.send_message(message.chat.id, "Для вывода данных из таблицы введите команду /showinfo и название таблицы")


@bot.message_handler(commands=['find'])
def find_message(message):
    text = message.text
    text = text.split()
    table = text[1]
    column = text[2]
    value = text[3]
    db.find_data_value(table, column, value)
    data = db.find_value
    for i in data: bot.send_message(message.chat.id,i)

@bot.message_handler(commands=['findinfo'])
def find_info_message(message):
    bot.send_message(message.chat.id,"Для вывода данных по параметру из таблицы введиете /find  наименование таблицы, наименование колонки и значение")


@bot.message_handler(commands=['update'])
def update_message(message):
    text = message.text
    text = text.split()
    table = text[1]
    name = text[2]
    column = text[3]
    value = text[4]
    db.data_update(table, name, column, value)
    bot.send_message(message.chat.id, "Изменение произведено!")

@bot.message_handler(commands=['updateinfo'])
def update_info_message(message):
    bot.send_message(message.chat.id,"Для обновления данных в таблице нужно ввести команду /find назвние таблицы, наименование машины, нименование колонки и новое значение")


@bot.message_handler(commands=['del'])
def del_message(message):
    text = message.text
    text = text.split()
    table = text[1]
    name = text[2]
    db.delete_data(table, name)
    bot.send_message(message.chat.id, "Данные удалены!")

@bot.message_handler(commands=['delinfo'])
def update_info_message(message):
    bot.send_message(message.chat.id,"Для удаление данных нужно ввести команду /del название таблицы и наименование машины")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "/start - начало работы")
    bot.send_message(message.chat.id, "/add - Добавление данных в таблицу")
    bot.send_message(message.chat.id, "/show - Показать данные в таблице")
    bot.send_message(message.chat.id, "/find - Поиск данных по параметру в таблице")
    bot.send_message(message.chat.id, "/update - Изменение данных в таблице")
    bot.send_message(message.chat.id, "/del - Удаление данных из таблицы")
    bot.send_message(message.chat.id, "/addinfo - Инстуркция по добавлению данных")
    bot.send_message(message.chat.id, "/showinfo - Инструкция по выводу данных")
    bot.send_message(message.chat.id, "/findinfo - Инструкция по поиску данных")
    bot.send_message(message.chat.id, "/updateinfo - Инструкция по изменению данных")
    bot.send_message(message.chat.id, "/delinfo - Инструкция по удалению данных")
    
     
@bot.message_handler(content_types = "text")
def check_message(message):
    bot.send_message(message.chat.id, "команда не распознана введите /help для получения списка доступных команд")
    
bot.polling()    