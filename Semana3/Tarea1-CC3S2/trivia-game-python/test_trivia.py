import pytest
from trivia import Question,  Quiz

#Comprueba que una respuesta correcta coincida con real
def test_question_correct_answer():
    question = Question("What is 2+2", ["1","2","3","4"],"4")
    assert question.is_correct("4")

#Comprueba que una respuesta incorrecta se deteccte como tal
def test_question_incorrect_answer():
    question = Question("What is 2+2", ["1","2","3","4"],"4")
    assert not question.is_correct("2")

#prueba para ver si el sistema de puntuaciones funciona correctamente 
def test_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?",["1","2","3","4"],"4")
    quiz.add_question(question)
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1