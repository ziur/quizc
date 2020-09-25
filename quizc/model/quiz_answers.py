import uuid


class QuizAnswer(object):
    def __init__(self, quiz):
        self.quiz = quiz
        self.id = uuid.uuid4()
        self.answers = []
        self.questions = []

    def add_answer(self, answer):
        self.answers.append(answer)
    
    def add_questions(self, question):
        self.questions.append(question)


class Answer(object):
    def __init__(self, answers, question):
        self.question = question
        self.answers = answers

