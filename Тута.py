import telebot 
import random , os    
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.Напиши /help чтоб посмотреть список команд")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Команды: 1 /mem показывает мем програмиста, 2 /aco показывает мем про мусор, 3 /aco2 рассказывает про помощь планете.  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.Напиши /help чтоб посмотреть список команд")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir("images")
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['aco'])
def send_mem(message):
    imagess = os.listdir("aco")
    img_name = random.choice(imagess)
    with open(f'aco/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['aco2'])
def send_mem(message):
    image = os.listdir("aco2")
    img_name = random.choice(image)
    with open(f'aco2/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
