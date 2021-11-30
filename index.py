import pyfirmata 
import time
from telegram.ext import (Updater, CommandHandler)


puerto = "/dev/ttyUSB0"
print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(puerto)
pin = (13)


def start(update, context):
	''' START '''
	tarjeta.digital[pin].write(1)
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Encendido")
	

def stop(update, context):
	''' START '''
	tarjeta.digital[pin].write(0)
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Apagado")



def main():
    #Puerto COM de emulación en USB
    TOKEN = "2111226480:AAEQwzNIDYs0vrcw4lZ1W03c6BJjEXvbOXo"
    updater=Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
	# Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    updater.start_polling()
	
    updater.idle()
    tarjeta.exit()
    

if __name__ == '__main__':
    main()