from abc import ABCMeta, abstractmethod


class IShapeImplementer(metaclass=ABCMeta):
    """Shape implementer"""

    @staticmethod
    @abstractmethod
    def draw_implementation():
        """The method that will be handled at the shapes implementer"""

