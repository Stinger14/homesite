from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    """The Cube B Interface"""

    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        """Manufactures a Cube with coords offset [0, 0, 0]"""
