from interface_camera import ICamera


class BigCamera(ICamera):
    """The big camera concrete class implements the ICamera interface"""

    def __init__(self):
        self._lens = "big lens"
        self._sensor = "big sensor"
        self._range = "big range"

    def get_properties(self):
        return {
            "lens": self._lens,
            "sensor": self._sensor,
            "range": self._range
        }
