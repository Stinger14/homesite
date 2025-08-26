from interface_value import IValue


class Add(IValue):
    """A decorator that adds a number to a number"""

    def __init__(self, val1, val2):
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 + val2
    
    def __str__(self):
        return str(self.value)
