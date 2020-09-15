import datetime
from enum import Enum
from quizc.model.validations import ValidatorType


class QuestionConfiguration(object):
    def __init__(self, has_additional_data, supported_validations):
        self.has_additional_data = has_additional_data
        self.supported_validations = supported_validations

    def convert_value(self, value):
        return value


class TextConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.MIN_LENGTH])


class DateConfiguration(QuestionConfiguration):
    DATE_FORMAT = '%d/%m/%Y'

    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.DATE])

    def convert_value(self, value):
        try:
            return datetime.datetime.strptime(value, DateConfiguration.DATE_FORMAT)
        except ValueError:
            return None


class NumericConfiguration(QuestionConfiguration):

    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.MIN, ValidatorType.MAX])

    def convert_value(self, value):
        try:
            return int(value)
        except ValueError:
            return None


class PickOneQuestionConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, True, [ValidatorType.REQUIRED])


class QuestionType(Enum):
    TEXT = (1, TextConfiguration())
    DATE = (2, DateConfiguration())
    NUMERIC = (3, NumericConfiguration())
    PICK_ONE = (4, PickOneQuestionConfiguration())

    def __init__(self, code, configuration):
        self.code = code
        self.configuration = configuration

    def get_validations(self):
        return self.configuration.validations

    def get_code(self):
        return self.code

    @staticmethod
    def get_by_code(code):
        for question_type in QuestionType:
            if question_type.code == code:
                return question_type
        return None


print(QuestionType.get_by_code(3).get_validations())
