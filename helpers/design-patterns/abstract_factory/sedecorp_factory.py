from interface_sedecorp_factory import ISedecorpFactory
from camera_factory import CameraFactory
from alarm_factory import AlarmFactory


class SedecorpFactory(ISedecorpFactory):
    """Abstract Factory Concrete Class"""

    @staticmethod
    def get_item(item):
        """Static get_factory method"""
        try:
            if item in ["SmallCamera", "BigCamera"]:
                return CameraFactory.get_camera(item)
            if item in ["SmallAlarm", "BigAlarm"]:
                return AlarmFactory.get_alarm(item)
            raise AssertionError("Item not found")
        except AssertionError as _e:
            print(_e)
        return None
