import datetime
from enum import Enum
from quizc.utils.class_loader import get_class_instance_by_name


class RequiredValidator(object):
    MESSAGE = "This question is required"

    def validate(self, value, errors):
        if value == "":
            errors.append(self.MESSAGE)


class DateValidator(object):
    DATE_FORMAT = '%m/%d/%Y'
    MESSAGE = "The date format is invalid, it should have the format mm/dd/yyyy"

    def validate(self, value, errors):
        try:
            datetime.datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            errors.append(self.MESSAGE)


class MinValidator(object):
    MESSAGE = "The value must be less than {min_value}"

    def validate(self, value, condition_value, errors):
        if value > condition_value:
            errors.append(self.MESSAGE.format(min_value=condition_value))


class MaxValidator(object):
    MESSAGE = "The value must be greater than {max_value}"

    def validate(self, value, condition_value, errors):
        if value < condition_value:
            errors.append(self.MESSAGE.format(max_value=condition_value))


class ValidatorType(Enum):
    REQUIRED = (1, "RequiredValidator")
    DATE = (2, "DateValidator")
    MIN = (3, "MinValidator")
    MAX = (4, "MaxValidator")

    def __init__(self, code, class_name):
        self.code = code
        self.class_name = class_name

    @staticmethod
    def get_validator(validator_code):
        for validator in ValidatorType:
            if validator.code == validator_code:
                return get_class_instance_by_name("quizc.model.validations", validator.class_name)
        return None
