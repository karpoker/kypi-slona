import telebot # импортируем библиотеку для работы с телеграм ботами

TOKEN = '6335859808:AAH693hwChPhIcObGunHU19YyfHGq1QgA70' # замените на свой токен, который получили от BotFather
bot = telebot.TeleBot(TOKEN) # создаем объект бота

@bot.message_handler(commands=['start']) # обрабатываем команду /start
def start(message):
    bot.send_message(message.chat.id, "Купи слона!") # отправляем приветственное сообщение

@bot.message_handler(func=lambda message: True) # обрабатываем любое другое сообщение
def buy_elephant(message):
    bot.send_message(message.chat.id, f"Все говорят {message.text}, а ты купи слона!") # отправляем ответ, повторяя текст пользователя и добавляя фразу "а ты купи слона"

bot.polling() # запускаем бота
