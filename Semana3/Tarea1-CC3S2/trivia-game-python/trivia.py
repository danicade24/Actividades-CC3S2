class Question:  
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
    
    #Compara si la respuesta dada coincide con la verdadera
    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = {
            'easy': [],
            'medium' : [],
            'hard' : []
        }
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.level_question = 'easy'    #por defecto
        self.questions_answered = 0
    
    #Agrega una pregunta a la lista dependiendo del nivel
    def add_question(self, question, level):
        if level in self.questions:
            self.questions[level].append(question)

    #Método para obtener la siguiente pregunta de la lista de preguntas segun el nivel
    def get_next_question(self):
        if self.questions_answered < 10:
            if self.level_question in self.questions and self.questions[self.level_question]:
                question = self.questions[self.level_question].pop(0)
                self.questions_answered += 1
                return question
            else:   #si ya no hay mas preguntas en el nivel actual
                if self.decrease_difficulty():  #busca en niveles inferiores
                    return self.get_next_question()
                elif self.increase_difficulty():    #busca en niveles superiores
                    return self.get_next_question()
                else:
                    return None     #no encuentra preguntas en ningun nivel
        return None
    
    #Verifica la veracidad de la pregunta 
    #en caso sea correcta aumenta el contador de respuestas correctas y retorna true
    def answer_question(self, question, answer):
        result = question.is_correct(answer)
        if result:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        
        #Actualizamos el nivel de dificultad luego de contestar una pregunta 
        self.update_difficulty()
        return result
    
    
    #Introduce niveles de dificultad
    def update_difficulty(self):
        if self.correct_answers > self.incorrect_answers:
            self.increase_difficulty()
        elif self.correct_answers < self.incorrect_answers:
            self.decrease_difficulty()
        else:
            pass    #en caso de empate se mantiene el nivel

    def increase_difficulty(self):
        if self.level_question == 'easy':
            self.level_question = 'medium'
            return True
        elif self.level_question == 'medium':
            self.level_question = 'hard'
            return True
        return False
    
    def decrease_difficulty(self):
        if self.level_question == 'hard':
            self.level_question = 'medium'
            return True
        elif self.level_question == 'medium':
            self.level_question = 'easy'
            return True
        return False