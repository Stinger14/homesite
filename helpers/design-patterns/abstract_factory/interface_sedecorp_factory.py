from abc import ABCMeta, abstractmethod


class ISedecorpFactory(metaclass=ABCMeta):
    """Abstract Sedecorp Factory Interface"""

    @staticmethod
    @abstractmethod
    def get_item(item):
        """The static abstract factory interface method"""
