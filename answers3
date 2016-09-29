answers = {"привет": "И тебе привет!", "как дела?": "Лучше всех", "пока": "Увидимся"} 
2 
 
3 def get_answer(question, answers): 
4     return answers.get(question) 
5 
 
6 def ask_user(answer): 
7     try: 
8         while True: 
9             user_input = input('Скажи что-нибудь:  ').lower() 
10             answer = get_answer(user_input, answers) 
11             print(answer) 
12 
 
13             if (user_input == "пока"):  
14                 break  
15 
 
16     except KeyboardInterrupt:  
17         print('\n\nУходите? Что, даже чаю не попьёте?\n\n') 
18 
 
19 if __name__ == "__main__": 
20     ask_user(answers) 
