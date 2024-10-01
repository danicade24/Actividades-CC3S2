from trivia import Question, Quiz

def run_quiz():
	print("Bienvenido al juego de Trivia!!")
	print("Responde las siguientes preguntas seleccionando el número de la opción correcta ")
	quiz = Quiz()
	while quiz.questions_answered < 10:
		question = quiz.get_next_question()	#retorna la pregunta y si no hay retorna None
		if question:	#Comprueba si quedan preguntas
			print(question.description)
			for idx, option in enumerate(question.options):	#el método devuelve tanto el ídice como el valor
				print(f'{idx + 1}{option}')
			answer = input("Tu respuesta: ")
			if quiz.answer_question(question, answer):
				print("¡Correcto!")
			else:
				break
