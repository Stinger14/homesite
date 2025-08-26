from abc import ABCMeta, abstractmethod


class ICubeA(metaclass=ABCMeta):
    """The Cube A Interface"""

    @staticmethod
    @abstractmethod
    def manufacture(witdh, height, depth):
        """Manufactures a cube A object"""
