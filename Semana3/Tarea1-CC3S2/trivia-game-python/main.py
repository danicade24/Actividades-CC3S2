from trivia import Question, Quiz

def run_quiz():
	quiz = Quiz()
	while quiz.current_question_index < 10:
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
		print(f'Juego terminado. Respuestas correctas: {quiz.correct_answers}, incorrectas: {quiz.incorrect_answers}')