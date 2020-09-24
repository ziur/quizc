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

    def validate(self, value, condition_value, errors):
        if value < condition_value:
            errors.append(self.MESSAGE.format(min_value=condition_value))

class MaxValidator(object):
    MESSAGE = "The value must be less than {max_value}"

    def validate(self, value, condition_value, errors):
        if value > condition_value:
            errors.append(self.MESSAGE.format(max_value=condition_value))


class MinLengthValidator(object):
    MESSAGE = "The value length must be greater than {min_length}"

    def validate(self, value, condition_value, errors):
        if len(value) < condition_value:
            errors.append(self.MESSAGE.format(min_length=condition_value))


class MaxLengthValidator(object):
    MESSAGE = "The value length must be less than {max_length}"

    def validate(self, value, condition_value, errors):
        if len(value) > condition_value:
            errors.append(self.MESSAGE.format(max_length=condition_value))

class UpperCaseValidator(object):
    MESSAGE = "The value must be in uppercase"

    def validate(self, value, condition_value, errors):
        if not value.isupper():
            errors.append(self.MESSAGE)

class ValidatorType(Enum):
    REQUIRED = (1, RequiredValidator())
    DATE = (2, DateValidator())
    MIN = (3, MinValidator())
    MIN_LENGTH = (4, MinLengthValidator())
    MAX_LENGTH = (5, MaxLengthValidator())
    UPPERCASE = (6, UpperCaseValidator())
    MAX = (7, MaxValidator())
    def __init__(self, code, validator_instance):
        self.code = code
        self.validator_instance = validator_instance

    @staticmethod
    def get_validator(validator_code):
        for validator in ValidatorType:
            if validator.code == validator_code or str(validator.code) == validator_code:
                return validator.validator_instance
        return None
