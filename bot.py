import telebot

# Configura el token de tu bot de Telegram
TOKEN = '5999092947:AAEs1oWAp6naTqmwJV1vOsBbijzipOSP84Q'

# Crea una instancia del bot
bot = telebot.TeleBot(TOKEN)

# Maneja el comando '/start'
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Un pequeño paso para el Hombre, un gran paso para la Humanidad")

# Maneja todos los mensajes de texto
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

# Inicia el bot
bot.polling()

def innit_bot():
   bot.infinity_polling(skip_pending=True)

   if __name__ == "__main__":
       innit_bot()
