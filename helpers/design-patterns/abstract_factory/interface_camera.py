from abc import ABCMeta, abstractmethod


class ICamera(metaclass=ABCMeta):
    """Abstract Camera Interface"""

    @staticmethod
    @abstractmethod
    def get_properties():
        """The static abstract factory interface method"""
