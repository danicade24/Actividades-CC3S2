class Question:  
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_aswer = correct_answer
    
    def is_correct(self, correect_answer):
        return self.correct_aswer == correect_answer
