from datetime import datetime, date
from calendar import monthrange
from typing import Union

def year_days(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365

class LifeStats:

    def __init__(self, birth_date: str):
        self._birth_date   = birth_date 

        values = self._birth_date.split("/")

        self.current_year  = datetime.now().year
        self.current_month = datetime.now().month
        self.current_day   = datetime.now().day

        self._birth_day    = int(values[0])
        self._birth_month  = int(values[1])
        self._birth_year   = int(values[2])

        self.y_days        = year_days(self._birth_year) 
        self.m_days        = monthrange(self.current_year, self.current_month)[1]

        if self.current_month >= self._birth_month and self.current_day >= self._birth_day:
            self._age = self.current_year - self._birth_year
        else:
            self._age = (self.current_year - self._birth_year) - 1

        d0 = date(2008, 1, 1)
        d1 = date(2008, 6, 15)
        l_days = d1 - d0

        self.lasting_days = l_days.days

        self.days_since   = 365 - self.lasting_days
        self.months_since = 12 - self._birth_month + self.current_month

        self.years  = round(self._age + (self.days_since / year_days(self.current_year)), 2)
        self.months = self._age * 12 - (12 - self._birth_month)
        self.days   = self._age * self.y_days - ((12 - self._birth_month) * self.m_days)

        self.birthday = False
        if self.current_month == self._birth_month and self.current_day == self._birth_day:
            self.birthday = True

    def stats(self) -> dict:
        return {
            "birth_date": self._birth_date,
            "years": self.years,
            "months": self.months,
            "days": self.days,
            "days_lasting": self.lasting_days,
            "days_since": self.days_since,
            "birthday": self.birthday
        }

    def age(self) -> Union[int, float]:
        return self.years

if __name__ == "__main__":
    s = LifeStats("30/07/2005")
    stats = s.stats()
    print(stats)