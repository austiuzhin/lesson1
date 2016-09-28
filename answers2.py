answers = {
	"привет": "Привет!",
	"как дела?": "Отлично, а у тебя?",
	"пока": "Еще увидимся"
}

def get_answer(question, answers):
	return answers.get(question)

def ask_user(answers):
	
	else:
		while True:
			user_input = input("Скажи что-нибудь: ")
			answer = get_answer(user_input, answers)
			try:
				answers[user_input] == True
			except KeyError:
				print("я не понимаю")
			else:
				print(answer)
		
if __name__ == "__main__"
	ask_user(answers)
