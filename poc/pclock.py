import datetime
import time
import sched
import abc


class PClock(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.delta = 0
        self.sch = sched.scheduler(time.time, time.sleep)

    def get_ptime(self):
        """Get ptime from true time and delta"""
        return datetime.datetime.now() + datetime.timedelta(0, self.delta)

    @abc.abstractmethod
    def shift_gen(self):
        """Generates a new shift between the duration of a real minute and a pminute"""
        pass

    def distrib_name(self):
        """The name of the distribution used"""
        pass

    def new_pminute(self):
        """Generates a new pminute and schedules the next call for when the pminute ends"""
        self.printpc()
        new_shift = self.shift_gen()
        if new_shift*self.delta > 0:
            new_shift = -new_shift
        print "New minute elapsed. Next minute will last {0} seconds.".format(60 + new_shift)
        self.delta += new_shift
        self.sch.enter(60 + new_shift, 1, self.new_pminute, ())
        self.sch.run()

    def printpc(self):
        """Prints both true clock and pclock"""
        print "Using a {0} distribution:".format(self.distrib_name)
        print "O'clock: {0} | P'clock: {1}".format(datetime.datetime.now(), self.get_ptime())
