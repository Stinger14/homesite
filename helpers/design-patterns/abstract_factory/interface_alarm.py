from abc import ABCMeta, abstractmethod


class IAlarm(metaclass=ABCMeta):
    """Abstract Alarm Interface"""

    @staticmethod
    @abstractmethod
    def get_properties():
        """The static abstract factory interface method"""
