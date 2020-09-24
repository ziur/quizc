from json import JSONEncoder
from quizc.model.quiz import Quiz
from quizc.model.quiz_answers import QuizAnswer, Answer

class MyClass:
    Questions = []
    def __init__(self, x, y):
        self.Quiz = x
        self.Questions = []
        print('-------------')
        for i in y:
            question = {"title":i.title,"type":i.type}
            print(i.title)
            print(i.type)
            print(i.validations)
            print(i.additional_data)
        print('-------------')
        # self.y = y


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def save(data):
    json = MyEncoder().encode(data)
    f = open("quizc/data/myform.json", "w")
    f.write(json)
    f.close()
