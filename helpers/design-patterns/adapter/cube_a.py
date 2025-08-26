import time
from interface_cube_a import ICubeA


class CubeA(ICubeA):
    """The Cube A Class"""

    # static variable indicating last time a cube was manufactured
    last_manufactured = int(time.time())
    
    def __init__(self):
        self.width = self.height = self.depth = 0

    def manufacture(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

        # if not busy, then manufacture a cube with dimensions
        now = int(time.time())
        if now > int(CubeA.last_manufactured + 1):
            CubeA.last_manufactured = now
            return True 
        return False # busy