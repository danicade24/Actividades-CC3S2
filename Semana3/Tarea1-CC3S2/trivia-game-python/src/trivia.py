class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = {
            'easy': [],
            'medium': [],
            'hard': []
        }
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.level_question = 'easy'
        self.questions_answered = 0

    def add_question(self, question, level):
        if level in self.questions:
            self.questions[level].append(question)

    def get_next_question(self):
        if self.questions_answered < 10:
            if self.level_question in self.questions and self.questions[self.level_question]:
                question = self.questions[self.level_question].pop(0)
                self.questions_answered += 1
                return question
            else:
                if self.decrease_difficulty():
                    return self.get_next_question()
                elif self.increase_difficulty():
                    return self.get_next_question()
                else:
                    return None
        return None

    def answer_question(self, question, answer):
        result = question.is_correct(answer)
        if result:
            self.correct_answers += 1
            self.increase_difficulty()
        else:
            self.incorrect_answers += 1
            self.decrease_difficulty()
        return result

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