from models.field import Field


class Name(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        is_string = isinstance(value, str)
        is_empty = len(value.strip()) < 0
        has_numbers = any(char.isdigit() for char in value)

        if not is_string and is_empty and has_numbers:
            raise ValueError("Field name is incorrect")

        self.__value = value
