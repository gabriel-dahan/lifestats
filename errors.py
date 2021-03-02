class DateStatsError(Exception):
    pass

class DateOutOfRange(DateStatsError):
    def __init__(self, msg):
        super().__init__(msg)

class DateNotValidError(DateStatsError):
    def __init__(self, msg):
        super().__init__(msg)

class HourNotValidError(DateStatsError):
    def __init__(self, msg):
        super().__init__(msg)