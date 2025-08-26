from small_camera import SmallCamera
from big_camera import BigCamera


class CameraFactory:
    """The camera factory class"""

    @staticmethod
    def get_camera(camera):
        """Static method to get camera"""
        try:
            if camera == "SmallCamera":
                return SmallCamera()
            if camera == "BigCamera":
                return BigCamera()
            raise AssertionError("Camera not found")
        except AssertionError as _e:
            print(_e)
        return None
        