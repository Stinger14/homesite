from house_builder import HouseBuilder


class ApartmentDirector:
    """One of the Directors that can build a complex representation"""

    @staticmethod
    def construct():
        """Create and return the final product"""
        return HouseBuilder()\
            .set_building_type("Apartment")\
            .set_wall_material("Brick")\
            .set_number_doors(6)\
            .set_number_windows(10)\
            .get_result()