from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = {
	"привет": "Привет!",
	"как дела?": "Отлично, а у тебя?",
	"пока": "Еще увидимся",
	"кто ты?": "Я бот, я же говорил, duh",
	"duh": "duh!",
	"что ты делаешь?": "Существую в твоем телеграме"
}

def get_answer(question, answers):
	return answers.get(question)


def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text = "Привет, я бот! Давай общаться:) Скажи что-нибудь")

def talk_to_me(bot, update):
	print("Пришло сообщение: " + update.message.text)
	answer = get_answer(update.message.text, answers)
	try:
		answers[update.message.text] == True
	except KeyError:
		bot.sendMessage(update.message.chat_id, text = "Не понимаю:( Я очень чувствителен к регистру строки. Попробуй набрать строчными буквами")
	else:
		bot.sendMessage(update.message.chat_id, text = answer)

def word_count(phrase):
	words_list = phrase.split(" ")
	return (len(words_list) - 1)

def count_bot(bot, update):
	print("Пришло сообщение: " + update.message.text)
	word_number = word_count(update.message.text)
	bot.sendMessage(update.message.chat_id, text = "В вашей фразе {} слов(а/о)".format(word_number))

def num(user_input):
	num_check = list(user_input)
	num_check = num_check[-4:-1]
	for ind in num_check:
		if ind == "+":
			result = int(num_check[0]) + int(num_check[2])
			return result
			#print(result)
		elif ind == "-":
			result = int(num_check[0]) - int(num_check[2])
			return result
			#print(result)
		elif ind == "*":
			result = int(num_check[0]) * int(num_check[2])
			return result
			#print(result)
		elif ind == "/":
			result = int(num_check[0]) / int(num_check[2])
			return result
			#print(result)
def calc(bot, update):
	print("Пришло сообщение: " + update.message.text)
	rslt = num(update.message.text)
	#splitter = list(update.message.text)
	#splitter = str(splitter[-4:-1])
	bot.sendMessage(update.message.chat_id, text = int(rslt))

def run_bot():
	updater = Updater("277701742:AAEaxsArqY95o-c8dFptddfZDpnVPFH-s8s")
	
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	dp.add_handler(CommandHandler("word_count", count_bot))
	dp.add_handler(CommandHandler("calc", calc))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	run_bot()
	#num("/calc 4+5=")