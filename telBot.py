import telebot
import logger as l
import model as m
import requests
import key as k

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'


bot = telebot.TeleBot(k.API_TOKEN)

answer = ""
log_bot = ""
expression = ""

API_URL = 'http://numbersapi.com/42'

calc = False
translate = False

@bot.message_handler(commands=['start'])
def start_message(message):
    l.logger_calc(message.text)
    bot.send_message(message.chat.id, "Ready")

@bot.message_handler(commands=['calc'])
def calc_message(message):
    l.logger_calc(message.text)
    bot.send_message(message.chat.id, "Введите выражение:")
    global calc
    calc = True

@bot.message_handler(commands=['help'])
def help_message(message):
    l.logger_calc(message.text)
    bot.send_message(message.chat.id, "/start - начало работы")
    bot.send_message(message.chat.id, "/calc - команда для начала расчета выражения")
    bot.send_message(message.chat.id, "/log - команда для вывода логов")
    bot.send_message(message.chat.id, "/translate - команда для вывода факта о числе")

@bot.message_handler(commands=['translate'])
def numbers_message(message):
    global translate
    translate = True
    bot.send_message(message.chat.id, "Введите слово для перевода: ")

@bot.message_handler(commands=['log'])
def help_message(message):
    l.logger_calc(message.text)
    global log_bot
    l.get_logger()
    log_bot = l.loge
    for i in log_bot:
        bot.send_message(message.chat.id, i)
      
@bot.message_handler(content_types = "text")
def check_message(message):
    global calc
    global translate
    l.logger_calc(message.text)
    if calc == True:
        calc = False
        m.calculation(message.text)
        answer = m.otvet
        l.logger_calc(answer)
        bot.send_message(message.chat.id, answer)
    elif translate == True:

        translate = False

        word = message.text
        headers_auth = {'Authorization': 'Basic ' + k.KEY}
        auth = requests.post(URL_AUTH, headers=headers_auth)
        token = auth.text
        headers_translate = {
        'Authorization': 'Bearer ' + token
        }
        params = {
        'text': word,
        'srcLang': 1033,
        'dstLang': 1049
        }
        r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()
        enter = res['Translation']['Translation']
        l.logger_calc(enter)
        try:
             bot.send_message(message.chat.id,enter)
             print(res['Translation']['Translation'])
        except: print('Превод такого слова не найден')

    else: bot.send_message(message.chat.id,"Команда не определена, введите /help для вывода доступных команд")
bot.polling()    