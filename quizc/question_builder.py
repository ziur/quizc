class QuestionBuilder(object):
    def __init__(self, title):
        self.title = title
        self.validations = []

    def add_validation(self, validation):
        self.validations.append(validation)
        return self

    def build(self):
        return