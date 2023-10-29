from models.field import Field


class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone is incorrect")

        self.__value = value
