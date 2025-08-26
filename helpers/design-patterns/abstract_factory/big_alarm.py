from interface_alarm import IAlarm


class BigAlarm(IAlarm):
    """The big alarm concrete class implements the IAlarm interface"""

    def __init__(self):
        self._sound = "big sound"
        self._range = "big range"

    def get_properties(self):
        return {
            "sound": self._sound,
            "range": self._range
        }
