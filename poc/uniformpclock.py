import random
from pclock import PClock


class UniformPClock(PClock):
    def __init__(self, lower_limit, upper_limit):
        super(UniformPClock, self).__init__()
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    @property
    def distrib_name(self):
        return "uniform"

    def shift_gen(self):
        return random.randint(self.lower_limit, self.upper_limit)

