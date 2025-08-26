from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    """The House Builder Interface"""

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        """Set the building type"""

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        """Set the wall material"""

    @staticmethod
    @abstractmethod
    def set_number_doors(number_doors):
        """Set the number of doors"""

    @staticmethod
    @abstractmethod
    def set_number_windows(number_windows):
        """Set the number of windows"""

    @staticmethod
    @abstractmethod
    def get_result():
        """Return the final product"""
