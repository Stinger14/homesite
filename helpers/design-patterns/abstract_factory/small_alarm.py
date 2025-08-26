from interface_alarm import IAlarm


class SmallAlarm(IAlarm):
    """The small alarm concrete class implements the IAlarm interface"""

    def __init__(self):
        self._sound = "small sound"
        self._range = "small range"

    def get_properties(self):
        return {
            "sound": self._sound,
            "range": self._range
        }
