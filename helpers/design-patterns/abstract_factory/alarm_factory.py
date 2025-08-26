from small_alarm import SmallAlarm
from big_alarm import BigAlarm


class AlarmFactory:
    """The alarm factory class"""

    @staticmethod
    def get_alarm(alarm):
        """Static method to get an alarm"""
        try:
            if alarm == "SmallAlarm":
                return SmallAlarm()
            if alarm == "BigAlarm":
                return BigAlarm()
            raise AssertionError("Alarm not found")
        except AssertionError as _e:
            print(_e)
        return None
