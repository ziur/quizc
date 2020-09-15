import unittest
from quizc.model.validations import *


class UtilsTest(unittest.TestCase):

    def test_factory_returns_date_validator(self):
        date_validator = ValidatorFactory.get_validator(ValidatorType.DATE)
        self.assertTrue(isinstance(date_validator, DateValidator), "Invalid date validator")

    def test_factory_returns_required_validator(self):
        required_validator = ValidatorFactory.get_validator(ValidatorType.REQUIRED)
        self.assertTrue(isinstance(required_validator, DateValidator), "The factory returned a wrong validator instance")

    def test_valid_date_validator(self):
        error = []
        required_validator = ValidatorFactory.get_validator(ValidatorType.DATE)
        required_validator.validate("12/21/2020", error)
        self.assertEqual(len(error), 0, "The date 12/21/2020 should be valid but currently it is marked as invalid")

    def test_invalid_date_validator(self):
        error = []
        required_validator = ValidatorFactory.get_validator(ValidatorType.DATE)
        required_validator.validate("2020/12/12", error)
        self.assertEqual(DateValidator.MESSAGE, error[0])

    def test_incomplete_date_validator(self):
        error = []
        required_validator = ValidatorFactory.get_validator(ValidatorType.DATE)
        required_validator.validate("2020", error)
        self.assertTrue(len(error) == 1)

    def test_required_validator(self):
        required_validator = ValidatorFactory.get_validator(ValidatorType.REQUIRED)
        self.assertTrue(isinstance(required_validator, DateValidator))


if __name__ == '__main__':
    unittest.main()
