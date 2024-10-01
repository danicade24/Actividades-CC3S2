class Question:  
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_aswer = correct_answer
    
    #Compara si la respuesta dada coincide con la verdadera
    def is_correct(self, correct_answer):
        return self.correct_aswer == correct_answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
    
    #Agrega una pregunta a la lista
    def add_question(self, question):
        self.questions.append(question)

    #Método para obtener la siguiente pregunta de la lista de preguntas
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    #Verifica la veracidad de la pregunta 
    #en caso sea correcta aumenta el contador de respuestas correctas y retorna true
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            return False
