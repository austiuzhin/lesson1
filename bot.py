from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text = "Привет, давай общаться. Я бот")

def talk_to_me(bot, update):
	print("Пришло сообщение: " + update.message.text)
	bot.sendMessage(update.message.chat_id, text = update.message.text)

def run_bot():
	updater = Updater("277701742:AAEaxsArqY95o-c8dFptddfZDpnVPFH-s8s")
	
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()

