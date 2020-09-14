class Question(object):
    def __init__(self, title, question_type):
        self.title = title
        self.required = False
        self.type = question_type
        self.validations = []


class QuestionBuilder(object):
    def __init__(self, title, question_type):
        self.question_type = question_type
        self.title = title
        self.validations = []

    def add_validation(self, validation):
        self.validations.append(validation)
        return self

    def build(self):
        return Question(self.title, self.question_type)