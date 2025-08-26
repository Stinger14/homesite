from interface_shape import IShape


class Square(IShape):
    """The Square is a Refined Abstraction"""
    
    def __init__(self, implementer):
        self._implementer = implementer

    def draw(self):
        self._implementer.draw_implementation()
