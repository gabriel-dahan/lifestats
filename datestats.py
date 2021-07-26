from datetime import datetime, date
from calendar import monthrange
from typing import Union
import pathlib

from errors import *
from utils import *

class DateStats(object):

    def __init__(self, date: str, hour: str = "00:00:00"):

        self._date  = date.split("/")
        self._hour  = hour.split(":")

        self.now    = datetime.now().date()

        self.year   = int(self._date[2])
        self.month  = int(self._date[1])
        self.day    = int(self._date[0])
        self.hour   = int(self._hour[0])
        self.minute = int(self._hour[1])
        self.second = int(self._hour[2])

        m_days      = monthrange(self.year, self.month)[1]

        if self.year == self.now.year:
            if self.month > self.now.month:
                raise DateOutOfRange('{0.__name__}: Value for month is out of range (today = {1.day}/{1.month}/{1.year} --> date entered = {2.day}/{2.month}/{2.year})..'.format(self.__class__, self.now, self))
            if self.month == self.now.month:
                if self.day > self.now.day:
                    raise DateOutOfRange('{0.__name__}: Value for day is out of range (today = {1.day}/{1.month}/{1.year} --> date entered = {2}).'.format(self.__class__, self.now, date))
        if 1 < self.day > m_days or 1 < self.month > 12 or 1000 < self.year > self.now.year:
            raise DateNotValidError('{0.__class__.__name__}: Value for \'date\' is not valid. Try with the following format : "dd/MM/YYYY". You may have entered a calendar day which is not existing.'.format(self))
        if 0 < self.hour > 23 or 0 < self.minute > 59 or 0 < self.second > 59:
            raise HourNotValidError('{0.__class__.__name__}: Value for \'hour\' is not valid. Try with the following format : "hh:mm:ss". Rules --> 0 >= hh <= 24 | 0 >= mm <= 59 | 0 >= ss <= 59'.format(self))

        self.datetime = datetime(
            self.year, 
            self.month, 
            self.day, 
            self.hour, 
            self.minute, 
            self.second
        )

    def birthstats(self) -> dict:
        timedelta  = datetime.now() - self.datetime
        
        days       = timedelta.days
        weeks      = round(days / 7, 2)
        months     = round(days / (days / ((days / 365.25) * 12)), 2)
        years      = round(days / 365.25, 2)

        last_bd    = date(self.now.year - 1, self.month, self.day)
        print(self.now)
        days_left  = (self.now - last_bd).days

        if days_left + (366 - days_left) == 366:
            days_since = 366 - days_left
        else:
            days_since = 365 - days_left

        return {
            "birth_date": self._date,
            "birth_hour": self._hour,
            "years_old": years,
            "months_old": months,
            "days_old": days,
            "weeks_old": weeks,
            "days_before_next_birthday": days_left,
            "days_since_last_birthday": days_since,
            "next_bd_weekday": 'next_bd_weekday',
            "last_bd_weekday": 'last_bd_weekday',
            "birthday": 'birthday'
        }

    def dayssince(self) -> int:
        # _date = date(self.year, self.month, self.day)
        # today = date(self.current_year, self.current_month, self.current_day)
        # dates_op = today - _date
        # return dates_op.days
        pass

    def secondssince(self) -> int:
        pass

if __name__ == "__main__":
    d = DateStats("11/07/1985")
    stats = d.birthstats()
    print(stats)