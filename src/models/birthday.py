from datetime import datetime
from models.field import Field


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value, expected_format="%d.%m.%Y"):
        try:
            parsed_date = datetime.strptime(value, expected_format)
            self.__value = parsed_date.strftime("%d %B %Y")
        except ValueError:
            print("The date format is not 'DD.MM.YYYY'")
