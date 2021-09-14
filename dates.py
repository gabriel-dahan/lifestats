from typing import Literal, Tuple
import re

class Date(object):

    def __init__(self, date: str) -> None:
        self.date = date
        assert self.is_valid_date(), 'Date is not valid, it must respect the format dd(/-.)mm(/-.)yyyy (ie. 30/07/2005 or 30-07-2005 or 30.07.2005).'
        self._parsed_date = tuple(int(elem) for elem in date.split(self.get_separator()))
        self.dyear = self._parsed_date[2]
        self.dmonth = self._parsed_date[1]
        self.dday = self._parsed_date[0]

    def get_tuple(self) -> Tuple[int]:
        return self._parsed_date

    def is_valid_date(self) -> bool:
        test = re.match('^([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2})$', self.date)
        return True if test else False

    def is_leap_year(self) -> bool:
        return True if self.dyear % 4 == 0 and not self.dyear % 100 == 0 else False

    def get_separator(self) -> str:
        return self.date[2:][0]

    def year_days_nmb(self) -> int:
        """ Returns the amount of days in a year depending on if it's a leap year or not """
        return 366 if self.is_leap_year() else 365

    def month_days_nmb(self, month: Literal[28, 29, 30, 31]) -> int:
        """ Returns the amount of days in a month of a year """
        if self.is_leap_year() and month == 2:
            return 29
        if month == 2:
            return 28
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        else:
            return 30

    def passed_days(self) -> int:
        """ Returns the number of passed days since the date's year started. """
        days = 0
        for month in range(1, self.dmonth):
            days += self.month_days_nmb(month)
        days += self.dday
        return days

    def remaining_days(self) -> int:
        """ Returns the number of remaining days before the date's year end. """
        days = 0
        for month in range(self.dmonth + 1, 13):
            days += self.month_days_nmb(month)
        days += self.month_days_nmb(self.dmonth) - self.dday
        return days

    def days_to(self, date: str) -> int:
        date2 = Date(date)
        assert date2.dyear > self.dyear, f'{date2} cannot be smaller than {self}.'

        days = 0
        for year in range(self.dyear, date2.dyear + 1):
            if year == self.dyear:
                days += self.remaining_days()
                continue
            elif year == date2.dyear:
                days += date2.passed_days()
                continue
            d = Date(f'01-01-{year}')
            days += d.year_days_nmb()
        return days

    def __repr__(self) -> str:
        return f'Date({self.dday}, {self.dmonth}, {self.dyear})'

    def __str__(self) -> str:
        return self.date

if __name__ == "__main__":
    d = Date('30.07.2005')
    print(d.days_to('14.09.2021'))