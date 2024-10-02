from trivia import Question, Quiz

def run_quiz():
    print("-------------------------¡Bienvenido al juego de Trivia!------------------------")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    
    quiz = Quiz()
    print("")
    
	#Agregamos las preguntas al nivel facil
    question = Question(f"¿Cuánto es 3 + 5?",["9","10","8","7"],"8")
    quiz.add_question(question, "easy")
    question = Question(f"¿Cuál es el planeta más cercano al Sol?",["Tierra", "Marte", "Venus", "Mercurio"], "Mercurio")
    quiz.add_question(question, "easy")
    question = Question("¿Cuánto es 10 - 4?", ["5", "6", "4", "7"], "6")
    quiz.add_question(question, "easy")
    question = Question("¿Qué animal es conocido como el rey de la selva?",["León", "Tigre", "Elefante", "Canguro"], "León")
    quiz.add_question(question, "easy")
    
    #Agregamos las preguntas al nivel medio
    question = Question(f"¿Cuál es el elemento químico con el símbolo Fe?",["Fósforo", "Hierro", "Flúor", "Francio"],"Hierro")
    quiz.add_question(question, "medium")
    question = Question(f"¿Cuánto es 17 + 28?",["44", "45", "46", "47"],"45")
    quiz.add_question(question, "medium")
    question = Question(f"¿Cuál es el país más grande del mundo?",["Estados Unidos", "Canadá", "Rusia", "China"],"Rusia")
    quiz.add_question(question, "medium")
    question = Question(f"¿Cuál es el océano más grande del mundo?",["Atlántico", "Pacífico", "Índico", "Ártico"],"Pacífico")
    quiz.add_question(question, "medium")
    question = Question(f"¿Cuánto es 100 - 47?",["51", "53", "57", "63"],"53")
    quiz.add_question(question, "medium")
    
	#Agregamos las preguntas al nivel dificil
    question = Question(f"¿Cuánto es 234 + 567?",["789", "801", "800", "812"],"801")
    quiz.add_question(question, "hard")
    question = Question(f"¿En qué año comenzó la Primera Guerra Mundial?",["1912", "1914", "1916", "1918"],"1914")
    quiz.add_question(question, "hard")
    question = Question(f"¿Cuál es el órgano más grande del cuerpo humano?",["Hígado", "Piel", "Cerebro", "Corazón"],"Piel")
    quiz.add_question(question, "hard")
    question = Question(f"¿Qué protocolo se utiliza para enviar correos electrónicos?",["FTP", "SMTP","HTTP", "IMAP"],"SMTP")
    quiz.add_question(question, "hard")
    question = Question(f"¿Cuánto es 25 x 19?",["475", "480", "485", "490"],"475")
    quiz.add_question(question, "hard")

    letters = ["a", "b", "c", "d"]
    i = 1
    #Bucle del juego para mostrar preguntas y recoger respuestas
    while quiz.questions_answered < 10:
        question = quiz.get_next_question()  # Retorna la pregunta y si no hay, retorna None
        if question:  # Comprueba si quedan preguntas
            print(f"{i}) {question.description}")
            for idx, option in enumerate(question.options):  # Muestra las opciones
                print(f'{letters[idx]}: {option}')

		# verificamos que la respuesta sea válida
            while True:
                answer = input("Tu respuesta (a, b, c, d): ").lower()  # convierte la letra en minúscula
                
                if answer in letters:
                    selected_option = question.options[letters.index(answer)]
                    if quiz.answer_question(question, selected_option):
                        print("¡Correcto!")
                    else:
                        print("¡Incorrecto!")
                    break  #sale del bucle si la respuesta es válida
                
                else:
                    print("Opción no válida. Por favor, selecciona a, b, c o d.")
        i += 1
                
    print("")
    #Al finalizar el juego
    print("Juego terminado")
    print(f'Preguntas contestadas: {quiz.questions_answered}')
    print(f'Respuestas correctas: {quiz.correct_answers}')
    print(f'Respuestas incorrectas: {quiz.incorrect_answers}')

run_quiz()