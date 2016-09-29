answers = {
	"привет": "Привет!",
	"как дела?": "Отлично, а у тебя?",
	"пока!": "Еще увидимся"
}

def get_answer(question, answers):
	return answers.get(question)

def ask_user(answers):
	
	while True:
		user_input = input("Скажи что-нибудь: ")
		answer = get_answer(user_input, answers)
		print(answer)

		if user_input == "ой, все":
			break
		
if __name__ == "__main__":
	ask_user(answers)
	ask_user(answers)
