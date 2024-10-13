import pytest
from ..src.trivia import Question,  Quiz

#Comprueba que una respuesta correcta coincida con real
def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1","2","3","4"],"4")
    assert question.is_correct("4")

#Comprueba que una respuesta incorrecta se deteccte como tal
def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1","2","3","4"],"4")
    assert not question.is_correct("2")

#Prueba para ver si el sistema de puntuaciones funciona bien para respuestas correctas
def test_scoring_correct_answer():
    quiz = Quiz()
    question = Question("What is 2+2?", ["1","2","3","4"],"4")

    #Añadimos una pregunta fácil
    quiz.add_question(question, "easy")

    assert quiz.answer_question(question,"4") == True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0

#Prueba para ver si el sistema de puntuaciones funciona bien para respuestas incorrectas
def test_scoring_correct_answer():
    quiz = Quiz()
    question = Question("What is 2+2?", ["1","2","3","4"],"4")

    #Añadimos una pregunta fácil
    quiz.add_question(question, "easy")

    assert quiz.answer_question(question,"1") == False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1

#Prueba para ver el cambio de nivel (incrementa)
def test_increase_difficulty():
    quiz = Quiz()
    question_easy = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    question_medium = Question("What is 3 + 3?", ["5", "6", "7", "8"], "6")
    
    #Añadimos una pregunta fácil y una de nivel medio
    quiz.add_question(question_easy, "easy")
    quiz.add_question(question_medium, "medium")
    
    #Responde bien la pregunta fácil
    quiz.answer_question(question_easy, "4")
    
    #Comprueba que ha subido de nivel a 'medium'
    assert quiz.level_question == 'medium'

#Prueba para ver el cambio de nivel (decrementa)
def test_decrease_difficulty():
    quiz = Quiz()
    question_hard = Question("What is 5 + 5?", ["10", "12", "15", "20"], "10")
    question_easy = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    
    #Añadimos preguntas
    quiz.add_question(question_hard, "hard")
    quiz.add_question(question_easy, "easy")
    
    #Simulamos que la dificultad está en 'hard' y falla la pregunta
    quiz.level_question = 'hard'
    quiz.answer_question(question_hard, "12")
    
    #Comprueba que ha bajado de nivel a 'medium'
    assert quiz.level_question == 'medium' or quiz.level_question == 'easy'

#Prueba si cambia de nivel si no hay preguntas en el nivel actual
#Verifica que si no hay preguntas en el nivel actual, el sistema ajusta el nivel y busca en otro.
def test_change_level_if_no_questions():
    quiz = Quiz()
    question_medium = Question("What is 3 + 3?", ["5", "6", "7", "8"], "6")
    
    #Añade preguntas al nivel medio
    quiz.add_question(question_medium, "medium")
    
    #Simular que está en nivel 'easy' sin preguntas
    quiz.level_question = 'easy'
    
    #verificar que pasa al nivel 'medium' al no haber preguntas en 'easy'
    question = quiz.get_next_question()
    assert quiz.level_question == 'medium'
    assert question is not None
    assert question.description == "What is 3 + 3?"

#Prueba si se obtiene la siguiente pregunta correcta y se mantiene el límite de 10 preguntas
def test_limit_of_questions():
    quiz =  Quiz()
    
    #Añadimos 11 preguntas
    for i in range(11):
        question = Question(f"What is {i} + {i}?", [str(i) for i in range(4)], str(i))
        quiz.add_question(question, "easy")
    
    #Responde 10 preguntas
    for j in range(10):
        question = quiz.get_next_question()
        assert question is not None
        quiz.answer_question(question, str(j))  #simulamos que siempre responde
    
    #Verifica que al intentar obtener la pregunta 11 no hay más disponibles
    assert quiz.get_next_question() is None