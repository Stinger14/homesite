from abc import ABCMeta, abstractmethod


class IValue(metaclass=ABCMeta):
    """The Vehicle Interface"""

    @staticmethod
    @abstractmethod
    def __str__(self):
        """Override the object to return the value attribute by default"""
