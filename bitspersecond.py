from math import ceil
from typing import Tuple

class BitsNSeconds:

    @classmethod
    def get_bits(self, **kwargs):
        types = ('kilo', 'mega', 'giga', 'tera',)
        for i in range(len(types)):
            if types[i] not in kwargs:
                continue
            return kwargs[types[i]] * 10 ** (3 * (i + 1))
    
    @classmethod
    def get_hms(self, seconds: int) -> Tuple[str]:
        import datetime
        return tuple(str(datetime.timedelta(seconds = seconds)).split(':'))

    def __init__(self, **kwargs) -> None:
        self.bits = self.get_bits(**kwargs)

    def time_remaining_for(self, **kwargs):
        """ Returns the time remaining (in seconds) for n bits. """
        remaining_bits = self.get_bits(**kwargs)
        time_r = round(remaining_bits / self.bits, 2)
        if 'gethms' in kwargs and kwargs['gethms']:
            return self.get_hms(time_r)
        return time_r

if __name__ == '__main__':
    bns = BitsNSeconds(mega = 1.5).time_remaining_for(giga = 5)
    print(bns)