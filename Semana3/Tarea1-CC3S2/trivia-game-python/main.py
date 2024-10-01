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
				print('¡Incorrecto!')	#el juego debe de continuar aunque se equivoque

	#Al finalizar el juego
	print("Juego terminado")
	print(f'Preguntas contestadas: {quiz.questions_answered}')
	print(f'Respuestas correctas: {quiz.correct_answers}')
	print(f'Respuestas incorrectas: {quiz.incorrect_answers}')
