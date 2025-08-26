from interface_camera import ICamera


class SmallCamera(ICamera):
    """The small camera concrete class implements the ICamera interface"""

    def __init__(self):
        self._lens = "small lens"
        self._sensor = "small sensor"
        self._range = "small range"

    def get_properties(self):
        return {
            "lens": self._lens,
            "sensor": self._sensor,
            "range": self._range
        }
