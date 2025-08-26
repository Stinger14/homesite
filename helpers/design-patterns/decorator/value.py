from interface_value import IValue


class Value(IValue):
    """The Value class"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
