from src.trivia import Quiz, Question
from src.db.database import get_db
from sqlalchemy.orm import Session
from src.questions.question_model import Question as DBQuestion

def load_questions_from_db(db: Session, quiz: Quiz):
    questions = db.query(DBQuestion).all()
    for q in questions:
        quiz.add_question(Question(q.description, q.options, q.correct_answer), q.level)

def run_quiz():
    db = next(get_db())  # Obtiene la sesión de la base de datos del generador
    quiz = Quiz()
    load_questions_from_db(db, quiz)  # Carga las preguntas desde la base de datos

    print("-------------------------¡Bienvenido al juego de Trivia!------------------------")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    
    letters = ["a", "b", "c", "d"]
    i = 1
    
    while quiz.questions_answered < 10:
        question = quiz.get_next_question()
        if question:
            print(f"Nivel actual: {quiz.level_question.capitalize()}")
            print(f"Pregunta {i}) {question.description}")
            for idx, option in enumerate(question.options):
                print(f'{letters[idx]}: {option}')

            while True:
                answer = input("Tu respuesta (a, b, c, d): ").lower()
                if answer in letters:
                    selected_option = question.options[letters.index(answer)]
                    if quiz.answer_question(question, selected_option):
                        print("¡Correcto!")
                    else:
                        print("¡Incorrecto!")
                    break
                else:
                    print("Opción no válida. Por favor, selecciona a, b, c o d.")
        i += 1
        print("")
                
    print("")
    print("Juego terminado")
    print(f'Preguntas contestadas: {quiz.questions_answered}')
    print(f'Respuestas correctas: {quiz.correct_answers}')
    print(f'Respuestas incorrectas: {quiz.incorrect_answers}')

if __name__ == "__main__":
    run_quiz()
