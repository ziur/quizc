class RequiredValidator(object):
    MESSAGE = "This question is required"

    def validate(self, value, errors):
        if value == "":
            errors.append(self.MESSAGE)


class DateValidator(object):
    MESSAGE = "The date format is invalid, it should have the format mm/dd/yyyy"

    def validate(self, value, errors):
        if value == "":
            errors.append(self.MESSAGE)
