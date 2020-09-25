import datetime
from enum import Enum


class RequiredValidator(object):
    MESSAGE = "This question is required"

    def validate(self, value, condition_value, errors):
        if value == "":
            errors.append(self.MESSAGE)


class DateValidator(object):
    DATE_FORMAT = '%m/%d/%Y'
    MESSAGE = "The date format is invalid, it should have the format mm/dd/yyyy"

    def validate(self, value, condition_value, errors):
        try:
            datetime.datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            errors.append(self.MESSAGE)


class MinValidator(object):
    MESSAGE = "The value must be greater than {min_value}"
    MESSAGE2 = "Please insert a number"

    def validate(self, value, condition_value, errors):
        try:
          if int(value) < intcondition_value:
             errors.append(self.MESSAGE.format(min_value=condition_value))
        except ValueError:
          errors.append(self.MESSAGE2)


class MaxValidator(object):
    MESSAGE = "The value must be greater than {max_value}"
    MESSAGE2 = "Please insert a number"

    def validate(self, value, condition_value, errors):
        try:
          if int(value) > intcondition_value:
             errors.append(self.MESSAGE.format(max_value=condition_value))
        except ValueError:
          errors.append(self.MESSAGE2)

class MinLengthValidator(object):
    MESSAGE = "The value length must be more than {min_length}"

    def validate(self, value, condition_value, errors):
        if len(value) < condition_value:
            errors.append(self.MESSAGE.format(min_length=condition_value))

class MaxLengthValidator(object):
    MESSAGE = "The value length must be less than {max_length}"

    def validate(self, value, condition_value, errors):
        if len(value) > condition_value:
            errors.append(self.MESSAGE.format(max_length=condition_value))

class OnlyUppercase(object):
    MESSAGE = "The answer must be in UPEERCASE!"

    def validate(self, value, errors):
        if value != value.upper():
            errors.append(self.MESSAGE)

class ValidatorType(Enum):
    REQUIRED = (1, RequiredValidator())
    DATE = (2, DateValidator())
    MIN = (3, MinValidator())
    MAX = (4, MinValidator())
    MIN_LENGTH = (5, MinLengthValidator())
    MAX_LENGTH = (6, MaxLengthValidator())
    UPPERCASE = (7, OnlyUppercase())


    def __init__(self, code, validator_instance):
        self.code = code
        self.validator_instance = validator_instance

    @staticmethod
    def get_validator(validator_code):
        for validator in ValidatorType:
            if validator.code == validator_code or str(validator.code) == validator_code:
                return validator.validator_instance
        return None
