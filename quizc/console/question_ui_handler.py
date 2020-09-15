from quizc.model.question_type import QuestionType


class QuestionUIHandler(object):

    @staticmethod
    def show_supported_questions():
        for question_type in QuestionType:
            message = "{code}. {question}"
            print(message.format(code=question_type.get_code(), question=question_type.name))

    @staticmethod
    def show_supported_validations(question_code):
        question_type = QuestionType.get_by_code(question_code)
        if question_type is None:
            print("Invalid question type:", question_code)
        else:
            for validation in question_type .get_validations():
                message = "{code}. {validation}"
                print(message.format(code=validation.code, validation=validation.name))


    def ask_for_question(question_type):
        input()