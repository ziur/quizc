class Form(object):
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add(self, question):
        self.questions.append(question)


class Question(object):
    def __init__(self, label, type):
        self.title = label
        self.type = type


def run(title):
    form = Form(title)
    return form
