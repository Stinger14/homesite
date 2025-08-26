from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    """The Game Interface"""

    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """add winner implementation"""
