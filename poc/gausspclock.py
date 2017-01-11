import random
from pclock import PClock


class GaussPClock(PClock):
    def __init__(self, std_dev):
        super(GaussPClock, self).__init__()
        self.std_dev = std_dev

    @property
    def distrib_name(self):
        return "normal"

    def shift_gen(self):
        return random.gauss(0, self.std_dev)
